import os

from DateResolver import DateResolver
from DateSetter import DateSetter

dateResolver = DateResolver()
dateSetter = DateSetter()
output_dir_name = "output"
os.mkdir(output_dir_name)

processed_dirs = 0
processed_files = 0

dirs = [entry.name for entry in os.scandir() if entry.is_dir() and not entry.name.startswith(".") and not entry.name.startswith("_")]
for dir in dirs:
    dateTuple = dateResolver.resolve(dir)
    if dateTuple is None:
        continue

    d, m, y = dateTuple
    prefix = "{:04d}{:02d}{:02d}_".format(y, m, d)

    print("Processing dated folder '{}' using prefix '{}'".format(dir, prefix))
    files = [entry.name for entry in os.scandir(dir) if entry.is_file()]
    print("Moving {} file(s)".format(len(files)))

    for file in files:
        inputFile = "{}/{}".format(dir, file)
        outputFile = "{}/{}{}".format(output_dir_name, prefix, file)
        print("\tMoving '{}' -> '{}'".format(inputFile, outputFile))
        os.rename(inputFile, outputFile)
        dateSetter.setTime(outputFile, dateTuple)

    processed_dirs += 1
    processed_files += len(files)

print("Processed {} files in {} dirs".format(processed_files, processed_dirs))

