import requests
import json
import os
import sys
#from PIL import Image
from io import BytesIO
import pandas as pd


def analyze():

    subscription_key = "c55ec6fb7454432fba8eeef2c2bdbf3f"

    face_api_url = 'https://automathon.cognitiveservices.azure.com/face/v1.0/detect'
    headers = {'Ocp-Apim-Subscription-Key': subscription_key, "Content-type": "application/octet-stream"}

    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'emotion',
    }

    dicti = {}
    path="C:\\Users\\suyashadmin\\Desktop\\data\\pics\\"
    print(path)

    for time1 in os.listdir(path):
        res12 = path + "\\" + time1
        res12=os.path.join(path,time1)
        time1=time1[0:2]+":"+time1[2:4]
        #print(i)
        print(res12)
        for j in os.listdir(res12):
            image_url = os.path.abspath(res12) + "\\" + j
            print(image_url)
        #image_url=res12

            image_data = open(image_url, "rb").read()

            response = requests.post(face_api_url, headers=headers, params=params, data=image_data)
            res = json.loads(response.content)

            
            
            if time1 not in dicti.keys():
                dicti[time1]={}

            for i in range(0, len(res)):

                Keymax = max(res[i]["faceAttributes"]["emotion"], key=res[i]["faceAttributes"]["emotion"].get)

                if Keymax not in dicti[time1].keys():
                    dicti[time1][Keymax] = 1
                else:
                    dicti[time1][Keymax] = dicti[time1][Keymax] + 1

    df=pd.DataFrame.from_dict(dicti,orient='index')
    df.to_csv(r'C:\Users\suyashadmin\Desktop\data\data.csv')
    df.sort_index().plot.barh(figsize=(25,30),width=1).get_figure().savefig('C:\\Users\\suyashadmin\\Desktop\\data\\output.png') #replace <user name> with user name of the computer