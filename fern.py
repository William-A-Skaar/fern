import numpy as np
import matplotlib.pyplot as plt

class AffineTransform:

    def __init__(self, a = 0, b = 0, c = 0, d = 0, e = 0, f = 0):
        self.a = a; self.b = b; self.c = c; self.d = d; self.e = e; self.f = f

    def __call__(self, p):
        A = np.zeros((2,2))
        A[0][0] = self.a; A[0][1] = self.b
        A[1][0] = self.c; A[1][1] = self.d
        C = np.zeros(2)
        C[0] = self.e; C[1] = self.f
        f_xy = np.matmul(A, p) + C
        return f_xy

def rand_function():
    f_1 = AffineTransform(d = 0.16)
    f_2 = AffineTransform(0.85, 0.04, -0.04, 0.85, 0, 1.6)
    f_3 = AffineTransform(0.2, -0.26, 0.23, 0.22, 0, 1.6)
    f_4 = AffineTransform(-0.15, 0.28, 0.26, 0.24, 0, 0.44)
    func_lst = [f_1, f_2, f_3, f_4]

    p_1 = 0.01; p_2 = 0.85; p_3 = 0.07; p_4 = 0.07
    p_cumulative = np.array([p_1, p_1 + p_2, p_1 + p_2 + p_3, p_1 + p_2 + p_3 + p_4])

    r = np.random.random()
    for i, p in enumerate(p_cumulative):
        if r < p:
            return func_lst[i]

N = 50000
X = np.zeros((N,2))

for i in range(N-1):
    f = rand_function()
    X[i+1] = f(X[i])

plt.scatter(*zip(*X), s = 0.2, marker = ".", c = "g")
plt.axis("equal")
plt.axis("off")
plt.savefig("figures/fern" , dpi = 1000)
plt.show()
