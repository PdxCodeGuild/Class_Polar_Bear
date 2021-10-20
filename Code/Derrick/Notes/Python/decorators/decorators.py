import time 

def timer(func):
    def wrapper(url):
        start = time.perf_counter()
        func(url)
        end = time.perf_counter()
        print(f'Took {end - start} seconds!')
    return wrapper 

@timer
def get_webPage(url):
    import requests  
    response = requests.get(url)
    print(response.status_code)

get_webPage('https://google.com')