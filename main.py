

from src.finetune_masked_language_model.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.finetune_masked_language_model.pipeline.data_validation_pipeline import DataValidationPipeline

from src.finetune_masked_language_model.logging import logger



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
