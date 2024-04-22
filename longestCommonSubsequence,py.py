#solutions to the longest common subsequence problem between two strings



def dna_match_topdown(DNA1, DNA2):
    cache = [[0 for x in range(len(DNA1)+1)] for x in range(len(DNA2)+1)]
    return dna_match_topdown_helper(DNA1, DNA2, len(DNA1), len(DNA2), cache)

def dna_match_topdown_helper(DNA1, DNA2, p1, p2, cache):
    if p1 == 0 or p2 == 0:
        return 0

    if cache[p2][p1] != 0:
        return cache[p2][p1]

    elif DNA1[p1-1] == DNA2[p2-1]:
        cache[p2][p1] = 1 + dna_match_topdown_helper(DNA1, DNA2, p1-1, p2-1, cache)
        return cache[p2][p1]

    else:
        cache[p2][p1] = max(dna_match_topdown_helper(DNA1, DNA2, p1-1, p2, cache),
                            dna_match_topdown_helper(DNA1, DNA2, p1, p2-1, cache))

        return cache[p2][p1]


def lcs_bottomup(str1, str2):
    m, n = len(str1), len(str2)
    cache = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                cache[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1] + 1
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

    return cache[m][n]


if __name__ == "__main__":
    print(lcs_bottomup("bac", "abcat"))
    # why do we have one off errror?