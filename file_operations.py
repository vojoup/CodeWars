# https://www.codewars.com/trainer/python
class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath
    def extension(self):
        return self.filepath[-3:]
    def filename(self):

    # def dirpath(self):
    #     #Your code here

master = FileMaster('/Users/person1/Pictures/house.png')

master.extension()
# should return >>> png

# master.filename()
# should return >>> house

# master.dirpath()
# should return >>> /Users/person1/Pictures/
