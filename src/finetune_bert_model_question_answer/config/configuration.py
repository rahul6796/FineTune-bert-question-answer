

from src.finetune_bert_model_question_answer.entity import DataIngestionConfig
from src.finetune_bert_model_question_answer.entity import DataValidationConfig
from src.finetune_bert_model_question_answer.entity import DataTransformationConfig

from src.finetune_bert_model_question_answer.utils.common import read_yaml, create_directories
from src.finetune_bert_model_question_answer.constant import CONFIG_YAML, PARAMS_YAML



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


    def get_data_validation_config(self)->DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            ALL_FILES = config.ALL_FILES
        )

        return data_validation_config

    def get_data_transform_config(self)->DataTransformationConfig:

        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            tokenizer_name = config.tokenizer_name
        )

        return data_transformation_config


