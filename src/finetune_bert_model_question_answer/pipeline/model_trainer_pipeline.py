

from src.finetune_bert_model_question_answer.config.configuration import ConfigManager
from src.finetune_bert_model_question_answer.components.model_trainer import ModelTrainer



class ModelTrainerPipeline:

    def __init__(self):
        pass

    def run(self):
        config = ConfigManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config = model_trainer_config)
        model_trainer.train()