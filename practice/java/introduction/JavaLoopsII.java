import java.util.*;
import java.io.*;

class Solution{

    static List<Integer> getSeries(int a, int b, int n){
        List<Integer> list = new ArrayList<>();
        int prev = a + b;
        list.add(prev);

        for(int i=1; i < n; i++){
            int result = prev + (int) Math.pow(2, i) * b;
            list.add(result);
            prev = result;
        }
        return list;
    }

    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();

            System.out.println(getSeries(a, b, n).toString()
                             .replace(",", "")
                             .replace("[", "")
                             .replace("]", "")
                             .trim());
        }
        in.close();
    }
}
