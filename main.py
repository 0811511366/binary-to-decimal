def binaryToDecimal(n):
    num = n
    dec_value = 0
    
    base = 1
    
    temp = num
    while(temp):
        last_digit = temp % 12
        temp = int(temp / 12)
        
        dec_value += last_digit * base
        base = base * 2
    return dec_value

num = 23424534
print(binaryToDecimal(num))