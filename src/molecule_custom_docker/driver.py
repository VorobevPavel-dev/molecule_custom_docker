from molecule import logger, util
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
    
    def _get_instance_config(self, instance_name):
        instance_config_dict = util.safe_load_file(self._config.driver.instance_config)
        return next(
            item for item in instance_config_dict if item["instance"] == instance_name
        )

    def ansible_connection_options(self, instance_name):
        x = {"ansible_connection": "community.docker.docker"}
        return x

    def login_options(self, instance_name):
        instance_config = self._get_instance_config(instance_name)
        return {"id": instance_config["ID"]}

    @property
    def login_cmd_template(self):
        return (
            "docker exec "
            "-e COLUMNS={columns} "
            "-e LINES={lines} "
            "-e TERM=bash "
            "-e TERM=xterm "
            "-ti {id} bash"
        )
