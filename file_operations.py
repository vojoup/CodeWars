# https://www.codewars.com/trainer/python
class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath
    def extension(self):
        return self.filepath.split('.')[-1]
    def filename(self):
        parts = self.filepath.split('/')
        return parts[-1].split('.')[0]
    def dirpath(self):
        d = len(self.filename()) + len(self.extension()) + 1
        return self.filepath[:len(self.filepath) - d]

master = FileMaster('/Users/person1/Pictures/house.png')
master.extension()
# should return >>> png
master.filename()
# should return >>> house
master.dirpath()
# should return >>> /Users/person1/Pictures/
