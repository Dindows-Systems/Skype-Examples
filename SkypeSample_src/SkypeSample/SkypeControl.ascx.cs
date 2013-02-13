using System;
using System.Data;
using System.Configuration;
using System.Collections;
using System.Web;
using System.Web.Security;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.UI.WebControls.WebParts;
using System.Web.UI.HtmlControls;

public partial class SkypeControl : System.Web.UI.UserControl
{
    protected void Page_Load(object sender, EventArgs e)
    {

    }
    protected void Populate_Click(object sender, EventArgs e)
    {
        try
        {
            this.SetSkype();
        }
        catch
        {
            //Todo
        }
        finally
        {
            //Todo
        }
    }
    protected void SetSkype()
    {

        Image1.Visible = true;
        Image2.Visible = true;
        Image3.Visible = true;
        Image4.Visible = true;
        Image5.Visible = true;
        Image6.Visible = true;

        //Create Strings
        string SkypeName = txtSkypeName.Text;
        string LandPhone = txtPhoneNr.Text;
        string PathSkypeStatusString = "";
        string SkypeAddContactString = "";
        string SkypeCallString = "";
        string SkypeLandCall = "";
        string SkypeChattString = "";
        string SkypeProfileString = "";
        string SkypeSendFileString = "";
        //Get Spype Status
        try
        {
            string s1 = "http://mystatus.skype.com/mediumicon/";
            string s2 = SkypeName;
            string sT = s1 + s2;
            PathSkypeStatusString = sT;
            Image1.ImageUrl = PathSkypeStatusString;
        }
        catch
        {
            //
        }
        finally
        {
            //
        }

        //Set CallString
        try
        {
            string s1 = "<a href=";
            string s2 = "skype:";
            string s3 = SkypeName;
            string s4 = "?call";
            string s5 = '"'.ToString();
            string s6 = ">Skype Me</a>";
            string sT = s1 + s2 + s3 + s4 + s5 + s6;
            SkypeCallString = sT;
            LinkButton1.Text = SkypeCallString;
        }
        catch
        {
            //Todo
        }
        finally
        {
            //Todo
        }
        //Set LandCallString
        try
        {
            string s1 = "<a href=";
            string s2 = "skype:";
            string s3 = LandPhone;
            string s4 = "?call";
            string s5 = '"'.ToString();
            string s6 = ">Call Me</a>";
            string sT = s1 + s2 + s3 + s4 + s5 + s6;
            SkypeLandCall = sT;
            LinkButton6.Text = SkypeLandCall;
        }
        catch
        {
            //Todo
        }
        finally
        {
            //Todo
        }
        //SetSkypeUserProfile
        try
        {
            string s1 = "<a href=";
            string s2 = "skype:";
            string s3 = SkypeName;
            string s4 = "?userinfo";
            string s5 = '"'.ToString();
            string s6 = ">User Info</a>";
            string sT = s1 + s2 + s3 + s4 + s5 + s6;
            SkypeProfileString = sT;
            LinkButton2.Text = SkypeProfileString;
        }
        catch
        {
            //Todo
        }
        finally
        {
            //Todo
        }
        //Set Skype ChattString
        try
        {
            string s1 = "<a href=";
            string s2 = "skype:";
            string s3 = SkypeName;
            string s4 = "?chat";
            string s5 = '"'.ToString();
            string s6 = ">Start Chat</a>";
            string sT = s1 + s2 + s3 + s4 + s5 + s6;
            SkypeChattString = sT;
            LinkButton3.Text = SkypeChattString;
        }
        catch
        {
            //Todo
        }
        finally
        {
            //Todo
        }
        //Set Skype SendFileString
        try
        {
            string s1 = "<a href=";
            string s2 = "skype:";
            string s3 = SkypeName;
            string s4 = "?sendfile";
            string s5 = '"'.ToString();
            string s6 = ">Send File</a>";
            string sT = s1 + s2 + s3 + s4 + s5 + s6;
            SkypeSendFileString = sT;
            LinkButton4.Text = SkypeSendFileString;
        }
        catch
        {
            //Todo
        }
        finally
        {
            //Todo
        }
        //Set Skype AddContactString
        try
        {
            string s1 = "<a href=";
            string s2 = "skype:";
            string s3 = SkypeName;
            string s4 = "?add";
            string s5 = '"'.ToString();
            string s6 = ">Add Contact</a>";
            string sT = s1 + s2 + s3 + s4 + s5 + s6;
            SkypeAddContactString = sT;
            LinkButton5.Text = SkypeAddContactString;
        }
        catch
        {
            //Todo
        }
        finally
        {
            //Todo
        }
    }
}