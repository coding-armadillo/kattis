import java.util.Scanner;

class RatingProblems {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int k = s.nextInt();
        int score = 0;
        for (int i = 0; i < k; i++) {
            score += s.nextInt();
        }
        float min = (score - 3 * (n - k)) / (float) n;
        float max = (score + 3 * (n - k)) / (float) n;
        System.out.println(min + " " + max);
    }
}
