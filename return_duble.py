def double(num):
    return num*num
print(double(3))


def double_lambda(n):
    return lambda x:x*n
y=double_lambda(3)

print(y(5))
