import java.util.Scanner;

class Railroad {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int x = s.nextInt();
        int y = s.nextInt();
        if (y % 2 == 1) {
            System.out.println("impossible");
        } else {
            System.out.println("possible");
        }
    }
}
