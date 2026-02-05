num = [1, 2, 3, 4, 5]

start = 0
end = len(num) - 1

while start < end:
    num[start], num[end] = num[end], num[start]
    start += 1
    end -= 1

print(num)
