package HW1;
public class hw2 {
    public static void main(String[] args) {
        String[][] arr = {{"1","2"},{"3","4"},{"1","6"}};
        System.out.println(sum2d(arr));
    }
    public static int sum2d(String[][] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) { //NPE
            for (int j = 0; j < 2; j++) { //выход за границы массива
                int val = Integer.parseInt(arr[i][j]); //ошибка парсинга
                sum += val;
            }
        }
        return sum;
    }
}
