a = [5, 2, 4, 8, 1, 3]

for i in range(len(a)):
    min_idx = i
    print(a)
    for j in range(i+1, len(a)):
        if a[j] < a[min_idx]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]
