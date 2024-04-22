def dna_match_topdown(DNA1, DNA2):
    cache = [[0 for x in range(len(DNA1))] for x in range(len(DNA2))]
    return dna_match_topdown_helper(DNA1, DNA2, len(DNA1) - 1, len(DNA2) - 1, cache)

def dna_match_topdown_helper(DNA1, DNA2, p1, p2, cache):
    if p1 == 0 or p2 == 0:
        return 0

    if cache[p2][p1] != 0:
        return cache[p2][p1]

    elif DNA1[p1] == DNA2[p2]:
        cache[p2][p1] = 1 + dna_match_topdown_helper(DNA1, DNA2, p1-1, p2-1, cache)
        return cache[p2][p1]

    else:
        cache[p2][p1] = max(dna_match_topdown_helper(DNA1, DNA2, p1-1, p2, cache),
                   dna_match_topdown_helper(DNA1, DNA2, p1, p2-1, cache))

        return cache[p2][p1]

def dna_match_bottomup(DNA1, DNA2):
    m, n = len(DNA1), len(DNA2)
    cache = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                cache[i][j] = 0
            elif DNA1[i - 1] == DNA2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1] + 1
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

    return cache[m][n]

if __name__ == "__main__":
    print(dna_match_topdown('ATAGTTCCGTCAAA', 'GTGTTCCCGTCAAA'))
    print(dna_match_bottomup('ATAGTTCCGTCAAA', 'GTGTTCCCGTCAAA'))