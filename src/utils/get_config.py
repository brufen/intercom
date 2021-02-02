import yaml
import os


class Config:
    """
    Class that represent config file (yaml)
    """
    path_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            '../..', 'config'))

    def __init__(self):
        """
        Init config path
        """
        self.conf_path = Config.path_dir + '/config.yml'
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("No config file")

    def parse(self):
        """
        Load yaml config as json object
        """
        with open(self.conf_path, 'rt', encoding = 'utf-8') as f:
            config = yaml.safe_load(f)
        return config
