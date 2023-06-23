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
    for _ in range(count_zero):
        binary_string += '0'

    result_string = ''
    for i in range(len(binary_string) // 6):
        target = binary_string[i*6:i*6+6]
        result_char = default_base64_table[target]
        
        result_string += result_char
        
    return result_string


default_base64_table = make_table()
string = 'abcde'
encoding_string = encoding(string, default_base64_table)
print(encoding_string)
