using System;
using System.IO;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace LogParser
{
    class Program
    {     
        static void Main(string[] args)
        {
            // Read the entire file and using regex extract the needed
            string logContent = File.ReadAllText(@"var_log_messages.txt");
            Regex rx = new Regex(@"\w{3} \d{2} \d{2}:\d{2}", RegexOptions.Compiled | RegexOptions.IgnoreCase);
            MatchCollection mc = rx.Matches(logContent);

            Version1(mc);

            Console.WriteLine();
            Version2(mc);

            Console.WriteLine();
            Version3(mc);

            Console.ReadKey();
        }

        private static void Version3(MatchCollection mc)
        {
            Dictionary<string, int> dic = new Dictionary<string, int>();
            foreach (Match mt in mc)
                if (dic.ContainsKey(mt.Value))
                    dic[mt.Value]++;
                else
                    dic.Add(mt.Value, 1);

            // Sort
            List<KeyValuePair<string, int>> l = new List<KeyValuePair<string, int>>(dic);
            l.Sort(delegate (KeyValuePair<string, int> fp, KeyValuePair<string, int> np)
            { return fp.Key.CompareTo(np.Key); });

            // Print the list with count
            Console.WriteLine("minute, number_of_messages");
            foreach (KeyValuePair<string, int> kvp in l)
                Console.WriteLine("{0},{1}", kvp.Key, kvp.Value);
        }

        private static void Version2(MatchCollection mc)
        {
            SortedDictionary<string, int> dic = new SortedDictionary<string, int>();
            foreach (Match mt in mc)
                if (dic.ContainsKey(mt.Value))
                    dic[mt.Value]++;
                else
                    dic.Add(mt.Value, 1);

            // Print the list with count
            Console.WriteLine("minute, number_of_messages");
            foreach (KeyValuePair<string, int> kvp in dic)
                Console.WriteLine("{0},{1}", kvp.Key, kvp.Value);
        }

        public class Item
        {
            public int count;
            public string line;
            public Item(int i, string s) { count = i; line = s; }
        }

        private static void Version1(MatchCollection mc)
        {
            // Sort first
            List<string> logList = new List<string>(mc.Count);
            foreach (Match m in mc) { logList.Add(m.Value); }
            logList.Sort();

            // Create a list with count
            List<Item> reportList = new List<Item>(logList.Count);
            foreach (string s in logList)
                if (reportList.Count != 0 && s.Equals(reportList[reportList.Count - 1].line))
                    reportList[reportList.Count - 1].count++;
                else
                    reportList.Add(new Item(1, s));

            // Print the list with count
            Console.WriteLine("minute, number_of_messages");
            foreach (Item i in reportList)
                Console.WriteLine("{0},{1}", i.line, i.count);
        }
    }
}