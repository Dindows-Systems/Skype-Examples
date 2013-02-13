using System;
using Skypekit.NET;
using com.skype.api;
using java.util;
using java.io;
using java.text;

namespace Tutorial12
{
    /**
 * Copyright (C) 2010, 2011 Skype Limited
 *
 * All intellectual property rights, including but not limited to copyrights,
 * trademarks and patents, as well as know how and trade secrets contained in,
 * relating to, or arising from the internet telephony software of
 * Skype Limited (including its affiliates, "Skype"), including without
 * limitation this source code, Skype API and related material of such
 * software proprietary to Skype and/or its licensors ("IP Rights") are and
 * shall remain the exclusive property of Skype and/or its licensors.
 * The recipient hereby acknowledges and agrees that any unauthorized use of
 * the IP Rights is a violation of intellectual property laws.
 *
 * Skype reserves all rights and may take legal action against infringers of
 * IP Rights.
 *
 * The recipient agrees not to remove, obscure, make illegible or alter any
 * notices or indications of the IP Rights and/or Skype's rights and
 * ownership thereof.
 */

    /**
  * Getting Started With SkypeKit: Tutorial Application, Step 12.
  *
  * This example illustrates a simple SkypeKit-based program that:
  * <ol>
  *   <li>Takes a Skype Name, password, and optional AppKeyPair PEM file pathname as command-line arguments</li>
  *   <li>Initiates login for that user</li>
  *   <li>Waits until the login process is complete</li>
  *   <li>assembles and displays an event history of:
  *     <ul>
  *       <li>incoming calls</li>
  *       <li>outgoing calls</li>
  *       <li>authorization requests</li>
  *       <li>authorizations granted</li>
  *     </ul>
  *   </li>
  *   <li>Initiates logout</li>
  *   <li>Waits until logout is complete</li>
  *   <li>Cleans up and exits</li>
  * </ol>
  * 
  * @author Andrea Drane (ported/refactored from existing C++ tutorial code)
  * 
  * @since 1.0
  */
    class Program
    {
        /**
	 * Info/Debug console output message prefix/identifier tag.
	 * Corresponds to class name.
	 * 
	 * @since 1.0
	 */
        public static String MY_CLASS_TAG = "Tutorial_12";

        /**
         * Index of the account name in the command line argument list.
         * 
         * @since 1.0
         */
        public static int ACCOUNT_NAME_IDX = 0;

        /**
         * Index of the account password in the command line argument list.
         * 
         * @since 1.0
         */
        public static int ACCOUNT_PWORD_IDX = 1;

        /**
         * Number of required arguments in the command line argument list.
         * 
         * @since 1.0
         */
        public static int REQ_ARG_CNT = 2;

        /**
         * Number of <em>optional</em> arguments in the command line argument list.
         * 
         * @since 1.0
         */
        public static int OPT_ARG_CNT = 1;

        /**
         * Index of the <em>optional</em> AppKeyPair PEM file pathname in
         * the command line argument list, which is always last.
         * 
         * @since 1.0
         */
        public static int APP_KEY_PAIR_IDX = ((REQ_ARG_CNT + OPT_ARG_CNT) - 1);

        /**
         * ParsePosition instance representing the beginning of a target string.
         * 
         * @since 1.0
         */
        public static ParsePosition ZERO_POS = new ParsePosition(0);

        private static AppKeyPairMgr myAppKeyPairMgr = new AppKeyPairMgr();
        private static MySession mySession = new MySession();
        private static XmlStrMgr myXmlStrMgr = new XmlStrMgr();

        /**
         * Main loop - Event History
         * 
         * @param args
         * <ol>
         *   <li>Name of the target Skype account.</li>
         *   <li>Password for the target Skype account.</li>
         *   <li>Pathname of a PEM file.</li>
         * </ol>
         * 
         * @since 1.0
         */
        public static void Main(String[] args)
        {

            if (args.Length < REQ_ARG_CNT)
            {
                MySession.myConsole.printf("Usage is %s accountName accountPassword [appTokenPathname]%n%n", MY_CLASS_TAG);
                return;
            }
            if (args.Length > (REQ_ARG_CNT + OPT_ARG_CNT))
            {
                MySession.myConsole.printf("%s: Ignoring %d extraneous arguments.%n", MY_CLASS_TAG, (args.Length - REQ_ARG_CNT));
            }

            // Ensure our certificate file name and contents are valid
            if (args.Length > REQ_ARG_CNT)
            {
                // AppKeyPairMgrmethods will issue all appropriate status and/or error messages!
                if ((!myAppKeyPairMgr.resolveAppKeyPairPath(args[APP_KEY_PAIR_IDX])) ||
                    (!myAppKeyPairMgr.isValidCertificate()))
                {
                    return;
                }
            }
            else
            {
                if ((!myAppKeyPairMgr.resolveAppKeyPairPath()) ||
                    (!myAppKeyPairMgr.isValidCertificate()))
                {
                    return;
                }
            }

            MySession.myConsole.printf("%s: main - Creating session - Account = %s%n",
                                MY_CLASS_TAG, args[ACCOUNT_NAME_IDX]);
            mySession.doCreateSession(MY_CLASS_TAG, args[ACCOUNT_NAME_IDX], myAppKeyPairMgr.getPemFilePathname());

            MySession.myConsole.printf("%s: main - Logging in w/ password %s%n",
                    MY_CLASS_TAG, args[ACCOUNT_PWORD_IDX]);
            if (mySession.mySignInMgr.Login(MY_CLASS_TAG, mySession, args[ACCOUNT_PWORD_IDX]))
            {
                doEventHistory(mySession);
                mySession.mySignInMgr.Logout(MY_CLASS_TAG, mySession);
            }
            // SkypeKitListeners, SignInMgr, and MySession will have logged/written
            // all appropriate diagnostics if login is not successful

            MySession.myConsole.printf("%s: Cleaning up...%n", MY_CLASS_TAG);
            if (mySession != null)
            {
                mySession.doTearDownSession();
            }
            MySession.myConsole.printf("%s: Done!%n", MY_CLASS_TAG);
        }


        /**
         * Handles event history.
         * <ol>
         * 	<li>Obtains an unfiltered list of all Conservations</li>
         * 	<li>For each conversation:
         * 	  <ol style="list-style-type:lower-alpha">
         * 	    <li>Lists associated context messages</li>
         * 	    <li>Lists associated unconsumed messages</li>
         * 	  </ol>
         *   </li>
         * </ol>
         * 
         * @param mySession
         *	Populated session object
         * 
         * @since 1.0
         */
        static void doEventHistory(MySession mySession)
        {

            Conversation[] myConversationList =
                mySession.mySkype.getConversationList(Conversation.ListType.REALLY_ALL_CONVERSATIONS);
            int conversationListCount = myConversationList.Length;

            for (int i = 0; i < conversationListCount; i++)
            {
                Conversation currConv = myConversationList[i];
                MySession.myConsole.printf("%n%s: Processing Conversation \"%s\" (%d of %d)...%n",
                                    MY_CLASS_TAG, currConv.getDisplayName(),
                                    (i + 1), conversationListCount);
                // Get messages after midnight 01 December, 2010 local time
                // Replace timestamp argument with '0' to get only messages within the last 24 hours
                Calendar calTimeStamp = Calendar.getInstance();
                calTimeStamp.set(2010, Calendar.DECEMBER, 1, 0, 0, 0);
                long l_calTimeStamp = calTimeStamp.getTimeInMillis() / 1000L;
                Conversation.GetLastMessagesResponse currConvMsgList = currConv.getLastMessages((int)l_calTimeStamp);
                /*
                 *     		Conversation.GetLastMessagesResponse currConvMsgList = currConv.GetLastMessages(0);
                 */
                MySession.myConsole.printf("%s: Rendering context messages... found ", MY_CLASS_TAG);
                doRenderHistory(mySession, currConvMsgList.contextMessages);
                MySession.myConsole.printf("%s: Rendering unconsumed messages... found ", MY_CLASS_TAG);
                doRenderHistory(mySession, currConvMsgList.unconsumedMessages);
            }

            MySession.myConsole.printf("%s: Press Enter to quit.%n%n", mySession.myTutorialTag);
            try
            {
                while (true)
                {
                    int keyboardChar = (int)System.Console.ReadKey().KeyChar;
                    // Some platforms think ENTER is 0x0D; others think it's 0x0A...
                    if ((keyboardChar == 0x0D) || (keyboardChar == 0x0A))
                    {
                        break;
                    }
                }
            }
            catch (IOException e)
            {
                // TODO Auto-generated catch block
                e.printStackTrace();
                return;
            }
        }

        /**
         * Processes messages associated with a Conversation.
         * Processes <em>only</em> messages of type:
         * <ul>
         *   <li>STARTED_LIVESESSION&#8212;lists details of in-coming and out-going calls</li>
         *   <li>POSTED_VOICE_MESSAGE&#8212;lists details of in-coming and out-going voicemails</li>
         *   <li>REQUESTED_AUTH&#8212;lists Contact authorization requests</li>
         *   <li>GRANTED_AUTH&#8212;lists Contacts granted authorization</li>
         * </ul>
         * 
         * @param mySession
         *	Populated session object
         * @param myMessages
         *	Array of message strings to process.
         * 
         * @since 1.0
         */
        static void doRenderHistory(MySession mySession, Message[] myMessages)
        {
            ParsePosition s_pos;
            ParsePosition e_pos;

            int msgTimeStamp;
            Date dateTimeStamp;
            DateFormat dateFmt = DateFormat.getDateTimeInstance();

            String author;
            String bodyXml;
            int bodyXmlLength;

            /*
             *         myXmlStrMgr.setVerboseDebug(true);
             */

            int msgCount = myMessages.Length;
            Message currMsg;
            Message.Type currMsgType;
            MySession.myConsole.printf("%d ...%n", msgCount);
            for (int i = 0; i < msgCount; i++)
            {
                currMsg = myMessages[i];
                currMsgType = currMsg.getType();

                if (currMsgType == Message.Type.STARTED_LIVE_SESSION)
                {
                    MySession.myConsole.printf("%nProcessing message of type %s%n", currMsgType.toString());
                    // Message.Property.P_AUTHOR tells who initiated the call.
                    author = currMsg.getAuthor();

                    // For duration we unfortunately have to parse the XML
                    // The duration we're interested in is
                    // <part identity="&me">%n...<duration>x</duration>...
                    //
                    // Real implementation should use a proper XML-parser here!
                    java.lang.StringBuffer partTag = new java.lang.StringBuffer("<part identity=\"");
                    partTag.append(mySession.myAccountName + "\">");
                    s_pos = myXmlStrMgr.getXmlSubStrPos(currMsg.getBodyXml(),
                                                        partTag.toString(), ZERO_POS);
                    if (s_pos == null)
                    {
                        MySession.myConsole.printf("%s: Could not find \"%s\" in xmlDoc%n%s%n%nSkipping...%n%n",
                                MY_CLASS_TAG, partTag.toString(),
                                currMsg.getBodyXml());
                        break;
                    }

                    int duration =
                        myXmlStrMgr.getXmlValueNum(currMsg.getBodyXml(),
                                                    "<duration>", s_pos);

                    // Ditto for counting how many parts the body has...
                    int num_parts = 0;
                    s_pos.setIndex(0);
                    do
                    {
                        e_pos = myXmlStrMgr.getXmlSubStrPos(currMsg.getBodyXml(),
                                                            "<part ", s_pos);
                        if (e_pos != null)
                        {
                            num_parts++;
                            s_pos.setIndex(e_pos.getIndex());
                        }
                    }
                    while (e_pos != null);

                    // Get timestamp -- it's in seconds, and the Date constructor needs milliseconds!
                    msgTimeStamp = currMsg.getTimestamp();
                    dateTimeStamp = new Date((msgTimeStamp * 1000L));
                    MySession.myConsole.printf("[%s] ", dateFmt.format(dateTimeStamp));
                    // Last part is to fetch message reason
                    String reason = currMsg.getReason();

                    if (author.Equals(mySession.myAccountName))
                    {
                        // I initiated the call
                        MySession.myConsole.println("outgoing call to ");
                    }
                    else
                    {
                        // Somebody else called me
                        MySession.myConsole.println("incoming call from ");
                    }

                    // List identities
                    doListIdentities(currMsg);

                    if (duration >= 0)
                    {
                        MySession.myConsole.printf("duration %d seconds", duration);
                    }
                    else if (num_parts > 1)
                    {
                        if (reason.Equals("manual"))
                        {
                            MySession.myConsole.printf("refused");
                        }
                        else
                        {
                            MySession.myConsole.printf("failed (%s)", reason);
                        }
                    }
                    else
                    {
                        MySession.myConsole.printf("missed");
                    }

                    MySession.myConsole.printf(" (%d parts).%n", num_parts);
                }
                else if (currMsgType == Message.Type.POSTED_VOICE_MESSAGE)
                {
                    MySession.myConsole.printf("%nProcessing message of type %s%n", currMsgType.toString());
                    author = currMsg.getAuthor();
                    // XML parsing again...
                    bodyXml = currMsg.getBodyXml();
                    bodyXmlLength = myXmlStrMgr.getXmlValueNum(bodyXml, "<length>", ZERO_POS);
                    // Get timestamp -- it's in seconds, and the Date constructor needs milliseconds!
                    msgTimeStamp = currMsg.getTimestamp();
                    dateTimeStamp = new Date((msgTimeStamp * 1000L));
                    MySession.myConsole.printf("[%s] ", dateFmt.format(dateTimeStamp));
                    if (author.Equals(mySession.myAccountName))
                    {
                        // I initiated the call
                        MySession.myConsole.println("Sent voicemail to ");
                    }
                    else
                    {
                        // Somebody else called me
                        MySession.myConsole.println("Got voicemail from ");
                    }
                    // List identities
                    doListIdentities(currMsg);
                    MySession.myConsole.printf("duration %d%n", bodyXmlLength);
                }
                else if (currMsgType == Message.Type.REQUESTED_AUTH)
                {
                    MySession.myConsole.printf("%nProcessing message of type %s%n", currMsgType.toString());
                    // Please note that REQUESTED_AUTH is not used to request authorization
                    // ALERT is used for that. REQUESTED_AUTH is used only for history
                    author = currMsg.getAuthor();
                    // Get timestamp -- it's in seconds, and the Date constructor needs milliseconds!
                    msgTimeStamp = currMsg.getTimestamp();
                    dateTimeStamp = new Date((msgTimeStamp * 1000L));
                    MySession.myConsole.printf("[%s] ", dateFmt.format(dateTimeStamp));
                    MySession.myConsole.printf("Authorization request from %s to ", author);
                    // List identities
                    doListIdentities(currMsg);
                    MySession.myConsole.println("");
                }
                else if (currMsgType == Message.Type.GRANTED_AUTH)
                {
                    MySession.myConsole.printf("%nProcessing message of type %s%n", currMsgType.toString());
                    author = currMsg.getAuthor();
                    // Get timestamp -- it's in seconds, and the Date constructor needs milliseconds!
                    msgTimeStamp = currMsg.getTimestamp();
                    dateTimeStamp = new Date((msgTimeStamp * 1000L));
                    MySession.myConsole.printf("[%s] ", dateFmt.format(dateTimeStamp));
                    MySession.myConsole.printf("%s granted authorization to ", author);
                    // List identities
                    doListIdentities(currMsg);
                    MySession.myConsole.println("");
                }

                else
                    MySession.myConsole.printf("%nIgnoring message of type %s%n", currMsgType.toString());
            }
        }


        /**
         * Writes identities associated with a Message to the console as a single string.
         * <br /><br />
         * If the target message's <code>identities</code> property is empty,
         * writes <code>--NONE--</code>. Otherwise, writes the
         * individual identity values <em>separated by commas</em>.
         * <br /><br />
         * Makes no assumptions about any preceding characters already written to the console.
         * Terminates the string with a colon followed by a space ("code>": "</code>). Does
         * <em>not</em> include any carriage return/line feed!
         * <br /><br />
         * For example:
         * <pre>
         *     (empty)     => --NONE--
         *                    ********
         *     abc         => abc:
         *                    *****
         *     abc def ghi => abc, def, ghi:
         *                    ***************
         * </pre>
         * 
         * @param currMsg
         *	Target Message instance.
         * 
         * @since 1.0
         */
        static void doListIdentities(Message currMsg)
        {

            String[] identities = currMsg.getIdentities().Split(' ');

            int i = 0;
            int j = identities.Length;

            if (j == 0)
            {
                MySession.myConsole.println("--NONE--: ");
                return;
            }

            while (--j >= 0)
            {
                MySession.myConsole.printf("\"%s\"", identities[i++]);
                if (j > 0)
                {
                    MySession.myConsole.printf(", ");
                }
            }

            MySession.myConsole.printf(": ");
        }
    }
}