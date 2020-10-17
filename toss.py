def gen(n,r=[]):
    for _ in range(n):
        l = len(r)
        r = [1 if i == 0 or i == l else r[i-1]+r[i] for i in range(l+1)]
        yield r

def draw(n):
    ps = list(gen(n))
    max = len(' '.join(map(str,ps[-1])))
    for p in ps:
        print(' '.join(map(str,p)).center(max)+'\n')
rows = int(input("How many rows?: "))
draw(rows)
