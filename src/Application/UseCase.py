import abc

from Domain.Repository import PersistRepository
from Domain.Entity import Entity
from Application.Command import Command


class UseCase(abc.ABC):
    @classmethod
    def create(cls, command: Command):
        pass


class CreateService(UseCase):
    def __init__(self, save_repository: PersistRepository):
        self.saveRepository = save_repository

    def create(self, command: Command):
        new_entity = Entity(command.name)
        self.saveRepository.persist(new_entity)
        pass
