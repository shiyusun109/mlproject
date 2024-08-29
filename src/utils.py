import os
import sys
import dill

import numpy as np
import pandas as pd


from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path) #get the directory path

        os.makedirs(dir_path,exist_ok=True) #create the directory if it does not exist

        with open(file_path,'wb') as file_obj: #open the file in write mode
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)