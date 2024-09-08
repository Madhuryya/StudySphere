from studybud.wsgi import application
from uvicorn.workers import UvicornWorker

app = application

class VercelUvicornWorker(UvicornWorker):
    def _init_(self, config, target, **kwargs):
        super()._init_(config, target, **kwargs)

    def run(self):
        self.config.app = self.wsgi
        super().run()