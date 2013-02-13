using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace CustomerSkypeDriver
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

        [DllImport("user32")]
        static extern IntPtr WindowFromPoint(POINT pt);

        [Flags]
        public enum MouseEventFlags
        {
            LEFTDOWN   = 0x2,
            LEFTUP     = 0x4,
            MIDDLEDOWN = 0x20,
            MIDDLEUP   = 0x40,
            MOVE       = 0x1,
            ABSOLUTE   = 0x8000,
            RIGHTDOWN  = 0x8,
            RIGHTUP    = 0x10
        }

        [DllImport("user32")]
        private static extern void mouse_event(MouseEventFlags flags, int x, int y, int data, int extraInfo);

        const int WM_CHAR    = 0x102;

        [DllImport("user32")]
        static extern IntPtr PostMessage(IntPtr hWnd, int msg, int wParam, int lParam);

        [DllImport("user32")]
        static extern IntPtr SendMessage(IntPtr hWnd, int msg, int wParam, int lParam);

        private static IntPtr hWnd = IntPtr.Zero;

        public static void SendChar(char ch)
        {
            PostMessage(hWnd, WM_CHAR, (int)ch, 0);
        }

        public static void MouseClick(int x, int y, MouseEventFlags mefDown)
        {
            MouseEventFlags mefUp = MouseEventFlags.LEFTUP;
            switch (mefDown)
            {
                case MouseEventFlags.RIGHTDOWN: mefUp = MouseEventFlags.RIGHTUP; break;
            }

            Point prevCursorPos = Cursor.Position;
            Cursor.Position = new Point(x, y);
            mouse_event(mefDown | MouseEventFlags.ABSOLUTE, x, y, 0, 0);
            mouse_event(mefUp, 0, 0, 0, 0);
            Cursor.Position = prevCursorPos;
            hWnd = WindowFromPoint(new POINT(x, y));
        }

        public static void MouseMove(int xFrom, int yFrom, int xTo, int yTo)
        {
            //Point prevCursorPos = Cursor.Position;
            //Cursor.Position = new Point(xFrom, yFrom);
            //mouse_event(MouseEventFlags.LEFTDOWN | MouseEventFlags.ABSOLUTE, xFrom, yFrom, 0, 0);
            //System.Threading.Thread.Sleep(100);
            //mouse_event(MouseEventFlags.MOVE | MouseEventFlags.ABSOLUTE, xTo - xFrom, yTo - yFrom, 0, 0);
            //System.Threading.Thread.Sleep(100);
            //mouse_event(MouseEventFlags.LEFTUP, 0, 0, 0, 0);
            //System.Threading.Thread.Sleep(100);

            //Cursor.Position = new Point(xTo, yTo);
            //mouse_event(MouseEventFlags.LEFTUP | MouseEventFlags.ABSOLUTE, xTo, yTo, 0, 0);
            //mouse_event(MouseEventFlags.LEFTUP, 0, 0, 0, 0);

            //Cursor.Position = prevCursorPos;
        }
    }
}
