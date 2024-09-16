

from src.finetune_bert_model_question_answer.config.configuration import ConfigManager
from src.finetune_bert_model_question_answer.components.data_validation import DataValidation



class DataValidationPipeline:

    def __init__(self):
        pass

    
    def run(self):
        config = ConfigManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_files()
