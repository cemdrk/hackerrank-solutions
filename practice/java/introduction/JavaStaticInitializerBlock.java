import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    private static boolean flag;
    private static int B;
    private static int H;
    private static final Scanner scanner = new Scanner(System.in);

    static{
        B = scanner.nextInt();
        H = scanner.nextInt();
        if(B > 0 && H > 0){
            flag = true;
        }
        else{
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        }
    }

    public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}

	}//end of main

}//end of class
