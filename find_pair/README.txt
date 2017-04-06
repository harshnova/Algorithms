DOCUMENTATION

---------------------------------------------------------------------------------------
Purpose: 
---------------------------------------------------------------------------------------
Given a set of numbers, this utility would analyze the set to find out which
numbers are in pairs in the set, and how many times they pair. 
For example, the in the set (10, 20, 30, 10, 10, 30, 10), 
10 (4 occurances) has a pair and pairs two times (10-10, 10-10). 
30 (2 occurances) has a pair and pairs once (30-30). 
20 (1 occurance) has no pair (20-).

---------------------------------------------------------------------------------------
Solution approach A (occurances count):
---------------------------------------------------------------------------------------
From the above analysis, we understand the pattern:
If the number of occurances is even and greater than 0, then the item has a pair, 
and number of time it pairs is equal to its occurance frequency divided by 2.  

If the number of occurances is odd and greater than 1, then the item has a pair, 
and the number of times it pairs is equal to (its occurance frequency - 1) / 2
and one residual copy of that number will not pair

If the number of occurances is 1, the number has no pair.

---------------------------------------------------------------------------------------
Solution approach B (pair search):
---------------------------------------------------------------------------------------
On line 42 at the onset of the code run, we assume that pair search is on.
We keep on searching for the pairs inside the list and remove the pair from the list
to put it inside another list that contains the found pairs. 
As the elements from the input set are kept on getting removed, the set length get reduced to 
zero. On line 56, we stop the search as the length of input set is zero.
To search pairs, we consider first element (call it pivot) of the input set, on line 59.
Then we search second element onwards if there is any pair for the pivot, on line 60.
If there is a pair for the pivot, we clean off the pivot and pairing number from the list
on line numbers 61 and 62, and put this pairable number in an array that contains all pairable
numbers, on line 63.
If the search on line 60 does not return any pairing number, we clean off the pivot from the
set, on line 66 and add this number to an array of non-pairable numbers on line 66.


