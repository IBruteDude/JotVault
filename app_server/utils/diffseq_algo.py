from random import randbytes
from pprint import pp
import itertools as it

def diff_seq(s1, s2):
    """Compute the sequence of operations for transforming string s1 to s2
    """
    # Construct the longest common subsequence matrix
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for m in range(1, m + 1):
        for n in range(1, n + 1):
            if s1[m - 1] == s2[n - 1]:
                dp[m][n] = dp[m - 1][n - 1] + 1
            else:
                dp[m][n] = max(dp[m - 1][n], dp[m][n - 1])

    # Reconstruct the diff by tracing back through the matrix
    ops = []

    while m > 0 or n > 0:
        if m > 0 and (n == 0 or dp[m][n] == dp[m - 1][n]):
            ops.append(('D', s1[m - 1]))
            m -= 1
        elif n > 0 and (m == 0 or dp[m][n] == dp[m][n - 1]):
            ops.append(('A', s2[n - 1]))
            n -= 1
        else:
            ops.append(('N', s1[m - 1]))
            m -= 1
            n -= 1

    ops.reverse()
    return ops


def diff_accumulator(ops):
    accumulations = []
    i, length = 0, len(ops)

    while ops[i][0] == 'N':
        i += 1

    strIdx = i

    while i < length:
        op, ch = ops[i]
        if op == ops[i - 1][0]:
            ...

s1 = "language"
s2 = "jingloage"

diff_result = diff_seq(s1, s2)

