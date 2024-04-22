# You are playing a puzzle. A random number N is given, you have blocks of length 1 unit and 2
# units. You need to arrange the blocks back to back such that you get a total length of N units. In
# how many distinct ways can you arrange the blocks for given N.

def block_puzzle(n):
    # base cases
    if n == 1:
        return 1
    if n == 2:
        return 2
    # the number of solutions is equal to the sum of number of solutions for the previous 2 lengths
    return block_puzzle(n-1) + block_puzzle(n-2)

if __name__ == "__main__":
    print(block_puzzle(2))
    print(block_puzzle(3))
    print(block_puzzle(4))
    print(block_puzzle(5))
    print(block_puzzle(6))