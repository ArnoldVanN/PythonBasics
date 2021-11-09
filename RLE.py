def rle_encode(input):
    output = ''
    last_char = ''
    count = 1

    if not input: return ''

    for char in input:
        if char != last_char:
            if last_char:
                output += str(count) + last_char
            count = 1
            last_char = char
        else:
            count += 1
    else:
        output += str(count) + last_char
        return output

print(rle_encode(input()))