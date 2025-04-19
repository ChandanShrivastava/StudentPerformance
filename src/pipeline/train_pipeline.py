import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException
from src.logger import logging

def start_training_pipeline():
    try:
        logging.info("Starting the training pipeline...")

        # Step 1: Data Ingestion
        logging.info("Initiating Data Ingestion...")
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        logging.info(f"Data Ingestion completed. Train data path: {train_data_path}, Test data path: {test_data_path}")

        # Step 2: Data Transformation
        logging.info("Initiating Data Transformation...")
        data_transformation = DataTransformation()
        train_array, test_array, _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        logging.info("Data Transformation completed.")

        # Step 3: Model Training
        logging.info("Initiating Model Training...")
        model_trainer = ModelTrainer()
        r2_score = model_trainer.initiate_model_trainer(train_array, test_array)
        logging.info(f"Model Training completed. R2 Score: {r2_score}")

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    start_training_pipeline()