#solutions to the longest common subsequence problem between two strings



def lcs(str1, str2):
    cache = [[0 for x in range(len(str1))] for x in range(len(str2))]
    return lcs_helper(str1, str2, len(str1)-1, len(str2)-1, cache)

def lcs_helper(str1, str2, p1, p2, cache):
    if p1 == 0 or p2 == 0:
        return 0

    if cache[p2][p1] != 0:
        return cache[p2][p1]

    elif str1[p1] == str2[p2]:
        cache[p2][p1] = 1 + lcs_helper(str1, str2, p1-1, p2-1, cache)
        return cache[p2][p1]

    else:
        cache[p2][p1] = max(lcs_helper(str1, str2, p1-1, p2, cache),
                   lcs_helper(str1, str2, p1, p2-1, cache))
        return cache[p2][p1]


def lcs_bottomup(str1, str2):
    m, n = len(str1)-1, len(str2)-1
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
    print(lcs("bac", "abcat"))
    print(lcs_bottomup("bac", "abcat"))