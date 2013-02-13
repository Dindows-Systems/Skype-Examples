using System;
using com.skype.api;
using com.skype.ipc;

namespace Skypekit.NET
{
    public class MySession
    {
        /**
	 * Default value for the Info/Debug console output message prefix/identifier tag,
	 * in case we get passed a null or empty string.
	 * 
	 * @since 1.0
	 */
        public static String T_TAG_DFLT = "SkypeMain";

        /**
         * Info/Debug console output message prefix/identifier tag.
         * Corresponds to the tutorial's class name.
         * 
         * @since 1.0
         */
        public String myTutorialTag;

        /**
         * Console PrintStream.
         * <br /><br />
         * Based off <code>System.out</code>, but specifies <code>autoFlush</code> as true to ensure
         * that console output does not intermingle since both the tutorial code and the
         * event handlers write to the console.
         * 
         * @since 1.0
         */
        //public static PrintStream myConsole = new PrintStream(System.Console, true);
        public static PrintStream myConsole = new PrintStream();

        /**
         * Name of the target Skype account, which is actually the Skype Name
         * of the user that created it.
         * 
         * @since 1.0
         */
        public String myAccountName;

        public SignInMgr mySignInMgr = new SignInMgr();

        /**
         * Skype instance for this tutorial session.
         * 
         * @see com.skype.api.Skype
         * 
         * @since 1.0
         */
        public Skype mySkype = null;

        /**
         * SkypeKit configuration instance for this tutorial session.
         * Contains transport port/IP address and certificate file data.
         * 
         * @since 2.0
         */
        public ClientConfiguration myClientConfiguration = null;

        /**
         * SkypeKit version number parse instance for this tutorial session.
         * <br /><br />
         * Do <em>not</em> attempt to instantiate this instance until <em>after intializing</em>
         * {@link #mySkype}!
         * 
         * @see com.skype.tutorial.util.ParseSkypeKitVersion
         * 
         * @since 1.0
         */
        public ParseSkypeKitVersion myParseSkypeKitVersion = null;

        /**
         * Account instance for this tutorial session.
         * Set on successful login, <i>not</i> during session creation!
         * 
         * @see com.skype.api.Account
         * 
         * @since 1.0
         */
        public Account myAccount = null;

        /**
         * Whether we are currently in a call.
         * <br /><br />
         * Set to true when a Conversation goes live (<code>Conversation.LOCAL_LIVEStatus.RINGING_FOR_ME</code>)
         * after a successful <code>Conversation.join</code> or <code>Conversation.JoinLiveSession</code>;
         * set to false when a Conversation goes non-live (<code>Conversation.LOCAL_LIVEStatus.RECENTLY_LIVE</code> or
         * <code>Conversation.LOCAL_LIVEStatus.NONE</code>).
         * 
         * @see com.skype.tutorial.util.Listeners#onPropertyChange(com.skype.api.Conversation, com.skype.api.Conversation.Property, int, String)
         * @see com.skype.tutorial.util.Listeners#onConversationListChange(Skype, com.skype.api.Conversation, com.skype.api.Conversation.ListType, boolean)
         *  
         * @since 1.0
         */
        public bool callActive = false;

        /**
         * Cached status of this session's associated Account.
         * <br /><br />
         * Initialized to <code>Account.Status.LOGGED_OUT</code>; updated by
         * Account onPropertyChange handler.
         * 
         * @see com.skype.tutorial.util.Listeners#onPropertyChange(com.skype.api.Account, com.skype.api.Account.Property, int, String)
         * @see com.skype.api.Account
         * 
         * @since 1.1
         */
        public Account.Status loginStatus = Account.Status.LOGGED_OUT;

        /**
         * Datagram stream ID, used by Tutorial 11.
         * 
         * @since 1.0
         */
        public String streamName = "";

        /**
         * Callbacks/event handlers for this tutorial session.
         * 
         * @since 1.0
         */
        public Listeners myListeners = null;

        /**
         * Server IP Address.
         * 
         * @since 1.0
         */
        public static String IP_ADDR = "127.0.0.1";

        /**
         * Server Port.
         * <br /><br />
         * If you modify this compiled-in default, you will need to start the matching SkypeKit runtime with option:<br />
         * &nbsp;&nbsp;&nbsp;&nbsp;<code>-p <em>9999</em></code><br />
         * where <code>-p <em>9999</em></code> reflects this value. 
         * 
         * @since 1.0
         */
        public static int PORT_NUM = 8963;

        /**
         * Creates <em>most</em> everything needed for a tutorial session; the Account instance is populated during sign-in. 
         * 
         * @param tutorialTag
         *  The tutorial's class name. If null or the empty string, default it to <code>T_TAG_DFLT</code>.
         * @param accountName
         *  The <em>name</em> of the account to use for this tutorial. If null or the empty string,
         *  <em>fail</em> by throwing a RuntimeException indicating that fact.
         * @param pathName
         * 	Pathname of the certificate file, which should be a PEM file.
         * 
         * @return
         * <ul>
         *   <li>true: session initialized</li>
         *   <li>false: session initialization failed due to:
         *   	<ul>
         *   		<li>no or empty account name</li>
         *   		<li>com.skype.api.Skype.Init failed - most likely from an invalid AppKeyPair</li>
         *   		<li>could not obtain an Account instance</li>
         *   	</ul>
         *   </li>
         * </ul>
         *  
         * @see com.skype.tutorial.util.SignInMgr
         * 
         * @since 1.0
         */
        /*	public boolean doCreateSession(String tutorialTag, String accountName, AppKeyPairMgr myAppKeyPairMgr) {
        */
        public bool doCreateSession(String tutorialTag, String accountName, String pathName)
        {

            if ((tutorialTag != null) && (tutorialTag.Length != 0))
            {
                myTutorialTag = tutorialTag;
            }
            else
            {
                myTutorialTag = T_TAG_DFLT;
            }

            if ((accountName != null) && (accountName.Length != 0))
            {
                myAccountName = accountName; // All tutorials minimally require an account name
            }
            else
            {
                throw new Exception((myTutorialTag + ": Cannot initialize session instance - no account name!"));
            }

            // Set up our session with the SkypeKit runtime...
            // Note that most of the Skype methods - including static methods and GetVersionString - will
            // fail and/or throw an exception if invoked prior to successful initialization!
            mySkype = new Skype();
            myClientConfiguration = new ClientConfiguration();
            myClientConfiguration.setTcpTransport(IP_ADDR, PORT_NUM);
            myClientConfiguration.setCertificate(pathName);
            myListeners = new Listeners(this);
            myConsole.printf("%s: Instantiated Skype, ClientConfiguration, and Listeners instances...%n", myTutorialTag);

            mySkype.init(myClientConfiguration, myListeners);
            mySkype.start(); // You must invoke start --immediately-- after invoking init!

            myParseSkypeKitVersion = new ParseSkypeKitVersion(mySkype);
            myConsole.printf("%s: Initialized MySkype instance - version = %s (%d.%d.%d)%n",
                        myTutorialTag, myParseSkypeKitVersion.getVersionStr(),
                        myParseSkypeKitVersion.getMajorVersion(),
                        myParseSkypeKitVersion.getMinorVersion(),
                        myParseSkypeKitVersion.getPatchVersion());


            // Get the Account
            if ((myAccount = mySkype.getAccount(myAccountName)) == null)
            {
                myConsole.printf("%s: Could not get Account for %s!%n", myTutorialTag, myAccountName);
                myConsole.printf("%s: Session initialization failed!%n", myTutorialTag);
                return (false);
            }

            myConsole.printf("%s: Got Account for %s%n", myTutorialTag, myAccountName);
            myConsole.printf("%s: Initialized session!%n", myTutorialTag);

            return (true);
        }


        /**
         * Tears down a tutorial session.
         * <br /><br />
         * Specifically, this involves:
         * <ol>
         *   <li>Un-registering the listeners</li>
         *   <li>Disconnecting the transport</li>
         *   <li>"Closing" our Skype instance, which terminates the SkypeKit runtime</li> 
         * </ol> 
         * 
         * @see Listeners#unRegisterAllListeners()
         * 
         * @since 1.0
         */
        public void doTearDownSession()
        {

            if (myListeners != null)
            {
                myListeners.unRegisterAllListeners();
                myListeners = null;
            }
            // Closing Skype also disconnects the transport
            if (mySkype != null)
            {
                mySkype.stop();
                mySkype = null;
            }

            myConsole.printf("%s: Tore down session instance%n", myTutorialTag);
        }

        /**
         * Retrieves the current login status of this session's Account.
         * @return
         * 	Cached login status of this session's Account.
         * 
         * @see com.skype.tutorial.util.Listeners#onPropertyChange(com.skype.api.Account, com.skype.api.Account.Property, int, String)
         * 
         * @since 1.0
         */
        public Account.Status getLoginStatus()
        {

            return (this.loginStatus);
        }

        /**
         * Establishes the login status of this session's Account.
         * @param loginStatus
         * 	Reported login status of this session's Account.
         * 
         * @see com.skype.tutorial.util.Listeners#onPropertyChange(com.skype.api.Account, com.skype.api.Account.Property, int, String)
         * 
         * @since 1.0
         */
        public void setLoginStatus(Account.Status loginStatus)
        {

            this.loginStatus = loginStatus;

            MySession.myConsole.printf(myTutorialTag + ": " + "setting loginStatus to %s%n", loginStatus);
            return;
        }

        /**
         * Determines if an Account is signed in.
         * <br /><br />
         * Specifically, this involves examining the last cached value for
         * the associated Account's status property. Essentially, <em>only</em>
         * a current status of <code>Account.Status.LOGGED_IN</code> returns true
         * <br /><br />
         * Caching the status avoids having to query the DB. For mobile devices,
         * WiFi-connected laptops running on battery power, and so forth this
         * typically avoids expending battery charge to transmit the server request.
         * 
         * @return
         * <ul>
         *   <li>true: currently signed in</li>
         *   <li>false: currently signed out <em>or</em> target Account is null</li>
         * </ul>
         * 
         * @see com.skype.tutorial.util.SignInMgr#isLoggedIn(Account)
         * 
         * @since 1.0
         */
        public bool isLoggedIn()
        {

            if (this.loginStatus == Account.Status.LOGGED_IN)
            {
                return (true);
            }
            return (false);
        }

        /**
         * Assigns active input and output devices from among those available.
         * Notifies user regarding the name of the selected devices or whether the request failed.
         * <em>Both</em> devices must exist for the request to succeed.
         * 
         * @param micIdx
         * 	Index into the array of available recording devices of the requested input device.
         * @param spkrIdx
         * 	Index into the array of available playback devices of the requested output device.
         * 
         * @return
         * <ul>
         *   <li>true: success</li>
         *   <li>false: failure</li>
         * </ul>
         * 
         * @see com.skype.api.Skype#getAvailableRecordingDevices()
         * @see com.skype.api.Skype#getAvailableOutputDevices()
         * 
         * @since 2.0
         */
        public bool setupAudioDevices(int micIdx, int spkrIdx)
        {
            bool passFail = true;	// Ever the optimist, assume success!

            Skype.GetAvailableRecordingDevicesResponse inputDevices = mySkype.getAvailableRecordingDevices();
            Skype.GetAvailableOutputDevicesResponse outputDevices = mySkype.getAvailableOutputDevices();

            if (micIdx > (inputDevices.handleList.Length + 1))
            {
                MySession.myConsole.printf("%s: Invalid mic device no. (%d) passed!%n", myTutorialTag, micIdx);
                passFail = false;
            }

            if (spkrIdx > (outputDevices.handleList.Length + 1))
            {
                MySession.myConsole.printf("%s: Invalid speaker device no. (%d) passed!%n", myTutorialTag, spkrIdx);
                passFail = false;
            }

            if (passFail)
            {
                MySession.myConsole.printf("%s: Setting mic to %s (%s)%n",
                        myTutorialTag, inputDevices.nameList[micIdx], inputDevices.productIdList[micIdx]);
                MySession.myConsole.printf("%s: Setting speakers to %s  (%s)%n",
                        myTutorialTag, outputDevices.nameList[spkrIdx], outputDevices.productIdList[spkrIdx]);
                mySkype.selectSoundDevices(inputDevices.handleList[micIdx],
                        outputDevices.handleList[spkrIdx], outputDevices.handleList[spkrIdx]);
                mySkype.setSpeakerVolume(100);
            }

            return (passFail);
        }


        /*
             **
             * Translates an APP2APP_STREAMS type to a displyable string.
             * Used by Tutorial 11.
             * 
             * @param listType
             * 	APP2APP_STREAMS enum to translate.
             * 
             * @return
             *   A string representation of the enum value, or "unknown stream type" if not recognized.
             * 
             * @see com.skype.api.Skype.APP2APP_STREAMS
             * 
             * @since 1.0
             *
            public String streamListType(MySession mySession, Skype.APP2APP_STREAMS listType) {
                String listTypeAsText;
		
                switch (listType) {
                    case ALL_STREAMS:
                        listTypeAsText = "all streams";
                        break;
                    case SENDING_STREAMS:
                        listTypeAsText = "sending stream";
                        break;
                    case RECEIVED_STREAMS:
                        listTypeAsText = "receiving stream";
                        break;
                    default:
                        listTypeAsText = "unknown stream type";
                        break;
                }
                return (listTypeAsText);
            }
        */
    }
}
