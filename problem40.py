a = "Nawsheen Salsabeel"

print(a[2])   # Output: w
print(a[4])   # Output: h

# Visualization
#
# Outer loop:
# "CAT"
#
# Iteration 1:
# i = 'C'
#     print(C)
#
#     Inner loop starts
#     N
#     a
#     w
#     s
#     h
#     e
#     e
#     n
#       (space)
#     S
#     a
#     l
#     s
#     a
#     b
#     e
#     e
#     l
#
# Iteration 2:
# i = 'A'
#     print(A)
#
#     Inner loop prints the whole string again.
#
# Iteration 3:
# i = 'T'
#     print(T)
#
#     Inner loop prints the whole string again.

for i in "CAT":
    print(i)

    for i in a:
        print(i)




 # Strings in Python are sequences of characters.
# Each character has an index starting from 0.
# We can access individual characters using square brackets [].
# Strings are immutable, meaning individual characters cannot be changed.    