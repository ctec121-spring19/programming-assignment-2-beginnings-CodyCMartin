# Module 2
#   Programming Assignment 2
#     Prob-3.py

# YOUR NAME
# Cody Martin

def example():
    print("\nExample Output")

    # print a blank line
    print()

    # create three variables and assign three values in a single statement
    v1, v2, v3 = 21, 12.34, "hello"

    # print the variables
    print("v1:", v1)
    print("v2:", v2)
    print("v3:", v3)


def studentCode():
    # replace <name> with your name
    print("\nCody's Output")
    
    # print a blank line
    print()

    # replicate the assignment statement above, but use your own variable
    # names and values
    A, B, C = 21, 12.34, "hello"

    # print the values of the 3 variables
    print("A:", A)
    print("B:", B)
    print("C:", C)

    print()

    # Get 3 values from the user and assign them to the variables defined
    A, B, C = eval(input("Input 3 values seperated by commas: "))
    print(A,B,C)
    # above. See the page in Canvas on Simulataneous Assignment
    # BONUS POINTS for using the split() method

    print()

example()
studentCode()

