# Бойєра-Мура
def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0: return 0
    skip = {}
    for k in range(m):
        skip[pattern[k]] = k
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return i
        i += max(1, j - skip.get(text[i + j], -1))
    return -1

# Кнута-Морріса-Пратта
def kmp(text, pattern):
    n, m = len(text), len(pattern)
    lps = [0]*m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            j = lps[j - 1] if j != 0 else 0
    return -1

# Рабіна-Карпа
def rabin_karp(text, pattern, prime=101):
    m, n = len(pattern), len(text)
    d = 256
    h = pow(d, m - 1) % prime
    p = t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    for s in range(n - m + 1):
        if p == t:
            if text[s:s + m] == pattern:
                return s
        if s < n - m:
            t = (t - h * ord(text[s])) * d + ord(text[s + m])
            t %= prime
    return -1
