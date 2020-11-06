//Sum of positive
//https://www.codewars.com/kata/5715eaedb436cf5606000381/train/csharp
//Add all positive numbers from an array

using System;
using System.Linq;

public class Kata
{
  public static int PositiveSum(int[] arr)
  {
    int result = 0;
    
    foreach (int number in arr) 
    {
        if(number > 0) {
          result = result + number;
        }
    }
    return result;
  }
}
