HASH_SIZE = 256

input_string = "619ee6c50eb282a878975903cee801ac5baa259ae889082eda894cf1151380a3"
perturbed_string = "1a426df39ddc13b8cfd954b33b66e46f98cf920ef39c7d308d993b33535123b5"


if __name__ == '__main__':
    input_bin = bin(int(input_string, 16))[2:]
    perturbed_string = bin(int(perturbed_string, 16))[2:]
    input_bin = "0" * (HASH_SIZE - len(input_bin)) + input_bin
    perturbed_string = "0" * \
        (HASH_SIZE - len(perturbed_string)) + perturbed_string
    result = [input_bin[i] != perturbed_string[i]
              for i in range(HASH_SIZE)]
    print hex(result.count(True))
