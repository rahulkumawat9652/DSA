hash_last = [0]*26
s = "asdfghjkl"
q = ["a", "f", "h" ,"k"]
for ch in s:
    ascii_val = ord(ch)
    index = ascii_val-97
    hash_last[index] += 1
for ch in q:
    ascii_val = ord(ch)
    index = ascii_val-97
    print(hash_last[index])