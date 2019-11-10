'''
Given two n-element data sets, X and Y, calculate the value
of the Pearson correlation coefficient.
'''

def pearson(n, X, Y):
    sx = 0
    sy = 0
    p = 0
    
    mx = sum(X) / n                
    my = sum(Y) / n
    
    for i in range(n):
        sx += (X[i] - mx) ** 2         
        sy += (Y[i]  - my) ** 2
        p += (X[i]  - mx) * (Y[i] - my)

    sx = (sx / n) ** 0.5
    sy = (sy / n) ** 0.5

    return p / (n * sx * sy)


n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

print('{:.3f}'.format(pearson(n, X, Y))))
