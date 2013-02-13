using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;

namespace WindowFinderNET
{
    #region IWndFinder Interface

    [InterfaceType(ComInterfaceType.InterfaceIsDual)]
    [Guid("DAD1D14D-7F77-47D4-BB04-0AFDD58F1206")]
    [ComVisible(true)]
    public interface IWndFinder
    {
        IntPtr GetWindow(string wndClassName);
    }

    #endregion

    #region WndFinder Class

	[ClassInterface(ClassInterfaceType.AutoDual)]
    [Guid("1EE9A897-0E20-4047-8BF3-CCE64C2F062B")]
    [ProgId("WindowFinderNET.WinFinder")]
    [ComVisible(true)]
    public class WndFinder : IWndFinder
	{
		[DllImport("user32")]
		private static extern int GetWindowText(IntPtr hWnd, StringBuilder text, int count);

        private delegate bool EnumWindowsProcDelegate(IntPtr hWnd, int lParam);

		[DllImport("user32")]
		private static extern bool EnumWindows(EnumWindowsProcDelegate dlgtEnumWindowsProc, int lParam);

        [DllImport("user32.dll")]
        private static extern bool EnumChildWindows(IntPtr hWndParent, EnumWindowsProcDelegate dlgtEnumWindowsProc, int lParam);

        [DllImport("user32.dll", SetLastError = true, CharSet = CharSet.Auto)]
        static extern int GetClassName(IntPtr hWnd, StringBuilder className, int maxCount);
        
        [DllImport("user32")]
        public static extern IntPtr GetParent(IntPtr hWnd);

        private string WndClassName { set; get; }
        private IntPtr WndHandle { set; get; }

        private EnumWindowsProcDelegate dlgtEnumWindowsProc = null;

        const int maxAttempts = 10;
        const int interval = 20;

        public WndFinder()
        {
            dlgtEnumWindowsProc = new EnumWindowsProcDelegate(ProcessWindow);
        }

        [ComVisible(true)]
        public IntPtr GetWindow(string wndClassName)
        {
            WndHandle = IntPtr.Zero;
            if (!string.IsNullOrEmpty(wndClassName))
            {
                WndClassName = wndClassName;

                for (int i = 0; i < maxAttempts; i++ )
                {
                    EnumWindows(dlgtEnumWindowsProc, 0);
                    if (WndHandle != IntPtr.Zero)
                        break;
                    else
                        Thread.Sleep(20);
                }
            }

            return WndHandle;
        }

        private bool ProcessWindow(IntPtr hWnd, int lParam)
        {
            StringBuilder sbClassName = new StringBuilder(1000);
            GetClassName(hWnd, sbClassName, sbClassName.Capacity);
            if (sbClassName.ToString() == WndClassName)
            {
                WndHandle = hWnd;
                return false;
            }
            else
            {
                EnumChildWindows(hWnd, dlgtEnumWindowsProc, 0);
                return true;
            }
        }  
	}

    #endregion
}

//private static bool PrintWindow(IntPtr hWnd, int lParam)
//{
//    int nRet;
//    StringBuilder ClassName = new StringBuilder(100);
//    //Get the window class name
//    nRet = GetClassName(hWnd, ClassName, ClassName.Capacity);

//    StringBuilder text = new StringBuilder(255);
//    GetWindowText(hWnd, text, 255);

//    Console.WriteLine("Window caption: {0}", text);
//    return true;
//}