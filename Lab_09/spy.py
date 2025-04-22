from abc import ABCMeta, abstractmethod


class Spy(metaclass=ABCMeta):
    @abstractmethod
    def visitGeneralStaff(self, military_obj):
        pass

    @abstractmethod
    def visitMilitaryBase(self, military_obj):
        pass


class MilitaryObj(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor: Spy):
        pass


class GeneralStaff(MilitaryObj):
    def __init__(self, generals, secretPaper):
        self.generals = generals
        self.secretPaper = secretPaper

    def __str__(self):
        return f"GeneralStaff: У генеральному штабі є {self.generals} геренералів та {self.secretPaper} секретних паперів."

    def accept(self, visitor: Spy):
        visitor.visitGeneralStaff(self)


class MilitaryBase(MilitaryObj):
    def __init__(self, officers, soldiers, jeeps, tanks):
        self.officers = officers
        self.soldiers = soldiers
        self.jeeps = jeeps
        self.tanks = tanks

    def __str__(self):
        return f"MilitaryBase: На військовій базі є {self.officers} офіцерів, {self.soldiers} солдатів, {self.jeeps} джипів та {self.tanks} танків."

    def accept(self, visitor: Spy):
        visitor.visitMilitaryBase(self)


class SecretAgent(Spy):
    def __init__(self):
        self.stolenInf = ""

    def visitGeneralStaff(self, military_obj):
        gen = military_obj.generals
        sp = military_obj.secretPaper
        self.stolenInf = f"SecretAgent: В генеральному штабі рашистів є {gen} генералів та {sp} секретних паперів"
        military_obj.secretPaper = 0

    def visitMilitaryBase(self, military_obj):
        of = military_obj.officers
        sol = military_obj.soldiers
        tn = military_obj.tanks
        dj = military_obj.jeeps
        self.stolenInf = f"SecretAgent: на військовій базі рашистів є {of} офіцерів, {sol} солдат, {tn} танків, {dj} джипів"

    def __str__(self):
        return self.stolenInf


class Sabouter(Spy):
    def __init__(self):
        self.resInf = ""

    def visitMilitaryBase(self, military_obj):
        military_obj.jeeps = 0
        military_obj.tanks = 0
        military_obj.officers = 0
        military_obj.soldiers = 0

        self.resInf = f"на військовій базі рашистів"


    def visitGeneralStaff(self, military_obj):
        military_obj.generals = 0
        military_obj.secretPaper = 0
        self.resInf = f"В генеральному штабі рашистів"

    def __str__(self):
        return f"Sabouter: всі ворожі обʼєкти знищено {self.resInf}"



if __name__ == '__main__':
    generalStaff = GeneralStaff(20, 100)
    print(generalStaff)

    militaryBase = MilitaryBase(10, 1000, 300, 20)
    print(militaryBase)

    sec_agent = SecretAgent()
    sabot = Sabouter()

    generalStaff.accept(sec_agent)
    print(sec_agent)
    print(generalStaff)

    militaryBase.accept(sabot)
    print(sabot)