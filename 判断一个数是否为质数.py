def is-prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
        return True
test-nums=[7,15,23,1,2,9]
for num in test-nums:
    if is-prime(num):
        print(f"{num}是质数")
    else:
        print(f"{num}不是质数")
        
