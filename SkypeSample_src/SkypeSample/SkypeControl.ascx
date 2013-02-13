<%@ Control Language="C#" AutoEventWireup="true" CodeFile="SkypeControl.ascx.cs" Inherits="SkypeControl" %>
&nbsp;
<asp:ImageButton ID="ImageButton1" runat="server" ImageUrl="https://developer.skype.com/site/common/SDZ.png"
    PostBackUrl="https://developer.skype.com/" />
<table style="width: 674px; height: 87px">
    <tr>
        <td style="width: 139px">
            <asp:Label ID="lblSkypeName" runat="server" Text="SkypeName:" Font-Names="Comic Sans MS" ForeColor="Red"></asp:Label></td>
        <td>
            <asp:TextBox ID="txtSkypeName" runat="server" Width="346px"></asp:TextBox></td>
        <td>
        </td>
    </tr>
    <tr>
        <td style="width: 139px; height: 26px">
            <asp:Label ID="lblPhoneNr" runat="server" Text="Phone Nr:" Font-Names="Comic Sans MS" ForeColor="Red"></asp:Label></td>
        <td style="height: 26px">
            <asp:TextBox ID="txtPhoneNr" runat="server"></asp:TextBox>
            <asp:Button ID="Button1" runat="server" OnClick="Populate_Click" Text="Populate" /></td>
        <td style="height: 26px">
        </td>
    </tr>
    <tr>
        <td style="width: 139px; height: 26px">
        </td>
        <td style="height: 26px">
            <table style="width: 187px">
                <tr>
                    <td>
            <asp:Image ID="Image1" runat="server" Height="32px" Width="32px" ImageUrl="~/SkypeBtn/Question_32x32.png" Visible="False" /></td>
                    <td>
            <asp:LinkButton ID="LinkButton1" runat="server" BorderStyle="None" BorderWidth="0px" Font-Names="Comic Sans MS"></asp:LinkButton></td>
                    <td>
                    </td>
                </tr>
                <tr>
                    <td>
            <asp:Image ID="Image2" runat="server" ImageUrl="~/SkypeBtn/Info_32x32.png" Visible="False" /></td>
                    <td>
            <asp:LinkButton ID="LinkButton2" runat="server" BorderStyle="None" BorderWidth="0px" Font-Names="Comic Sans MS"></asp:LinkButton></td>
                    <td>
                    </td>
                </tr>
                <tr>
                    <td>
            <asp:Image ID="Image3" runat="server" ImageUrl="~/SkypeBtn/Message_32x32.png" Visible="False" /></td>
                    <td>
            <asp:LinkButton ID="LinkButton3" runat="server" Font-Names="Comic Sans MS"></asp:LinkButton></td>
                    <td>
                    </td>
                </tr>
                <tr>
                    <td>
            <asp:Image ID="Image4" runat="server" ImageUrl="~/SkypeBtn/FileUpload_32x32.png" Visible="False" /></td>
                    <td>
            <asp:LinkButton ID="LinkButton4" runat="server" Font-Names="Comic Sans MS"></asp:LinkButton></td>
                    <td>
                    </td>
                </tr>
                <tr>
                    <td>
            <asp:Image ID="Image5" runat="server" ImageUrl="~/SkypeBtn/AddContact_32x32.png" Visible="False" /></td>
                    <td>
            <asp:LinkButton ID="LinkButton5" runat="server" Font-Names="Comic Sans MS"></asp:LinkButton></td>
                    <td>
                    </td>
                </tr>
                <tr>
                    <td>
            <asp:Image ID="Image6" runat="server" ImageUrl="~/SkypeBtn/Dial_32x32.png" Visible="False" /></td>
                    <td>
                        <asp:LinkButton ID="LinkButton6" runat="server" Font-Names="Comic Sans MS"></asp:LinkButton></td>
                    <td>
                    </td>
                </tr>
            </table>
            </td>
        <td style="height: 26px">
        </td>
    </tr>
</table>
