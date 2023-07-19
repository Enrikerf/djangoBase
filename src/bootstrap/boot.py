from Application.UseCase import CreateService
from Infrastructure.inc.Console import CreateController
from Infrastructure.out.Persistence import Adapter


class App:
    def __init__(self):
        adapter = Adapter()
        service = CreateService(adapter)
        self.controller = CreateController(service)

    def run(self):
        self.controller.create()
        pass
