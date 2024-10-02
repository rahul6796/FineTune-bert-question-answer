

from src.finetune_bert_model_question_answer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.finetune_bert_model_question_answer.pipeline.data_validation_pipeline import DataValidationPipeline
from src.finetune_bert_model_question_answer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.finetune_bert_model_question_answer.pipeline.model_trainer_pipeline import ModelTrainerPipeline

from src.finetune_bert_model_question_answer.logging import logger



STATE_NAME = "Data Ingestion"

try:
    data_ingestion = DataIngestionPipeline()
    data_ingestion.run()
    logger.info(f"Data ingestion completed successfully for state: {STATE_NAME}")
except Exception as e:
    logger.error(f'error raised from {STATE_NAME} : {e}')


STATE_NAME = "Data Validation"

try:
    data_validation = DataValidationPipeline()
    data_validation.run()
    logger.info(f"Data Validation completed successfully for state: {STATE_NAME}")
except Exception as e:
    logger.error(f'error raised from {STATE_NAME} : {e}')


STATE_NAME = "Data Transformation"

try:
    data_transformation = DataTransformationPipeline()
    data_transformation.run()
    logger.info(f"Data transformation completed successfully for state: {STATE_NAME}")
except Exception as e:
    logger.error(f'error raised from {STATE_NAME} : {e}')


# STATE_NAME = "Model Trainer"

# try:
#     model_trainer = ModelTrainerPipeline()
#     model_trainer.run()
#     logger.info(f"Model trainer completed successfully for state: {STATE_NAME}")
# except Exception as e:
#     logger.error(f'error raised from {STATE_NAME} : {e}')
