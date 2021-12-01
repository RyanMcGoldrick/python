totalNonErroneous = 0
countNonErroneous = 0

numBS = [1, -23, 4, 95, -12]
for item in numBS:
    if item < 0:
        totalNonErroneous += item
        countNonErroneous +=1
averageNonErroneous = totalNonErroneous / countNonErroneous
print(averageNonErroneous)
