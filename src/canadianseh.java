import java.util.Scanner;

class CanadiansEh {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String line = s.nextLine();
        if (line.endsWith("eh?")) {
            System.out.println("Canadian!");
        } else {
            System.out.println("Imposter!");
        }
    }
}
