'Program to find the final array after a sequence of left and/or right rotations on the input array'
'Author: Harsh Vardhan(harshvardhan.mse@gmail.com)'
'First commit: Dec 04, 2016'

#Defining the rotation operation
#Input: array = the array(list) to be rotated
#Input: direction = 'l' for left and 'r' for right rotations
#Output: the array rotated in the provided direction
def rotate(array, direction):
    try:
        if(direction == 'l'):
            arrayInit = array[0]
            array = array[1:]
            array.append(arrayInit)
        elif(direction == 'r'):
            arrayFin = array[len(array) - 1]
            array.insert(0, arrayFin)
            array.pop(len(array) - 1) 
        return(array)  
    except:
        return('Invalid roration input(s)')    

#User inputs and rotation sequence
#Command line inputs:
#1. Number of elements in the array
#2. Array elements space separated in one row
#3. Rotation sequence consisting of left('l') and right ('r') rotations linked by the separator('-'), check example
def rotate_array():
    input_array = []
    i = 0
    array_satisfied = False
    rotation_sequence_satisfied = False
    try:
        size = int(input('Enter the array size: '))
        print('Enter the array elements of 1 x {0} array space separated: '.format(size))
        while((i <= 0) and (not(array_satisfied))):    
            try:
                input_array = [int(x) for x in input().strip().split(' ')]
                if((not(int(len(input_array)) == int(size)))):
                    array_satisfied = False
                    print('Invalid argument. Size should be {0}. Enter again.'.format(size))                    
                else:
                    array_satisfied = True
                    i += 1                    
            except:
                array_satisfied = False
                print('Invalid input(s) in forming input array rows. Enter again.')                
        while(not(rotation_sequence_satisfied)):
            try:
                print('Enter the rotation sequence:')
                rotation_sequence = [ops for ops in input().strip().split('-')]
                for ops in rotation_sequence:                       
                    if((ops not in ['r', 'l']) or (not(int(len(ops)) == 1))):
                        rotation_sequence_satisfied = False  
                        print('Invalid rotation sequence.')
                        break
                    else:
                        rotation_sequence_satisfied = True
                        input_array = rotate(input_array, ops)
            except:
                rotation_sequence_satisfied = False  
                print('Invalid rotation sequence. Enter again.')                         
    except:
        print('Invalid input size. Enter again.')
        rotate_array()
    return(input_array)
        
#Example 1 (As the program is set on run on the command line)
#Enter the array size: 5
#Enter the array elements of 1 x 1 array space separated:
#1 2 3 4 5 
#Enter the rotation sequence:
#r-l-l-l-r-l-l-r-r
#Final rotated array is: [2, 3, 4, 5, 1]

#If any improper input is provided, user will be prompted to enter the input again

#Calling the function and allowing user to provide the inputs as the program is set on run
print('\nFinal rotated array is: ' + str(rotate_array()))
    
    
