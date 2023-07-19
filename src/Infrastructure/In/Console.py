from Application.Command import Command
from Application.UseCase import UseCase


class CreateController:
    def __init__(self, use_case: UseCase):
        self.use_case = use_case

    def create(self):
        self.use_case.create(Command(""))
        pass
