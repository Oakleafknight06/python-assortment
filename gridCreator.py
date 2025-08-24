# Create a grid
squareDimension = int(input("Input the length of one side of the n*n square: "))
spacing = int(input("Input the spacing between the grid lines: "))

i = 1
j = 1
intersections = []
iList = []
jList = []
while i <= squareDimension:
    if i % spacing == 0:
        j = 1
        while j <= squareDimension:
            if i % spacing == 0 and j % spacing == 0:
                coordinate = i,j
                intersections.append(coordinate)
                iList.append(i)
                jList.append(j)
            j += 1
    i += 1

print("The list of intersection coordinates to create your grid is: ")
print(intersections)

n = squareDimension

j = 1
while j <= n:
    i = 1
    print("\n")
    while i <= n:
        if i in iList and j in jList:
            print("*  ", end="")
        else:
            print("-  ", end="")
        i += 1
    j += 1


