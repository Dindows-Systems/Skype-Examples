using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using HumanActionSimulation;

namespace UserSkypeDriver
{
    public class Processor
    {
        readonly Dictionary<string, ActionSimulation.MouseEventFlags> dctClick = new Dictionary<string, ActionSimulation.MouseEventFlags>()
                {
                    {"lck", ActionSimulation.MouseEventFlags.LEFTDOWN},
                    {"rck", ActionSimulation.MouseEventFlags.RIGHTDOWN},
                };

        private delegate void MouseClickDelegate(int x, int y, ActionSimulation.MouseEventFlags mef);
        private MouseClickDelegate dlgtMouseClick = new MouseClickDelegate(ActionSimulation.MouseClick);

        private delegate void MouseMoveDelegate(int xFrom, int yFrom, int xTo, int yTo);
        private MouseMoveDelegate dlgtMouseMove = new MouseMoveDelegate(ActionSimulation.PressedMouseMove);
        
        private Form frm = null;

        public Processor(Form frm)
        {
            this.frm = frm;
        }

        public void lck(string[] pmrs)
        {
            ck("lck",  pmrs);
        }

        public void rck(string[] pmrs)
        {
            ck("rck",  pmrs);
        }

        private void ck(string command, string[] pmrs)
        {
            int x = int.Parse(pmrs[0]);
            int y = int.Parse(pmrs[1]);
            ActionSimulation.MouseEventFlags mefDown = dctClick[command];
            if (frm.InvokeRequired)
                dlgtMouseClick.Invoke(x, y, mefDown);
            else
                ActionSimulation.MouseClick(x, y, mefDown);
        }

        public void mv(string[] pmrs)
        {
            int xFrom = int.Parse(pmrs[0]);
            int yFrom = int.Parse(pmrs[1]);
            int xTo = int.Parse(pmrs[2]);
            int yTo = int.Parse(pmrs[3]);
            if (frm.InvokeRequired)
                dlgtMouseMove.Invoke(xFrom, yFrom, xTo, yTo);
            else
                ActionSimulation.PressedMouseMove(xFrom, yFrom, xTo, yTo);
        }

        public void s(string[] pmrs)
        {
            string s = pmrs[0];
            for (int i = 0; i < s.Length; i++)
                ActionSimulation.SendChar(s[i]);                                  
        }
    }
}
