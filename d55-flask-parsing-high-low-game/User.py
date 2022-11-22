
class User:
    def __init__(self, name) -> None:
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            return function(args[0])
    return wrapper


def loggin_decorator(function):
    def wrapper(*args):
        return function(f'{function.__name__}, {args[0]}')
    return wrapper

    print("strings : ", strings)

# new_user = User("bob")
# new_user.is_logged_in = True
# create_blog_post(new_user)

#=======================================

@is_authenticated_decorator
def create_blog_post(user):
    print(f"this is the {user.name}'s new blog post")

@loggin_decorator
def print_str(strings):
    print(strings)

print_str("xyz")