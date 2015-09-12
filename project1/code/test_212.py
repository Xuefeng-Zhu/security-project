from pymd5 import md5, padding
from urllib import quote
PASSWORD_LENGTH = 8


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

    new_query = ''.join([message_query, padding_text, command])
    return new_token, new_query

if __name__ == '__main__':
    password = "12345678"
    message = "&user=admin&command1=ListFiles&command2=NoOp"
    command = "&command3=DeleteAllFiles"
    md_hash = md5(password + message)

    query_text = ''.join(['token=', md_hash.hexdigest(), message])

    result = extend_query(query_text, command)
    print result
    md_hash2 = md5(password+result[1])
    print md_hash.hexdigest()
