using System;

namespace Skypekit.NET
{
    public class SkypeMain
    {
        public SkypeMain()
        {
            APP_KEY_PAIR_IDX = ((REQ_ARG_CNT + OPT_ARG_CNT) - 1);
        }

        /**
     * Info/Debug console output message prefix/identifier tag.
     * Corresponds to class name.
     * 
     * @since 1.0
     */
        public String MY_CLASS_TAG = "SkypeMain";

        /**
         * Index of the account name in the command line argument list.
         * 
         * @since 1.0
         */
        public int ACCOUNT_NAME_IDX = 0;

        /**
         * Index of the account password in the command line argument list.
         * 
         * @since 1.0
         */
        public int ACCOUNT_PWORD_IDX = 1;

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
        public int OPT_ARG_CNT = 1;

        /**
         * Index of the <em>optional</em> AppKeyPair PEM file pathname in
         * the command line argument list, which is always last.
         * 
         * @since 1.0
         */
        public int APP_KEY_PAIR_IDX;

        public AppKeyPairMgr myAppKeyPairMgr = new AppKeyPairMgr();
        public MySession mySession = new MySession();
    }
}