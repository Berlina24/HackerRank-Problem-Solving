def simpleArraySum(ar):
    sum = 0
    for i in ar:
        sum += i
    return sum


ar_count = int(input().strip())   # number of elements in array

ar = list(map(int, input().rstrip().split()))    # input for the elements of array

result = simpleArraySum(ar)

print(result)
