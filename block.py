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

def block_puzzle_bottomup(n):
    # initialize array to store solutions
    vals = [0] * n
    #add base cases to solutions array as needed
    if n >= 1:
        vals[0] = 1
    if n >= 2:
        vals[1] = 2
    # start from the simplest problem and use previous solutions to solve each subproblem
    for i in range(3,n+1):
            vals[i-1] = vals[i-2] + vals[i-3]
    # return the solution for n from array
    return vals[n-1]



if __name__ == "__main__":
    print(block_puzzle_bottomup(1))
    print(block_puzzle_bottomup(2))
    print(block_puzzle_bottomup(3))
    print(block_puzzle_bottomup(4))
    print(block_puzzle_bottomup(5))
    print(block_puzzle_bottomup(6))