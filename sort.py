import os
import json
import sys

args = sys.argv[1:]

inputFile = args[0]

mode = args[1]

def GetJsonHolders():
        with open(os.path.dirname(__file__) + '/' + inputFile) as inJson:
            return json.load(inJson)

jsonHolders = GetJsonHolders()
holdersList = dict(jsonHolders)
outList = []

def whitelist():
    for key, value in holdersList.items():
        case = {'handle': key, 'amount': value['amount']}
        outList.append(case)

def giveaway():
    for key, value in holdersList.items():
        case = key
        amount = value['amount']
        for x in range(amount):
            outList.append(case)

if mode == "-w":
    whitelist()
    outputFile = inputFile[:-5] + '_whitelist_out.json'
elif mode == "-g":
    giveaway()
    outputFile = inputFile[:-5] + '_giveaway_out.json'
else:
    print("wrong option")
    sys.exit()


with open(os.path.dirname(__file__) + '/' + outputFile, 'w') as jsonFile:
            json.dump(outList, jsonFile, indent = 4)
