using System;
using System.Windows.Forms;
using SKYPE4COMLib;


namespace SkypeBing
{
    public partial class Form1 : Form
    {
        private Skype skype;
        private const string trigger = "!"; // Say !help
        private const string nick = "BOT";
        
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            skype = new Skype();
            // Use skype protocol version 7 
            skype.Attach(7, false); 
            // Listen 
            skype.MessageStatus +=new _ISkypeEvents_MessageStatusEventHandler(skype_MessageStatus);
        }
        private void skype_MessageStatus(ChatMessage msg, TChatMessageStatus status)
        {
            // Proceed only if the incoming message is a trigger
            if (msg.Body.IndexOf(trigger) >= 0)
            {
                // Remove trigger string and make lower case
                string command = msg.Body.Remove(0, trigger.Length).ToLower();

                // Send processed message back to skype chat window
                skype.SendMessage(msg.Sender.Handle, nick + " Says: " + ProcessCommand(command));
            }
        }

        private string ProcessCommand(string str)
        {
            string result;
            switch (str)
            {
                case "hello":
                    result = "Hello!";
                    break;
                case "help":
                    result = "Sorry no help available";
                    break;
                case "date":
                    result = "Current Date is: " + DateTime.Now.ToLongDateString();
                    break;
                case "time":
                    result = "Current Time is: " + DateTime.Now.ToLongTimeString();
                    break;
                case "who":
                    result = "It is Praveen, aka NinethSense who wrote this tutorial";
                    break;
                default:
                    result = "Sorry, I do not recognize your command";
                    break;
            }

            return result;
        }
    }
}
