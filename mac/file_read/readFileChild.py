class ReadFileChild:

    def __init__(self,file_obj):
        self.read_conf = file_obj

    def read_file(self):

        fileFormat = self.read_conf.file_format
        fileName = self.read_conf.filename
        fileLocation =self.read_conf.location
        print("Output: ",fileLocation)