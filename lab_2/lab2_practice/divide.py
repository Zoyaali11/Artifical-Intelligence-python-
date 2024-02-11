def calc_quo_rem(dividend, divisor):
    q = 0  
    r = dividend  
    
    while r >= divisor:
        r -= divisor  
        q += 1        
    return q, r
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))
quotient, remainder = calc_quo_rem(dividend, divisor)
print("Quotient:", quotient)
print("Remainder:", remainder)
# Used basic division in this code following are the steps :
# 1) Start with the dividend and divisor.
# 2)Begin with a quotient of 0 and make the remainder the same as the dividend.
# 3)Subtract the divisor from the remainder and Increment the quotient  by 1.
# 4)keep doing step 3 until remainder becomes less than the divisor.
# 5)Once the remainder becomes smaller than the divisor, stop the process. Then, return the quotient , which is the number of times the divisor was subtracted from the dividend, and the final remainder .