using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Threading;
using System.Runtime.InteropServices;
using System.IO;
using System.ServiceModel;
using SkypeAutoHelper;
using HumanActionSimulation;
using WindowFinderNET;
using InjectorLib;
using SKYPE4COMLib;

namespace AdviserSkypeDriver
{
    public partial class FormAdviser : Form
    {
        #region Constants

        const string targetAppName = "Skype.exe";
        const string pluginName = "SkypePlugin.dll";        
        const string targetWndClassName = "TLiveConversationWindow";

        #endregion

        private ServiceHost serviceHost = null;                        
        public static string UserId { private set; get; }
        private System.Windows.Forms.Timer timer = new System.Windows.Forms.Timer();

        public FormAdviser()
        {
            InitializeComponent();

            txbUser.Text = string.Empty;

            btnInject.Enabled = false;
            btnCloseSkype.Enabled = false;
            btnCall.Enabled = false;
           
            CloseServiceHost();

            try
            {
                // Create service
                serviceHost = new ServiceHost(typeof(CommSvc));

                // Open service
                serviceHost.Open();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString(), Name, MessageBoxButtons.OK, MessageBoxIcon.Error);
                serviceHost = null;
            }

            timer.Tick += new EventHandler(timer_Tick);
            timer.Interval = 2000;
        }

        public void CloseServiceHost()
        {
            if (null != serviceHost)
                // Close the service hostBase
                serviceHost.Close();

            if (timer != null)
                timer.Dispose(); 
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
                btnAttach.Enabled = false;
                btnCall.Enabled = false;
                btnInject.Enabled = false;
                btnCloseSkype.Enabled = true;

                SkypeAutomation.SkypeObj.MessageStatus += new _ISkypeEvents_MessageStatusEventHandler(skype_MessageStatus);

                timer.Start();
            }
            else
                Close();
        }

        private void timer_Tick(object sender, EventArgs e)
        {
            btnCall.Enabled = false;
            if (SkypeAutomation.SkypeObj != null)
            {
                User user = null;
                if (!string.IsNullOrEmpty(txbUser.Text))
                {
                    try
                    {
                        // Check whether user specified in txbUser text box is available
                        user = SkypeAutomation.SkypeObj.get_User(txbUser.Text);
                        btnCall.Enabled =
                                user.OnlineStatus == TOnlineStatus.olsOnline ||
                                user.OnlineStatus == TOnlineStatus.olsAway ||
                                user.OnlineStatus == TOnlineStatus.olsDoNotDisturb ||
                                user.OnlineStatus == TOnlineStatus.olsSkypeMe;
                    }
                    catch { }
                }
            }
        }

        private void btnCall_Click(object sender, EventArgs e)
        {
            timer.Stop();
            btnCall.Enabled = false;
            UserId = txbUser.Text;
            SkypeAutomation.PlaceCall(this, new SkypeAutomation.MainThreadActionDelegate(AfterPlaceCall), UserId);
        }

        private void AfterPlaceCall(bool ok)
        {
            if (ok)
                btnInject.Enabled = true;
            else
                btnCall.Enabled = true;
        }

        private void btnInject_Click(object sender, EventArgs e)
        {
            string pluginPath = string.Format(@"{0}\{1}", System.Windows.Forms.Application.StartupPath, pluginName);
            if (File.Exists(pluginPath))
            {
                try
                {
                    // Inject plugin to Skype process
                    new InjHelperClass().Run(targetAppName, pluginPath, targetWndClassName);
                    btnCall.Enabled = false;
                    btnInject.Enabled = false;
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.ToString(), Name, MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            else
                MessageBox.Show("Skype plugin is not found.", Name, MessageBoxButtons.OK, MessageBoxIcon.Error);
        }

        private void skype_MessageStatus(ChatMessage message, TChatMessageStatus status)
        {
            if (status == TChatMessageStatus.cmsReceived)
            {
                // Get commands as text messages from User Skype Driver
                SkypeAutoHelper.Command command = SkypeAutoHelper.Command.Create(message.Body);

                switch (command.Name)
                { 
                    case "screenbounds":
                        UserData.Instance.ScreenBounds = new Size(int.Parse(command.Params[0]), int.Parse(command.Params[1]));
                        break;
                }

                SkypeAutomation.SkypeObj.ClearChatHistory();
            }       
        }

        private void btnCloseSkype_Click(object sender, EventArgs e)
        {
            SkypeAutomation.SkypeObj.Client.Shutdown();
            btnAttach.Enabled =
            btnInject.Enabled =
            btnCall.Enabled = 
            btnCloseSkype.Enabled = false;

            timer.Stop();
            
            Thread.Sleep(3000);

            btnAttach.Enabled = true;
        }
    }
}
