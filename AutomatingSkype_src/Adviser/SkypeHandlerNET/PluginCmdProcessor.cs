using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using System.Windows.Forms;
using System.Threading;
using System.Runtime.InteropServices;
using SkypeHandlerNET.CommSvcReference;

namespace SkypeHandlerNET
{
    public class PluginCmdProcessor
    {
        #region Const

        const int maxUniqueMsgCount = 100;
        readonly Dictionary<string, string> dctCmd = new Dictionary<string, string>()
        {
            {"lclick", "lck"},             
            {"rclick", "rck"},
        };

        #endregion

        #region Var

        private Point ptClick = Point.Empty;
        private Point ptMoveFrom = Point.Empty;
        private Point ptMoveTo = Point.Empty;
        private int hWndFrame = 0;
        private int hWndView = 0;
        private StringBuilder sb = new StringBuilder();
        private Size userScreenBounds;
        private Size screenBounds;
        private int uniqueMsgCount = 0;
        
        private DateTime lastLClickTime = DateTime.MinValue;
        public ICommSvc Proxy { set; private get; }

        #endregion

        #region Interop

        [StructLayout(LayoutKind.Sequential)]
        public struct _RECT
        {
            public int left;
            public int top;
            public int right;
            public int bottom;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct _POINT
        {
            public int x;
            public int y;
        }

        [DllImport("user32")]
        static extern bool GetClientRect(int hWnd, out _RECT lpRect);

        [DllImport("user32")]
        static extern bool GetWindowRect(int hWnd, out _RECT lpRect);

        [DllImport("user32")]
        internal static extern bool MoveWindow(IntPtr hWnd, int x, int y, int width, int height, bool repaint);

        private static Point GetFrameViewDelta(int hWnd)
        {
            _RECT rcClient, rcWindow;
            _POINT ptDiff;
            GetClientRect(hWnd, out rcClient);
            GetWindowRect(hWnd, out rcWindow);
            ptDiff.x = (rcWindow.right - rcWindow.left) - rcClient.right;
            ptDiff.y = (rcWindow.bottom - rcWindow.top) - rcClient.bottom;
            return new Point(ptDiff.x, ptDiff.y);
        }

        private static Point GetOffset(int hWnd, Size userScreenBounds, int orgCorner)
        {
            _RECT rcClient;
            GetClientRect(hWnd, out rcClient);
            int x = 0, y = 0;  // left-top - default
            switch (orgCorner)
            {
                /* left-bottom */  case 1: y = userScreenBounds.Height - (rcClient.bottom - rcClient.top); break; 
                /* right-top */    case 2: x = userScreenBounds.Width - (rcClient.right - rcClient.left);  break; 
                /* right-bottom */ case 3:
                                        x = userScreenBounds.Width - (rcClient.right - rcClient.left);
                                        y = userScreenBounds.Height - (rcClient.bottom - rcClient.top);
                                        break;                                    
            }

            return new Point(x, y);
        }

        #endregion

        #region Aux

        private int UniqueMsgCount
        {
            get
            {
                if (++uniqueMsgCount > maxUniqueMsgCount)
                    uniqueMsgCount = 0;

                return uniqueMsgCount;
            }
        }

        #endregion

        #region Commands

        public object text(object data)
        {
            string sData = data as string;
            ThreadPool.QueueUserWorkItem(state => { Proxy.SendMessage("", string.Format("s({0}){1}", sData, UniqueMsgCount)); });
            return data;
        }

        #region Windows

        public object hwndframe(object data)
        {
            hWndFrame = (int)data;
            return data;
        }

        public object hwndview(object data)
        {
            hWndView = (int)data;
            return data;
        }
        
        public object getoffsetx(object data)
        {
            return GetOffset(hWndFrame, userScreenBounds, (int)data).X;
        }

        public object getoffsety(object data)
        {
            return GetOffset(hWndFrame, userScreenBounds, (int)data).Y;
        }

        #endregion

        #region Clicks

        #region Left Click

        public object lclickx(object data)
        {
            ptClick.X = (int)data;
            return data;
        }

        public object lclicky(object data)
        {
            return click("lclick", data);
        }

        #endregion

        #region Right Click

        public object rclickx(object data)
        {
            ptClick.X = (int)data;
            return data;
        }

        public object rclicky(object data)
        {
            return click("rclick", data);
        }

        #endregion

        #region Double Click

        public object dblclickx(object data)
        {
            ptClick.X = (int)data;
            return data;
        }

        #endregion

        public object click(string command, object data)
        {
            ptClick.Y = (int)data;
            ThreadPool.QueueUserWorkItem(state => { Proxy.SendMessage("", string.Format("{0}({1},{2}){3}", dctCmd[command], ptClick.X, ptClick.Y, UniqueMsgCount)); });
            return data;
        }

        #endregion

        #region Move

        public object pressedmovefromx(object data)
        {
            ptMoveFrom = Point.Empty;
            ptMoveTo = Point.Empty;
            ptMoveFrom.X = (int)data;
            return data;
        }

        public object pressedmovefromy(object data)
        {
            ptMoveFrom.Y = (int)data;
            return data;
        }

        public object pressedmovetox(object data)
        {
            ptMoveTo.X = (int)data;
            return data;
        }

        public object pressedmovetoy(object data)
        {
            ptMoveTo.Y = (int)data;
            ThreadPool.QueueUserWorkItem(state => Proxy.SendMessage("", string.Format("mv({0},{1},{2},{3}){4}",
                    ptMoveFrom.X, ptMoveFrom.Y, ptMoveTo.X, ptMoveTo.Y, UniqueMsgCount))
                );
            return data;
        }

        #endregion

        #region Resize

        public object resizeoperativewindow(object data)
        {
            string s = Proxy.GetInfo("", "UserScreenSize") as string;
            if (!string.IsNullOrEmpty(s))
            {
                string[] ss = s.Split(new char[] { ',' });
                userScreenBounds = new Size(int.Parse(ss[0]), int.Parse(ss[1]));
                screenBounds = new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);
                int width = userScreenBounds.Width > screenBounds.Width ? screenBounds.Width : userScreenBounds.Width;
                int height = userScreenBounds.Height > screenBounds.Height ? screenBounds.Height : userScreenBounds.Height;

                Point delta = GetFrameViewDelta(hWndFrame);

                width = width < screenBounds.Width ? width + delta.X + 20 : screenBounds.Width;
                height = height < screenBounds.Height ? height + delta.Y : screenBounds.Height;
                MoveWindow((IntPtr)hWndFrame, 0, 0, width, height, true);
            }

            return data;
        }

        #endregion

        #region Destroy

        public object destroy(object data)
        {
            return data;
        }

        #endregion 

        #endregion
    }
}
