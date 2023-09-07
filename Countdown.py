# As part of an online quiz gam eyou have been asked to write some code that displays a bonus score
# the score starts at 1 000 000 and count down in steps of 100 000 to zero
# At the end of the countdown print "Bonus points lost"

countdown = 1000000
print("Bonus Points: " + str(countdown))
while countdown > 0:
    countdown -= 100000
    print("Bonus Points: " + str(countdown))

print("Bonus Points Lost!")

# Now this piece of code uses for loops to print out a tree
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print("£", end=" ")
    
    print() #this puts the next code on a new line 