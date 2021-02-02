import logging
import logging.config
import os
import yaml
from src.utils.get_config import Config


class SetupLogging:
    """
    Class that represents logging and gets logging setup from config file
    """

    def __init__(self):
        """
        Init config
        """
        self.default_config = Config().parse()

    def setup_logging(self, default_level = logging.INFO):
        """
        Setup logging with values from config
        """
        if self.default_config:
            logging.config.dictConfig(self.default_config)
        else:
            logging.info("Error in loading logging configuration. "
                         "Using default configs from module.")
            logging.basicConfig(level = default_level)
