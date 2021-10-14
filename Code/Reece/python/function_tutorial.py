

def hello():
    word = 'hello'
    print('We\'re learning functions.')
    print(f"We're learning functions." )
    return word

# hello()
# print(hello())


x = 0

def count(count):
    list = []
    count += 1
    # print(count)
    value_from_hello = hello()
    # list.append(hello())
    # return value_from_hello
    return count

# count(x)
value_from_fcuntions = count(7) 
print(value_from_fcuntions)