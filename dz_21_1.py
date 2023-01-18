# Pavlo Yatluk
# dz_21_1
# Написати клас роботі з матрицями. Клас повинен створювати об'ект матриць з вкладених списків,
# виводити матриці на друк, виконувати операції додавання, віднімання, множення на число, множення на матрицю,
# транспонування. Передбачити мождивість приведення матриць для оперцій додавання і віднімання та обробку
# виключних ситуацій для рперації множення матриці на матрицю.

class Matrix:
    def __init__(self, m_list):
        for i in range(len(m_list)-1):
            if len(m_list[i]) != len(m_list[i+1]):
                raise Exception(f"It's impossible to create matrix from {m_list} list")
        self.matrix = m_list
        self.n_col = len(m_list)
        self.n_row = len(m_list[0])

    def print_matrix(self):
        print('Result matrix:')
        [print(i) for i in self.matrix]

    def matrix_tr(self, n_row, n_col):
        if self.n_row < n_col:
            for row in self.matrix:
                row.extend([0] * (n_col - self.n_row))
            self.n_row = n_col
        if self.n_col < n_row:
            self.matrix.extend([[0] * self.n_row] * (n_row - self.n_row))

    def mult_v_matrix(self, var):
        res = []
        for i in range(len(self.matrix)):
            res.append([])
            for j in range(len(self.matrix[i])):
                res[i].append(self.matrix[i][j] * var)
        return Matrix(res)

    def sum_matrix(self, data):
        m = max(self.n_col, data.n_col)
        n = max(self.n_row, data.n_row)
        self.matrix_tr(m, n)
        data.matrix_tr(m, n)
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] + data.matrix[i][j])
        return Matrix(result)

    def sub_matrix(self, data):
        m = max(self.n_col, data.n_col)
        n = max(self.n_row, data.n_row)
        self.matrix_tr(m, n)
        data.matrix_tr(m, n)
        res = []
        for i in range(len(self.matrix)):
            res.append([])
            for j in range(len(self.matrix[i])):
                res[i].append(self.matrix[i][j] - data.matrix[i][j])
        return Matrix(res)

    def transp_matrix(self):
        res = [[0] * len(self.matrix) for _ in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                res[j][i] = self.matrix[i][j]
        return Matrix(res)

    def mult_matrix(self, data):
        if self.n_row != data.n_col:
            raise Exception(f'Number of row({self.n_row}) != number of col({data.n_col})')
        res = []
        for i in range(len(self.matrix)):
            res.append([])
            for j in range(len(data.matrix[i])):
                m_sum = 0
                for k in range(len(data.matrix)):
                    m_sum += self.matrix[i][k] * data.matrix[k][j]
                res[i].append(m_sum)
        return Matrix(res)


A = Matrix(m_list=[
    [4, 5, 6],
    [1, 2, 3],
    [7, 8, 9]])
print(f"Друкуємо матрицю A:")
A.print_matrix()

B = Matrix(m_list=[
    [7, 8, 9],
    [1, 2, 3],
    [4, 5, 6]])
print(f"Друкуємо матрицю B:")
B.print_matrix()

M = Matrix(m_list=[
    [7, 8],
    [4, 5]])
print(f"Друкуємо матрицю M:")
M.print_matrix()

print(f"Множимо матрицю A на число 3:")
C = A.mult_v_matrix(3)
C.print_matrix()

print(f"Додаємо матриці А і B:")
D = A.sum_matrix(B)
D.print_matrix()

print(f"Віднімаємо матриці А і B:")
F = A.sub_matrix(B)
F.print_matrix()

print(f"Траспонуємо матрицю А:")
E = A.transp_matrix()
E.print_matrix()

print(f"Множимо матриці А і B:")
S = A.mult_matrix(B)
S.print_matrix()

print(f"Множимо матриці А і M:")
K = A.mult_matrix(M)
K.print_matrix()