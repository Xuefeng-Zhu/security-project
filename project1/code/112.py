from utils import read_file

if __name__ == "__main__":
    file_content = read_file("../1.1.2_value.hex")
    integer_parsed = int(file_content, 16)
    binary_content = bin(integer_parsed)
    # check if the binary content format is correct
    print integer_parsed, binary_content
