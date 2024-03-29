def radixsort(A):
    n = len(A)
    maxelement = max(A)
    digits = len(str(maxelement))
    l = []
    bins = [l] * 10

    for i in range(digits):
        for j in range(n):
            e = (A[j] // 10 ** i) % 10
            if bins[e]:
                bins[e] += [A[j]]
            else:
                bins[e] = [A[j]]

        k = 0
        for x in range(10):
            if bins[x]:
                for y in bins[x]:
                    A[k] = bins[x].pop(0)
                    k += 1


if __name__ == '__main__':
    A = [6, 25, 35, 57, 65, 28]
    print(A)
    radixsort(A)
    print(A)