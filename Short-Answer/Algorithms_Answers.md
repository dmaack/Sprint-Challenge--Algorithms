#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - incrementing a by n^2, n number of times, is bounded by n^3. So the loop should execute on order of n times


b) O(nlogn) - THe outer loop is executed n times, the inner loop is executed (j) increases by a multiple. So the product of the two create the nlogn time complexity


c) linear O(n) - the recurisve parameter (bunnies) is decremented by 1 in each recursion and the base case is 0. So its linear

## Exercise II
I would use a binary search. 
1- I would start at the center floor of the building and test out whether the egg broke on that floor

  1a- if the egg did break I would know that it would also break on all the floor above me so I can eliminate those floors

2 - I would then move to the floor half way between where I am now and the bottom floor and toss an egg off that floor
  
  2a- if the egg did not break, I can eliminate the floors below me and move to the mid point of my first drop and my previous one and continue until I have exhausted all the drops in this pattern


