def make_table():
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    table_dict = {}

    for i in range(64):
        number = format(i, "b").zfill(6)
        table_dict[number] = string[i]
    
    return table_dict


def encoding(string:str, table:dict):
    
    default_base64_table = table
    binary_string = ''

    for s in string:
        binary_string += format(ord(s), "b").zfill(8)

    count_zero = 6 - (len(binary_string) % 6)
    if count_zero != 6:
        for _ in range(count_zero):
            binary_string += '0'

    result_string = ''
    for i in range(len(binary_string) // 6):
        target = binary_string[i*6:i*6+6]
        result_char = default_base64_table[target]
        
        result_string += result_char
        
    return result_string


def make_reverse_table(table:dict):
    return {v: k for k, v in table.items()}


def decoding(string:str, reverse_table:dict):
    binary_string = ''
    
    for s in string:
        binary_string += reverse_table[s]

    #패딩
    #while binary_string.endswith('000000'):
    #    binary_string = binary_string[:-6]
        
    result_string = ''
    for i in range(0, len(binary_string), 8):
        target = binary_string[i:i+8]
        result_char = chr(int(target, 2))
        
        result_string += result_char
    
    return result_string


if __name__=="__main__":
    string = input("Please Input string: ")
    
    default_base64_table = make_table()
    test_string = 'abcdeQRTEVP'
    print("origin_string:", string)
    encoding_string = encoding(string, default_base64_table)
    print("encoding_string:", encoding_string)
    reverse_base64_table = make_reverse_table(default_base64_table)
    decoding_string = decoding(encoding_string, reverse_base64_table)
    print("decoding_string:", decoding_string)
