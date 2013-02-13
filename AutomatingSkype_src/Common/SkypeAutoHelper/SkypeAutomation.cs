using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading;
using System.Windows.Forms;
using WF = System.Windows.Forms;
using System.Runtime.InteropServices;
using System.IO;
using System.Reflection;
using System.Diagnostics;
using HumanActionSimulation;
using WindowFinderNET;
using SKYPE4COMLib;

namespace SkypeAutoHelper
{
    public static class SkypeAutomation
    {
        #region Constants

        readonly static int[] compactViewMenuItem = new int[2] { 4, 14 };
        
        #endregion

        public delegate void MainThreadActionDelegate(bool ok);

        public static Skype SkypeObj { private set; get; }

        private static AutoResetEvent ev = new AutoResetEvent(false);

        static SkypeAutomation()
        {
            SkypeObj = null;
            try
            {
                SkypeObj = new Skype();
            }
            catch { }

            if (SkypeObj == null)
            {
                try
                {
                    RegisterComObject("skype4com");
                    SkypeObj = new Skype();
                }
                catch (Exception ex)
                {
                    string msg = "Skype4COM.dll is not registered as COM DLL.\n" + ex.ToString();
                    MessageBox.Show(msg, WF.Application.ProductName, MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }

        private static void RegisterComObject(string comDllName)
        {
            Process process = new Process();
            process.StartInfo = new ProcessStartInfo("regsvr32.exe", string.Format("/s {0}.dll", comDllName));
            process.Start();
            process.WaitForExit();
        }

        public static void Connect(Form form, MainThreadActionDelegate dlgtAfterConnect)
        {
            if (form != null && dlgtAfterConnect != null)
                ThreadPool.QueueUserWorkItem(new WaitCallback(state => { form.Invoke(dlgtAfterConnect, new object[] { Connect() }); }));         
        }

        private static bool Connect()
        {
            const int maxAttempts = 30;
            bool br = IsSkypeRunning;
            if (!br)
            {
                // Start with no splash screen 
                SkypeObj.Client.Start(false, true);
                Thread.Sleep(7000);
            }

            Exception ex = null;
            for (int i = 0; i < 3; i++)
            {
                // Mechanism to allow access
                Thread thread = thread = new Thread(new ThreadStart(() =>
                {
                    int downCount = 30 * maxAttempts;
                    SetToCompactView();
                    while (!ev.WaitOne(2000) && downCount-- > 0)
                    {
                        SetToCompactView();
                        AllowAccess();
                    }
                }));
                thread.Start();

                SetToCompactView();

                try
                {
                    SkypeObj.Attach(6, true);
                    br = true;
                }
                catch (Exception e)
                {
                    ex = e;
                }
                finally
                {
                    ev.Set();
                    thread.Join();
                }

                if (br)
                    break;
            }

            if (!br)
                MessageBox.Show("Skype start / connection problem!\n" + ex.ToString(),
                        WF.Application.ProductName, MessageBoxButtons.OK, MessageBoxIcon.Error);
            
            return br;
        }

        private static bool IsSkypeRunning
        {
            get
            {
                const string processName = "Skype";
                foreach (Process process in Process.GetProcesses()) 
		            if (process.ProcessName == processName)
		                return true;
		            
	            return false;
            }
        }

        public static void AllowAccess()
        {
            ActionSimulation.CommandWithClick("TCommunicatorForm", 500, 110, 0.37, 0.8);
        }

        public static void SetToCompactView()
        {
            ActionSimulation.ActivateMenuItem("tSkMainForm", compactViewMenuItem[0], compactViewMenuItem[1]);
        }

        public static void ShareFullScreen()
        {
            const string wndClass = "TConversationForm";
            int width;
            int height = width = 500;
            
            Thread.Sleep(1000);

            // Share screen action
            ActionSimulation.CommandWithClick(wndClass, width, height, 0.53, 0.9);

            Thread.Sleep(1000);

            // Full screen action
            ActionSimulation.CommandWithClick(wndClass, width, height, 0.53, 0.75);
        }

        public static void PlaceCall(Form form, MainThreadActionDelegate dlgtAfterPlaceCall, string userId)
        {
            if (form != null && dlgtAfterPlaceCall != null)
                ThreadPool.QueueUserWorkItem(new WaitCallback(state => { form.Invoke(dlgtAfterPlaceCall, new object[] { PlaceCall(userId) }); }));
        }

        public static bool PlaceCall(string userId)
        {
            bool br = false;
            try
            {
                SkypeObj.PlaceCall(userId, "", "", "");
                br = true;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString(), WF.Application.ProductName, MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

            return br;
        }
    }
}
