using System;
using System.Collections.Generic;

namespace CustomSipher
{
    class Program
    {
        static void Main(string[] args)
        {
            string test = Encode("Test szyfru dla innego tekstu", 7).ToCustomString();
            Console.WriteLine(test); //84, 101, 124, 131, 58, 149, 157, 162, 140, 176, 165, 120, 185, 173, 181, 170, 221, 162, 257, 258, 228, 286, 240, 288, 281, 269, 256, 289, 325
            Console.WriteLine(Encode(password, 13).ToCustomString()); //102, 136, 152, 158, 85, 134, 151, 208, 153, 140, 236, 315, 195, 246, 257, 296, 230, 280, 317, 410, 359, 360, 424, 282, 518, 474
            Console.ReadKey();
        }

        static List<int> Encode(string str, int key)
        {
            throw new NotImplementedException();
        }
    }

    public static class ExtensionMethods
    {
        public static string ToCustomString(this List<int> list)
        {
            return String.Join(", ", list.ToArray());
        }
    }
}
