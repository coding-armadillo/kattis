import java.util.Scanner;

class BreakingBranches {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        if (n % 2 == 0) {
            System.out.println("Alice");
            System.out.println(1);
        } else {
            System.out.println("Bob");
        }
    }
}
