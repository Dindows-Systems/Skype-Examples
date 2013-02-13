using System;
using System.Collections.Generic;
using System.Text;
using System.ServiceModel;
using System.ServiceModel.Description;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using System.Threading;
using System.Configuration;
using System.IO;
using System.Drawing;
using System.Reflection;
using SkypeHandlerNET.CommSvcReference;

namespace SkypeHandlerNET
{
    #region IHandler Interface

    /// <summary>
    /// Interface IHandler exposed to unmanaged SkypePlugin DLL via COM Interop.
    /// </summary>
    [InterfaceType(ComInterfaceType.InterfaceIsDual)]
    [Guid("CAE57E0B-07F9-4936-BFFF-9B19C9C0DF35")]
    [ComVisible(true)]
    public interface IHandler
    {
        int Do(object inData, ref object outData);
    }

    #endregion

    #region Handler Class

    /// <summary>
    /// Class Handler implementing IHandler interface. 
    /// Its methods are called from unmanaged SkypePluin.dll.
    /// </summary>
    [ClassInterface(ClassInterfaceType.AutoDual)]
    [Guid("85CD0691-A2C0-4DD8-BBDA-C52BA33E4733")]
    [ProgId("SkypeHandlerNET.Handler")]
    [ComVisible(true)]
    public class Handler : IHandler 
    {
        const string endpointAddressUri = "net.pipe://localhost/SkypeDriver/";
        
        private PluginCmdProcessor processor = null;

        /// <summary>
        /// Default public ctor, compulsory for COM Interop.
        /// </summary>
        public Handler()
        {
            try
            {
                processor = new PluginCmdProcessor();
                processor.Proxy = SvcClient.ConnectTo<ICommSvc>(endpointAddressUri);
            }
            catch (Exception e)
            {
                MessageBox.Show(e.ToString(), "SkypeHandlerNET");
            }
        }

        /// <summary>
        /// Method Do is called from unmanaged SkypePluin.dll to perform various operation
        /// and, the most important notify client.
        /// </summary>
        [ComVisible(true)]
        public int Do(object inData, ref object outData)
        {
            string command = inData.ToString().ToLower();
            try
            {
                outData = processor.GetType().GetMethod(command).Invoke(processor, new object[] { outData });
            }
            catch (Exception e)
            {
                MessageBox.Show(string.Format("Method \"{0}\": ", command) + e.ToString(), "SkypeHandlerNET");
            }

            return 0;
        }       
    }

    #endregion
}
