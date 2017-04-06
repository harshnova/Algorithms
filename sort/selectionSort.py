import sys

#method for linear search to find max or min, and corresponding position in an array
def find_extreme(shuffledArray, extreme):
    if(extreme == 'min'):
        return(min(shuffledArray), shuffledArray.index(min(shuffledArray)))
    elif(extreme == 'max'):
        return(max(shuffledArray), shuffledArray.index(max(shuffledArray)))

#method for iterative sorting
def selection_sort_iterative(shuffledArray, reversed = False):
    if(not(shuffledArray == None)):
        if(not(len(shuffledArray) == 0)):
            if(not(len(shuffledArray) == 1)):
                for i in range(0, len(shuffledArray)):
                    try:
                        if(not(reversed)):
                            min_encountered = find_extreme(shuffledArray[i:], 'min')
                            k = shuffledArray[i]
                            shuffledArray[i] = min_encountered[0]
                            shuffledArray[min_encountered[1]+i] = k
                        elif(reversed):
                            max_encountered = find_extreme(shuffledArray[i:], 'max')
                            k = shuffledArray[i]
                            shuffledArray[i] = max_encountered[0]
                            shuffledArray[max_encountered[1]+i] = k
                    except Exception as e:
                        return(1,"Datatype error encountered. " + str(e) + "\n")
                return(0,shuffledArray)
            else:
                return(0,shuffledArray)
        else:
            return(1,"There are no numbers for sorting.\n")
    else:
        return(1,"No array is being supplied.\n")

#driver
if __name__ == '__main__':
    #example input to be sorted
    inputArray = [5,9,3,1,2,8,'b',4,7,6,'a']
    #increasing order
    output = selection_sort_iterative(inputArray)
    #decreasing order
    # output = selection_sort_iterative(inputArray, True)
    if(output[0] == 1):
        sys.stderr.write(output[1])
    else:
        sys.stdout.write(str(output[1]) + "\n")
