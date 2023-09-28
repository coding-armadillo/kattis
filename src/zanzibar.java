import java.util.Scanner;

class StandOnZanzibar {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        for (int i = 0; i < t; i++) {
            int total = 0;
            int n = 0;
            int init = 1;
            while (true) {
                n = s.nextInt();
                if (n == 0) {
                    break;
                }
                total += Math.max(n - 2 * init, 0);
                init = n;
            }
            System.out.println(total);
        }
    }
}
