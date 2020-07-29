def decoded_len(rle_str):
    decoded_len = 0

    to_decode = list(rle_str)
    while to_decode:
        char = to_decode.pop(0)
        if char.isalpha():
            if not (to_decode) or to_decode[0].isalpha():
                decoded_len += 1
            else:
                char_len = ''
                while to_decode and to_decode[0].isdigit():
                    char_len += to_decode.pop(0)
                char_len = int(char_len)
                decoded_len += char_len

    return decoded_len


# input
rle_str = input()

# output
print(decoded_len(rle_str))
