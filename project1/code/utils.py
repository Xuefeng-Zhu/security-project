def read_file(file_name):
    with open(file_name) as f:
        file_content = f.read().strip()
    return file_content
