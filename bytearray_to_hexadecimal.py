#Convert a given Bytearray to Hexadecimal string.

def bytearray_to_hexadecimal(list_val):
    result = ' '.join('{:02x}'.format(x) for x in list_val)
    return result


list_val = [111, 12, 45, 8, 67, 109]
print("Original Bytearry:")
print(list_val)
print("\nHexadecimal String:")
print(bytearray_to_hexadecimal(list_val))

