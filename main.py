
from src.CNNClassifier import logger
from src.CNNClassifier.pipeline.stage_01 import DataIngestionTrainingPipiline
from src.CNNClassifier.pipeline.stage_02 import PrepareBaseModelTrainingPipeline
from src.CNNClassifier.pipeline.stage_03 import ModelTrainingPipeline
from src.CNNClassifier.pipeline.stage_04 import EvaluationPipeline
import dagshub

STAGE_NAME  = "Data Ingestion stage"


try:
    logger.info(f"Starting {STAGE_NAME}")
    pipeline = DataIngestionTrainingPipiline()
    pipeline.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"Failed to run {STAGE_NAME} pipeline")
    logger.error(e)



STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Evaluation"
dagshub.init(repo_owner='eashwaransridhar', repo_name='End-to-End-Chest-Cancer-Classification', mlflow=True)
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e
