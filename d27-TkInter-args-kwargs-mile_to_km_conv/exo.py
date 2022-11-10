def add(n, **kwargs):
    n+=kwargs['add']

    n*=kwargs['pouet']
    print(n)


add(1,add=2,pouet=3)

class Car:
    def __init__(self, **kwargs) -> None:
        self.name=kwargs.get('make')
        self.model = kwargs.get('model','xtz')

my_car=Car()


print(my_car.name,my_car.model)