import shutil

def swapFileData():
    data1="C:/Users/nmish/OneDrive/Desktop/Python/sampletext1.txt"
    data2="C:/Users/nmish/OneDrive/Desktop/Python/sampletext2.txt"
    middlesource="C:/Users/nmish/OneDrive/Desktop/Python/sampletextblank.txt"
    hi=shutil.copy(data1,middlesource)
    hi=shutil.copy(data2,data1)
    hi=shutil.copy(middlesource,data2)

swapFileData()