using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using SkypeControl;

namespace TestApp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            aSkype.SkypeAttach += new SkypeAttachHandler(aSkype_SkypeAttach);
            aSkype.SkypeResponse += new SkypeResponseHandler(aSkype_SkypeResponse);
        }

        void aSkype_SkypeAttach(object theSender, SkypeAttachEventArgs theEventArgs)
        {
            textBox1.AppendText(string.Format("Attach: {0}\r\n", theEventArgs.AttachStatus));
        }

        void aSkype_SkypeResponse(object theSender, SkypeResponseEventArgs theEventArgs)
        {
            textBox1.AppendText(string.Format("Response: {0}\r\n", theEventArgs.Response));
        }

        SkypeProxy aSkype = new SkypeProxy();

        private void button1_Click(object sender, EventArgs e)
        {
            aSkype.Conect();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.AppendText(string.Format("Command: {0}\r\n", comboBox1.Text));
            aSkype.Command(comboBox1.Text);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            aSkype.Disconnect();
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start(@"http://share.skype.com/sites/devzone/2006/01/api_reference_for_skype_20_bet.html#Reference");
        }

        private void linkLabel2_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start(@"mailto:ag1206@pobox.sk&subject=Skype API Test");
        }
    }
}