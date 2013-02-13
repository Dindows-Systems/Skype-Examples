using System;
using java.text;

namespace Skypekit.NET
{
    public class XmlStrMgr
    {
        /**
	 * Info/Debug console output message prefix/identifier tag.
	 * Corresponds to class name.
	 * 
	 * @since 1.0
	 */
        public static String MY_CLASS_TAG = "XmlStrMgr";

        /**
         * Debug console output level: true for verbose; false for normal (default).
         * 
         * @since 1.0
         */
        private bool verboseDebugLvl = false;

        private static ParsePosition parsePos = new ParsePosition(0);
        private java.lang.Number parseResult;
        private static DecimalFormat parseFmt = new DecimalFormat();


        /**
         * "Parse" an XML document for the first occurrence of a particular tag and return its value.
         * 
         * The parse terminates upon encountering the <em>first</em> opening angle bracket (<) following
         * the opening target tag. 
         * 
         * @param xmlDoc
         * 	The target XML document. 
         * @param xmlTag
         * 	The target tag <em>including</em> the enclosing angle brackets.
         * @param xmlStart
         * 	The character position (from zero) in the document at which to start
         *  looking for the target tag.
         * 
         * @return
         * 	<ul>
         * 		<li>a String representation of the element value, which will be the empty
         * 			string if target tag is empty, for example, <code>&lt;part&gt;&lt;/part&gt;</code></li>
         * 		<li>null if not found</li>
         * </ul>
         * 
         * @since 1.0
         */
        public String getXmlValueStr(String xmlDoc, String xmlTag, ParsePosition xmlStart)
        {

            if (verboseDebugLvl)
            {
                MySession.myConsole.printf("%s.getXmlValueStr: xmlDoc =%n%s%nxmlTag = %s%nstartIdx = %d%n",
                                MY_CLASS_TAG, xmlDoc, xmlTag, xmlStart.getIndex());
            }

            int i = xmlDoc.IndexOf(xmlTag, xmlStart.getIndex());
            if (i != -1)
            {
                i += xmlTag.Length;
                int j = xmlDoc.IndexOf("</", i);
                return (xmlDoc.Substring(i, j));
            }
            return (null);
        }


        /**
         * "Parse" an XML document for the first occurrence of a particular tag and return its value, which is assumed to be a number.
         * 
         * The parse terminates based on the rules for java.text.DecimalFormat, using the
         * pattern and symbol sets for the default Locale.
         * 
         * @param xmlDoc
         * 	The target XML document. 
         * @param xmlTag
         * 	The target tag <em>including</em> the enclosing angle brackets.
         * @param xmlStart
         * 	The character position (from zero) in the document at which to start
         *  looking for the target tag.
         * 
         * @return
         * 	<ul>
         * 		<li>an integer representation of the element value</li>
         * 		<li>-1 if:
         * 			<ul>
         * 				<li>not found</li>
         * 				<li>the target tag is empty, for example, <code>&lt;part&gt;&lt;/part&gt;</code></li>
         * 				<li>a parse error occurred</li>
         * 			</ul>
         * 		</li>
         * 	</ul>
         * 
         * @since 1.0
         */
        public int getXmlValueNum(String xmlDoc, String xmlTag, ParsePosition xmlStart)
        {

            if (verboseDebugLvl)
            {
                MySession.myConsole.printf("%s.getXmlValueNum: xmlDoc =%n%s%nxmlTag = %s%nstartIdx = %d%n",
                                MY_CLASS_TAG, xmlDoc, xmlTag, xmlStart.getIndex());
            }

            parseFmt.setParseBigDecimal(false);
            parsePos.setErrorIndex(-1);

            int i = xmlDoc.IndexOf(xmlTag, xmlStart.getIndex());
            if (i != -1)
            {
                parsePos.setIndex((i + xmlTag.Length));
                if ((parseResult = parseFmt.parse(xmlDoc, parsePos)) != null)
                {
                    return (parseResult.intValue());
                }
            }
            return (-1);
        }

        /**
         * "Parse" an XML document for the first occurrence of a particular substring and
         * return the position of the character <em>following</em> it.
         * 
         * This enables the invoker to "count" its way through an XML document (by placing
         * the invocation in a loop), access attribute values, skip over closing XML tags,
         * and so forth.
         * 
         * @param xmlDoc
         * 	The target XML document. 
         * @param subStr
         * 	The target substring, typically an opening XML tag and its initial attribute
         * 	<em>or</em> a closing XML tag, such as:
         * <ul>
         * 	<li><code>&lt;part identity="</code></li>
         * 	<li><code>&lt;/part&gt;</code></li>
         * </ul>
         * @param xmlStart
         * 	The character position (from zero) in the document at which to start
         *  looking for the target substring.
         * 
         * @return
         * 	A ParsePosition instance with its index set to the position of the character
         *  <em>following</em> the target substring or null if not found.
         * 
         * @since 1.0
         */
        public ParsePosition getXmlSubStrPos(String xmlDoc, String subStr, ParsePosition xmlStart)
        {

            if (verboseDebugLvl)
            {
                MySession.myConsole.printf("%s.getXmlSubStrPos: xmlDoc =%n%s%nsubStr = %s%nstartIdx = %d%n",
                        MY_CLASS_TAG, xmlDoc, subStr, xmlStart.getIndex());
            }

            parsePos.setErrorIndex(-1);

            int i = xmlDoc.IndexOf(subStr, xmlStart.getIndex());
            if (i != -1)
            {
                parsePos.setIndex((i + subStr.Length));
                return (parsePos);
            }

            return (null);
        }


        /**
         * Determine whether verbose debug is set.
         * 
         * @return
         * 	<ul>
         * 		<li>true: verbose debug set</li>
         * 		<li>false: normal debug set</li>
         * </ul>
         * 
         * @since 1.0
         */
        public bool getVerboseDebug()
        {

            return (this.verboseDebugLvl);
        }


        /**
         * Turn verbose debug on/off.
         * 
         * @param onOff
         * 	<ul>
         * 		<li>true: turn on verbose debug</li>
         * 		<li>false: turn off verbose debug</li>
         * </ul>
         * 
         * @since 1.0
         */
        public void setVerboseDebug(bool onOff)
        {

            this.verboseDebugLvl = onOff;
        }
    }
}