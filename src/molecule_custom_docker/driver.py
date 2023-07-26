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

    @property
    def default_safe_files(self):
        return []

    @property
    def required_collections(self):
        return {"community.docker": "3.4.6"}

    def ansible_connection_options(self, instance_name):
        x = {"ansible_connection": "community.docker.docker"}
        return x