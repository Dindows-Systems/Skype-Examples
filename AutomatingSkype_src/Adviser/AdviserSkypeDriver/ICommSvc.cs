using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;

namespace AdviserSkypeDriver
{
    [ServiceContract]
    public interface ICommSvc
    {
        [OperationContract]
        void SendMessage(string user, string message);

        [OperationContract]
        object GetInfo(string user, string message);
    }
}
