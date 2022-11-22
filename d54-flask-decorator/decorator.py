import time

route="/home"

def delay(function):
    if(route=="/home"):
        def wrapper_fn():
            time.sleep(2)
            #do before
            function()
            #do after
        return wrapper_fn

@delay
def print_hello():
    print("hello")

decorated_function = delay(print_hello)
decorated_function()

