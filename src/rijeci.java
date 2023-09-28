import java.util.Scanner;

class Rijeci {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int k = s.nextInt();
        int a = 1;
        int b = 0;
        for (int i = 0; i < k; i++) {
            int t = b;
            b = a + b;
            a = t;

        }

        System.out.println(a + " " + b);
    }
}
