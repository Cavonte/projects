class temp():
    def __init__(self):
        self.__privater = 'Super Private'
        self._privateIsh = 'Private Ish'


temp = temp()

print(temp._privateIsh) ##prints no prob
print(temp.__privater) ##fack you