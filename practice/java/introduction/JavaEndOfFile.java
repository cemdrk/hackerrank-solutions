import java.io.*;
import java.util.*;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int count = 0;
        while(scanner.hasNext()){
            count++;
            System.out.printf("%d " + scanner.nextLine() + "\n", count);
        }
    }
}
