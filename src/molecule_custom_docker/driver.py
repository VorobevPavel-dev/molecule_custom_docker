from molecule import logger
from molecule.api import Driver

LOG = logger.get_logger(__name__)


class CustomDocker(Driver):
    def __init__(self, config=None):
        super(CustomDocker, self).__init__(config)
        self._name = "custom_docker"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
