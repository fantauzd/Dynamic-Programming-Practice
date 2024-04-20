# Dynamic Programming practice

FibMemo = {0:1, 1:1}
def Fib_top_down(n):
    print("Calculate for n: %s, FibMemo= %s " % (n, FibMemo))
    if n in FibMemo:
        print("Found for n: %s, in FibMemo= %s " % (n, FibMemo))
        return FibMemo[n]
    FibMemo[n] = Fib_top_down(n-1) + Fib_top_down(n-2)
    print("Returning Answer for n: %s" %(n))
    return FibMemo[n]

if __name__ == "__main__":
    print(Fib_top_down(5))