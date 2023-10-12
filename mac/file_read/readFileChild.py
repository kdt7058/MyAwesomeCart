import pandas


class ReadFileChild:

    def __init__(self, file_obj):
        self.read_conf = file_obj

    def read_file(self):
        fileFormat = self.read_conf.file_format
        fileName = self.read_conf.filename
        fileLocation = self.read_conf.location

        full_path = "{}\{}.{}".format(fileLocation, fileName, fileFormat)
        csvFile = pandas.read_csv(full_path, encoding='ISO-8859-1')
        print(csvFile)
