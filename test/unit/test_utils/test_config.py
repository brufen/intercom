import pytest
import yaml
import os
from src.utils.get_config import Config


class TestConfig:
    @pytest.fixture
    def parse_context(self):
        return Config()

    @pytest.fixture
    def test_yaml_context(self):
        config_path = os.path.join(os.path.dirname(os.path.realpath(
            __file__)), 'test_config.yml')
        print("config path: ", config_path)
        with open(config_path) as yaml_file:
            return yaml.safe_load(yaml_file)

    def test_validation_function(self, parse_context, test_yaml_context):
        config = parse_context.parse()
        assert config['radius'] == test_yaml_context['radius']
        assert 'radius' in test_yaml_context

        with pytest.raises(KeyError):
            parse_context.parse(test_yaml_context['missing_key_case'])
