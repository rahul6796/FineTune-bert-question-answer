

from src.finetune_bert_model_question_answer.config.configuration import ConfigManager
from src.finetune_bert_model_question_answer.components.data_ingestion import DataIngestion



class DataIngestionPipeline:

    def __init__(self):
        pass

    def run(self):
        config = ConfigManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
