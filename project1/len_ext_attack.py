"""
Xuefeng Zhu, Robert King
len_ext_attack.py
This script takes command into old query to perform
md5 length extension attack
"""

from pymd5 import md5, padding
from urllib import quote

PASSWORD_LENGTH = 8


def read_file(file_name):
    with open(file_name) as f:
        file_content = f.read().strip()
    return file_content


def extend_query(query, command):
    divider_pos = query.find('&')
    token_query = query[:divider_pos]
    message_query = query[divider_pos + 1:]
    token = token_query.split('=')[1]

    data_length = PASSWORD_LENGTH + len(message_query)
    padding_text = padding(data_length * 8)

    md_hash = md5(state=token.decode('hex'), count=512)
    md_hash.update(command)
    new_token = md_hash.hexdigest()

    new_query = ''.join(
        ['token=', new_token, '&', message_query, quote(padding_text), command])
    return new_query

if __name__ == '__main__':
    query_text = read_file('2.1.2_query.txt')
    command = read_file('2.1.2_command3.txt')
    print extend_query(query_text, command)
