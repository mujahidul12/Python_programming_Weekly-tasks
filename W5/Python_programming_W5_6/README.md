# W5_6
Make a menu-driven Python program which mimics Tally Counter.

This menu-driven program must contain a maintainable program structure with the following requirements:

* main function which represents the main program logic including menu cycle.
* showOptions function which takes no arguments, shows the available options in the standard output and returns None.
* askChoice function which takes no arguments, prompts user to insert choice and returns an integer regardless of the user feed.
In case user incorrectly inserts text as a choice, the program must output "Unknown option!". For this, see the string method isnumeric().

See other requirements in the example program runs below.

Example program runs

Run 1
````
Program starting.
Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 1
Current count - 0

Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 0
Exiting program.

Program ending.
````

Run 2
````
Program starting.
Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 2
Count increased!

Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 1
Current count - 1

Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 0
Exiting program.

Program ending.
````

Run 3
````
Program starting.
Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 1
Current count - 0

Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 2
Count increased!

Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 3
Cleared count!

Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 1
Current count - 0

Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 0
Exiting program.

Program ending.
````

Run 4
````
Program starting.
Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 4
Unknown option!

Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 0
Exiting program.

Program ending.
````

Run 5
````
Program starting.
Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 2
Count increased!

Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 2
Count increased!

Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 2
Count increased!

Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 1
Current count - 3

Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 0
Exiting program.

Program ending.
````

Run 6
````
Program starting.
Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: Show count
Unknown option!

Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: a
Unknown option!

Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 1 - Show count
Unknown option!

Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 1
Current count - 0

Options:
1 - Show count
2 - Increase count
3 - Reset count
0 - Exit
Your choice: 0
Exiting program.

Program ending.
````
