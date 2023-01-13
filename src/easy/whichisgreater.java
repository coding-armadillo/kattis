import java.util.Scanner;

class WhichisGreater {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        int b = s.nextInt();
        if (a>b){
            System.out.println(1);
        }else{
            System.out.println(0);
        }
    }
}
