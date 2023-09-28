import java.util.Scanner;

class Spavanac {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int h = s.nextInt();
        int m = s.nextInt();

        int mm = m - 45;
        int borrow = 0;
        if (mm < 0) {
            mm += 60;
            borrow = 1;
        }

        int hh = h - borrow;
        if (hh < 0) {
            hh += 24;
        }
        System.out.println(hh + " " + mm);
    }
}
