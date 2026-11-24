# convert binary to decimal
x = "1101"
decimal_number = 0
power = 0
index = len(x)-1
while index >= 0:
    num = int(x[index])*(2**power)
    decimal_number += num
    index -= 1
    power += 1
print(decimal_number)