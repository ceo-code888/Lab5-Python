shift = int(input())
text = input()

start_code = 0x1F600
end_code = 0x1F64F
alphabet_size = end_code - start_code + 1

result = []
for char in text:
    code = ord(char)
    if start_code <= code <= end_code:
        new_code = start_code + (code - start_code + shift) % alphabet_size
        result.append(chr(new_code))
    else:
        result.append(char)

print("".join(result))