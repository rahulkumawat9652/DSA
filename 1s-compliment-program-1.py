x = "1101"
result = ""
index = 0
while index < len(x):
    if x[index] == "1":
        result += "0"
    else:
        result += "1"
    index += 1
print(result)