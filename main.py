from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys
if __name__=='__main__':
  try:
    trainingpipelineconfig=TrainingPipelineConfig()
    dataingetionconfig=DataIngestionConfig(trainingpipelineconfig)
    data_ingetion=DataIngestion(dataingetionconfig)
    logging.info("initiating data ingestion")
    data_ingestion_artifact=data_ingetion.initiate_data_ingestion()
    logging.info("data ingestion completed")
    print(data_ingestion_artifact)
    
    
    data_validation_config=DataValidationConfig(trainingpipelineconfig)
    data_validation=DataValidation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=data_validation_config)
    logging.info("initiating data validation")
    data_validation_artifact=data_validation.initate_data_validation()
    logging.info("data validation completed")
    print(data_validation_artifact)
    
    data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
    data_transformation=DataTransformation(data_validation_artifact=data_validation_artifact,data_transformation_config=data_transformation_config)
    logging.info("initiating data transformation")
    data_transformation_artifact=data_transformation.initiate_data_transformation()
    logging.info("data transformation completed")
    print(data_transformation_artifact)
    
    
  except Exception as e:
    raise NetworkSecurityException(e,sys)   