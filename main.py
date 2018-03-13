import os
from DateResolver import DateResolver
from DateSetter import DateSetter

dateResolver = DateResolver()
dateSetter = DateSetter()
output_dir_name = "output"
os.mkdir(output_dir_name)

dirs = [entry.name for entry in os.scandir() if entry.is_dir() and not entry.name.startswith(".") and not entry.name.startswith("_")]
for dir in dirs:
    dateTuple = dateResolver.resolve(dir)
    if dateTuple is None:
        continue

    d, m, y = dateTuple
    prefix = "{}{}{}".format(y, m, d)
    files = [entry.name for entry in os.scandir(dir) if entry.is_file()]
    for file in files:
        inputFile = "{}/{}".format(dir, file)
        outputFile = "{}/{}{}".format(output_dir_name, prefix, file)
        os.rename(inputFile, outputFile)
        dateSetter.setTime(outputFile, dateTuple)

