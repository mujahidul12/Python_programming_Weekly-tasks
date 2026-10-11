# W4_7

The mathematical problem, Multiplicative persistency, is described in the following [video](https://youtu.be/Wim9WJeDTHQ)

Also at the [wikipedia](https://en.wikipedia.org/wiki/Persistence_of_a_number)

Create program which prompts the user to insert an integer and then display the steps to calculate the multiplicative persistency based on the user input.

In short, the steps in the multiplicative persistency is calculated by multiplying digits together in a given integer. This process is then repeated for the result which makes the result value smaller on each iteration till the result contains only one digit.

The program must stop the iteration when the result contains only one digit. Finally before the program closes, it shows the steps taken.

Run 1
````
Program starting.

Check multiplicative persistence.
Insert an integer: 277777788888899
2 * 7 * 7 * 7 * 7 * 7 * 7 * 8 * 8 * 8 * 8 * 8 * 8 * 9 * 9 = 4996238671872
4 * 9 * 9 * 6 * 2 * 3 * 8 * 6 * 7 * 1 * 8 * 7 * 2 = 438939648
4 * 3 * 8 * 9 * 3 * 9 * 6 * 4 * 8 = 4478976
4 * 4 * 7 * 8 * 9 * 7 * 6 = 338688
3 * 3 * 8 * 6 * 8 * 8 = 27648
2 * 7 * 6 * 4 * 8 = 2688
2 * 6 * 8 * 8 = 768
7 * 6 * 8 = 336
3 * 3 * 6 = 54
5 * 4 = 20
2 * 0 = 0
No more steps.

This program took 11 step(s)

Program ending.
````

Run 2
````
Program starting.

Check multiplicative persistence.
Insert an integer: 796
7 * 9 * 6 = 378
3 * 7 * 8 = 168
1 * 6 * 8 = 48
4 * 8 = 32
3 * 2 = 6
No more steps.

This program took 5 step(s)

Program ending.
````

Run 3
````
Program starting.

Check multiplicative persistence.
Insert an integer: 10000000000
1 * 0 * 0 * 0 * 0 * 0 * 0 * 0 * 0 * 0 * 0 = 0
No more steps.

This program took 1 step(s)

Program ending.
````

Run 4
````
Program starting.

Check multiplicative persistence.
Insert an integer: 7
No more steps.

This program took 0 step(s)

Program ending.
````
