def print_matrix(str1, str2, matrix, modifier=lambda x: x):
    padding = 14
    print(''.ljust(padding * 2) + ' '.join(c.ljust(padding) for c in str2))
    print(
        '\n'.join(
            (str1[i-1] if i > 0 else '').ljust(padding)  + ' '.join(str(modifier(cell)).ljust(padding)
            for j, cell in enumerate(row)) for i, row in enumerate(matrix))
    )


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        matrix = [
            [
                (c, 'L') if r == 0 else ((r, 'U') if c == 0 else (None, ' '))
                for c in range(len(str2)+1)
            ]
            for r in range(len(str1)+1)
        ]

        for i, c1 in enumerate(str1, 1):
            for j, c2 in enumerate(str2, 1):
                if c1 == c2:
                    matrix[i][j] = min(
                        (matrix[i][j-1][0]+1, 'L'),
                        (matrix[i-1][j][0]+1, 'U'),
                        (matrix[i-1][j-1][0], 'D'),
                    )
                else:
                    matrix[i][j] = min(
                        (matrix[i][j-1][0] + 1, 'L'),
                        (matrix[i-1][j][0] + 1, 'U'),
                    )

        result = ''
        i, j = len(str1), len(str2)
        while (i, j) != (0, 0):
            op = matrix[i][j][1]
            if op == 'D':
                i -= 1
                j -= 1
                result = str1[i] + result
            elif op == 'U':
                i -= 1
                result = str1[i] + result
            elif op == 'L':
                j -= 1
                result = str2[j] + result
            else:
                break
        
        # print_matrix(str1, str2, matrix, lambda x: x[0])
        # print_matrix(str1, str2, matrix, lambda x: x[1])

        return result
