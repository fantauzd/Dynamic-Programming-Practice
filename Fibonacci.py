# Dynamic Programming practice

def Fib_top_down(n, fibmemo=None):
    print("Calculate for n: %s, FibMemo= %s " % (n, fibmemo))
    if fibmemo is None:
        fibmemo = {0:1, 1:1}
    if n not in fibmemo:
        fibmemo[n] = Fib_top_down(n-1, fibmemo) + Fib_top_down(n-2, fibmemo)
    print("Returning Answer for n: %s" %(n))
    return fibmemo[n]

def Fib_bottom_up(n):
    fib_table = [0]*(n+1)
    fib_table[0] = 1
    fib_table[1] = 1

    for i in range(2,n+1):
        print("Calculate for n: %s, fib_table before adding next index= %s " % (i, fib_table))
        fib_table[i] = fib_table[i-1] + fib_table[i-2]
        print("Updated fib_fibtable =%s" %(fib_table))
    return fib_table[n]

if __name__ == "__main__":
    print(Fib_bottom_up(5))