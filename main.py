

from src.finetune_masked_language_model.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.finetune_masked_language_model.logging import logger



STATE_NAME = "Data Ingestion"

try:
    data_ingestion = DataIngestionPipeline()
    data_ingestion.run()
    logger.info(f"Data ingestion completed successfully for state: {STATE_NAME}")
except Exception as e:
    logger.error(f'error raised from {STATE_NAME} : {e}')
