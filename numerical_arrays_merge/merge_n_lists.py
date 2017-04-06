'A function to merge any number of arrays, given in Python list or tuple'
'Returns sorted array if input arrays are sorted'
'Useful for n-way merge sort problems'
'We take advantage of the fact that input lists are already sorted, so save on computational complexity'
'Author: Harsh Vardhan(harshvardhan.mse@gmail.com)'
'Dec 04, 2016'

#include mergebase.py in the same folder as this file
import mergebase

####Function 1
#Main function for sorting n arrays in increasing order
#Input: n integer arrays, comma separated, all increasingly sorted
#Output: Increasingly sorted integer array formed by merging all input arrays
def mergeAllListsInc(*arg):
    params = locals()
    if(len(arg) >= 2):        
        mergedList = []
        for lists in list(params['arg']):
            mergedList = mergebase.mergeTwoListsInc(mergedList, lists)
        return mergedList
    elif(len(arg) == 1):
        return list(params['arg'])[0]

#Examples
#print(mergeAllListsInc([1,4,6,7], [8,9], (2,3,5), [2,9,15,18]))
#print(mergeAllListsInc([1,4,6,7], [8,9], [2,3,5]))
#print(mergeAllListsInc((1,4,6,7), [8,9]))
#print(mergeAllListsInc([1,4,6,7]))
#print(mergeAllListsInc())

####Function 2
#Main function for sorting n arrays in decreasing order
#Input: n integer arrays, comma separated, all decreasingly sorted
#Output: Decreasingly sorted integer array formed by merging all input arrays
def mergeAllListsDec(*arg):
    params = locals()
    if(len(arg) >= 2):        
        mergedList = []
        for lists in list(params['arg']):
            mergedList = mergebase.mergeTwoListsDec(mergedList, lists)
        return mergedList
    elif(len(arg) == 1):
        return list(params['arg'])[0]    

#Examples
#print(mergeAllListsDec([7,6,4,1], [9,8], (5,3,2), [18,15,9,2]))
#print(mergeAllListsDec([7,6,4,1], [9,8], [5,3,2]))
#print(mergeAllListsDec([7,6,4,1], [9,8]))
#print(mergeAllListsDec([7,6,4,1]))
#print(mergeAllListsDec())

######Some applications may require that the n input arrays are in descending order and we need to merge them in ascending order, and vice versa

####Function 3
#Base function for n arrays sorted in descending order and to be merged in ascending order
#Input: n integer arrays, decreasingly sorted
#Output: An integer array consisting of input arrays merged and overall increasingly sorted
def mergeAllListsDecToInc(*arg):
    params = locals()
    if(len(arg) >= 2):        
        mergedList = []
        inputList = list(params['arg'])
        mergedList = mergebase.mergeTwoListsDecToInc(mergedList, inputList[0])
        inputList.pop(0)
        for lists in inputList:
            mergedList = mergebase.mergeTwoListsIncAndDecToInc(mergedList, lists)
        return mergedList
    elif(len(arg) == 1):
        return mergebase.mergeTwoListsDecToInc(list(params['arg'])[0], [])

#Examples
#print(mergeAllListsDecToInc([7,6,4,1], [9,8], (5,3,2), [18,15,9,2]))
#print(mergeAllListsDecToInc([7,6,4,1], [9,8], [5,3,2]))
#print(mergeAllListsDecToInc([7,6,4,1], [9,8]))
#print(mergeAllListsDecToInc([7,6,4,1]))
#print(mergeAllListsDecToInc())

####Function 4
#Base function for n arrays sorted in increasing order and to be merged in decreasing order
#Input: n integer arrays, increasingly sorted
#Output: An integer array consisting of input arrays merged and overall decreasingly sorted
def mergeAllListsIncToDec(*arg):
    params = locals()
    if(len(arg) >= 2):        
        mergedList = []
        inputList = list(params['arg'])
        mergedList = mergebase.mergeTwoListsIncToDec(mergedList, inputList[0])
        inputList.pop(0)
        for lists in inputList:
            mergedList = mergebase.mergeTwoListsDecAndIncToDec(mergedList, lists)
        return mergedList
    elif(len(arg) == 1):
        return mergebase.mergeTwoListsIncToDec(list(params['arg'])[0], [])

#Examples
#print(mergeAllListsIncToDec([1,4,6,7], [8,9], (2,3,5), [2,9,15,18]))
#print(mergeAllListsIncToDec([1,4,6,7], [8,9], [2,3,5]))
#print(mergeAllListsIncToDec((1,4,6,7), [8,9]))
#print(mergeAllListsIncToDec([1,4,6,7]))
#print(mergeAllListsIncToDec())

