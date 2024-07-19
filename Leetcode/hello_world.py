sum = 0
ser_i = 1
n = int(input("Enter n: "))

for i in range(0,n):
    ser_i = ser_i + i
    if ser_i <= n:
        sum = sum + ser_i**4
        print("ser_i: ",ser_i)
        # print("sum: ",sum)
    else:
        break
    
print("sum: ",sum)