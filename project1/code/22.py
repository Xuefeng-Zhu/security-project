"""
Implement Wiener' attack to find the private key for RSA
Citation: we use sympy lib to solve the quadratic equation
http://docs.sympy.org/dev/modules/solvers/solvers.html
"""

from sympy import Symbol
from sympy.solvers import solve


def read_file(file_name):
    with open(file_name) as f:
        file_content = f.read().strip()
    return file_content


def find_kd(result_list):
    numerator = 1
    denominator = result_list[-1]
    for result in reversed(result_list[:-1]):
        tmp = denominator * result + numerator
        numerator = denominator
        denominator = tmp
    return (numerator, denominator)


def check_kd(k, d, N, e):
    if d % 2 == 0:
        return False

    if (e * d - 1) % k != 0:
        return False
    N_factorization = (e * d - 1) / k

    # use sympy to solve the equation since the number is very large
    # and hard to solve in pure python
    x = Symbol('x')
    roots = solve(x * x + (N + 1 - N_factorization) * x + N, x)
    try:
        x_1 = roots[0]
        x_2 = roots[1]
        return x_1 * x_2 == N
    except:
        return False


def converge(N, e):
    divisor = N
    dividend = e
    result_list = []
    found = False
    while not found:
        result, remainder = dividend / divisor, dividend % divisor
        dividend, divisor = divisor, remainder
        if result != 0:
            result_list.append(result)
            k, d = find_kd(result_list)
            if check_kd(k, d, N, e):
                return d

if __name__ == '__main__':
    e = int(read_file("../2.2_public_key.hex"), 16)
    N = int(read_file("../2.2_modulo.hex"), 16)
    ciphertext = int(read_file("../2.2_ciphertext.hex"), 16)
    d = converge(N, e)
    print pow(ciphertext, d, N)
