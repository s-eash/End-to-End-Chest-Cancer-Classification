
from src.CNNClassifier import logger
from src.CNNClassifier.pipeline.stage_01 import DataIngestionTrainingPipiline

STAGE_NAME  = "Data Ingestion stage"


try:
    logger.info(f"Starting {STAGE_NAME}")
    pipeline = DataIngestionTrainingPipiline()
    pipeline.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"Failed to run {STAGE_NAME} pipeline")
    logger.error(e)