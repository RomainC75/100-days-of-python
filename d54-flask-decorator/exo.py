import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper_fn():
        current_time = time.time()
        function()
        time_after = time.time()
        print(f"=>{function.__name__} // speed : {time_after-current_time}s")

    return wrapper_fn

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
        
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

# pointeur = speed_calc_decorator(fast_function)
# pointeur()

fast_function()
slow_function()