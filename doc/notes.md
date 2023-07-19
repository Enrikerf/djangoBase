pendinente actualizar el ultimo pip tbn
pip install --upgrade pip

pip install pipenv

setting up django projecto

sudo apt install python3-django


import abc


class MyInterface(abc.ABC):
    @classmethod
    def example_method(cls, word: str):
        pass


class MyClass(MyInterface):
    @staticmethod
    def example_method(word: str, **kwargs):
        print(" Hello from MyClass " + word)


o1 = MyClass()
o1.example_method("hello")


# list active containers
docker ps

# list all containers
docker ps -a

# remove all containers
docker system prune -a

# stop the container
docker stop NAMES (or CONTAINER ID)
