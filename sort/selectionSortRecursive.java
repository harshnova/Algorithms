// Pesudocode -->
// loop (each number in the array, designated by index i){
//     if any number on the right of i is smaller than i at index j then
//         swap numbers at i and j
// }

// recursive version algorithm --> 
// find the smallest element in the complete array (0 .. len-1) and swap it with first element
// reduce the array by dropping the first array and then repeat last step on the new remaining (i .. len - 1)
// repeat steps until no elements remaining

// complexity: best O(n^2) worst O(n^2). this complexity is not recommended for large datasets.

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class AlgSortSelection{

    // iterative version
    public static int[] selectionSortIterative(int[] intArray, String order){
        
        for (int i = 0; i < intArray.length; i++){
            for (int j = i+1; j < intArray.length; j++){
                if(order == "ascending"){
                    if(intArray[j] < intArray[i]){
                        swap(intArray, j, i);
                    }
                }else if(order == "descending"){
                    if(intArray[j] > intArray[i]){
                        swap(intArray, j, i);
                    }
                }
            }
        }
        return(intArray);
    }

    // recursive version (frontend)
    // keeping the frontend and backends separate so that user just pass the array and order into the function call
    public static void selectionSortRecursive(int[] intArray, String order){
        if(!(intArray.length == 0 || intArray.length == 1)){ // base case handled
            selectionSortRecursiveBackend(intArray, order, 0, intArray.length);
        }
    }

    // recursive version (backend) -- original recursion logic
    public static void selectionSortRecursiveBackend(int[] intArray, String order, int i, int n){
        // finding the smallest integer and swapping it with first element
        if(order == "ascending"){
            int min = intArray[i];
            int idx = i;
            for (int j = i; j < intArray.length; j++){
                if(intArray[j] < min){
                    min = intArray[j];
                    idx = j;
                }
            }
            swap(intArray, i, idx);
        }else if(order == "descending"){
            int max = intArray[i];
            int idx = i;
            for (int j = i; j < intArray.length; j++){
                if(intArray[j] > max){
                    max = intArray[j];
                    idx = j;
                }
            }
            swap(intArray, i, idx);
        }
        if(i+1 < n){
            selectionSortRecursiveBackend(intArray, order, i+1, n);
        }
    }

    // usage
    public static void main(String[] args){

        int[] unsortedArray0 = {};
        System.out.println("\nOriginal: " + Arrays.toString(unsortedArray0));
        System.out.println("Iterative Ascending: " + Arrays.toString(selectionSortIterative(unsortedArray0, "ascending")));
        System.out.println("Iterative Descending: " + Arrays.toString(selectionSortIterative(unsortedArray0, "descending")));
        selectionSortRecursive(unsortedArray0, "ascending");
        System.out.println("Recursive Ascending: " + Arrays.toString(unsortedArray0));
        selectionSortRecursive(unsortedArray0, "descending");
        System.out.println("Recursive Descending: " + Arrays.toString(unsortedArray0));
        
        int[] unsortedArray1 = {4,6,7,2,3,8,9,0,1,2};
        System.out.println("\nOriginal: " + Arrays.toString(unsortedArray1));
        System.out.println("Iterative Ascending: " + Arrays.toString(selectionSortIterative(unsortedArray1, "ascending")));
        System.out.println("Iterative Descending: " + Arrays.toString(selectionSortIterative(unsortedArray1, "descending")));
        selectionSortRecursive(unsortedArray1, "ascending");
        System.out.println("Recursive Ascending: " + Arrays.toString(unsortedArray1));
        selectionSortRecursive(unsortedArray1, "descending");
        System.out.println("Recursive Descending: " + Arrays.toString(unsortedArray1));
        
        int[] unsortedArray2 = {0};
        System.out.println("\nOriginal: " + Arrays.toString(unsortedArray2));
        System.out.println("Iterative Ascending: " + Arrays.toString(selectionSortIterative(unsortedArray2, "ascending")));
        System.out.println("Iterative Descending: " + Arrays.toString(selectionSortIterative(unsortedArray2, "descending")));
        selectionSortRecursive(unsortedArray2, "ascending");
        System.out.println("Recursive Ascending: " + Arrays.toString(unsortedArray2));
        selectionSortRecursive(unsortedArray2, "descending");
        System.out.println("Recursive Descending: " + Arrays.toString(unsortedArray2));
        
        int[] unsortedArray3 = {1,0};
        System.out.println("\nOriginal: " + Arrays.toString(unsortedArray3));
        System.out.println("Iterative Ascending: " + Arrays.toString(selectionSortIterative(unsortedArray3, "ascending")));
        System.out.println("Iterative Descending: " + Arrays.toString(selectionSortIterative(unsortedArray3, "descending")));
        selectionSortRecursive(unsortedArray3, "ascending");
        System.out.println("Recursive Ascending: " + Arrays.toString(unsortedArray3));
        selectionSortRecursive(unsortedArray3, "descending");
        System.out.println("Recursive Descending: " + Arrays.toString(unsortedArray3));
    }

    // method to swap values at two given indices in an array
    public static void swap(int[] intArray, int i, int j){

        int temp = intArray[i];
        intArray[i] = intArray[j];
        intArray[j] = temp;
    }
}