namespace UserSkypeDriver
{
    partial class FormUser
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnAttach = new System.Windows.Forms.Button();
            this.btnCloseSkype = new System.Windows.Forms.Button();
            this.txbConsultant = new System.Windows.Forms.TextBox();
            this.lblAdviser = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btnAttach
            // 
            this.btnAttach.Location = new System.Drawing.Point(12, 12);
            this.btnAttach.Name = "btnAttach";
            this.btnAttach.Size = new System.Drawing.Size(159, 23);
            this.btnAttach.TabIndex = 0;
            this.btnAttach.Text = "Start / Attach to Skype";
            this.btnAttach.UseVisualStyleBackColor = true;
            this.btnAttach.Click += new System.EventHandler(this.btnAttach_Click);
            // 
            // btnCloseSkype
            // 
            this.btnCloseSkype.Location = new System.Drawing.Point(12, 73);
            this.btnCloseSkype.Name = "btnCloseSkype";
            this.btnCloseSkype.Size = new System.Drawing.Size(159, 23);
            this.btnCloseSkype.TabIndex = 1;
            this.btnCloseSkype.Text = "Close Skype";
            this.btnCloseSkype.UseVisualStyleBackColor = true;
            this.btnCloseSkype.Click += new System.EventHandler(this.btnCloseSkype_Click);
            // 
            // txbConsultant
            // 
            this.txbConsultant.Location = new System.Drawing.Point(61, 45);
            this.txbConsultant.Name = "txbConsultant";
            this.txbConsultant.Size = new System.Drawing.Size(110, 20);
            this.txbConsultant.TabIndex = 2;
            // 
            // lblAdviser
            // 
            this.lblAdviser.AutoSize = true;
            this.lblAdviser.Location = new System.Drawing.Point(12, 47);
            this.lblAdviser.Name = "lblAdviser";
            this.lblAdviser.Size = new System.Drawing.Size(45, 13);
            this.lblAdviser.TabIndex = 3;
            this.lblAdviser.Text = "Adviser:";
            // 
            // FormUser
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(224, 126);
            this.Controls.Add(this.lblAdviser);
            this.Controls.Add(this.txbConsultant);
            this.Controls.Add(this.btnCloseSkype);
            this.Controls.Add(this.btnAttach);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "FormUser";
            this.Text = "User Skype Driver";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnAttach;
        private System.Windows.Forms.Button btnCloseSkype;
        private System.Windows.Forms.TextBox txbConsultant;
        private System.Windows.Forms.Label lblAdviser;
    }
}

