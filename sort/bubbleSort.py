import sys

#method for iterative sorting
def bubble_sort_iterative(shuffledArray, reversed = False):
    if(not(shuffledArray == None)):
        if(not(len(shuffledArray) == 0)):
            if(not(len(shuffledArray) == 1)):
                swapped = True
                iteration = 1
                while(swapped):
                    swapped = False
                    for i in range(len(shuffledArray) - iteration):
                        try:
                            if(not(reversed)):
                                if(shuffledArray[i] > shuffledArray[i+1]):
                                    k = shuffledArray[i]
                                    shuffledArray[i] = shuffledArray[i+1]
                                    shuffledArray[i+1] = k
                                    swapped = True
                            else:
                                if(shuffledArray[i] < shuffledArray[i+1]):
                                    k = shuffledArray[i]
                                    shuffledArray[i] = shuffledArray[i+1]
                                    shuffledArray[i+1] = k
                                    swapped = True
                        except Exception as e:
                            return(1,"Datatype error encountered. " + str(e) + "\n")
                    iteration += 1
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
    output = bubble_sort_iterative(inputArray)
    #decreasing order
    # output = bubble_sort_iterative(inputArray, True)
    if(output[0] == 1):
        sys.stderr.write(output[1])
    else:
        sys.stdout.write(str(output[1]) + "\n")
