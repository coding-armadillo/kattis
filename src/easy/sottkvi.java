import java.util.Scanner;

class Sottkvi {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int k = s.nextInt();
        int today = s.nextInt();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int d = s.nextInt();
            if (d + 14 - today <= k) {
                ans += 1;
            }
        }
        System.out.println(ans);

    }
}
