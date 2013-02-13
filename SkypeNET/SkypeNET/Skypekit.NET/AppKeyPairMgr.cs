using System;
using System.IO;
using com.skype.util;

namespace Skypekit.NET
{
    public class AppKeyPairMgr
    {
        /**
		 * Info/Debug console output message prefix/identifier tag.
		 * Corresponds to class name.
		 * 
		 * @since 1.0
		 */
        public static String MY_CLASS_TAG = "AppKeyPairMgr";

        /**
         * Expected suffixes (case insensitive) for the file containing the AppKeyPair data.
         * Used by {@link #resolveAppKeyPairPath(String)}.
         * 
         * @since 1.0
         */
        public static String[] KEY_PAIR_FILE_SUFFIXES = {
	    	"crt",
	    	"pem",
	    	"CRT",
	    	"PEM"
	    };

        /**
         * Default name of the PEM file containing the AppKeyPair data string.
         * Used by {@link #resolveAppKeyPairPath(String)}.
         * 
         * @since 1.0
         */
        public static String KEY_PAIR_DEFAULT_PATHNAME = "Tawasol Version 1.1.pem";

        /**
         * The resolved name of the PEM file containing the certificate.
         * Used by {@link #resolveAppKeyPairPath(String)}.
         * 
         * @since 2.0
         */
        public String pemFilePathname = KEY_PAIR_DEFAULT_PATHNAME;


        /**
         * Retrieves the fully resolved PEM file path.
         * This reflects the resultant path (valid or invalid) used
         * by the latest invocation of
         * <code>@link{#resolveAppKeyPairPath(String)}</code>, or its default
         * if <code>resolveAppKeyPairPath(String)</code> has not been invoked.
         * 
         * @return
         * 	The the fully resolved PEM file path, which might not be a valid PEM file.
         * 
         * @see #KEY_PAIR_DEFAULT_PATHNAME
         * @see #pemFilePathname
         * 
         * @since 2.0
         */
        public String getPemFilePathname()
        {

            return (this.pemFilePathname);
        }

        /**
         * Resolves the AppKeyPair X.509 certificate file name based on the <i>configured default</i> pathname of the PEM file containing the actual AppKeyPair data.
         * Sets @link{pemFilePathname} to the resolved name.
         * 
         * @return
         * 	<ul>
         *	  <li>true: AppKeyPair certificate file exists</li>
         *	  <li>false:
         *	    <ul>
         *	      <li>Could not resolve the pathname</li>
         *	      <li>The specified certificate file does not exist</li>
         *	    </ul>
         *	    pemFilePathname is unchanged.
         *	  </li>
         *	</ul>
         * 
         * @see #KEY_PAIR_DEFAULT_PATHNAME
         * @see #resolveAppKeyPairPath(String)
         * 
         * @since 2.0
         */
        public bool resolveAppKeyPairPath()
        {
            return (resolveAppKeyPairPath(KEY_PAIR_DEFAULT_PATHNAME));
        }

        /**
         * Common method to resolve the AppKeyPair certificate file name.
         * <br /><br />
         * Initially assumes the name of the path of the file containing the AppKeyPair data includes a
         * path component. If it doesn't end in one of the recognized suffixes, assumes its a
         * path-only component and appends the default file pathname {@link #KEY_PAIR_DEFAULT_PATHNAME},
         * which it assumes is configured as a filename. Writes diagnostic messages to the console
         * if the specified file does not exist.
         * <br /><br />
         * This is useful since SkypeKit currently reports only "TLS handshake failure" (with no further explanation)
         * if the certificate can't be found/accessed or is not validly formatted.
         * 
         * @param pathName
         * 	The path of the file containing the actual certificate data.
         * 
         * @return
         * 	<ul>
         *	  <li>true: AppKeyPair successfully read (and set) from the file data</li>
         *	  <li>false:
         *	    <ul>
         *	      <li>Could not open the file</li>
         *	      <li>Could not read the file</li>
         *	      <li>Not a valid certificate file</li>
         *	    </ul>
         *	    AppKeyPair is unchanged.
         *	  </li>
         *	</ul>
         * 
         * @see #KEY_PAIR_FILE_SUFFIXES
         * @see #KEY_PAIR_DEFAULT_PATHNAME
         * 
         * @since 2.0
         */
        public bool resolveAppKeyPairPath(String pathName)
        {
            int i;
            int j;
            FileInfo tmpFile = null;

            j = KEY_PAIR_FILE_SUFFIXES.Length;
            for (i = 0; i < j; i++)
            {
                if (pathName.EndsWith(KEY_PAIR_FILE_SUFFIXES[i]))
                {
                    break;
                }
            }

            // Check for no suffix match - either an unrecognized suffix or just a path name.
            if (i >= j)
            {
                if (pathName[(pathName.Length - 3)] == '.')
                {
                    // Unrecognized suffix (if you mean a path that includes ".xyz" as it's last
                    // four characters, pass it as ".xyz/"
                    MySession.myConsole.printf("%s/resolveAppKeyPairPath: Unrecognized Certificate file suffix.%n\tPathname: %s%n\tRecognized suffixes:%n",
                            MY_CLASS_TAG, pathName);
                    j = KEY_PAIR_FILE_SUFFIXES.Length;
                    for (i = 0; i < j; i++)
                    {
                        MySession.myConsole.printf("\t\t%s%n", KEY_PAIR_FILE_SUFFIXES[i]);
                    }
                    return (false);
                }
                else
                {
                    // Just a path name, so append the default portion of the path.
                    pemFilePathname = pathName + "\\" + KEY_PAIR_DEFAULT_PATHNAME;
                }
            }
            else
            {
                // Found a matching suffix, so go with what we have.
                pemFilePathname = pathName;
            }

            try
            {
                tmpFile = new FileInfo(pathName);
            }
            catch (NullReferenceException e)
            {
                // This should really never happen...
                MySession.myConsole.printf("%s/resolveAppKeyPairPath: Specified pathname is NULL%n",
                        MY_CLASS_TAG);
                pemFilePathname = KEY_PAIR_DEFAULT_PATHNAME;
                return (false);
            }

            if (!tmpFile.Exists)
            {
                MySession.myConsole.printf("%s/resolveAppKeyPairPath: Certificate file doesn't exist:%n\t%s%n",
                        MY_CLASS_TAG, pemFilePathname);
                return (true);
            }

            MySession.myConsole.printf("%s/resolveAppKeyPairPath: Found certificate file:%n\t%s%n",
                   MY_CLASS_TAG, pemFilePathname);
            return (true);
        }

        /**
         * Determines whether the current AppKeyPair (as specified by {@link #pemFilePathname}) is a valid X.509 certificate.
         * <br /><br />
         * Writes diagnostic messages to the console if the the current AppKeyPair does not exist or is not valid.
         * This is useful since SkypeKit currently reports only "TLS handshake failure" (with no further explanation)
         * if the certificate can't be found/accessed or is not validly formatted.
         * 
         * @return
         * 	<ul>
         *	  <li>true: Valid certificate file</li>
         *	  <li>false:
         *	    <ul>
         *	      <li>Could not open the file</li>
         *	      <li>Could not read the file</li>
         *	      <li>Not a valid certificate file</li>
         *	    </ul>
         *	  </li>
         *	</ul>
         * 
         * @see #pemFilePathname
         * @see com.skype.tutorial.util.MySession#myClientConfiguration
         * @since 2.0
         */
        public bool isValidCertificate()
        {
            java.security.cert.X509Certificate x509CertificateData;
            java.security.PrivateKey privateKeyData;

            String pathName = getPemFilePathname();

            try
            {
                String derPath = pathName.Substring(0, pathName.Length - 3);
                derPath += "der";

                PemReader myPemReader = new PemReader(getPemFilePathname());
                x509CertificateData = myPemReader.getCertificate();
                privateKeyData = myPemReader.getKey();
            }
            catch (FileNotFoundException e1)
            {
                MySession.myConsole.printf("%s/isValidCertificate: Could not find certificate file:%n\t%s%n",
                        MY_CLASS_TAG, pathName);
                return (false);
            }
            catch (IOException e2)
            {
                MySession.myConsole.printf("%s/isValidCertificate: Unable to read certificate file:%n\t%s%n",
                           MY_CLASS_TAG, pathName);
                return (false);
            }
            catch (Exception e3)
            {
                MySession.myConsole.printf("%s/isValidCertificate: Certificate file %s contains invalid certficate data.%n",
                        MY_CLASS_TAG, pathName);
                return (false);
            }

            if ((x509CertificateData != null) && (privateKeyData != null))
            {
                MySession.myConsole.printf("%s/isValidCertificate: Certificate has valid format%n",
                       MY_CLASS_TAG);
                return (true);
            }
            else
            {
                MySession.myConsole.printf("%s/isValidCertificate: Certificate has invalid format%n",
                        MY_CLASS_TAG);
                return (false);
            }
        }
    }
}
