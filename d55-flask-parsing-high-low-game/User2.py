
class User:
    def __init__(self, name) -> None:
        self.name=name
        self.is_logged_in=False



def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            return function(args[0])
    return wrapper


@is_authenticated_decorator
def create_post(user):
    print(f'new post of : {user.name}')


user = User("bob")
user.is_logged_in = True
create_post(user)
