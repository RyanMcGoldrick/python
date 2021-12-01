totalNonErroneous = 0
countNonErroneous = 0

numBS = [1, -19, 4, 3, -5, 2]
for item in numBS:
    if item >= 0:
        totalNonErroneous += item
        countNonErroneous +=1
averageNonErroneous = totalNonErroneous / countNonErroneous
print(averageNonErroneous)
