import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from data_transformation import DataTransformation
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#reading of dataset from various sources

"""
The @dataclass decorator is used to simplify the 
creation of classes that store data.
 Instead of writing boilerplate code like constructors (__init__), __repr__, and __eq__ methods,
 @dataclass automatically generates them for you.
"""
@dataclass
class DataIngestionConfig:
    #Whenever an object of DataIngestionConfig is created, it automatically sets paths for data files.
    train_data_path:str=os.path.join('artifacts',"train.csv")
    test_data_path:str=os.path.join('artifacts',"test.csv")
    raw_data_path:str=os.path.join('artifacts',"raw.csv")

class DataIngestion:
    def __init__(self):
        #as soon as DataIngestion gets created
        #config will initialize all three paths
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # in real life application this will be the part 
            # where the data will be extracted from mongodb , SQL database
            df=pd.read_csv(r'notebook\data\stud.csv')

            logging.info('Read the dataset as dataframe')

            #creating the train and test data path
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path),exist_ok=True)

            #saving the raw data obtained to the raw_data.csv
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info('Train Test split initiated')

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            ##saving the train and test set to the respective dir
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e,sys)



if __name__ == "__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    
    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)


