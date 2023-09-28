import java.util.Scanner;

class SMIL {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String m = s.nextLine();
        int size = m.length();
        int i = 0;
        while (i < size) {
            if (m.charAt(i) == ':' || m.charAt(i) == ';') {
                if (i + 1 < size && m.charAt(i + 1) == ')') {
                    System.out.println(i);
                    i += 2;
                    continue;
                }
                if (i + 2 < size && m.charAt(i + 1) == '-' && m.charAt(i + 2) == ')') {
                    System.out.println(i);
                    i += 3;
                    continue;
                }
            }
            i += 1;
        }
    }
}
