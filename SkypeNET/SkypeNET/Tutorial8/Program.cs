using System;
using Skypekit.NET;
using com.skype.api;
using java.util;

namespace Tutorial8
{
    /**
 * Copyright (C) 2010-2012 Skype
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
 * Getting Started With SkypeKit: Tutorial Application, Step 8.
 *
 * In this example, we'll write a command-line utility for adding, deleting, and 
 * listing PSTN (telephone number) contacts.
 * 
 * This example illustrates a simple SkypeKit-based program that:
 * <ol>
 *   <li>Takes a Skype Name, password, target Contact information, command, and
 *       optional AppKeyPair PEM file pathname as command-line arguments</li>
 *   <li>Initiates login for that user</li>
 *   <li>Waits until the login process is complete</li>
 *   <li>Depending on the value of the <em>command</em> argument:
 *     <ul>
 *       <li>adds the target Contact</li>
 *       <li>deletes the target Contact</li>
 *       <li>lists the user&#8217;s Contacts</li>
 *     </ul>
 *   </li>
 *   <li>Initiates logout</li>
 *   <li>Waits until logout is complete</li>
 *   <li>Cleans up and exits</li>
 * </ol>
 * 
 * @author Andrea Drane (ported from existing C++ tutorial code)
 * 
 * @since 1.0
 */
    class Program
    {
        /**
     * Command option string for adding a Contact.
     * 
     * @since 1.0
     * 
     */
        public static String ADD_CONTACT = "-a";

        /**
         * Command option string for deleting a Contact.
         * 
         * @since 1.0
         * 
         */
        public static String DELETE_CONTACT = "-d";

        /**
         * Command option string for listing Contact.
         * 
         * @since 1.0
         * 
         */
        public static String LIST_CONTACTS = "-l";

        /**
         * Info/Debug console output message prefix/identifier tag.
         * Corresponds to class name.
         * 
         * @since 1.0
         */
        public static String MY_CLASS_TAG = "Tutorial_8";

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
         * Index of the command option key in the command line argument list.
         * 
         * @since 1.0
         */
        public static int COMMAND_OPT_IDX = 2;

        /**
         * Number of required arguments in the command line argument list.
         * 
         * @since 1.0
         */
        public static int REQ_ARG_CNT = 3;

        /**
         * Index of the "optional" phone number in the command line argument list.
         * <em>Required</em> if {@link #COMMAND_OPT_IDX} specified as -a or -d. 
         * 
         * @since 1.0
         */
        public static int PSTN_IDX = 3;

        /**
         * Index of the "optional" Contact display name in the command line argument list.
         * <em>Required</em> if {@link #COMMAND_OPT_IDX} specified as -a. 
         * 
         * @since 1.0
         */
        public static int DISPLAY_NAME_IDX = 4;

        /**
         * Number of <em>optional</em> arguments in the command line argument list.
         * This includes the <em>optional</em> AppKeyPair PEM file pathname in the
         * command line argument list, which must always appears last.
         * 
         * @since 1.0
         */
        public static int OPT_ARG_CNT = 3;

        /**
         * What to do with my Contacts
         *
         * @since 1.0
         */
        private static String commandOpt;

        /**
         * Phone number for the PSTN Contact
         *
         * @since 1.0
         */
        private static String newPstn = "Omitted";

        /**
         * Display name for the PSTN Contact
         *
         * @since 1.0
         */
        private static String displayName = "Omitted";

        private static AppKeyPairMgr myAppKeyPairMgr = new AppKeyPairMgr();
        private static MySession mySession = new MySession();

        /**
         * Main loop
         * 
         * @param args
         * <ol>
         *   <li>Name of the target Skype account.</li>
         *   <li>Password for the target Skype account.</li>
         *   <li>One of the following commands:
         *     <ul>
         *       <li>-l (list all PSTN contacts)</li>
         *       <li>-a (add a contact)</li>
         *       <li>-d (delete a contact)</li>
         *     </ul>
         *   </li>
         *   <li>Contact's phone number (to be added or removed).</li>
         *   <li>Contact's displayname (to be added)</li>
         *   <li>Optional pathname of an AppKeyPair PEM file.</li>
         * </ol>
         * 
         * @since 1.0
         */
        public static void Main(String[] args)
        {
            int argsLimit = REQ_ARG_CNT;	// Command-specific maximum number of arguments so we can tell
            // if there's an optional AppKeyPair pathname specification.
            // Default to number of arguments for "list" command

            if (args.Length < REQ_ARG_CNT)
            {
                MySession.myConsole.printf("Usage is %s accountName accountPassword -l|-a|-d| [phoneNumber displayName appKeyPairPathname]%n%n", MY_CLASS_TAG);
                return;
            }
            if (args.Length > (REQ_ARG_CNT + OPT_ARG_CNT))
            {
                MySession.myConsole.printf("%s: Ignoring %d extraneous arguments.%n", MY_CLASS_TAG, (args.Length - REQ_ARG_CNT));
            }

            commandOpt = args[COMMAND_OPT_IDX].ToString();
            // Don't get confused by just an AppKeyPair path!
            // (Command opts are all the same length...)
            if (commandOpt.Length != LIST_CONTACTS.Length)
            {
                MySession.myConsole.printf("%s: Required command option appears to be missing; found %s. Exiting!%n",
                                    MY_CLASS_TAG, commandOpt);
                return;
            }

            if (commandOpt.Equals(DELETE_CONTACT))
            {
                argsLimit = (REQ_ARG_CNT + 1);
                if (args.Length < argsLimit)
                {
                    MySession.myConsole.printf("%s: Delete Contact requires Contact's phone number!.%n", MY_CLASS_TAG);
                    return;
                }
                newPstn = args[PSTN_IDX].ToString();
            }
            else if (commandOpt.Equals(ADD_CONTACT))
            {
                argsLimit = (REQ_ARG_CNT + 2);
                if (args.Length < argsLimit)
                {
                    MySession.myConsole.printf("%s: Add Contact requires Contact's phone number and display name!.%n", MY_CLASS_TAG);
                    return;
                }
                newPstn = args[PSTN_IDX].ToString();
                displayName = args[DISPLAY_NAME_IDX].ToString();
            }

            MySession.myConsole.printf("%s: main - Account: %s%n", MY_CLASS_TAG, args[ACCOUNT_NAME_IDX]);
            MySession.myConsole.printf("\t\tCommand: %s%n", commandOpt);
            MySession.myConsole.printf("\t\tPhone Number: %s%n", newPstn);
            MySession.myConsole.printf("\t\tContact Name: %s%n", displayName);

            // Ensure our certificate file name and contents are valid
            if (args.Length > argsLimit)
            {
                // AppKeyPairMgrmethods will issue all appropriate status and/or error messages!
                if ((!myAppKeyPairMgr.resolveAppKeyPairPath(args[argsLimit])) ||
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
                doPstnContact(mySession, newPstn, displayName, commandOpt);
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
         * List, add, or delete Contacts.
         * 
         * @param mySession
         *	Populated session object.
         * @param pstn
         * 	Properly formatted phone number of the target PSTN Contact.
         * @param displayName
         * 	Display name of the target PSTN Contact (used by add <em>only</em>).
         * @param commandOpt
         * 	Command string, which must be one of:
         * 	<ul>
         * 	  <li>{@link #ADD_CONTACT}</li>
         * 	  <li>{@link #DELETE_CONTACT}</li>
         * 	  <li>{@link #LIST_CONTACTS}</li>
         * 	</ul>
         * 
         * @since 1.0
         */
        static void doPstnContact(MySession mySession, String pstn, String displayName, String commandOpt)
        {

            // Verify that our command option is valid -- something our invoker should have already done!
            if ((!(commandOpt.Equals(LIST_CONTACTS))) && (!(commandOpt.Equals(ADD_CONTACT))) &&
                (!(commandOpt.Equals(DELETE_CONTACT))))
            {
                // We shouldn't get here -- the invoker should have already validated the command.
                MySession.myConsole.printf("%s: Unrecognized command option: %s%n", mySession.myTutorialTag, commandOpt);
                return;
            }

            int contactIdx;
            Skype.NormalizeIdentityResponse nrmlResponse = null;

            ContactGroup soContactGroup = mySession.mySkype.getHardwiredContactGroup(ContactGroup.Type.SKYPEOUT_BUDDIES);
            Contact[] soContactList = soContactGroup.getContacts();
            int contactCount = soContactList.Length;

            // Handle list operations...
            if (commandOpt.Equals(LIST_CONTACTS))
            {
                // Make sure there's something to list!
                if (contactCount == 0)
                {
                    MySession.myConsole.printf("%s: There are no PSTN contacts.%n", mySession.myTutorialTag);
                    return;
                }
                MySession.myConsole.printf("%s: Current list of PSTN contacts:%n", mySession.myTutorialTag);
                for (contactIdx = 0; contactIdx < contactCount; contactIdx++)
                {
                    MySession.myConsole.printf("%s: %d. %s (%s)%n", mySession.myTutorialTag, (contactIdx + 1),
                                            soContactList[contactIdx].getPstnNumber(),
                                            soContactList[contactIdx].getDisplayName());
                }
                return;
            }

            //Handle add & delete operations...
            String contactPstn;
            bool contactAlreadyListed = false;

            // Ensure that the pstn argument contains a valid contact identity
            nrmlResponse = getNormalizationStr(pstn);
            if (nrmlResponse.result != Skype.NormalizeResult.IDENTITY_OK)
            {
                MySession.myConsole.printf("%s: Cannot normalize pstn %s using %s%n",
                                        mySession.myTutorialTag, pstn,
                                        mySession.mySkype.getIsoCountryInfo().countryPrefixList[0]);
                return;
            }

            // Check whether the PSTN contact already exists, which is relevant to both
            // adding and removing contacts. In current wrapper version, the only way to do this
            // is to loop over a contact group. 
            for (contactIdx = 0; contactIdx < contactCount; contactIdx++)
            {
                contactPstn = soContactList[contactIdx].getPstnNumber();
                if (contactPstn.Equals(nrmlResponse.normalized))
                {
                    contactAlreadyListed = true;
                }
            }

            // Handle adding a Contact. The Contact must not exist in that group!
            if (commandOpt.Equals(ADD_CONTACT))
            {
                if (contactAlreadyListed)
                {
                    MySession.myConsole.printf("%s: Error: %s already present in ContactGroup.%n",
                                            mySession.myTutorialTag, nrmlResponse.normalized);
                    return;
                }
                MySession.myConsole.printf("%s: Adding PSTN Contact...%n", mySession.myTutorialTag);
                Contact newContact = mySession.mySkype.getContact(nrmlResponse.normalized);
                if ((newContact != null) && (soContactGroup.canAddContact(newContact)))
                {
                    newContact.giveDisplayName(displayName);
                    soContactGroup.addContact(newContact);
                    MySession.myConsole.printf("%s: Contact %s (%s) added.%n",
                                            mySession.myTutorialTag, nrmlResponse.normalized, displayName);
                }
                else
                {
                    ContactGroup.Type soContactGroupType = soContactGroup.getType();
                    MySession.myConsole.printf("%s: Cannot add Contact %s (%s) to ContactGroup %s (\"%s\") using AddContact():%n",
                                            mySession.myTutorialTag, nrmlResponse.normalized, displayName,
                                            soContactGroupType.toString(),
                                            soContactGroup.getGivenDisplayName());
                    if (newContact == null)
                    {
                        MySession.myConsole.println("\tCould not create new Contact (normalized PSTN likely invalid)");
                    }
                    else if (!(soContactGroup.canAddContact(newContact)))
                    {
                        MySession.myConsole.println("\tCannot add Contacts to target ContactGroup");
                    }
                    else
                    {
                        MySession.myConsole.println("\tReason unknown?!?%n");
                    }
                }
                return;
            }

            // Handle deleting a Contact. The Contact must exist in that group!
            if (!contactAlreadyListed)
            {
                MySession.myConsole.printf("%s: PSTN Contact %s not present in ContactGroup.%n",
                                        mySession.myTutorialTag, nrmlResponse.normalized);
                return;
            }

            MySession.myConsole.printf("%s: Removing PSTN Contact...%n", mySession.myTutorialTag);
            Contact removableContact = mySession.mySkype.getContact(nrmlResponse.normalized);
            if ((removableContact != null) && (soContactGroup.canRemoveContact()))
            {
                String removableDisplayName = removableContact.getDisplayName();
                soContactGroup.removeContact(removableContact);
                // Can't include any Contact-specific identifying information in the message that we haven't already
                // extracted since RemoveContact leaves the target Contact instance in an undefined (mostly nulled-out) state!
                MySession.myConsole.printf("%s: Removed PSTN Contact %s (\"%s\").%n",
                        mySession.myTutorialTag, nrmlResponse.normalized, removableDisplayName);
            }
            else
            {
                ContactGroup.Type soContactGroupType = soContactGroup.getType();
                MySession.myConsole.printf("%s: Cannot remove Contact %s from ContactGroup %s (\"%s\") using RemoveContact():%n",
                                        mySession.myTutorialTag, nrmlResponse.normalized,
                                        soContactGroupType.toString(),
                                        soContactGroup.getGivenDisplayName());
                if (removableContact == null)
                {
                    MySession.myConsole.println("\tCould not remove Contact (normalized PSTN likely invalid)");
                }
                else if (!(soContactGroup.canRemoveContact()))
                {
                    MySession.myConsole.println("\tCannot remove Contacts from target ContactGroup");
                }
                else
                {
                    MySession.myConsole.println("\tReason unknown?!?%n");
                }
            }

            return;
        }

        /**
         * Normalizes a phone number and indicates that operation's success/failure.
         * <br /><br />
         * Determines the country code dialing prefix through {@link com.skype.api.Skype#getIsoCountryInfo()}
         * by matching the default Locale country with an entry in the
         * {@link com.skype.api.Skype.GetIsoCountryInfoResponse#countryCodeList}.
         * Writes a message to the console indicating success/failure reason.
         * 
         * @param pstn
         * 	Phone number to normalize.
         * 
         * @return
         *   The normalization result, which includes:
         *   <ul>
         *     <li>an Enum instance detailing success/failure reason.</li>
         *     <li>the normalized string (success) or error message string (failure)</li>
         *   </ul>
         * 
         * @see com.skype.api.Skype#normalizePstnWithCountry(String, int)
         * @see com.skype.api.Skype#getIsoCountryInfo()
         * 
         * @since 1.0
         */
        public static Skype.NormalizeIdentityResponse getNormalizationStr(String pstn)
        {
            Skype.NormalizeIdentityResponse nrmlResponseReturn = new com.skype.api.Skype.NormalizeIdentityResponse((mySession.mySkype));

            Skype.GetIsoCountryInfoResponse isoInfo = mySession.mySkype.getIsoCountryInfo();
            int availCountryCodes = isoInfo.countryCodeList.Length;
            int isoInfoIdx;
            String ourCountryCode = Locale.getDefault().getCountry();
            for (isoInfoIdx = 0; isoInfoIdx < availCountryCodes; isoInfoIdx++)
            {
                if (ourCountryCode.Equals(isoInfo.countryCodeList[isoInfoIdx], StringComparison.CurrentCultureIgnoreCase))
                {
                    break;
                }
            }
            if (isoInfoIdx >= availCountryCodes)
            {
                nrmlResponseReturn.result = Skype.NormalizeResult.IDENTITY_EMPTY; // Anything but IDENTITY_OK...
                nrmlResponseReturn.normalized = "Couldn't match Locale!";
                MySession.myConsole.printf("%s: Error! Couldn't match Locale %s in Skype.getIsoCountryInfo results%n",
                        mySession.myTutorialTag, ourCountryCode);
                return (nrmlResponseReturn);
            }
            MySession.myConsole.printf("%n%s ISOInfo match (%d of %d):%n\tCode: %s%n\tDialExample: %s%n\tName: %s%n\tPrefix: %s%nLocale: %s%n%n",
                    mySession.myTutorialTag, (isoInfoIdx + 1),
                    mySession.mySkype.getIsoCountryInfo().countryCodeList.Length,
                    mySession.mySkype.getIsoCountryInfo().countryCodeList[isoInfoIdx],
                    mySession.mySkype.getIsoCountryInfo().countryDialExampleList[isoInfoIdx],
                    mySession.mySkype.getIsoCountryInfo().countryNameList[isoInfoIdx],
                    mySession.mySkype.getIsoCountryInfo().countryPrefixList[isoInfoIdx],
                    Locale.getDefault().getCountry());

            Skype.NormalizePstnWithCountryResponse nrmlResponse =
                mySession.mySkype.normalizePstnWithCountry(pstn, isoInfo.countryPrefixList[isoInfoIdx]);

            if (nrmlResponse.result == Skype.NormalizeResult.IDENTITY_OK)
                nrmlResponseReturn.normalized = nrmlResponse.normalized;
            else if (nrmlResponse.result == Skype.NormalizeResult.IDENTITY_EMPTY)
                nrmlResponseReturn.normalized = "Identity input was empty";
            else if (nrmlResponse.result == Skype.NormalizeResult.IDENTITY_TOO_LONG)
                nrmlResponseReturn.normalized = "Identity string too long";
            else if (nrmlResponse.result == Skype.NormalizeResult.IDENTITY_CONTAINS_INVALID_CHAR)
                nrmlResponseReturn.normalized = "Invalid character(s) found in identity string";
            else if (nrmlResponse.result == Skype.NormalizeResult.PSTN_NUMBER_TOO_SHORT)
                nrmlResponseReturn.normalized = "PSTN number too short";
            else if (nrmlResponse.result == Skype.NormalizeResult.PSTN_NUMBER_HAS_INVALID_PREFIX)
                nrmlResponseReturn.normalized = "Invalid character(s) found in PSTN prefix";
            else if (nrmlResponse.result == Skype.NormalizeResult.SKYPENAME_STARTS_WITH_NONALPHA)
                nrmlResponseReturn.normalized = "Skype Name string starts with non-alphanumeric character";
            else if (nrmlResponse.result == Skype.NormalizeResult.SKYPENAME_SHORTER_THAN_6_CHARS)
                nrmlResponseReturn.normalized = "Skype Name too short";
            else
                nrmlResponseReturn.normalized = "Cannot determine Skype.NORMALIZATION ?!?";

            if (nrmlResponse.result != Skype.NormalizeResult.IDENTITY_OK)
            {
                MySession.myConsole.printf("%s: Error! Raw PSTN: %s - Normalized PSTN: %s.%n",
                                        mySession.myTutorialTag, pstn, nrmlResponseReturn.normalized);
            }
            else
            {
                MySession.myConsole.printf("%s: Raw PSTN: %s / Normalized PSTN: %s.%n",
                                        mySession.myTutorialTag, pstn, nrmlResponseReturn.normalized);
            }

            nrmlResponseReturn.result = nrmlResponse.result;
            return nrmlResponseReturn;
        }
    }
}