using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SkypeAutoHelper
{
    public class Command
    {
        public string Name { private set; get; }
        public string[] Params { private set; get; }
        public int UniqueCounter { private set; get; }

        public static Command Create(string str)
        {
            Command command = null;
            if (!string.IsNullOrEmpty(str))
            {
                int indexCmd = str.IndexOf("(");
                string commandName = str.Substring(0, indexCmd);
                int indexPmrs = str.LastIndexOf(")");
                string allParameters = str.Substring(indexCmd + 1, indexPmrs - indexCmd - 1);
                string[] pmrs = null;
                if (!string.IsNullOrEmpty(allParameters))
                {                  
                    pmrs = commandName == "s"                        
                        ? pmrs = new string[] { allParameters } // String transfer command "s" always has only one parameter
                        : allParameters.Split(new char[] { ',' });
                }

                int uniqueCounter = -1;
                if (!int.TryParse(str.Substring(indexPmrs + 1, str.Length - indexPmrs - 1), out uniqueCounter))
                    uniqueCounter = -1;
                              
                command = new Command(commandName, pmrs, uniqueCounter);
            }

            return command;
        }

        public Command(string commandName, string[] pmrs, int uniqueCounter)
        {
            Name = commandName;
            Params = pmrs;
            UniqueCounter = uniqueCounter;
        }
    }
}

