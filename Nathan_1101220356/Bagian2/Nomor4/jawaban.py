'''
# Example
matriks = [[98, 88, 78],
           [77, 78, 79],
           [66, 67, 68],
           [32, 33, 31]]

# Expected result
matriks_transpose = [[98, 77, 66, 32],
                     [88, 78, 67, 68],
                     [78, 79, 68, 31]]
'''

''' Program to transpose a matrix using list comprehension'''

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

for r in result:
   print(r)
