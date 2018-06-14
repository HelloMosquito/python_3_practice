# getFolderName = ['RECF_Apartment', 'RECF_Offices_retails', 'RECF-new_Apt', 'RECF-new_Offices']
# getFileName = ['RECF_Apartment_Page_Analytics', ]
#
#

import os


getFolderList = []
rootDir = 'F:\code test\Ma'
getRootList = os.listdir(rootDir)
# print(getRootList)
for item in getRootList:
    combPath = os.path.join(rootDir, item)
    if os.path.isdir(combPath) and (item[:4] == 'eREI' or item[:4] == 'RECF'):
        getFolderList.append(combPath)

sum = 0
for i in range(7):
    eachFolderPath = getFolderList[i]
    getFilesList = os.listdir(eachFolderPath)
    for item in getFilesList:
        getFilePath = os.path.join(eachFolderPath, item)
        with open(getFilePath) as f:
            getNo = len(f.readlines())
        sum = sum + getNo

print(sum)