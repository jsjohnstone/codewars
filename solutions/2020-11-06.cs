//First and Last Character
//https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/csharp
//
//Remove the first and last character of a provided string.
//The solution doesn't need to handle strings less than 2 characters long.

using System;

public class Kata
{
    public static string Remove_char(string s)
    {
        // Get string length
        int length = s.Length - 2;

        // Obtain a substring, starting at char[1] and ending at char[length-2]
        string word = s.Substring(1, length);
      
      // return the word
      return word;
    }
}