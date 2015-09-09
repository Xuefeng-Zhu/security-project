import re
import linecache
from Crypto.Cipher import AES
import random
from ast import literal_eval


def read_student_solution(filepath):
    with open (filepath, "r") as myfile:
        data = ""
        for line in myfile:
            line = line.strip()
            if not line:
                continue
            if line[0] == "#":
                continue;
            data = data+line

        # remove newline characters
        data = data.translate(None, '\n')

    return data


def main():
    filepaths = ['./sol_1.1.2_decimal.txt',
                   './sol_1.1.2_binary.txt',
                   './sol_1.2.1.txt',
                   './sol_1.2.2.txt',
                   './sol_1.2.3.hex',
                   './sol_1.2.4.hex',
                   './sol_1.3.1.hex',
                   './sol_1.3.2.txt'
                   ]

    for path in filepaths:
        print "Checking: " + path
        data = read_student_solution(path)
        print "Data read in and formatted for grading as: >>>{0}<<<".format(data)

        if path.find('.hex') > 0:
            print "Data parsed to int as: >>>{0}<<<".format(int(data, 16))

        if path == './sol_1.1.2_binary.txt':
            print "Data parsed to int as: >>>{0}<<<".format(int(data, 2))

        if path == './sol_1.2.3.hex':
            key = data.decode('hex')
            iv = "00000000000000000000000000000000".decode('hex')
            try:
              aes = AES.new(key, AES.MODE_CBC, iv)
              print 'AES initialized successfully with student\'s key'

            except:
              print 'AES initialization failed, check key formatting'

        print "\n" +"="*40 + "\n"

if __name__ == "__main__":
    main()