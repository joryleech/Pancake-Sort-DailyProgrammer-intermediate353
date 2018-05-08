# Pancake-Sort-DailyProgrammer-intermediate353
Daily Programmer Challenge - Sort a stack of pancakes with only a spatula

In this challenge you must sort a stack of pancakes by size but you may only flip subsets of the stack from the bottom up. 

## Input

Input a list of numbers with spaces in between. These act as the sizes of the pancakes with smaller numbers equalling smaller pancakes. 

Example Input

    5 8 100 2 30 5
    
## Output 
Outputs the number of flips it took to sort as well as the iterations, removing duplicates from the end of the list.

Example Output

    5 Flips: [5, 8, 100, 2, 30, 5]->[5, 30, 2, 5, 8, 100]->[8, 5, 2, 5, 30, 100]->[5, 2, 5, 8, 30, 100]->[5, 2, 5, 8, 30, 100]->[2, 5, 5, 8, 30, 100]
