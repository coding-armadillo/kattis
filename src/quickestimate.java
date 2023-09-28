import java.util.Scanner;

class QuickEstimates {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        for (int i = 0; i < n; i++) {
            String cost = s.next();
            System.out.println(cost.length());
        }
    }
}
