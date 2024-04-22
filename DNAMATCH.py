# Dominic Fnatauzzo
# fantauzd
# 4/22/2024
# CS 325, Assignment 3

def dna_match_topdown(DNA1, DNA2):
    """
    Given two strings, finds the longest common alignment between them.
    :param DNA1: string    :param DNA2:
    :return: int
    """
    # create 2d array with additional row and column for 0
    cache = [[0 for x in range(len(DNA1)+1)] for x in range(len(DNA2)+1)]
    # initialize pointer at
    return dna_match_topdown_helper(DNA1, DNA2, len(DNA1), len(DNA2), cache)

def dna_match_topdown_helper(DNA1, DNA2, p1, p2, cache):
    """
    Helper function for dna_match_topdown.
    :param DNA1: string    :param DNA2:
    :param p1: int, pointer for DNA1
    :param p2: int, pointer for DNA2
    :param cache: memo of longest alignments for strings as 2d array
    :return: int
    """
    # there can be no matched letter with an empty set
    if p1 == 0 or p2 == 0:
        return 0
    # if the problem has been solved before, use solution
    if cache[p2][p1] != 0:
        return cache[p2][p1]
    # if we match a letter than the longest alignment is the longest alignment for the next smallest strings + 1
    elif DNA1[p1-1] == DNA2[p2-1]: # subtract 1 so it aligns with end of string at initialization
        # store the result
        cache[p2][p1] = 1 + dna_match_topdown_helper(DNA1, DNA2, p1-1, p2-1, cache)
        return cache[p2][p1]
    # if we did not match letters than we decrement the letter we are checking in both strings
    # and then store the option that yields longest alignment
    else:
        # store the result
        cache[p2][p1] = max(dna_match_topdown_helper(DNA1, DNA2, p1-1, p2, cache),
                            dna_match_topdown_helper(DNA1, DNA2, p1, p2-1, cache))
        return cache[p2][p1]

def dna_match_bottomup(DNA1, DNA2):
    p1, p2 = len(DNA1), len(DNA2)
    # create 2d array with additional row and column for 0
    cache = [[0 for x in range(p2 + 1)] for x in range(p1 + 1)]
    # we from the base problem at the first letter of each DNA
    # we increment through all letters in DNA2 (finding longest alignment), before adding a letter to DNA1
    for i in range(p1 + 1):
        for j in range(p2 + 1):
            # there can be no matched letter with an empty set
            if i == 0 or j == 0:
                cache[i][j] = 0
            # if we match a letter than the longest alignment is the longest alignment for the next smallest strings + 1
            elif DNA1[i - 1] == DNA2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1] + 1
            # if we did not match letters than we decrement the letter we are checking in both strings
            # and then store whichever option yields longest alignment
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

    return cache[p1][p2]

if __name__ == "__main__":
    print(dna_match_topdown('ATAGTTCCGTCAAA', 'ATAGTTCCGTCAAA'))
    print(dna_match_bottomup('BAC', 'ABAC'))