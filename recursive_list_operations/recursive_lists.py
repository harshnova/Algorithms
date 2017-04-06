'Programs to manipulate nested lists to find useful information using recursion'
'Author: Harsh Vardhan(harshvardhan.mse@gmail.com)'
'First commit: Dec 04, 2016'


####Function 1
#Find the extreme number in the nested list
#Input: args = nested list of numbers
#Input: extreme = minimum of maximum extreme number identifer. set 'min' to find minimum. set 'max' to find maximum.
#Input: initiator = initiator to find the first number in the nested list to be used as benchmark. initiator shall always be set to 1.
#Output: extreme number in the root nested list according to the extreme variable identifier 

def extreme_number(args, extreme, initiator = 1):
    try:
        global extremum
        if(initiator == 1):
            if(not(type(args[0]) == type([]))):
                extremum = args[0]
            else:
                extremum = extreme_number(args[0], extreme)
        for item in args:
            if((type(item)) == type([])):
                extremum = extreme_number(item, extreme, 0)
            else:
                if(extreme == 'min'):
                    if item < extremum:
                        extremum = item
                elif(extreme == 'max'):
                    if item > extremum:
                        extremum = item
        return extremum
    except:
        return('Invalid input(s)')

#Examples
#print(extreme_number([2, 9, [1, 13], 8, 6], 'min', 1))
#print(extreme_number([2, [[100, 1], 90], [10, 13], 8, 6], 'min', 1))
#print(extreme_number([2, [[13, -7], 90], [1, 100], 8, 6], 'min', 1))
#print(extreme_number([[[-13, 7], 90], 2, [1, 100], 8, 6], 'min', 1))
#print(extreme_number([2, 9, [1, 13], 8, 6], 'max', 1))
#print(extreme_number([2, [[100, 1], 90], [10, 13], 8, 6], 'max', 1))
#print(extreme_number([2, [[13, -7], 90], [1, 100], 8, 6], 'max', 1))
#print(extreme_number([[[-13, 7], 90], 2, [1, 100], 8, 6], 'max', 1))


####Function 2
#Count the number of occurances of a target number in a nested list
#Input: target = target number whose count of occurances in the nested list is to be determined.
#Input: args = nested list of numbers
#Output: Number of times the target has been found in the root nested list
def count_target(target, args):
    try:
        count = 0
        for item in args:
            if(type(item) == type([])):
                count = count + count_target(target, item)
            else:
                if(item == target):
                    count = count + 1
        return count
    except:
        return('Invalid input(s)')

#Examples
#print(count_target(2, []))
#print(count_target(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]))
#print(count_target(7, [[9, [7, 1, 13, 2], 8], [7, 6]]))
#print(count_target(15, [[9, [7, 1, 13, 2], 8], [2, 6]]))
#print(count_target(5, [[5, [5, [1, 5], 5], 5], [5, 6]]))
#print(count_target("a", [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]))
    

####Function 3
#De-nest all the lists inside a nested list, to a single list of numbers in the order of their visual occurance
#Input: args = nested list of numbers
#Output: A list which has no nested lists, and contains all the numbers in the root nested list. 
def flatten(args):
    try:
        flat_list = []
        for item in args:
            if(type(item) == type([])):
                flat_list.extend(flatten(item))
            else:
                flat_list.append(item)
        return flat_list
    except:
        return('Invalid input(s)')

#Examples
#print(flatten([2,9,[2,1,13,2],8,[2,6]]))
#print(flatten([[9,[7,1,13,2],8],[7,6]]))
#print(flatten([[9,[7,1,13,2],8],[2,6]]))
#print(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]))
#print(flatten([]))
            
        
