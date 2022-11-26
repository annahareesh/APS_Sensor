import pymongo

import pandas as pd

import json

client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME = 'aps'

Collection_Name = 'Sensor'

data_file_path = '/config/workspace/aps_failure_training_set1.csv'

if __name__ == "__main__":
    df = pd.read_csv(data_file_path)
    print(df.shape)
    
    # converting data frame in JSON Format - used to import data in to mango db

    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    # inserting json record to Mango db

    client[DATABASE_NAME][Collection_Name].insert_many(json_record)

    
