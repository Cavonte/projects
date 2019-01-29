import abc

class Student(object):
    __metaclass = abc.ABCMeta
    _grade = 0
    _nickName = "End me"

    @abc.abstractmethod
    def correct(self):
        print("Correcting")
        print("Setting Grade")

    @abc.abstractmethod
    def getGrade(self):
        return __grade


class PGMDelamortQuiTue(Student):
    __defaultMark = 100

    def correct(self):
        super(PGMDelamortQuiTue, self).correct()
        print("pgm")
        self._grade = self.__defaultMark

    def getGrade(self):
        return self._grade


class meirl(Student):
    __defaultMark = 50

    def correct(self):
        super(meirl, self).correct()
        print("meIrl")
        self._grade = self.__defaultMark

    def getGrade(self):
        return self._grade


class notgood(Student):
    __defaultMark = 0

    def correct(self):
        super(notgood, self).correct()
        print("notgood")
        self._grade = self.__defaultMark

    def getGrade(self):
        return self._grade


if '__main__' == __name__:
    print('la di da di da')
    me = meirl()
    pgm = PGMDelamortQuiTue()
    nop = notgood()

    stuff = [me, pgm, nop]

    for student in stuff:
        student.correct()
        print(student.getGrade())

    print(me._nickName)
