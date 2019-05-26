import json
import csv
import pandas as pd
with open ("/home/cherukuri/Downloads/HadoopProject.json","r") as file1:
    for i in file1:
        m = json.loads(i)
        df = pd.DataFrame(m,index=[0])
    return df