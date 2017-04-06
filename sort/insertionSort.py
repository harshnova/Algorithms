import sys

#method for iterative sorting
def insertion_sort_iterative(shuffledArray, sortReversed = False):
    if(not(shuffledArray == None)):
        if(not(len(shuffledArray) == 0)):
            if(not(len(shuffledArray) == 1)):
                for i in range(1, len(shuffledArray)):
                    for j in reversed(range(0,i)):
                        try:
                            if(not(sortReversed)):
                                if(shuffledArray[i] < shuffledArray[j]):
                                    k = shuffledArray[j]
                                    shuffledArray[j] = shuffledArray[i]
                                    shuffledArray[i] = k
                                    i -= 1
                            elif(sortReversed):
                                if(shuffledArray[i] > shuffledArray[j]):
                                    k = shuffledArray[j]
                                    shuffledArray[j] = shuffledArray[i]
                                    shuffledArray[i] = k
                                    i -= 1
                        except Exception as e:
                            return(1,"Datatype error encountered. " + str(e) + "\n")
                return(0, shuffledArray)
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
    # output = insertion_sort_iterative(inputArray)
    #decreasing order
    output = insertion_sort_iterative(inputArray, True)
    if(output[0] == 1):
        sys.stderr.write(output[1])
    else:
        sys.stdout.write(str(output[1]) + "\n")
