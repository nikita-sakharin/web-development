def levenshtein_distance(s1: str, s2: str,
        replace: int, insert: int, delete: int) -> int:
    m, n = len(s1), len(s2)
    d = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for j in range(n):
        d[0][j + 1] = d[0][j] + insert

    for i in range(m):
        d[i + 1][0] = d[i][0] + delete
        for j in range(n):
            if s1[i] == s2[j]:
                d[i + 1][j + 1] = d[i][j]
            else:
                d[i + 1][j + 1] = min(d[i][j] + replace,
                    min(d[i + 1][j] + insert, d[i][j + 1] + delete))
    return d[m][n]

assert levenshtein_distance('', '', 1, 1, 1) == 0
assert levenshtein_distance('abc', 'abc', 1, 1, 1) == 0
assert levenshtein_distance('abcdef', '0123abc', 1, 1, 1) == 7
assert levenshtein_distance('abcdef', '0123abc', 100, 1, 10) == 34
assert levenshtein_distance('abcdef', '0123abc', 1, 10, 100) == 16
