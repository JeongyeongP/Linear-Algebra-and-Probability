import csv
import numpy as np
#read csv file and parse its content into a matrix
csv_file = open('binary_data.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
l = list(csv_reader)
matrix= np.array(l).astype("int")
print(matrix)

#compute prior probabilities
#array for count and save cases under the given condition
countForl=np.array([0,0])
for i in range(0,100,1):
    if(matrix[i,5]==0):
        countForl[0]+=1
    else:
        countForl[1]+=1
#array for save prior probabilities
priorProb=np.array([0.0,0.0])
for j in range(0,2,1):
    priorProb[j]=countForl[j]/100
    print("p( l =",j,") =",priorProb[j])

#compute the conditional probabilities
count = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
#counting cases
for i in range(0, 5, 1):
    for j in range(0, 100, 1):
        if (matrix[j, i] == 0 and matrix[j, 5] == 0):
            count[i, 0] += 1
        if (matrix[j, i] == 1 and matrix[j, 5] == 0):
            count[i, 1] += 1
        if (matrix[j, i] == 0 and matrix[j, 5] == 1):
            count[i, 2] += 1
        if (matrix[j, i] == 1 and matrix[j, 5] == 1):
            count[i, 3] += 1
# calculate the conditional probabilities
# p%2=0 is for ai=0 since column index 0,2 of 5x4 matrix(count) is for ai=0(i=0,1,2,3,4)
# p%2=1 is for ai=1 since column index 1,3 of 5x4 matrix(count) is for ai=1(i=0,1,2,3,4)
for k in range(0, 5, 1):
    for p in range(0, 4, 1):
        if (p == 0 or p == 1):
            print("p(a",k,"=",p%2,"|l = 0) =",count[k, p]/countForl[0])
        else:
            print("p(a",k,"=",p%2,"|l = 1) =",count[k, p]/countForl[1])