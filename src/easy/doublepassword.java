import java.util.Scanner;

class DoublePassword {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String a = s.nextLine();
        String b = s.nextLine();
        int number = 1;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) == b.charAt(i)) {
                number *= 1;
            } else {
                number *= 2;
            }
        }
        System.out.println(number);

    }
}
