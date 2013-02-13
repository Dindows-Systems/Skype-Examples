using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

namespace AdviserSkypeDriver
{
    /// <summary>
    /// Singleton class containing data for Adviser Skype Driver
    /// </summary>
    public class UserData
    {
        private static UserData helper = null;

        public Size ScreenBounds { set; get; }

        public static UserData Instance
        {
            get
            {
                if (helper == null)
                    helper = new UserData();

                return helper;
            }
        }

        private UserData()
        {
        }
    }
}
