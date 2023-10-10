from readFileChild import ReadFileChild


class ReadFile:

    def __init__(self):
        self.file_format = 'csv'
        self.filename = 'sales_data_sample'
        self.location = r"C:\Users\Krishna\OneDrive\Documents"


if __name__ == "__main__":
    obj1 = ReadFile()
    obj2 = ReadFileChild(obj1)
    obj2.read_file()
