# Iteration Method
def get_sum(n):
    s = 0
    while n != 0:
        s += n % 10
        n = n // 10
    return s

def find_smallest_number(N):
    i = 1
    while i < 1000:	# while True
        if get_sum(i) == N:
            break
        i += 1
    return i
        
N = 10
print(find_smallest_number(N))

# 2. Math method
def smallestNumber(N):
 
    print((N % 9 + 1) * pow(10, (N // 9)) - 1)
 
# Driver code
N = 10
smallestNumber(N)