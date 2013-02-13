using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Threading;
using SkypeAutoHelper;
using HumanActionSimulation;
using WindowFinderNET;
using SKYPE4COMLib;

namespace UserSkypeDriver
{
    public partial class FormUser : Form
    {
        private Processor processor;
        private int uniqueMsgCount = 0;

        public FormUser()
        {
            InitializeComponent();

            processor = new Processor(this);

            txbConsultant.Text = string.Empty;
            btnAttach.Enabled = true;
            btnCloseSkype.Enabled = false;
        }

        private void btnAttach_Click(object sender, EventArgs e)
        {
            btnAttach.Enabled = false;
            SkypeAutomation.Connect(this, new SkypeAutomation.MainThreadActionDelegate(AfterConnect));
        }

        private void AfterConnect(bool ok)
        {
            if (ok)
            {               
                btnCloseSkype.Enabled = true;

                SkypeAutomation.SkypeObj.MessageStatus += new _ISkypeEvents_MessageStatusEventHandler(skype_MessageStatus);
                SkypeAutomation.SkypeObj.CallStatus += new _ISkypeEvents_CallStatusEventHandler(skype_CallStatus);
            }
            else
                btnAttach.Enabled = true;
        }

        private void skype_CallStatus(Call call, TCallStatus status)
        {
            if (status == TCallStatus.clsRinging)
            {
                if (call.PartnerHandle == txbConsultant.Text)
                {
                    call.Answer();
                    Point screenBounds = ScreenBounds;
                    SkypeAutomation.SkypeObj.SendMessage(txbConsultant.Text, string.Format("screenbounds({0},{1})", screenBounds.X, screenBounds.Y));

                    SkypeAutomation.ShareFullScreen();
                }
                else
                    call.Finish();
            }
        }

        private void skype_MessageStatus(ChatMessage message, TChatMessageStatus status)
        {     
            if (status == TChatMessageStatus.cmsReceived)
            {
                try
                {
                    SkypeAutoHelper.Command command = SkypeAutoHelper.Command.Create(message.Body);
                    if (command != null && command.UniqueCounter != uniqueMsgCount)
                    {
                        uniqueMsgCount = command.UniqueCounter;
                        Do(command.Name, command.Params); 
                    }
                }
                catch (Exception e)
                { 
                }

                SkypeAutomation.SkypeObj.ClearChatHistory();
            }
        }

        public void Do(string command, string[] pmrs)
        {
            try
            {
                processor.GetType().GetMethod(command.ToLower()).Invoke(processor, new object[] { pmrs });
            }
            catch (Exception e)
            {
                MessageBox.Show(string.Format("Method \"{0}\": ", command) + e.ToString(), "SkypeHandlerNET");
            }
        }

        private void btnCloseSkype_Click(object sender, EventArgs e)
        {
            SkypeAutomation.SkypeObj.Client.Shutdown();
            btnAttach.Enabled = false;
            btnCloseSkype.Enabled = false;

            Thread.Sleep(3000);

            btnAttach.Enabled = true;
        }

        private static Point ScreenBounds
        {
            get
            {
                return new Point(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);
            }
        }
    }
}
