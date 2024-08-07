import json

# def readJsonFile(fileName):
#     data=""     

def readJsonFile(fileName):
    data = ""
    with open('files/insulin.json') as json_file:
        data = json.load(json_file)
    return data

