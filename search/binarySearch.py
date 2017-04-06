import sys

#method for binary search of a key inside an array
def binary_search_recursive(inputSet, key):
    'sorting the input set to ensure correct input for binary search'
    inputSet = sorted(inputSet)
    if((key > max(inputSet)) or (key < min(inputSet))):
        return(1, 'Key not found\n')
    mid = int(len(inputSet)/2)
    midElement = inputSet[mid]
    if(key == midElement):
        return(0, 'Key found\n')
    elif(key > midElement):
        return binary_search_recursive(inputSet[mid+1:], key)
    elif(key < midElement):
        return binary_search_recursive(inputSet[:mid], key)

#driver
if __name__ == '__main__':
    #example input to be searched in
    inputArray = [5,9,3,1,2,8,4,7,6]
    key = 2
    #search
    output = binary_search_recursive(inputArray,key)
    if(output[0] == 1):
        sys.stderr.write(output[1])
    else:
        sys.stdout.write(output[1])
