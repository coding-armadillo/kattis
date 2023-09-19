import java.util.Scanner;

class OffWorldRecords {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int c = s.nextInt();
        int p = s.nextInt();
        int ans = 0;

        for (int i = 0; i < n; i++) {
            int h = s.nextInt();
            if (h > c + p) {
                ans += 1;
                p = c;
                c = h;
            }
        }
        System.out.println(ans);
    }
}
