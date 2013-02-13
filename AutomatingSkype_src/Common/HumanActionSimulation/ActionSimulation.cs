using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using System.Threading;
using WindowFinderNET;

namespace HumanActionSimulation
{
    public static class ActionSimulation
    {
        [StructLayout(LayoutKind.Sequential)]
        public struct POINT
        {
            public int x;
            public int y;

            public POINT(int x, int y)
            {
                this.x = x;
                this.y = y;
            }

            public POINT(Point pt)
            {
                this.x = pt.X;
                this.y = pt.Y;
            }
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct RECT
        {
            public int left;
            public int top;
            public int right;
            public int bottom;
        }

        [DllImport("user32")]
        static extern IntPtr WindowFromPoint(POINT pt);

        [Flags]
        public enum MouseEventFlags
        {
            LEFTDOWN = 0x2,
            LEFTUP = 0x4,
            MIDDLEDOWN = 0x20,
            MIDDLEUP = 0x40,
            MOVE = 0x1,
            ABSOLUTE = 0x8000,
            RIGHTDOWN = 0x8,
            RIGHTUP = 0x10
        }

        [DllImport("user32")]
        private static extern void mouse_event(MouseEventFlags flags, int x, int y, int data, int extraInfo);

        const int WM_CHAR          = 0x0102;
        const int WM_COMMAND       = 0x0111;
        const int WM_ACTIVATE      = 0x0006;
        const int WM_CLOSE         = 0x0010;
        const int WM_MENUSELECT    = 0x011F;
        const int WM_INITMENU      = 0x0116;
        const int WM_INITMENUPOPUP = 0x0117;

        [Flags()]
        private enum SetWindowPosFlags : uint
        {
            /// <summary>If the calling thread and the thread that owns the window are attached to different input queues, 
            /// the system posts the request to the thread that owns the window. This prevents the calling thread from 
            /// blocking its execution while other threads process the request.</summary>
            /// <remarks>SWP_ASYNCWINDOWPOS</remarks>
            SynchronousWindowPosition = 0x4000,
            /// <summary>Prevents generation of the WM_SYNCPAINT message.</summary>
            /// <remarks>SWP_DEFERERASE</remarks>
            DeferErase = 0x2000,
            /// <summary>Draws a frame (defined in the window's class description) around the window.</summary>
            /// <remarks>SWP_DRAWFRAME</remarks>
            DrawFrame = 0x0020,
            /// <summary>Applies new frame styles set using the SetWindowLong function. Sends a WM_NCCALCSIZE message to 
            /// the window, even if the window's size is not being changed. If this flag is not specified, WM_NCCALCSIZE 
            /// is sent only when the window's size is being changed.</summary>
            /// <remarks>SWP_FRAMECHANGED</remarks>
            FrameChanged = 0x0020,
            /// <summary>Hides the window.</summary>
            /// <remarks>SWP_HIDEWINDOW</remarks>
            HideWindow = 0x0080,
            /// <summary>Does not activate the window. If this flag is not set, the window is activated and moved to the 
            /// top of either the topmost or non-topmost group (depending on the setting of the hWndInsertAfter 
            /// parameter).</summary>
            /// <remarks>SWP_NOACTIVATE</remarks>
            DoNotActivate = 0x0010,
            /// <summary>Discards the entire contents of the client area. If this flag is not specified, the valid 
            /// contents of the client area are saved and copied back into the client area after the window is sized or 
            /// repositioned.</summary>
            /// <remarks>SWP_NOCOPYBITS</remarks>
            DoNotCopyBits = 0x0100,
            /// <summary>Retains the current position (ignores X and Y parameters).</summary>
            /// <remarks>SWP_NOMOVE</remarks>
            IgnoreMove = 0x0002,
            /// <summary>Does not change the owner window's position in the Z order.</summary>
            /// <remarks>SWP_NOOWNERZORDER</remarks>
            DoNotChangeOwnerZOrder = 0x0200,
            /// <summary>Does not redraw changes. If this flag is set, no repainting of any kind occurs. This applies to 
            /// the client area, the nonclient area (including the title bar and scroll bars), and any part of the parent 
            /// window uncovered as a result of the window being moved. When this flag is set, the application must 
            /// explicitly invalidate or redraw any parts of the window and parent window that need redrawing.</summary>
            /// <remarks>SWP_NOREDRAW</remarks>
            DoNotRedraw = 0x0008,
            /// <summary>Same as the SWP_NOOWNERZORDER flag.</summary>
            /// <remarks>SWP_NOREPOSITION</remarks>
            DoNotReposition = 0x0200,
            /// <summary>Prevents the window from receiving the WM_WINDOWPOSCHANGING message.</summary>
            /// <remarks>SWP_NOSENDCHANGING</remarks>
            DoNotSendChangingEvent = 0x0400,
            /// <summary>Retains the current size (ignores the cx and cy parameters).</summary>
            /// <remarks>SWP_NOSIZE</remarks>
            IgnoreResize = 0x0001,
            /// <summary>Retains the current Z order (ignores the hWndInsertAfter parameter).</summary>
            /// <remarks>SWP_NOZORDER</remarks>
            IgnoreZOrder = 0x0004,
            /// <summary>Displays the window.</summary>
            /// <remarks>SWP_SHOWWINDOW</remarks>
            ShowWindow = 0x0040,
        }

        [DllImport("user32")]
        static extern IntPtr PostMessage(IntPtr hWnd, int msg, int wParam, int lParam);

        [DllImport("user32")]
        public static extern IntPtr SendMessage(IntPtr hWnd, int msg, int wParam, int lParam);

        [DllImport("user32")]
        public static extern bool GetWindowRect(IntPtr hWnd, out RECT rect);

        [DllImport("user32")]
        static extern bool SetWindowPos(IntPtr hWnd, IntPtr hWndInsertAfter, int X, int Y, int cx, int cy, SetWindowPosFlags flags);

        [DllImport("user32")]
        public static extern IntPtr GetMenu(IntPtr hWnd);

        [DllImport("user32")]
        public static extern IntPtr GetSubMenu(IntPtr hMenu, int pos);

        [DllImport("user32")]
        static extern int GetMenuItemID(IntPtr hMenu, int pos);

        [DllImport("user32")]
        internal static extern bool MoveWindow(IntPtr hWnd, int x, int y, int width, int height, bool repaint);

        private static IntPtr hWnd = IntPtr.Zero;

        public static void SendChar(char ch)
        {
            PostMessage(hWnd, WM_CHAR, (int)ch, 0);
        }

        public static void MouseLeftClick(int x, int y)
        {
            MouseClick(x, y, MouseEventFlags.LEFTDOWN);
        }

        public static void MouseClick(int x, int y, MouseEventFlags mefDown)
        {
            PressedMouseMove(int.MinValue, int.MinValue, x, y, mefDown);
        }

        public static void PressedMouseMove(int xFrom, int yFrom, int xTo, int yTo)
        { 
            PressedMouseMove(xFrom, yFrom, xTo, yTo, MouseEventFlags.LEFTDOWN);
        }

        public static void PressedMouseMove(int xFrom, int yFrom, int xTo, int yTo, MouseEventFlags mefDown)
        {
            MouseEventFlags mefUp = mefDown == MouseEventFlags.LEFTDOWN ? MouseEventFlags.LEFTUP : MouseEventFlags.RIGHTUP;

            //Point prevCursorPos = Cursor.Position;

            int xDown, yDown, xUp, yUp;
            bool drag;
            if (drag = !(xFrom == int.MinValue || yFrom == int.MinValue))
            {
                // Movement in pressed state
                xDown = xFrom;
                yDown = yFrom;
                xUp = xTo;
                yUp = yTo;
            }
            else
            {
                // Click, no movement in pressed state
                xDown = xUp = xTo;
                yDown = yUp = yTo;
            }
            
            Cursor.Position = new Point(xDown, yDown);
            mouse_event(mefDown | MouseEventFlags.ABSOLUTE, xDown, yDown, 0, 0);

            if (drag)
            {
                mouse_event(MouseEventFlags.MOVE | MouseEventFlags.ABSOLUTE, xUp - xDown, yUp - yDown, 0, 0);
                Cursor.Position = new Point(xUp, yUp);
            }

            mouse_event(mefUp | MouseEventFlags.ABSOLUTE, 0, 0, 0, 0);

            //Cursor.Position = prevCursorPos;

            hWnd = WindowFromPoint(new POINT(xUp, yUp));
        }

        public static void CommandWithClick(string wndClass, int width, int height, double xFactor, double yFactor)
        {
            WndFinder wf = new WndFinder();
            IntPtr hWnd = wf.GetWindow(wndClass);
            if (hWnd != IntPtr.Zero)
            {
                SetWindowPos(hWnd, /*HWND_TOPMOST*/(IntPtr)(-1), 0, 0, width, height, SetWindowPosFlags.ShowWindow); 
                int x = (int)(width * xFactor);
                int y = (int)(height * yFactor);
                MouseLeftClick(x, y);
            }
        }

        public static void ActivateMenuItem(string mainWndClass, int menuItemNum, int menuSubItemNum)
        {
            IntPtr hWnd = new WndFinder().GetWindow(mainWndClass);
            IntPtr hMenu = GetSubMenu(GetMenu(hWnd), menuItemNum);

            SendMessage(hWnd, WM_INITMENU, (int)hMenu, 0);
            SendMessage(hWnd, WM_INITMENUPOPUP, (int)hMenu, 0);

            SendMessage(hWnd, WM_COMMAND, GetMenuItemID(hMenu, menuSubItemNum), 0);
        }
    }
}
