def generate_tuscan_permutations(arg):
    r = None  # Initialize r variable

    def helper(a, i):
        r[i] = a.copy()

    def generate_tuscan_square(n):
        nonlocal r  # Use the outer r variable

        nn = n
        while (n - 1) % 4 == 0 and n != 1 and n != 9:
            n = (n - 1) // 2 + 1
        r = [[0] * (nn + 1) for _ in range(nn)]

        if n % 2 == 0:
            a = [0] * n
            for i in range(0, n, 2):
                a[i] = i // 2
                a[i + 1] = n - 1 - a[i]
            helper(a, 0)
            for j in range(1, n):
                for i in range(n):
                    a[i] = (a[i] + 1) % n
                helper(a, j)
        elif n % 4 == 3:
            k = (n - 3) // 4
            b = [0] * n
            for i in range(n - 1):
                p = 1 if i == 0 else (4 * k + 2 if i == k + 1 else (3 if i == 2 * k + 2 else (4 * k if i == 3 * k + 2 else 2 * k)))
                a = [0] * n
                for j in range(n):
                    a[j] = (n + j - p) if j < p else (j - p)
                    a[j] = (n - 1) if j == 0 else (i + (j // 2 if j % 2 == 0 else (n - 1 - (j - 1) // 2))) % (n - 1)
                b[a[n - 1]] = a[0]
                helper(a, i)
            t = [0] * n
            t[0] = n - 1
            for i in range(1, n):
                t[i] = b[t[i - 1]]
            helper(t, n - 1)
        elif n == 9:
            t = [
                [0, 1, 7, 2, 6, 3, 5, 4, 8],
                [3, 7, 4, 6, 5, 8, 1, 2, 0],
                [1, 4, 0, 5, 7, 6, 8, 2, 3],
                [6, 0, 7, 8, 3, 4, 2, 5, 1],
                [2, 7, 1, 0, 8, 4, 5, 3, 6],
                [7, 3, 0, 2, 1, 8, 5, 6, 4],
                [5, 0, 4, 1, 3, 2, 8, 6, 7],
                [4, 3, 8, 7, 0, 6, 1, 5, 2],
                [8, 0, 3, 1, 6, 2, 4, 7, 5]
            ]
            for i in range(9):
                helper(t[i], i)
        else:
            assert False

        while nn != n:
            n = n * 2 - 1
            h = (n + 1) // 2
            for i in range(h):
                for j in range(h):
                    r[i][n - j] = r[i][j] + h
            for i in range(h, n):
                for j in range(h - 1):
                    r[i][j] = (0 if j % 2 == 0 else h) + (i - h + (j // 2 if j % 2 == 0 else (h - 2 - (j - 1) // 2))) % (h - 1)
                r[i][h - 1] = h - 1
                for j in range(h, n + 1):
                    r[i][j] = (0 if j % 2 == 0 else h) + r[i][j - h] % h
            for i in range(n):
                l = 0
                while r[i][l] != n:
                    l += 1
                t = r[i][l + 1:] + r[i][:l + 1]
                r[i] = t.copy()

        return r

    def generate_one():
        return [[0, 0]]

    def generate_three():
        return [
            [0, 1, 2],
            [1, 0, 2],
            [2, 1, 0],
            [2, 0, 1]
        ]

    def generate_five():
        return [
            [0, 1, 2, 3, 4],
            [1, 0, 3, 2, 4],
            [4, 3, 0, 2, 1],
            [1, 4, 2, 0, 3],
            [0, 4, 1, 3, 2],
            [4, 0, 3, 1, 2]
        ]

    if arg == 1:
        return generate_one()
    elif arg == 3:
        return generate_three()
    elif arg == 5:
        return generate_five()
    else:
        return generate_tuscan_square(arg)
