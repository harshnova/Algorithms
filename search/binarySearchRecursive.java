public class AlgSearchBinary{

    public static void main(String[] args){
        int[] sortedArray = {2,4,6,8,10,12,14,16,18};
        int target = 12;
        // iterative
        System.out.println(binarySearchIterative(sortedArray, target));
        // recursive
        int keyExists = search(sortedArray, target);
        System.out.println(keyExists);
    }

    // iterative
    public static int binarySearchIterative(int[] integers, int integer){
        int low = 0;
        int high = integers.length - 1;
        while (low <= high){
            int mid = (low + high) / 2;
            if(integers[mid] == integer){
                return(mid);
            }else if(integers[mid] < integer){
                low = mid + 1;
            }else{
                high = mid - 1;
            }
        }
        return(-1);
    }

    // recursive
    public static int binarySearchRecursive(int[] sortedArray, int target, int low, int high){
        if(high < low){
            return(-1);
        }
        int mid = (low + high) / 2;
        if(sortedArray[mid] == target){
            return(mid);
        }else if(sortedArray[mid] < target){
            return(binarySearchRecursive(sortedArray, target, mid+1, high));
        }else if(sortedArray[mid] > target){
            return(binarySearchRecursive(sortedArray, target, low, mid-1));
        }else{
            return(-1);
        }
    }

    public static int search(int[] sortedArray, int target){
        int low = 0;
        int high = sortedArray.length-1;
        return(binarySearchRecursive(sortedArray, target, low, high));
    }
}