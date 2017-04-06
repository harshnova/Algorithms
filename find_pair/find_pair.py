'Program to find the number of integer elements that have a pair in the given set of inputs, and number of times for which they have a pair'
'Author: Harsh Vardhan(harshvardhan.mse@gmail.com)'
'First commit: Dec 21, 2016'

import sys

## main functions to find pairable elements and number of times they have pairs
##input: a comma separated sequence of integers that are to be analyzed for existing pairs within them
##output: an analysis that tells how many numbers have pairs, how many times they have pairs, and what numbers do not have pairs

#approach A (using occurances count logic, see documentation)
def find_pair_a(*arg):
    pairs = {}
    noPairs = []
    try:
        if(len(arg) == 0):
            sys.stderr.write('Cant accept blank input.\n')
            return(-1)
        else:
            params = locals()
            items = list(params['arg'])
            try:
                frequencyTable = dict((i, items.count(i)) for i in items)
                for key in frequencyTable:
                    if((frequencyTable[key] > 0) and (frequencyTable[key]%2 == 0)):
                        pairs[key]=int(frequencyTable[key]/2)
                    elif((frequencyTable[key] > 1) and (frequencyTable[key]%2 == 1)):
                        pairs[key]=int((frequencyTable[key]-1)/2)
                        noPairs.append(key)
                    else:
                        noPairs.append(key)
                return(pairs, noPairs)
            except Exception as e:
                sys.stderr.write('Invalid inputs. ' + str(e) + '.\n')
                return(-1)           
    except Exception as e:
        sys.stderr.write('Some error in inputs. ' + str(e) + '.\n')
        return(-1)

#approach B (using pair search, see documentation)
def find_pair_b(*arg):
    searchOn = True
    pairs = []
    noPairs = []
    try:
        if(len(arg) == 0):
            searchOn = False
            sys.stderr.write('Cant accept blank input.\n')
            return(-1)
        else:
            params = locals()
            items = list(params['arg'])
            try:
                while(searchOn):
                    if(len(items) == 0):
                        searchOn = False
                    else:
                        try:
                            item = items[0]
                            i = items[1:].index(item)
                            items.pop(0)
                            items.pop(i)
                            pairs.append(item)
                        except ValueError:
                            noPairs.append(item)
                            items.pop(0)
                return(pairs, noPairs)     
            except Exception as e:
                sys.stderr.write('Invalid inputs. ' + str(e) + '.\n')
                return(-1)           
    except Exception as e:
        sys.stderr.write('Some error in inputs. ' + str(e) + '.\n')
        return(-1)

#executing the main function
if __name__ == '__main__':
    #an example input on approach A
    sys.stdout.write('Using approach A-->\n')
    response = find_pair_a(10,20,20,10,10,30,50,10,20)
    if(not(response == -1)):
        pairs = response[0]
        noPairs = response[1]
        sys.stdout.write('{0} numbers have found pairs.\n'.format(len(pairs)))
        for key in pairs:            
            sys.stdout.write('{0} found pair {1} time(s).\n'.format(key, pairs[key]))
        sys.stdout.write('The following numbers could not find pairs: \n' + str(noPairs) + '\n')
        del pairs
        del noPairs
    else:
        sys.stdout.write('Could not analyze the inputs. Check the error.\n')
    sys.stdout.write('\n\n')    
    #an example input on approach B
    sys.stdout.write('Using approach B-->\n')
    response = find_pair_b(10,20,20,10,10,30,50,10,20)
    if(not(response == -1)):
        pairs = response[0]
        noPairs = response[1]
        frequencyTable = dict((i, pairs.count(i)) for i in pairs)
        sys.stdout.write('{0} numbers have found pairs.\n'.format(len(frequencyTable)))
        for key in frequencyTable:
            sys.stdout.write('{0} found pair {1} time(s).\n'.format(key, frequencyTable[key]))
        sys.stdout.write('The following numbers could not find pairs: \n' + str(noPairs) + '\n')
        del pairs
        del noPairs
    else:
        sys.stdout.write('Could not analyze the inputs. Check the error.\n')
        
        
        
