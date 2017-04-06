'A function to merge two arrays, given in Python list or tuple'
'Returns sorted array if input arrays are sorted'
'Useful for 2-way merge sort problems'
'We take advantage of the fact that input lists are already sorted, so save on computational complexity'
'Author: Harsh Vardhan(harshvardhan.mse@gmail.com)'
'Dec 04, 2016'

####Function 1
#Base function for two arrays sorted in increasing order
#Input: Two integer arrays, increasingly sorted
#Output: An integer array consisting of input arrays merged and overall increasingly sorted
def mergeTwoListsInc(A, B):
    mergedList = []
    A = list(A)
    B = list(B)
    try:
        while((len(A) > 0) and (len(B) > 0)):
            if(A[0] < B[0]):
                mergedList.append(A[0])
                A.pop(0)
            else:
                mergedList.append(B[0])
                B.pop(0)
    except:
            print('Invlid input array. Contains non integer assets')
    if(len(A) == 0):
        mergedList.extend(B[0:])
    else:
        mergedList.extend(A[0:])
    if(len(mergedList) >= 1):
        return mergedList

#Examples
#print(mergeTwoListsInc([2,3,3.5,5], [1,4,6,6.8,7,8]))
#print(mergeTwoListsInc([1,4,6,7,8], [2,3,5]))
#print(mergeTwoListsInc((2,3,5), [1,4,6]))
#print(mergeTwoListsInc([], [1,4,6,7]))
#print(mergeTwoListsInc([2,3,5], []))
#print(mergeTwoListsInc(['a',3,5], [1,4,6,7]))


####Function 2
#Base function for two arrays sorted in decreasing order
#Input: Two integer arrays, decreasingly sorted
#Output: An integer array consisting of input arrays merged and overall decreasingly sorted
def mergeTwoListsDec(A, B):
    mergedList = []
    A = list(A)
    B = list(B)
    try:
        while((len(A) > 0) and (len(B) > 0)):
            if(A[0] > B[0]):
                mergedList.append(A[0])
                A.pop(0)
            else:
                mergedList.append(B[0])
                B.pop(0)
    except:
            print('Invlid input array. Contains non integer assets')
    if(len(A) == 0):
        mergedList.extend(B[0:])
    else:
        mergedList.extend(A[0:])
    if(len(mergedList) >= 1):
        return mergedList

#Examples
#print(mergeTwoListsDec([5,3,2], [8,7,6,4,1]))
#print(mergeTwoListsDec([8,7,6,4,1], [5,3,2]))
#print(mergeTwoListsDec((5,3,2), [6,4,1]))
#print(mergeTwoListsDec([], [7,6,4,1]))
#print(mergeTwoListsDec([5,3,2], []))
#print(mergeTwoListsDec(['a',5,3], [7,6,4,1]))


######Some applications may require that the two input arrays are in descending order and we need to merge them in ascending order, and vice versa

####Function 3
#Base function for two arrays sorted in descending order and to be merged in ascending order
#Input: Two integer arrays, decreasingly sorted
#Output: An integer array consisting of input arrays merged and overall increasingly sorted
def mergeTwoListsDecToInc(A, B):
    mergedList = []
    A = list(A)
    B = list(B)
    try:
        while((len(A) > 0) and (len(B) > 0)):
            if(A[len(A) - 1] < B[len(B) - 1]):
                mergedList.append(A[len(A) - 1])
                A.pop(len(A) - 1)
            else:
                mergedList.append(B[len(B) - 1])
                B.pop(len(B) - 1)
    except:
            print('Invlid input array. Contains non integer assets')
    if(len(A) == 0):
        i = len(B)
        while(i > 0):
            mergedList.append(B[i-1])
            i = i - 1
    else:
        j = len(A)
        while(j > 0):
            mergedList.append(A[j-1])
            j = j - 1
    if(len(mergedList) >= 1):
        return mergedList

#Examples
#print(mergeTwoListsDecToInc([5,3,2], [8,7,6,4,1]))
#print(mergeTwoListsDecToInc([8,7,6,4,1], [5,3,2]))
#print(mergeTwoListsDecToInc((5,3,2), [6,4,1]))
#print(mergeTwoListsDecToInc([], [7,6,4,1]))
#print(mergeTwoListsDecToInc([5,3,2], []))
#print(mergeTwoListsDecToInc(['a',5,3], [7,6,4,1]))
  
####Function 4
#Base function for two arrays sorted in ascending order and to be merged in descending order
#Input: Two integer arrays, increasingly sorted
#Output: An integer array consisting of input arrays merged and overall decreasingly sorted
def mergeTwoListsIncToDec(A, B):
    mergedList = []
    A = list(A)
    B = list(B)
    try:
        while((len(A) > 0) and (len(B) > 0)):
            if(A[len(A) - 1] > B[len(B) - 1]):
                mergedList.append(A[len(A) - 1])
                A.pop(len(A) - 1)
            else:
                mergedList.append(B[len(B) - 1])
                B.pop(len(B) - 1)
    except:
            print('Invlid input array. Contains non integer assets')
    if(len(A) == 0):
        i = len(B)
        while(i > 0):
            mergedList.append(B[i-1])
            i = i - 1
    else:
        j = len(A)
        while(j > 0):
            mergedList.append(A[j-1])
            j = j - 1
    if(len(mergedList) >= 1):
        return mergedList

#Examples
#print(mergeTwoListsIncToDec([2,3,5], [1,4,6,7,8]))
#print(mergeTwoListsIncToDec([1,4,6,7,8], [2,3,5]))
#print(mergeTwoListsIncToDec((2,3,5), [1,4,6]))
#print(mergeTwoListsIncToDec([], [1,4,6,7]))
#print(mergeTwoListsIncToDec([2,3,5], []))
#print(mergeTwoListsIncToDec(['a',3,5], [1,4,6,7]))


######Some applications may require that the two input arrays are in increasing and descending orders respectively and we need to merge them in ascending or descending
#orders, and arrays provided in descending and ascending orders respcetively to again ascending or descending orders


####Function 5
#Base function for two arrays sorted in ascending and descending order respectively and to be merged in overall ascending order
#Input: Two integer arrays, increasingly(A) and decreasingly(B) sorted respectively
#Output: An integer array consisting of input arrays merged and overall increasingly sorted
def mergeTwoListsIncAndDecToInc(A, B):
    mergedList = []
    A = list(A)
    B = list(B)
    try:
        while((len(A) > 0) and (len(B) > 0)):
            if(A[0] < B[len(B) - 1]):
                mergedList.append(A[0])
                A.pop(0)
            else:
                mergedList.append(B[len(B) - 1])
                B.pop(len(B) - 1)
    except:
            print('Invlid input array. Contains non integer assets')
    if(len(A) == 0):
        i = len(B)
        while(i > 0):
            mergedList.append(B[i-1])
            i = i - 1
    else:
        mergedList.extend(A[0:])
    if(len(mergedList) >= 1):
        return mergedList

#Examples
#print(mergeTwoListsIncAndDecToInc([1,4,6,7,8,9], [5,3,2]))
#print(mergeTwoListsIncAndDecToInc([2,3,5], [9,8,7,6,4,1]))

####Function 6
#Base function for two arrays sorted in ascending and descending order respectively and to be merged in overall descending order
#Input: Two integer arrays, increasingly(A) and decreasingly(B) sorted respectively
#Output: An integer array consisting of input arrays merged and overall decresingly sorted
def mergeTwoListsIncAndDecToDec(A, B):
    mergedList = []
    A = list(A)
    B = list(B)
    try:
        while((len(A) > 0) and (len(B) > 0)):
            if(A[len(A) - 1] < B[0]):
                mergedList.append(A[0])
                A.pop(0)
            else:
                mergedList.append(B[0])
                B.pop(0)
    except:
            print('Invlid input array. Contains non integer assets')
    if(len(A) == 0):
        mergedList.extend(B[0:])
    else:
        j = len(A)
        while(j > 0):
            mergedList.append(A[j-1])
            j = j - 1
        
    if(len(mergedList) >= 1):
        return mergedList

#Examples
#print(mergeTwoListsIncAndDecToInc([1,4,6,7,8,9], [5,3,2]))
#print(mergeTwoListsIncAndDecToInc([2,3,5], [9,8,7,6,4,1]))

####Function 7
#Base function for two arrays sorted in descending and ascending order respectively and to be merged in overall descending order
#Input: Two integer arrays, decreasingly(A) and increasingly(B) sorted respectively
#Output: An integer array consisting of input arrays merged and overall decresingly sorted
def mergeTwoListsDecAndIncToDec(A, B):
    mergedList = []
    A = list(A)
    B = list(B)
    try:
        while((len(A) > 0) and (len(B) > 0)):
            if(A[0] > B[len(B) - 1]):
                mergedList.append(A[0])
                A.pop(0)
            else:
                mergedList.append(B[len(B) - 1])
                B.pop(len(B) - 1)
    except:
            print('Invlid input array. Contains non integer assets')
    if(len(A) == 0):
        i = len(B)
        while(i > 0):
            mergedList.append(B[i-1])
            i = i - 1
    else:
        mergedList.extend(A[0:])
        
    if(len(mergedList) >= 1):
        return mergedList

#Examples
#print(mergeTwoListsDecAndIncToDec([5,3,2], [1,4,6,7,8,9]))
#print(mergeTwoListsDecAndIncToDec([9,8,7,6,4,1], [2,3,5]))


####Function 8
#Base function for two arrays sorted in descending and ascending order respectively and to be merged in overall ascending order
#Input: Two integer arrays, decreasingly(A) and increasingly(B) sorted respectively
#Output: An integer array consisting of input arrays merged and overall increasingly sorted
def mergeTwoListsDecAndIncToInc(A, B):
    mergedList = []
    A = list(A)
    B = list(B)
    try:
        while((len(A) > 0) and (len(B) > 0)):
            if(A[len(A) - 1] < B[0]):
                mergedList.append(A[len(A) - 1])
                A.pop(len(A) - 1)
            else:
                mergedList.append(B[0])
                B.pop(0)
    except:
            print('Invlid input array. Contains non integer assets')
    if(len(A) == 0):
        mergedList.extend(B[0:])
    else:
        j = len(A)
        while(j > 0):
            mergedList.append(A[j-1])
            j = j - 1
        
    if(len(mergedList) >= 1):
        return mergedList

#Examples
#print(mergeTwoListsDecAndIncToInc([5,3,2], [1,4,6,7,8,9]))
#print(mergeTwoListsDecAndIncToInc([9,8,7,6,4,1], [2,3,5]))
