from Domain.Repository import PersistRepository
from Domain.Entity import Entity


class Adapter(PersistRepository):
    def persist(self, entity: Entity):
        print("saved on db")
