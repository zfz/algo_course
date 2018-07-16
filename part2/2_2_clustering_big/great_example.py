# Copy from https://github.com/liuliqiu/study/blob/5ec0915021a8932da2f6bedfc04c75a741903e70/algorithm/clust_big.py

from itertools import combinations, product
def bytes_to_int(s):
    r = 0
    for i in s:
        r = r*2 + i
    return r


def cl(S, b_l):
    M = [2 ** i for i in range(0, b_l)]
    #print list(combinations(M, 2))
    M2 = {x^y for x, y in combinations(M, 2)} | set(M)
    print M2

    k = 0
    while len(S)>0:
        k += 1
        #print k, len(S)
        A = {S.pop()}
        #print A
        while len(A) > 0:
            B = {x^y for x, y in product(A, M2)}
            A = S & B
            S.difference_update(A)
    return k

def main():
    file_name = "clustering_big.txt"
    with open(file_name) as f:
        x, b_l = map(int, next(f).strip().split())
        S = {bytes_to_int(map(int, line.strip().split())) for line in f}
        print cl(S, b_l)

if __name__ == "__main__":
    main()
