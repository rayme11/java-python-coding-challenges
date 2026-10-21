public class Z_Concept01_Test_ByValueAndReference 
{
    public  static void main(String[] args) 
    {
      int a = 5;
      int b = a;
      b = 14;
      System.out.println("Orignal values are int a = 5, int b = a; then b = 14");
      System.out.println("The value of a should be 5 (by value) ==>" + a);
      System.out.println("Now if we use passed by reference,, difference story.... \n");
      
      int[] arrayA = {1, 2, 3, 4 };
      int[] arrayB = arrayA;
      System.out.println("Let's try to change A from using arrayB[0] = 99 since in theory both arrays are the same...");
      arrayB[0] = 99;
      System.out.println("Since this is a non primitive object, they share or point to the same object,value.. thus..\n");
      System.out.println("The value of arrayB[0] should be the same as arrayA[0], although it was modified by arrayB\n" + arrayA[0]);
    }
}
