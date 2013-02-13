using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.ServiceModel;
using System.ServiceModel.Description;

namespace SkypeHandlerNET
{
    public class SvcClient
    {
        /// <summary>
        /// Method creates proxy by its endpoint URI resolving server metadata.
        /// </summary>
        public static IT ConnectTo<IT>(string endpointAddressUri) where IT : class
        {
            const int maxAttempts = 10;
            const int delayBeforeNextAttempt = 3000;

            IT proxy = null;
            string err = null;
            ServiceEndpointCollection endpoints = null;

            EndpointAddress endpointAddress = new EndpointAddress(GetMexEndpointAddress(endpointAddressUri));

            int n = 0;
            for (int i = 0; i < maxAttempts && (endpoints == null || endpoints.Count == 0);
                        i++) // several attempts to obtain enpoints
            {
                n = i;
                err = null;
                try
                {
                    ServiceEndpoint endpoint = MetadataResolver.Resolve(typeof(IT), endpointAddress).First();
                    proxy = new ChannelFactory<IT>(endpoint.Binding,
                                    new EndpointAddress(endpoint.Address.Uri.AbsoluteUri)).CreateChannel();
                }
                catch (Exception e)
                {
                    err = e.Message;
                    Thread.Sleep(delayBeforeNextAttempt);
                }
            }

            return proxy;
        }

        private static string GetMexEndpointAddress(string uri)
        {
            return string.Format("{0}{1}Mex", uri, uri[uri.Length - 1] == '/' ? string.Empty : "/");
        }
    }
}
