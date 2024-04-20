# Dynamic Programming practice

def Fib_top_down(n, fibmemo=None):
    print("Calculate for n: %s, FibMemo= %s " % (n, fibmemo))
    if fibmemo is None:
        fibmemo = {0:1, 1:1}
    if n not in fibmemo:
        fibmemo[n] = Fib_top_down(n-1, fibmemo) + Fib_top_down(n-2, fibmemo)
    print("Returning Answer for n: %s" %(n))
    return fibmemo[n]

if __name__ == "__main__":
    print(Fib_top_down(5))