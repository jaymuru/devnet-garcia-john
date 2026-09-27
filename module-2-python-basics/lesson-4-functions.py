"""
Module 2 — Lesson 4: Functions
Student: Robert John Garcia
Date: 9-27-26

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
A function is a reusable block of code. Instead of writing the same code 
over and over, you write it once, give it a name, and run it whenever you need it. 
It takes inputs (parameters), does a task, and gives back a result (return).

============================================
KEY VOCABULARY
============================================
- def: The keyword used to create (define) a new function.
- parameter: A variable inside the function parentheses that receives incoming data.
- argument: The actual value you pass into the function when you run it.
- return: The keyword that sends the final result back out of the function to your main program.


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""


def calculate_area(length, width):
    area = length * width # Multiply length and width to find the area
    return area


room_area = calculate_area(5, 10)
print(room_area)  

#output is 50


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
I forgot to use the return keyword. I tried to use a variable creat it 
inside the function outside of it which did not work.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
Functions connect to variables and math operations because they take variables as 
inputs perform math or logic on them and output a new value.
"""
