



from src.finetune_bert_model_question_answer.config.configuration import ConfigManager
from src.finetune_bert_model_question_answer.components.data_transformation import DataTransformation



class DataTransformationPipeline:

    def __init__(self):
        pass

    def run(self):
        config = ConfigManager()
        data_transformation_config = config.get_data_transform_config()
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.convert()