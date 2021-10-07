import java.util.*;

public class greedy_ATM{
	 static int N;
	public static void main(String[] arg) {
		Scanner input = new Scanner(System.in);
		N = input.nextInt();
		int[] arr = new int[N];
		for(int i=0;i<N;i++) {
			arr[i] = input.nextInt();
		}
		ATM(arr);
	}
	
	private static void ATM(int[] array) {
		int[] arr = new int[N];
		Arrays.fill(arr, 0);
		int temp;
		int result=0;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++) {
				if(array[i]<array[j]) {
				temp = array[i];
				array[i] = array[j];
				array[j] = temp;
				}
			}
		}
		for(int i =N-1;i<N;i--) {
			 for(int j =0;j<i+1;j++) {
				arr[i] += array[j];
				 
			 }
		}
		for(int i=0;i<N;i++) {
			result += arr[i];
		}
		System.out.print(result);
	}
}
