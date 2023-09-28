import java.util.Scanner;

class NSum {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans += s.nextInt();
        }
        System.out.println(ans);
    }
}
