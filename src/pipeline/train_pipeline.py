import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer



data_ingestion=DataIngestion()
train_data, test_data=data_ingestion.initiate_data_ingestion()

data_transformation=DataTransformation()
train_arr,test_arr=data_transformation.initiate_data_transformation(train_data, test_data)

model_trainer=ModelTrainer()
print(model_trainer.initiate_model_trainer(train_arr, test_arr))