public class Z_Concept01_Test_StringBuilder {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= 10; i++) {
            sb.append(i);
        }

        System.out.println("Stringbuilder is a very efficient to mutate in place a primitive number..");
        for (int i = 0; i < sb.length(); i++) {
            System.out.print(sb.charAt(i) + "\n");
        }
    }
}
 