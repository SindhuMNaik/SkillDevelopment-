public class palindrome {
    // Check palindrome
 static boolean checkPalindrome(String str) {
 String reverse = "";

 for (int i = str.length() - 1; i >= 0; i--) {
 reverse = reverse + str.charAt(i);
 }

 return str.equals(reverse);
 }
 public static void main(String[] args) {
    System.err.println("Palindrome:"+checkPalindrome("madam"));
 }
    
}
