using System;

namespace Skypekit.NET
{
    public class PrintStream
    {
        public void printf(string x)
        {
            Console.WriteLine(x);
        }

        public void printf(params string[] x)
        {
            for (int i = 0; i < x.Length; i++)
                Console.WriteLine(x[i]);
        }

        public void printf(params object[] x)
        {
            for (int i = 0; i < x.Length; i++)
                Console.WriteLine(x[i]);
        }

        public void println(string x)
        {
            Console.WriteLine(x);
        }

        public void println()
        {
            Console.WriteLine();
        }
    }
}
