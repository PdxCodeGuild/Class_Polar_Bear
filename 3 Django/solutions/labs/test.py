

def add(*args, **kwargs):
    print(kwargs)

add(2, 3, 4, 5, 6, 7, 9, funny=True, cat='Dog')