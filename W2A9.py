x= float(input())
shipping_fee= 10
tax= x*0.30+x*0.10
total= x+shipping_fee +tax
print(f"{total:.2f}")