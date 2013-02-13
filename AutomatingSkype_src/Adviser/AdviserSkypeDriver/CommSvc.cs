using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;
using System.Threading;
using SkypeAutoHelper;

namespace AdviserSkypeDriver
{
    public class CommSvc : ICommSvc
    {
        public void SendMessage(string user, string message)
        {
            ThreadPool.QueueUserWorkItem(state => { SkypeAutomation.SkypeObj.SendMessage(FormAdviser.UserId, message); });       
        }

        public object GetInfo(string user, string message)
        {
            object ro = null;

            switch (message.ToLower())
            { 
                case "userscreensize":
                    ro = string.Format("{0},{1}", UserData.Instance.ScreenBounds.Width, UserData.Instance.ScreenBounds.Height);
                    break;
            }

            return ro;
        }
    }
}
