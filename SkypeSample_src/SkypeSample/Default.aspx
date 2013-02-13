<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Default.aspx.cs" ValidateRequest ="true" Inherits="MemberPages_SkypeTest" %>

<%@ Register Src="SkypeControl.ascx" TagName="SkypeControl" TagPrefix="uc1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" >
<head runat="server">
    <title>Skype Sample</title>
</head>
<script type="text/javascript"
src="http://download.skype.com/share/skypebuttons/js/skypeCheck.js">
</script>
<body>
    <form id="form1" runat="server">
        <uc1:SkypeControl ID="SkypeControl1" runat="server" />
        <br />
        <asp:Button ID="Button1" runat="server" BackColor="#FFFF80" Font-Bold="True" Font-Names="Comic Sans MS"
            Font-Size="Small" ForeColor="Orange" OnClientClick='<a href="skype:echo123?call" onclick="return skypeCheck();">'
            Text="Skype Detection" />
    </form>
</body>
</html>
