###
# A program for swapping two variable values
#

x = 7
y = 34
z = 0  # additional, auxiliary variable
print("Before swapping: x =", x, "y =", y)

# swap the values
z = x   # store x in z
x = y   # copy y into x
y = z   # copy old x (stored in z) into y

print("After swapping: x =", x, "y =", y)
