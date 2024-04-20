# given a list of coin denominations and the needed amount of change,
# return the least possible number of coins

def makechangeBF(coins, amount):
    """
    Brute Force solution to change problem.
    :param coins: A list of coin denominations like [1, 5, 10, 25]
    :param amount: The amount of change to return
    :return: minimum number of coins
    """
    # base case is when we have no amount left to return
    if(amount == 0): return 0
    result = amount+1 #some arbitary huge number that cannot be the answer
    # for each coin denomination
    for i in range(len(coins)):
        # if that denomination is viable for the amount
        if(coins[i] <= amount):
            # find the minimum number of coins to get that amount by checking the
            # branches for the minimum amount of steps to get each amount after subtracting one coin
            result = min(result, makechangeBF(coins, amount-coins[i]) + 1)
    return result

def makechange(coins, amount, countmemo={}):
    """
    Memoization solution to change problem.
    :param coins: A list of coin denominations like [1, 5, 10, 25]
    :param amount: The amount of change to return
    :return: minimum number of coins
    """
    # base case is when we have no amount left to return
    if(amount == 0): return 0
    result = amount+1 #some arbitary huge number that cannot be the answer
    if result in countmemo:
        result = countmemo[amount]
    else:
    # for each coin denomination
        for i in range(len(coins)):
            # if that denomination is viable for the amount
            if(coins[i] <= amount):
                # find the minimum number of coins to get that amount by checking the
                # branches for the minimum amount of steps to get each amount after subtracting one coin
                result = min(result, makechangeBF(coins, amount-coins[i]) + 1)
                countmemo[amount-coins[i]] = result
    return result

if __name__ == "__main__":
    print(makechange([1,3,5] , 9))