using System;
using com.skype.api;

namespace Skypekit.NET
{
    public class ParseSkypeKitVersion
    {
        /**
	 * Info/Debug console output message prefix/identifier tag <em>prefix</em>.
	 * Corresponds to class name.
	 * 
	 * @since 1.0
	 */
        public static String MY_CLASS_TAG = "ParseSkypeKitVersion";

        /**
         * The SkypeKit version string, as returned by com.skype.api.Skype.GetVersionString.
         * 
         * @since 1.0
         */
        protected static String versionStr;

        /**
         * Number of components in the version number string.
         * 
         * @since 1.0
         */
        protected static int versionNumCnt = 4;

        /**
         * Parsed array of the individual component version numbers.
         * 
         * @since 1.0
         */
        protected static String[] versionNums = new String[versionNumCnt];


        /**
         * Tutorial ructor.
         * <br /><br />
         * Obtain the skypeKit version string, for example:
         * <pre>
         * 2.0/windows-x86-skypekit-novideo_3.1.0.2689_125068
         * </pre>
         * and:
         * <ul>
         *   <li>store it in {@link #versionStr}</li>
         *   <li>split it at the underscores, yielding "2.0/windows-x86-skypekit-novideo",
         *   	"3.1.0.2689", and "125068"</li>
         *   <li>split the version number segment at the periods, yielding "3", "1", "0", and "2689"</li>
         *   <li>store the <i>number</i> of version number components in {@link #versionNumCnt}</li>
         *   <li>store the actual version number components in {@link #versionNums}</li>
         * </ul>
         * 
         * @since 1.0
         */
        public ParseSkypeKitVersion(Skype mySkype)
        {
            String[] versionParts;

            ParseSkypeKitVersion.versionStr = mySkype.getVersionString();
            if (ParseSkypeKitVersion.versionStr.Length > 1)
            {
                versionParts = ParseSkypeKitVersion.versionStr.Split('_');

                ParseSkypeKitVersion.versionNums = versionParts[1].Split(new string[] { "\\." }, ParseSkypeKitVersion.versionNumCnt, StringSplitOptions.None);
                /*
                            System.out.println(ParseSkypeKitVersion.versionStr);
                            System.out.println("0: " + versionParts[0]);
                            System.out.println("1: " + versionParts[1]);
                            System.out.println("2: " + versionParts[2]);
                            System.out.println("Major: " + versionNums[0]);
                            System.out.println("Minor: " + versionNums[1]);
                            System.out.println("Patch: " + versionNums[2]);
                            System.out.flush();
                 */
            }
        }


        /**
         * Obtain the <em>complete</em> unparsed version string exactly as as returned by com.skype.api.Skype.GetVersionString
         * 
         * @return
         * 	The unparsed SkypeKit version string.
         * 
         * @since 1.0
         */
        public String getVersionStr()
        {

            return (ParseSkypeKitVersion.versionStr);
        }


        /**
         * Obtain the <em>major</em> SkypeKit version number.
         * 
         * @return
         * 	The major SkypeKit version number, for example,</br />
         * 	&nbsp;&nbsp;&nbsp;&nbsp;<code>2.0/windows-x86-skypekit-novideo_3.1.0.2689_125068</code>
         *  <br />
         * 	would return 3.
         * 
         * @since 1.0
         */
        public int getMajorVersion()
        {
            if (ParseSkypeKitVersion.versionStr.Length > 0)
                return (int.Parse(ParseSkypeKitVersion.versionNums[0].Replace(".", "")));
            else
            {
                return 0;
            }

        }

        /**
         * Obtain the <em>minor</em> SkypeKit version number.
         * 
         * @return
         * 	The minor SkypeKit version number, for example,</br />
         * 	&nbsp;&nbsp;&nbsp;&nbsp;<code>2.0/windows-x86-skypekit-novideo_3.1.0.2689_125068</code>
         *  <br />
         * 	would return 1 (one).
         * 
         * @since 1.0
         */
        public int getMinorVersion()
        {
            if (ParseSkypeKitVersion.versionStr.Length > 0)
                return (int.Parse(ParseSkypeKitVersion.versionNums[0].Replace(".", "")));
            else
            {
                return 0;
            }
        }

        /**
         * Obtain the <em>patch</em> SkypeKit version number.
         * 
         * @return
         * 	The patch SkypeKit version number, for example,</br />
         * 	&nbsp;&nbsp;&nbsp;&nbsp;<code>2.0/windows-x86-skypekit-novideo_3.1.0.2689_125068</code>
         *  <br />
         * 	would return 0 (zero).
         * 
         * @since 1.0
         */
        public int getPatchVersion()
        {
            if (ParseSkypeKitVersion.versionStr.Length > 0)
                return (int.Parse(ParseSkypeKitVersion.versionNums[0].Replace(".", "")));
            else
            {
                return 0;
            }
        }
    }
}
