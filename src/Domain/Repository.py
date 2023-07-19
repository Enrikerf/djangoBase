import abc
from Domain.Entity import Entity


class PersistRepository(abc.ABC):
    @classmethod
    def persist(cls, entity: Entity):
        pass
