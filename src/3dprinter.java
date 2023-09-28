import java.util.Scanner;

class ThreeDPrintedStatues {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int d = 1;
        while (Math.pow(2, d - 1) < n) {
            d += 1;
        }
        System.out.println(d);
    }
}
