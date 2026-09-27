"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Robert John Garcia
Date: 9-27-26

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Control flow is how your code makes choices instead of running every line 
straight down, it sees if something is true and decides what to do next.


============================================
KEY VOCABULARY
============================================
-condition: A statement that is either True or False.
- if / elif / else: Words used to give your program different choices.
- comparison operator: Symbols used to compare values like greater than or equal to.
- boolean: Code that results in True or False.


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

gpa = 96

if gpa <= 96:
    print("President's Lister")
elif gpa <= 91:
    print("Dean's Lister")        # Output: Dean's Lister
else:
    print("Regular Student") # this one is when your grade is 90 below


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
I used a single equals sign instead of a double equals sign when checking if two values were equal.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
