import time


# def hello_goobye(func):
#     def wrapper():
#         print('Hello')
#         func()
#         print('Goodbye')
#     return wrapper


# @hello_goobye
# def is_even():
#     if 24 % 2 == 0:
#         print('That number is even')

# is_even()



def timer(f):
    def wrapper(llama):
        start = time.perf_counter()
        f(llama)
        stop = time.perf_counter()
        print(f"Took {stop - start} seconds")

    return wrapper

@timer
def get_webpage(url):
    import requests
    response = requests.get(url)
    print(response.status_code)


get_webpage('https://google.com')