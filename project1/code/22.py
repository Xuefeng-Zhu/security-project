from decimal import *

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

    N_factorization = (e * d - 1) / Decimal(k)
    if int(N_factorization) != N_factorization:
        return False

    b = (N - int(N_factorization)) + 1
    b = -b
    c = N
    tmp = Decimal(b * b - 4 * c).sqrt()
    x_1 = ((-b) + tmp) / 2
    x_2 = ((-b) - tmp) / 2
    if int(x_1) != x_1 or int(x_2) != x_2:
        return False

    return x_1 * x_2 == N


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
