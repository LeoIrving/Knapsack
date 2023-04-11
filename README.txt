Artificial Intelligence - Programming Assignment 1

Jiangjie Bian jb6942

Notes for Input:

1. By creating a 'test.txt' and pasting data into 'test.txt', you can directly test the program by running either 'Knapsack-ID.py' or 'Knapsack-HC.py'. Make sure all the files are in the same folder. If you are using an input txt file with name other than 'test.txt', please change the file name and routing in the source code (line 52 in 'Knapsack-ID.py' and line 68 in 'Knapsack-HC.py')

2. Please strictly follow the input format shown below (the length of space between data each does not matter)
20.0 10.0
A 10.0 8.0
B 8.0 4.0
C 7.0 3.0
D 6.0 3.0
E 4.0 1.0 

Notes for Output (Knapsack-HC):

1. The order of the goal state is not followed the alphabetic order. Sorry for the inconvenience.

2.  There might be many solution for some data set. Please be patient to rerun the program in order to get the result
(Input 1) There are many solution for this test. Please be patient to rerun the program in order to get an output as [A, B, J]
(Input 2) There are many solution for this test. Please be patient to rerun the program in order to get an output as [B, D, E]

3. There might be some special cases in which the goal is not found during ten repeats due to probability. Please be patient to rerun the program in order to get the result

4. Due to defect in hill climbing search (which could be solved by sideways motion), the program might stuck in the infinity loop: there are two neighbor states which are the best state among all their neighbors but their errors are exactly the same and not equal to 0.
(Input 4) Please press Ctrl + C (Wins) to manually interrupt the infinity loop