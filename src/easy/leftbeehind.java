import java.util.Scanner;

class LeftBeehind {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        while (true) {
            int x = s.nextInt();
            int y = s.nextInt();
            if (x == 0 && y == 0) {
                break;
            }
            if (x + y == 13) {
                System.out.println("Never speak again.");
            } else if (x > y) {
                System.out.println("To the convention.");
            } else if (x == y) {
                System.out.println("Undecided.");
            } else {
                System.out.println("Left beehind.");
            }
        }
    }
}
