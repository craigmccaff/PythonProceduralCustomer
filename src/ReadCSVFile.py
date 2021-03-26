import csv
def getFileData(fileName):
    fileData = []
    with open("resource/" + fileName, 'rt')as dataFile:
        fileReader = csv.reader(dataFile)
        for row in fileReader:
            fileData.append(row)
    return fileData

def getLastLines( fileName, numerOfLines):
    return getFileData(fileName)[-1 * numerOfLines]