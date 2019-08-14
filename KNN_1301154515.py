import csv

def importdata(file):
    data = []
    with open(file, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            r = []
            for col in row:
                r.append(int(col))
            data.append(r)
    return data

def eksportdata(text):
    with open('Hasil.csv', 'wb') as file:
        for line in text:
            file.write(', '.join([str(x) for x in line]))
            file.write('\n')

# a[i]testing ,b[i] train satu baris file excel
def euclidDist(a, b):
    temp = 0
    for i in range(len(a) - 1):
        temp += (a[i] - b[i]) ** 2
    return temp ** 0.5

def manhattan(a,b):
    temp = 0
    for i in range(len(a) - 1):
        temp += abs(a[i] - b[i])
    return temp

def chebyshev(a,b):
    temp = 0
    for i in range(len(a) - 1):
        temp += max(abs(a[i] - b[i]))
    return temp

def winner(a):
    win0 = 0
    win1 = 0
    for i in a:
        if i == 0:
            win0 += 1
        else:
            win1 += 1
    if win0 > win1:
        return 0
    else:
        return 1

def KNNz(train, test, k):
    for i in range(len(test)):
        # design array tuple
        dist = [[j, tr[-1], manhattan(tr, test[i])] for j, tr in enumerate(train)]
        dist = sorted(dist, key=lambda x: x[2])
        nearest = dist[:k]
        # print nearest
        labels = [x[1] for x in nearest]
        test[i].append(winner(labels))
        # print test[i]
    eksportdata(test)


a1 = importdata('a.csv')
a2 = importdata('b.csv')
a3 = importdata('c.csv')
b = importdata('minitest.csv')

KNNz(a1,b,31)
KNNz(a2,b,31)
KNNz(a3,b,31)

