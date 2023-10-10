import requests

url = 'http://localhost:8080/predict'
data = {'image_path': "C:/Users/Mouhcine FERDOUS/Desktop/etude/sid/MSD/chest_xray/test/NORMAL/IM-0011-0001-0002.jpeg"}
response = requests.post(url, json=data)
predictions = response.json()['predictions']
print(predictions)
