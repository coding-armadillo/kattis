import java.util.Scanner;

class BasketballOneOnOne {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String scores = s.nextLine();
        System.out.println(scores.charAt(scores.length() - 2));
    }
}
