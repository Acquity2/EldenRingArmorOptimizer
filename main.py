import tkinter as tk
import tkinter.messagebox as msgbox
from ArmorData import chest, helm, gauntlet, leg
import xlrd
import json

"""print(helm.text())"""
helmRawXMLStr = helm.text()
chestRawXMLStr = chest.text()
gauntletRawXMLStr = gauntlet.text()
legRawXMLStr = leg.text()

HelmList = {}
ChestList = {}
GauntletList = {}
LegList = {}
HelmList_ = {}
ChestList_ = {}
GauntletList_ = {}
LegList_ = {}

HelmList_SortByPoiPerWgt = {}
ChestList_SortByPoiPerWgt = {}
GauntletList_SortByPoiPerWgt = {}
LegList_SortByPoiPerWgt = {}

Player = {}
Player_SeparateByPoi = {}

FixTerm = {"helm": -1, "chest": -1, "gauntlet": -1, "leg": -1}

data = xlrd.open_workbook("ArmorNameList1.xls")
table = data.sheets()[0]
ArmorDir = {}
for i in range(0, 572):
    table_list = table.row_values(rowx=i, start_colx=0, end_colx=None)
    ArmorDir[table_list[0]] = table_list[1]


class Armor:
    Name = ""
    Wgt = 0
    Phy = 0
    VSStr = 0
    VSSla = 0
    VSPie = 0
    Mag = 0
    Fir = 0
    Lit = 0
    Hol = 0
    Imm = 0
    Robu = 0
    Foc = 0
    Vita = 0
    Poi = 0
    PoiPerWgt = 0

    def __init__(self, _string):
        self.Name = _string.split("</td>")[0].split("Ring ")[1].split("\" href")[0]
        self.Phy = float(_string.split("</td>")[1].split(">")[1])
        self.VSStr = float(_string.split("</td>")[2].split(">")[1])
        self.VSSla = float(_string.split("</td>")[3].split(">")[1])
        self.VSPie = float(_string.split("</td>")[4].split(">")[1])
        self.Mag = float(_string.split("</td>")[5].split(">")[1])
        self.Fir = float(_string.split("</td>")[6].split(">")[1])
        self.Lit = float(_string.split("</td>")[7].split(">")[1])
        self.Hol = float(_string.split("</td>")[8].split(">")[1])
        self.Imm = float(_string.split("</td>")[9].split(">")[1])
        self.Robu = float(_string.split("</td>")[10].split(">")[1])
        self.Foc = float(_string.split("</td>")[11].split(">")[1])
        self.Vita = float(_string.split("</td>")[12].split(">")[1])
        self.Wgt = float(_string.split("</td>")[14].split(">")[1])
        self.Poi = float(_string.split("</td>")[13].split(">")[1])
        self.PoiPerWgt = self.Poi / self.Wgt

    def showAll(self):
        msgbox.showinfo("title",
                        self.Name + "\n 重量：" +
                        str(self.Wgt) + "\n 物理：" +
                        str(self.Phy) + "\n 打击抗性：" +
                        str(self.VSStr) + "\n 斩击抗性：" +
                        str(self.VSSla) + "\n 突刺抗性：" +
                        str(self.VSPie) + "\n 魔力抗性：" +
                        str(self.Mag) + "\n 火抗性：" +
                        str(self.Fir) + "\n 雷抗性：" +
                        str(self.Lit) + "\n 圣抗性：" +
                        str(self.Hol) + "\n 免疫力：" +
                        str(self.Imm) + "\n 健壮度：" +
                        str(self.Robu) + "\n 理智度：" +
                        str(self.Foc) + "\n 抗死度：" +
                        str(self.Vita) + "\n 韧性：" +
                        str(self.Poi) + "\n 韧重比：" +
                        str(self.PoiPerWgt)
                        )


class Helm(Armor):
    type = "Helm"


class Chest(Armor):
    type = "Chest Armor"


class Gauntlet(Armor):
    type = "Gauntlet"


class Leg(Armor):
    type = "Leg"


class PlayerResistance:
    Helm = Helm
    Chest = Chest
    Gauntlet = Gauntlet
    Leg = Leg
    Wgt = 0
    Phy = 0
    VSStr = 0
    VSSla = 0
    VSPie = 0
    Mag = 0
    Fir = 0
    Lit = 0
    Hol = 0
    Imm = 0
    Robu = 0
    Foc = 0
    Vita = 0
    Poi = 0
    PoiPerWgt = 0

    def __init__(self, helmKey, helmList, chestKey, chestList, gauntletKey, gauntletList, legKey, legList):
        self.Helm = helmList[helmKey]
        self.Chest = chestList[chestKey]
        self.Gauntlet = gauntletList[gauntletKey]
        self.Leg = legList[legKey]
        self.Poi = self.Helm.Poi + self.Chest.Poi + self.Gauntlet.Poi + self.Leg.Poi

        self.Phy = \
            100 - 100 * (1 - self.Helm.Phy / 100) * (1 - self.Chest.Phy / 100) * \
            (1 - self.Gauntlet.Phy / 100) * (1 - self.Leg.Phy / 100)
        self.VSStr = \
            100 - 100 * (1 - self.Helm.VSStr / 100) * (1 - self.Chest.VSStr / 100) * \
            (1 - self.Gauntlet.VSStr / 100) * (1 - self.Leg.VSStr / 100)
        self.VSSla = \
            100 - 100 * (1 - self.Helm.VSSla / 100) * (1 - self.Chest.VSSla / 100) * \
            (1 - self.Gauntlet.VSSla / 100) * (1 - self.Leg.VSSla / 100)
        self.VSPie = \
            100 - 100 * (1 - self.Helm.VSPie / 100) * (1 - self.Chest.VSPie / 100) * \
            (1 - self.Gauntlet.VSPie / 100) * (1 - self.Leg.VSPie / 100)
        self.Mag = \
            100 - 100 * (1 - self.Helm.Mag / 100) * (1 - self.Chest.Mag / 100) * \
            (1 - self.Gauntlet.Mag / 100) * (1 - self.Leg.Mag / 100)
        self.Fir = \
            100 - 100 * (1 - self.Helm.Fir / 100) * (1 - self.Chest.Fir / 100) * \
            (1 - self.Gauntlet.Fir / 100) * (1 - self.Leg.Fir / 100)
        self.Lit = \
            100 - 100 * (1 - self.Helm.Lit / 100) * (1 - self.Chest.Lit / 100) * \
            (1 - self.Gauntlet.Lit / 100) * (1 - self.Leg.Lit / 100)
        self.Hol = \
            100 - 100 * (1 - self.Helm.Hol / 100) * (1 - self.Chest.Hol / 100) * \
            (1 - self.Gauntlet.Hol / 100) * (1 - self.Leg.Hol / 100)
        self.Imm = self.Helm.Imm + self.Chest.Imm + self.Gauntlet.Imm + self.Leg.Imm
        self.Robu = self.Helm.Robu + self.Chest.Robu + \
                    self.Gauntlet.Robu + self.Leg.Robu
        self.Foc = self.Helm.Foc + self.Chest.Foc + self.Gauntlet.Foc + self.Leg.Foc
        self.Vita = self.Helm.Vita + self.Chest.Vita + \
                    self.Gauntlet.Vita + self.Leg.Vita

        self.Wgt = self.Helm.Wgt + self.Chest.Wgt + self.Gauntlet.Wgt + self.Leg.Wgt
        if self.Poi == 0:
            self.PoiPerWgt = 0
        else:
            self.PoiPerWgt = self.Poi / self.Wgt

    def showAllResistance(self):
        msgbox.showinfo("title",
                        "头盔：" + self.Helm.Name +
                        "\n护甲：" + self.Chest.Name +
                        "\n手套：" + self.Gauntlet.Name +
                        "\n护腿：" + self.Leg.Name +
                        "\n 重量：" +
                        str(self.Wgt) + "\n 物理：" +
                        str(self.Phy) + "\n 打击抗性：" +
                        str(self.VSStr) + "\n 斩击抗性：" +
                        str(self.VSSla) + "\n 突刺抗性：" +
                        str(self.VSPie) + "\n 魔力抗性：" +
                        str(self.Mag) + "\n 火抗性：" +
                        str(self.Fir) + "\n 雷抗性：" +
                        str(self.Lit) + "\n 圣抗性：" +
                        str(self.Hol) + "\n 免疫力：" +
                        str(self.Imm) + "\n 健壮度：" +
                        str(self.Robu) + "\n 理智度：" +
                        str(self.Foc) + "\n 抗死度：" +
                        str(self.Vita) + "\n 韧性：" +
                        str(self.Poi) + "\n 韧重比：" +
                        str(self.PoiPerWgt)
                        )


def copyArr(arr1):
    arr2 = {}
    for i in range(0, len(arr1)):
        arr2[i] = arr1[i]
    return arr2


def PoiPerWgtInsertionSort(arr1):
    arr2 = arr1
    for arrI in range(1, len(arr2)):
        key = arr2[arrI]
        j = arrI - 1
        while j >= 0 and key.PoiPerWgt <= arr2[j].PoiPerWgt:
            arr2[j + 1] = arr2[j]
            j -= 1
        arr2[j + 1] = key
    return arr2


def PoiInsertionSort(arr1):  # 韧性排序
    arr2 = arr1
    for arrI in range(1, len(arr2)):
        key = arr2[arrI]
        j = arrI - 1
        while j >= 0 and key.Poi < arr2[j].Poi:
            arr2[j + 1] = arr2[j]
            j -= 1
        arr2[j + 1] = key
    return arr2


def PhyInsertionSort(arr1):  # 物理抗性排序
    arr2 = arr1
    for arrI in range(1, len(arr2)):
        key = arr2[arrI]
        j = arrI - 1
        while j >= 0 and key.Phy < arr2[j].Phy:
            arr2[j + 1] = arr2[j]
            j -= 1
        arr2[j + 1] = key
    return arr2


def VSStrInsertionSort(arr1):  # 物理抗性排序
    arr2 = arr1
    for arrI in range(1, len(arr2)):
        key = arr2[arrI]
        j = arrI - 1
        while j >= 0 and key.VSStr < arr2[j].VSStr:
            arr2[j + 1] = arr2[j]
            j -= 1
        arr2[j + 1] = key
    return arr2


def VSSlaInsertionSort(arr1):  # 物理抗性排序
    arr2 = arr1
    for arrI in range(1, len(arr2)):
        key = arr2[arrI]
        j = arrI - 1
        while j >= 0 and key.VSSla < arr2[j].VSSla:
            arr2[j + 1] = arr2[j]
            j -= 1
        arr2[j + 1] = key
    return arr2


def VSPieInsertionSort(arr1):  # 物理抗性排序
    arr2 = arr1
    for arrI in range(1, len(arr2)):
        key = arr2[arrI]
        j = arrI - 1
        while j >= 0 and key.VSPie < arr2[j].VSPie:
            arr2[j + 1] = arr2[j]
            j -= 1
        arr2[j + 1] = key
    return arr2


def MagInsertionSort(arr1):  # 魔抗性排序
    arr2 = arr1
    for arrI in range(1, len(arr2)):
        key = arr2[arrI]
        j = arrI - 1
        while j >= 0 and key.Mag < arr2[j].Mag:
            arr2[j + 1] = arr2[j]
            j -= 1
        arr2[j + 1] = key
    return arr2


def FirInsertionSort(arr1):  # 火抗性排序
    arr2 = arr1
    for arrI in range(1, len(arr2)):
        key = arr2[arrI]
        j = arrI - 1
        while j >= 0 and key.Fir < arr2[j].Fir:
            arr2[j + 1] = arr2[j]
            j -= 1
        arr2[j + 1] = key
    return arr2


def LitInsertionSort(arr1):  # 雷抗性排序
    arr2 = arr1
    for arrI in range(1, len(arr2)):
        key = arr2[arrI]
        j = arrI - 1
        while j >= 0 and key.Lit < arr2[j].Lit:
            arr2[j + 1] = arr2[j]
            j -= 1
        arr2[j + 1] = key
    return arr2


def HolInsertionSort(arr1):  # 圣抗性排序
    arr2 = arr1
    for arrI in range(1, len(arr2)):
        key = arr2[arrI]
        j = arrI - 1
        while j >= 0 and key.Hol < arr2[j].Hol:
            arr2[j + 1] = arr2[j]
            j -= 1
        arr2[j + 1] = key
    return arr2


def ImmInsertionSort(arr1):  # 免疫排序
    arr2 = arr1
    for arrI in range(1, len(arr2)):
        key = arr2[arrI]
        j = arrI - 1
        while j >= 0 and key.Imm < arr2[j].Imm:
            arr2[j + 1] = arr2[j]
            j -= 1
        arr2[j + 1] = key
    return arr2


def RobuInsertionSort(arr1):  # 健壮排序
    arr2 = arr1
    for arrI in range(1, len(arr2)):
        key = arr2[arrI]
        j = arrI - 1
        while j >= 0 and key.Robu < arr2[j].Robu:
            arr2[j + 1] = arr2[j]
            j -= 1
        arr2[j + 1] = key
    return arr2


def FocInsertionSort(arr1):  # 理智排序
    arr2 = arr1
    for arrI in range(1, len(arr2)):
        key = arr2[arrI]
        j = arrI - 1
        while j >= 0 and key.Foc < arr2[j].Foc:
            arr2[j + 1] = arr2[j]
            j -= 1
        arr2[j + 1] = key
    return arr2


def getArmorID(name, armorList):
    for i in range(0, len(armorList)):
        if armorList[i].Name == name:
            return i


def separateByPoi(playerList):
    list1 = {}
    initPoi = playerList[len(playerList) - 1].Poi
    list1[initPoi] = []
    list1[initPoi].append(playerList[len(playerList) - 1])
    for i in range(-len(playerList) + 2, 1):
        if playerList[-i].Poi == initPoi:
            list1[playerList[-i].Poi].append(playerList[-i])
        else:
            list1[playerList[-i].Poi] = []
            list1[playerList[-i].Poi].append(playerList[-i])
            initPoi = playerList[-i].Poi
    return list1


##########################################################################################
helmStrList = helmRawXMLStr.split("</tr>")
for i in range(0, len(helmStrList) - 2):
    HelmList[i] = Helm(helmStrList[i])

chestStrList = chestRawXMLStr.split("</tr>")
for i in range(0, len(chestStrList) - 2):
    ChestList[i] = Chest(chestStrList[i])

gauntletStrList = gauntletRawXMLStr.split("</tr>")
for i in range(0, len(gauntletStrList) - 2):
    GauntletList[i] = Chest(gauntletStrList[i])

legStrList = legRawXMLStr.split("</tr>")
for i in range(0, len(legStrList) - 2):
    LegList[i] = Chest(legStrList[i])

for k in HelmList:
    HelmList[k].Name = ArmorDir[HelmList[k].Name]

for k in ChestList:
    ChestList[k].Name = ArmorDir[ChestList[k].Name]

for k in GauntletList:
    GauntletList[k].Name = ArmorDir[GauntletList[k].Name]

for k in LegList:
    LegList[k].Name = ArmorDir[LegList[k].Name]
############################################# 初始化部分 #############################################

print("头盔总数：", len(HelmList), "胸甲总数：", len(ChestList), "手套总数：", len(GauntletList), "护腿总数：", len(LegList))
# _Helm[1].showAll()
# _Helm[2].showAll()

# 按韧重比排序
HelmList_SortByPoiPerWgt = HelmList.copy()
ChestList_SortByPoiPerWgt = ChestList.copy()
GauntletList_SortByPoiPerWgt = GauntletList.copy()
LegList_SortByPoiPerWgt = LegList.copy()

HelmList_SortByPoiPerWgt = PoiPerWgtInsertionSort(HelmList_SortByPoiPerWgt)
ChestList_SortByPoiPerWgt = PoiPerWgtInsertionSort(ChestList_SortByPoiPerWgt)
GauntletList_SortByPoiPerWgt = PoiPerWgtInsertionSort(GauntletList_SortByPoiPerWgt)
LegList_SortByPoiPerWgt = PoiPerWgtInsertionSort(LegList_SortByPoiPerWgt)

HelmList_["SortByPhy"] = HelmList.copy()
ChestList_["SortByPhy"] = ChestList.copy()
GauntletList_["SortByPhy"] = GauntletList.copy()
LegList_["SortByPhy"] = LegList.copy()

HelmList_["SortByPhy"] = PhyInsertionSort(HelmList_["SortByPhy"])
ChestList_["SortByPhy"] = PhyInsertionSort(ChestList_["SortByPhy"])
GauntletList_["SortByPhy"] = PhyInsertionSort(GauntletList_["SortByPhy"])
LegList_["SortByPhy"] = PhyInsertionSort(LegList_["SortByPhy"])

HelmList_["SortByVSStr"] = HelmList.copy()
ChestList_["SortByVSStr"] = ChestList.copy()
GauntletList_["SortByVSStr"] = GauntletList.copy()
LegList_["SortByVSStr"] = LegList.copy()

HelmList_["SortByVSStr"] = VSStrInsertionSort(HelmList_["SortByVSStr"])
ChestList_["SortByVSStr"] = VSStrInsertionSort(ChestList_["SortByVSStr"])
GauntletList_["SortByVSStr"] = VSStrInsertionSort(GauntletList_["SortByVSStr"])
LegList_["SortByVSStr"] = VSStrInsertionSort(LegList_["SortByVSStr"])

HelmList_["SortByVSSla"] = HelmList.copy()
ChestList_["SortByVSSla"] = ChestList.copy()
GauntletList_["SortByVSSla"] = GauntletList.copy()
LegList_["SortByVSSla"] = LegList.copy()

HelmList_["SortByVSSla"] = VSSlaInsertionSort(HelmList_["SortByVSSla"])
ChestList_["SortByVSSla"] = VSSlaInsertionSort(ChestList_["SortByVSSla"])
GauntletList_["SortByVSSla"] = VSSlaInsertionSort(GauntletList_["SortByVSSla"])
LegList_["SortByVSSla"] = VSSlaInsertionSort(LegList_["SortByVSSla"])

HelmList_["SortByVSPie"] = HelmList.copy()
ChestList_["SortByVSPie"] = ChestList.copy()
GauntletList_["SortByVSPie"] = GauntletList.copy()
LegList_["SortByVSPie"] = LegList.copy()

HelmList_["SortByVSPie"] = VSPieInsertionSort(HelmList_["SortByVSPie"])
ChestList_["SortByVSPie"] = VSPieInsertionSort(ChestList_["SortByVSPie"])
GauntletList_["SortByVSPie"] = VSPieInsertionSort(GauntletList_["SortByVSPie"])
LegList_["SortByVSPie"] = VSPieInsertionSort(LegList_["SortByVSPie"])

HelmList_["SortByMag"] = HelmList.copy()
ChestList_["SortByMag"] = ChestList.copy()
GauntletList_["SortByMag"] = GauntletList.copy()
LegList_["SortByMag"] = LegList.copy()

HelmList_["SortByMag"] = MagInsertionSort(HelmList_["SortByMag"])
ChestList_["SortByMag"] = MagInsertionSort(ChestList_["SortByMag"])
GauntletList_["SortByMag"] = MagInsertionSort(GauntletList_["SortByMag"])
LegList_["SortByMag"] = MagInsertionSort(LegList_["SortByMag"])

HelmList_["SortByFir"] = HelmList.copy()
ChestList_["SortByFir"] = ChestList.copy()
GauntletList_["SortByFir"] = GauntletList.copy()
LegList_["SortByFir"] = LegList.copy()

HelmList_["SortByFir"] = FirInsertionSort(HelmList_["SortByFir"])
ChestList_["SortByFir"] = FirInsertionSort(ChestList_["SortByFir"])
GauntletList_["SortByFir"] = FirInsertionSort(GauntletList_["SortByFir"])
LegList_["SortByFir"] = FirInsertionSort(LegList_["SortByFir"])

HelmList_["SortByLit"] = HelmList.copy()
ChestList_["SortByLit"] = ChestList.copy()
GauntletList_["SortByLit"] = GauntletList.copy()
LegList_["SortByLit"] = LegList.copy()

HelmList_["SortByLit"] = LitInsertionSort(HelmList_["SortByLit"])
ChestList_["SortByLit"] = LitInsertionSort(ChestList_["SortByLit"])
GauntletList_["SortByLit"] = LitInsertionSort(GauntletList_["SortByLit"])
LegList_["SortByLit"] = LitInsertionSort(LegList_["SortByLit"])

HelmList_["SortByHol"] = HelmList.copy()
ChestList_["SortByHol"] = ChestList.copy()
GauntletList_["SortByHol"] = GauntletList.copy()
LegList_["SortByHol"] = LegList.copy()

HelmList_["SortByHol"] = HolInsertionSort(HelmList_["SortByHol"])
ChestList_["SortByHol"] = HolInsertionSort(ChestList_["SortByHol"])
GauntletList_["SortByHol"] = HolInsertionSort(GauntletList_["SortByHol"])
LegList_["SortByHol"] = HolInsertionSort(LegList_["SortByHol"])

HelmList_["SortByImm"] = HelmList.copy()
ChestList_["SortByImm"] = ChestList.copy()
GauntletList_["SortByImm"] = GauntletList.copy()
LegList_["SortByImm"] = LegList.copy()

HelmList_["SortByImm"] = ImmInsertionSort(HelmList_["SortByImm"])
ChestList_["SortByImm"] = ImmInsertionSort(ChestList_["SortByImm"])
GauntletList_["SortByImm"] = ImmInsertionSort(GauntletList_["SortByImm"])
LegList_["SortByImm"] = ImmInsertionSort(LegList_["SortByImm"])

HelmList_["SortByRobu"] = HelmList.copy()
ChestList_["SortByRobu"] = ChestList.copy()
GauntletList_["SortByRobu"] = GauntletList.copy()
LegList_["SortByRobu"] = LegList.copy()

HelmList_["SortByRobu"] = RobuInsertionSort(HelmList_["SortByRobu"])
ChestList_["SortByRobu"] = RobuInsertionSort(ChestList_["SortByRobu"])
GauntletList_["SortByRobu"] = RobuInsertionSort(GauntletList_["SortByRobu"])
LegList_["SortByRobu"] = RobuInsertionSort(LegList_["SortByRobu"])

HelmList_["SortByFoc"] = HelmList.copy()
ChestList_["SortByFoc"] = ChestList.copy()
GauntletList_["SortByFoc"] = GauntletList.copy()
LegList_["SortByFoc"] = LegList.copy()

HelmList_["SortByFoc"] = FocInsertionSort(HelmList_["SortByFoc"])
ChestList_["SortByFoc"] = FocInsertionSort(ChestList_["SortByFoc"])
GauntletList_["SortByFoc"] = FocInsertionSort(GauntletList_["SortByFoc"])
LegList_["SortByFoc"] = FocInsertionSort(LegList_["SortByFoc"])

'''玩家护甲输入
player1 = PlayerResistance(1, HelmList, 3, ChestList, 2, GauntletList, 4, LegList)
print("头盔：", player1.Armor["Helm"].Name, player1.Armor["Helm"].Phy, "\n护甲：", player1.Armor["Chest"].Name,
      player1.Armor["Chest"].Phy, "\n手套：", player1.Armor["Gauntlet"].Name, player1.Armor["Gauntlet"].Phy,
      "\n护腿：", player1.Armor["Leg"].Name, player1.Armor["Leg"].Phy)
print(player1.Armor["Helm"].showAll())
print(player1.Poi, player1.Phy)
print(ChestList[30].showAll())
player1.showAllResistance()
player1.Armor["Leg"].showAll()
'''

'''
for i in range(1, len(HelmList_SortByPoiPerWgt)):
    print(HelmList_SortByPoiPerWgt[i].Name, HelmList_SortByPoiPerWgt[i].PoiPerWgt)
for i in range(1, len(ChestList)):
    print(ChestList[i].name, ChestList[i].PoiPerWgt)
for i in range(1, len(GauntletList)):
    print(GauntletList[i].name, GauntletList[i].PoiPerWgt)    
for i in range(1, len(LegList)):
    print(LegList[i].name, LegList[i].PoiPerWgt)
'''


def calculateWeight(_maxWeight, _currentWeight, _ratio):  # 计算可用负重
    return _maxWeight * _ratio - _currentWeight


def fixWeightFindMaxPoi(weight, fixTerm):  # 指定重量最大韧性
    key = 0
    _searchRange = 89
    _TmpPlayerList = []
    _playerLimit = 13000
    for ChestKey in range(-len(ChestList_SortByPoiPerWgt) + 1, 0):
        if fixTerm["chest"] != -1 and ChestKey != -fixTerm["chest"]:
            continue
        for LegKey in range(-len(LegList_SortByPoiPerWgt) + 1, 0):
            if fixTerm["leg"] != -1 and LegKey != -fixTerm["leg"]:
                continue
            for GauntletKey in range(-len(GauntletList_SortByPoiPerWgt) + 1, 0):
                if fixTerm["gauntlet"] != -1 and GauntletKey != -fixTerm["gauntlet"]:
                    continue
                for HelmKey in range(-len(HelmList_SortByPoiPerWgt) + 1, 0):
                    if fixTerm["helm"] != -1 and HelmKey != -fixTerm["helm"]:
                        continue
                    _weight = HelmList_SortByPoiPerWgt[-HelmKey].Wgt + ChestList_SortByPoiPerWgt[-ChestKey].Wgt + \
                              GauntletList_SortByPoiPerWgt[-GauntletKey].Wgt + LegList_SortByPoiPerWgt[-LegKey].Wgt
                    _poi = HelmList_SortByPoiPerWgt[-HelmKey].Poi + ChestList_SortByPoiPerWgt[-ChestKey].Poi + \
                           GauntletList_SortByPoiPerWgt[-GauntletKey].Poi + LegList_SortByPoiPerWgt[-LegKey].Poi
                    if weight >= _weight >= weight * 0.95:
                        _TmpPlayer = PlayerResistance(
                            -HelmKey, HelmList_SortByPoiPerWgt,
                            -ChestKey, ChestList_SortByPoiPerWgt,
                            -GauntletKey, GauntletList_SortByPoiPerWgt,
                            -LegKey, LegList_SortByPoiPerWgt
                        )
                        _TmpPlayerList.append(_TmpPlayer)
                        key = key + 1
                    if key >= _playerLimit:
                        return _TmpPlayerList
    return _TmpPlayerList


def fixWeightFindMaxAbs(weight, sortKey):  # 指定重量最大韧性
    key = 0
    _TmpPlayerList = []
    _playerLimit = 13000
    for ChestKey in range(-len(HelmList_[sortKey]) + 1, 0):
        for LegKey in range(-len(LegList_[sortKey]) + 1, 0):
            for GauntletKey in range(-len(GauntletList_[sortKey]) + 1, 0):
                for HelmKey in range(-len(HelmList_[sortKey]) + 1, 0):
                    _weight = HelmList_[sortKey][-HelmKey].Wgt + ChestList_[sortKey][-ChestKey].Wgt + \
                              GauntletList_[sortKey][-GauntletKey].Wgt + LegList_[sortKey][-LegKey].Wgt
                    if weight >= _weight >= weight - 10:
                        _TmpPlayer = PlayerResistance(
                            -HelmKey, HelmList_SortByPoiPerWgt,
                            -ChestKey, ChestList_SortByPoiPerWgt,
                            -GauntletKey, GauntletList_SortByPoiPerWgt,
                            -LegKey, LegList_SortByPoiPerWgt
                        )
                        _TmpPlayerList.append(_TmpPlayer)
                        key = key + 1
                    if key >= _playerLimit:
                        return _TmpPlayerList
    return _TmpPlayerList


def fixWeightPoiFindMaxAbs(weight, fixTerm, tgtPoi):  # 指定重量最大韧性
    key = 0
    _searchRange = 89
    _TmpPlayerList = []
    _playerLimit = 3000
    count = 0
    count1 = 0
    for ChestKey in range(-len(ChestList_SortByPoiPerWgt) + 1, 0):
        if fixTerm["chest"] != -1 and ChestKey != -fixTerm["chest"]:
            continue
        for LegKey in range(-len(LegList_SortByPoiPerWgt) + 1, 0):
            if fixTerm["leg"] != -1 and LegKey != -fixTerm["leg"]:
                continue
            for GauntletKey in range(-len(GauntletList_SortByPoiPerWgt) + 1, 0):
                if fixTerm["gauntlet"] != -1 and GauntletKey != -fixTerm["gauntlet"]:
                    continue
                for HelmKey in range(-len(HelmList_SortByPoiPerWgt) + 1, 0):
                    if fixTerm["helm"] != -1 and HelmKey != -fixTerm["helm"]:
                        continue
                    _weight = HelmList_SortByPoiPerWgt[-HelmKey].Wgt + ChestList_SortByPoiPerWgt[-ChestKey].Wgt + \
                              GauntletList_SortByPoiPerWgt[-GauntletKey].Wgt + LegList_SortByPoiPerWgt[-LegKey].Wgt
                    _poi = HelmList_SortByPoiPerWgt[-HelmKey].Poi + ChestList_SortByPoiPerWgt[-ChestKey].Poi + \
                           GauntletList_SortByPoiPerWgt[-GauntletKey].Poi + LegList_SortByPoiPerWgt[-LegKey].Poi
                    if weight >= _weight and _poi == tgtPoi:
                        _TmpPlayer = PlayerResistance(
                            -HelmKey, HelmList_SortByPoiPerWgt,
                            -ChestKey, ChestList_SortByPoiPerWgt,
                            -GauntletKey, GauntletList_SortByPoiPerWgt,
                            -LegKey, LegList_SortByPoiPerWgt
                        )
                        _TmpPlayerList.append(_TmpPlayer)
                        key = key + 1
                        count1 = count
                    if count > 46372560:
                        return _TmpPlayerList
                    count = count + 1
                    if key > 0 and count > count1 + 2000000:
                        return _TmpPlayerList
                    if key >= _playerLimit:
                        return _TmpPlayerList
    return _TmpPlayerList


'''
Player[1] = PlayerResistance(168, HelmList_SortByPoiPerWgt, 33, ChestList_SortByPoiPerWgt, 2, GauntletList_SortByPoiPerWgt, 4, LegList_SortByPoiPerWgt)
print("头盔：", Player[1].Armor["Helm"].Name, Player[1].Armor["Helm"].Phy, "\n护甲：", Player[1].Armor["Chest"].Name,
      Player[1].Armor["Chest"].Phy, "\n手套：", Player[1].Armor["Gauntlet"].Name, Player[1].Armor["Gauntlet"].Phy,
      "\n护腿：", Player[1].Armor["Leg"].Name, Player[1].Armor["Leg"].Phy)

Player[2] = PlayerResistance(1, HelmList_SortByPoiPerWgt, 3, ChestList_SortByPoiPerWgt, 2, GauntletList_SortByPoiPerWgt, 4, LegList_SortByPoiPerWgt)
print("头盔：", Player[2].Armor["Helm"].Name, Player[2].Armor["Helm"].Phy,
      "\n护甲：", Player[2].Armor["Chest"].Name,Player[2].Armor["Chest"].Phy, 
      "\n手套：", Player[2].Armor["Gauntlet"].Name, Player[2].Armor["Gauntlet"].Phy,
      "\n护腿：", Player[2].Armor["Leg"].Name, Player[2].Armor["Leg"].Phy)
'''


def testfunction():
    totalWeight = 50
    weaponAndRing = 17.2
    ratio = 0.699

    for i in range(0, len(HelmList_SortByPoiPerWgt)):  # 搜索装备id
        if HelmList_SortByPoiPerWgt[i].Name == "Night Maiden Twin Crown":
            print(i)

    '''计算并显示负重前五'''
    Weight = calculateWeight(totalWeight, weaponAndRing, ratio)
    Player = fixWeightFindMaxPoi(Weight, FixTerm)
    print(len(Player))
    PoiInsertionSort(Player)
    Player_SeparateByPoi = separateByPoi(Player)
    for k in Player_SeparateByPoi:
        print(k)
        Player_SeparateByPoi[k] = PhyInsertionSort(Player_SeparateByPoi[k])
    for i in range(0, len(Player_SeparateByPoi[26])):
        print("头盔：", Player_SeparateByPoi[26][i].Helm.Name,
              "\n护甲：", Player_SeparateByPoi[26][i].Chest.Name,
              "\n手套：", Player_SeparateByPoi[26][i].Gauntlet.Name,
              "\n护腿：", Player_SeparateByPoi[26][i].Leg.Name,
              "\n韧性：", Player_SeparateByPoi[26][i].Poi,
              "\n护甲重量：", Player_SeparateByPoi[26][i].Wgt,
              "\n韧重比：", Player_SeparateByPoi[26][i].PoiPerWgt,
              "\ni:", i,
              "\n###############################################")
    Player_SeparateByPoi[26].reverse()
    while len(Player_SeparateByPoi[26]) > 5:
        Player_SeparateByPoi[26].pop()
    for i in range(0, len(Player_SeparateByPoi[26])):
        print("头盔：", Player_SeparateByPoi[26][i].Helm.Name,
              "\n护甲：", Player_SeparateByPoi[26][i].Chest.Name,
              "\n手套：", Player_SeparateByPoi[26][i].Gauntlet.Name,
              "\n护腿：", Player_SeparateByPoi[26][i].Leg.Name,
              "\n韧性：", Player_SeparateByPoi[26][i].Poi,
              "\n护甲重量：", Player_SeparateByPoi[26][i].Wgt,
              "\n韧重比：", Player_SeparateByPoi[26][i].PoiPerWgt,
              "\ni:", i,
              "\n###############################################")


def testfunction2():
    totalWeight = 50
    weaponAndRing = 17.2
    ratio = 0.699
    tgtPoi = 25
    Weight = calculateWeight(totalWeight, weaponAndRing, ratio)
    Player = fixWeightPoiFindMaxAbs(Weight, FixTerm, tgtPoi)
    print(len(Player))
    Player_SeparateByPoi = separateByPoi(Player)
    print(Player_SeparateByPoi)
    for key in Player_SeparateByPoi:
        Player_SeparateByPoi[key] = LitInsertionSort(Player_SeparateByPoi[key])
        Player_SeparateByPoi[key].reverse()
        while len(Player_SeparateByPoi[key]) > 50:
            Player_SeparateByPoi[key].pop()
    for key in Player_SeparateByPoi:
        for i in range(0, len(Player_SeparateByPoi[key])):
            print("头盔：", Player_SeparateByPoi[key][i].Helm.Name,
                  "\n护甲：", Player_SeparateByPoi[key][i].Chest.Name,
                  "\n手套：", Player_SeparateByPoi[key][i].Gauntlet.Name,
                  "\n护腿：", Player_SeparateByPoi[key][i].Leg.Name,
                  "\n韧性：", Player_SeparateByPoi[key][i].Poi,
                  "\n护甲重量：", Player_SeparateByPoi[key][i].Wgt,
                  "\n韧重比：", Player_SeparateByPoi[key][i].PoiPerWgt,
                  "\nLightning：", Player_SeparateByPoi[key][i].Lit,
                  "\ni:", i,
                  "\n###############################################")


"""
    i = 0
    length = len(Player_SeparateByPoi[26])
    while i <= length - 5:
        Player_SeparateByPoi[26].remove(i)
        print(i, Player_SeparateByPoi[26][i + 1].Wgt)
        i = i + 1
"""


def calculateMod1(_totalWeight, _weaponAndRing, _ratio, _FixTerm):
    # totalWeight = 77.8
    # weaponAndRing = 14.7
    # ratio = 0.699
    '''计算并显示负重前五'''
    Weight = calculateWeight(_totalWeight, _weaponAndRing, _ratio)
    Player = fixWeightFindMaxPoi(Weight, _FixTerm)
    print(len(Player))
    PoiInsertionSort(Player)
    return separateByPoi(Player)


def calculateMod2(_totalWeight, _weaponAndRing, _ratio, _FixTerm, _tgtPoi):
    # totalWeight = 77.8
    # weaponAndRing = 14.7
    # ratio = 0.699
    '''计算并显示负重前五'''
    Weight = calculateWeight(_totalWeight, _weaponAndRing, _ratio)
    Player = fixWeightPoiFindMaxAbs(Weight, _FixTerm, _tgtPoi)
    if len(Player) == 0:
        return -1
    print(len(Player))
    PoiInsertionSort(Player)
    return separateByPoi(Player)


def calculateMod3(_totalWeight, _weaponAndRing, _ratio, sortKey):
    # totalWeight = 77.8
    # weaponAndRing = 14.7
    # ratio = 0.699
    '''计算并显示负重前五'''
    Weight = calculateWeight(_totalWeight, _weaponAndRing, _ratio)
    Player = fixWeightFindMaxAbs(Weight, sortKey)
    if len(Player) == 0:
        return -1
    return Player


'''
    for k in Player_SeparateByPoi:
        print(k)
        Player_SeparateByPoi[k] = PhyInsertionSort(Player_SeparateByPoi[k])
    for i in range(69, 72):
        print("头盔：", Player_SeparateByPoi[i][0].Helm.Name,
              "\n护甲：", Player_SeparateByPoi[i][0].Chest.Name,
              "\n手套：", Player_SeparateByPoi[i][0].Gauntlet.Name,
              "\n护腿：", Player_SeparateByPoi[i][0].Leg.Name,
              "\n韧性：", Player_SeparateByPoi[i][0].Poi,
              "\n护甲重量：", Player_SeparateByPoi[i][0].Wgt,
              "\n韧重比：", Player_SeparateByPoi[i][0].PoiPerWgt,
              "\n###############################################")
'''


def findArmor(_armorName):
    for i in range(0, len(HelmList_SortByPoiPerWgt)):  # 搜索装备id
        if HelmList_SortByPoiPerWgt[i].Name == _armorName:
            return i
    for i in range(0, len(ChestList_SortByPoiPerWgt)):  # 搜索装备id
        if ChestList_SortByPoiPerWgt[i].Name == _armorName:
            return i
    for i in range(0, len(GauntletList_SortByPoiPerWgt)):  # 搜索装备id
        if GauntletList_SortByPoiPerWgt[i].Name == _armorName:
            return i
    for i in range(0, len(LegList_SortByPoiPerWgt)):  # 搜索装备id
        if LegList_SortByPoiPerWgt[i].Name == _armorName:
            return i
    return "Nothing Found"


# testfunction()
# testfunction2()

'''
print(
    "总负重：", totalWeight,
    "武器和戒指重量：", weaponAndRing,
    "负重比例", ratio * 100,
    "\n可用重量", Weight,
    "\n################################"
)

for i in range(-len(Player) + 1, -len(Player) + 5):
    # Player[-i].showAllResistance()
    print("头盔：", Player[-i].Helm.Name, Player[-i].Helm.Wgt,
          "\n护甲：", Player[-i].Chest.Name, Player[-i].Chest.Wgt,
          "\n手套：", Player[-i].Gauntlet.Name, Player[-i].Gauntlet.Wgt,
          "\n护腿：", Player[-i].Leg.Name, Player[-i].Leg.Wgt,
          "\n韧性：", Player[-i].Poi,
          "\n护甲重量：", Player[-i].Wgt,
          "\n韧重比：", Player[-i].PoiPerWgt,
          "\n###############################################")
'''

'''
for i in range(-len(GauntletList_SortByPoiPerWgt) + 1, -len(GauntletList_SortByPoiPerWgt) + 10):
    print(GauntletList_SortByPoiPerWgt[-i].Name, GauntletList_SortByPoiPerWgt[-i].PoiPerWgt,"  ",i)

print("###########")

for i in range(-len(GauntletList) + 1, -len(GauntletList) + 10):
    print(GauntletList[-i].Name, GauntletList[-i].PoiPerWgt)

print(GauntletList_SortByPoiPerWgt[88].PoiPerWgt)
print(GauntletList_SortByPoiPerWgt[87].PoiPerWgt)

if GauntletList_SortByPoiPerWgt[88].PoiPerWgt < GauntletList_SortByPoiPerWgt[87].PoiPerWgt:
    print("true")
else:
    print("false")
'''
