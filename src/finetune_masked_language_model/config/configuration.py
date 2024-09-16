

from src.finetune_masked_language_model.entity import DataIngestionConfig
from src.finetune_masked_language_model.utils.common import read_yaml, create_directories
from src.finetune_masked_language_model.constant import CONFIG_YAML, PARAMS_YAML



class ConfigManager:

    def __init__(self, config_yaml_path=CONFIG_YAML, param_yaml_path=PARAMS_YAML):

        self.config = read_yaml(config_yaml_path)
        self.param = read_yaml(param_yaml_path)
        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])


        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_file_dir = config.local_file_dir,
            unzip_dir = config.unzip_dir

            
        )
        return data_ingestion_config



