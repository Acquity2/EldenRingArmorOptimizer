import tkinter.messagebox as msgbox
from ArmorData import chest, helm, gauntlet, leg
import xlrd
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from tkinter.ttk import Scrollbar
import pyglet
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
import main as main
import webbrowser


"""print(helm.text())"""
helmRawXMLStr = helm.text()
chestRawXMLStr = chest.text()
gauntletRawXMLStr = gauntlet.text()
legRawXMLStr = leg.text()

HelmList = []
ChestList = []
GauntletList = []
LegList = []
HelmList_ = {}
ChestList_ = {}
GauntletList_ = {}
LegList_ = {}

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


class hcgl(Armor):
    pass


class PlayerResistance:
    '''
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
    '''

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


def PoiPerWgtTimSort(arr, rever=False):  # PoiPerWgtTimSort
    return sorted(arr, key=lambda x: x.PoiPerWgt, reverse=rever)


def PoiTimSort(arr, rever=False):  # PoiTimSort
    return sorted(arr, key=lambda x: x.Poi, reverse=rever)


def PhyTimSort(arr, rever=False):  # PhyTimSort
    return sorted(arr, key=lambda x: x.Phy, reverse=rever)


def VSStrTimSort(arr, rever=False):  # VSStrTimSort
    return sorted(arr, key=lambda x: x.VSStr, reverse=rever)


def VSSlaTimSort(arr, rever=False):  # VSSlaTimSort
    return sorted(arr, key=lambda x: x.VSSla, reverse=rever)


def VSPieTimSort(arr, rever=False):  # VSPieTimSort
    return sorted(arr, key=lambda x: x.VSPie, reverse=rever)


def MagTimSort(arr, rever=False):  # MagTimSort
    return sorted(arr, key=lambda x: x.Mag, reverse=rever)


def FirTimSort(arr, rever=False):  # FirTimSort
    return sorted(arr, key=lambda x: x.Fir, reverse=rever)


def LitTimSort(arr, rever=False):  # LitTimSort
    return sorted(arr, key=lambda x: x.Lit, reverse=rever)


def HolTimSort(arr, rever=False):  # HolTimSort
    return sorted(arr, key=lambda x: x.Hol, reverse=rever)


def ImmTimSort(arr, rever=False):  # ImmTimSort
    return sorted(arr, key=lambda x: x.Imm, reverse=rever)


def RobuTimSort(arr, rever=False):  # RobuTimSort
    return sorted(arr, key=lambda x: x.Robu, reverse=rever)


def FocTimSort(arr, rever=False):  # FocTimSort
    return sorted(arr, key=lambda x: x.Foc, reverse=rever)


def getArmorID(name, armorList):
    for i in range(0, len(armorList)):
        if armorList[i].Name == name:
            return i


def separateByPoi(playerList):
    list1 = {}
    if len(playerList) == 0:
        return list1
    initPoi = playerList[len(playerList) - 1].Poi
    list1[initPoi] = []
    list1[initPoi].append(playerList[len(playerList) - 1])
    count = 1
    for i in range(-len(playerList) + 2, 1):
        if playerList[-i].Poi == initPoi:
            list1[playerList[-i].Poi].append(playerList[-i])
        else:
            count += 1
            if count>16:
                break
            list1[playerList[-i].Poi] = []
            list1[playerList[-i].Poi].append(playerList[-i])
            initPoi = playerList[-i].Poi
    return list1


##########################################################################################
helmStrList = helmRawXMLStr.split("</tr>")
for i in range(0, len(helmStrList) - 2):
    HelmList.append(hcgl(helmStrList[i]))

chestStrList = chestRawXMLStr.split("</tr>")
for i in range(0, len(chestStrList) - 2):
    ChestList.append(hcgl(chestStrList[i]))

gauntletStrList = gauntletRawXMLStr.split("</tr>")
for i in range(0, len(gauntletStrList) - 2):
    GauntletList.append(hcgl(gauntletStrList[i]))

legStrList = legRawXMLStr.split("</tr>")
for i in range(0, len(legStrList) - 2):
    LegList.append(hcgl(legStrList[i]))

for k in HelmList:
    k.Name = ArmorDir[k.Name]

for k in ChestList:
    k.Name = ArmorDir[k.Name]

for k in GauntletList:
    k.Name = ArmorDir[k.Name]

for k in LegList:
    k.Name = ArmorDir[k.Name]
############################################# 初始化部分 #############################################

print("头盔总数：", len(HelmList), "胸甲总数：", len(ChestList), "手套总数：", len(GauntletList), "护腿总数：", len(LegList))
# _Helm[1].showAll()
# _Helm[2].showAll()

# 按韧重比排序
HelmList_SortByPoiPerWgt = HelmList.copy()
ChestList_SortByPoiPerWgt = ChestList.copy()
GauntletList_SortByPoiPerWgt = GauntletList.copy()
LegList_SortByPoiPerWgt = LegList.copy()

HelmList_SortByPoiPerWgt = PoiPerWgtTimSort(HelmList_SortByPoiPerWgt)
ChestList_SortByPoiPerWgt = PoiPerWgtTimSort(ChestList_SortByPoiPerWgt)
GauntletList_SortByPoiPerWgt = PoiPerWgtTimSort(GauntletList_SortByPoiPerWgt)
LegList_SortByPoiPerWgt = PoiPerWgtTimSort(LegList_SortByPoiPerWgt)

HelmList_["SortByPhy"] = HelmList.copy()
ChestList_["SortByPhy"] = ChestList.copy()
GauntletList_["SortByPhy"] = GauntletList.copy()
LegList_["SortByPhy"] = LegList.copy()

HelmList_["SortByPhy"] = PhyTimSort(HelmList_["SortByPhy"])
ChestList_["SortByPhy"] = PhyTimSort(ChestList_["SortByPhy"])
GauntletList_["SortByPhy"] = PhyTimSort(GauntletList_["SortByPhy"])
LegList_["SortByPhy"] = PhyTimSort(LegList_["SortByPhy"])

HelmList_["SortByVSStr"] = HelmList.copy()
ChestList_["SortByVSStr"] = ChestList.copy()
GauntletList_["SortByVSStr"] = GauntletList.copy()
LegList_["SortByVSStr"] = LegList.copy()

HelmList_["SortByVSStr"] = VSStrTimSort(HelmList_["SortByVSStr"])
ChestList_["SortByVSStr"] = VSStrTimSort(ChestList_["SortByVSStr"])
GauntletList_["SortByVSStr"] = VSStrTimSort(GauntletList_["SortByVSStr"])
LegList_["SortByVSStr"] = VSStrTimSort(LegList_["SortByVSStr"])

HelmList_["SortByVSSla"] = HelmList.copy()
ChestList_["SortByVSSla"] = ChestList.copy()
GauntletList_["SortByVSSla"] = GauntletList.copy()
LegList_["SortByVSSla"] = LegList.copy()

HelmList_["SortByVSSla"] = VSSlaTimSort(HelmList_["SortByVSSla"])
ChestList_["SortByVSSla"] = VSSlaTimSort(ChestList_["SortByVSSla"])
GauntletList_["SortByVSSla"] = VSSlaTimSort(GauntletList_["SortByVSSla"])
LegList_["SortByVSSla"] = VSSlaTimSort(LegList_["SortByVSSla"])

HelmList_["SortByVSPie"] = HelmList.copy()
ChestList_["SortByVSPie"] = ChestList.copy()
GauntletList_["SortByVSPie"] = GauntletList.copy()
LegList_["SortByVSPie"] = LegList.copy()

HelmList_["SortByVSPie"] = VSPieTimSort(HelmList_["SortByVSPie"])
ChestList_["SortByVSPie"] = VSPieTimSort(ChestList_["SortByVSPie"])
GauntletList_["SortByVSPie"] = VSPieTimSort(GauntletList_["SortByVSPie"])
LegList_["SortByVSPie"] = VSPieTimSort(LegList_["SortByVSPie"])

HelmList_["SortByMag"] = HelmList.copy()
ChestList_["SortByMag"] = ChestList.copy()
GauntletList_["SortByMag"] = GauntletList.copy()
LegList_["SortByMag"] = LegList.copy()

HelmList_["SortByMag"] = MagTimSort(HelmList_["SortByMag"])
ChestList_["SortByMag"] = MagTimSort(ChestList_["SortByMag"])
GauntletList_["SortByMag"] = MagTimSort(GauntletList_["SortByMag"])
LegList_["SortByMag"] = MagTimSort(LegList_["SortByMag"])

HelmList_["SortByFir"] = HelmList.copy()
ChestList_["SortByFir"] = ChestList.copy()
GauntletList_["SortByFir"] = GauntletList.copy()
LegList_["SortByFir"] = LegList.copy()

HelmList_["SortByFir"] = FirTimSort(HelmList_["SortByFir"])
ChestList_["SortByFir"] = FirTimSort(ChestList_["SortByFir"])
GauntletList_["SortByFir"] = FirTimSort(GauntletList_["SortByFir"])
LegList_["SortByFir"] = FirTimSort(LegList_["SortByFir"])

HelmList_["SortByLit"] = HelmList.copy()
ChestList_["SortByLit"] = ChestList.copy()
GauntletList_["SortByLit"] = GauntletList.copy()
LegList_["SortByLit"] = LegList.copy()

HelmList_["SortByLit"] = LitTimSort(HelmList_["SortByLit"])
ChestList_["SortByLit"] = LitTimSort(ChestList_["SortByLit"])
GauntletList_["SortByLit"] = LitTimSort(GauntletList_["SortByLit"])
LegList_["SortByLit"] = LitTimSort(LegList_["SortByLit"])

HelmList_["SortByHol"] = HelmList.copy()
ChestList_["SortByHol"] = ChestList.copy()
GauntletList_["SortByHol"] = GauntletList.copy()
LegList_["SortByHol"] = LegList.copy()

HelmList_["SortByHol"] = HolTimSort(HelmList_["SortByHol"])
ChestList_["SortByHol"] = HolTimSort(ChestList_["SortByHol"])
GauntletList_["SortByHol"] = HolTimSort(GauntletList_["SortByHol"])
LegList_["SortByHol"] = HolTimSort(LegList_["SortByHol"])

HelmList_["SortByImm"] = HelmList.copy()
ChestList_["SortByImm"] = ChestList.copy()
GauntletList_["SortByImm"] = GauntletList.copy()
LegList_["SortByImm"] = LegList.copy()

HelmList_["SortByImm"] = ImmTimSort(HelmList_["SortByImm"])
ChestList_["SortByImm"] = ImmTimSort(ChestList_["SortByImm"])
GauntletList_["SortByImm"] = ImmTimSort(GauntletList_["SortByImm"])
LegList_["SortByImm"] = ImmTimSort(LegList_["SortByImm"])

HelmList_["SortByRobu"] = HelmList.copy()
ChestList_["SortByRobu"] = ChestList.copy()
GauntletList_["SortByRobu"] = GauntletList.copy()
LegList_["SortByRobu"] = LegList.copy()

HelmList_["SortByRobu"] = RobuTimSort(HelmList_["SortByRobu"])
ChestList_["SortByRobu"] = RobuTimSort(ChestList_["SortByRobu"])
GauntletList_["SortByRobu"] = RobuTimSort(GauntletList_["SortByRobu"])
LegList_["SortByRobu"] = RobuTimSort(LegList_["SortByRobu"])

HelmList_["SortByFoc"] = HelmList.copy()
ChestList_["SortByFoc"] = ChestList.copy()
GauntletList_["SortByFoc"] = GauntletList.copy()
LegList_["SortByFoc"] = LegList.copy()

HelmList_["SortByFoc"] = FocTimSort(HelmList_["SortByFoc"])
ChestList_["SortByFoc"] = FocTimSort(ChestList_["SortByFoc"])
GauntletList_["SortByFoc"] = FocTimSort(GauntletList_["SortByFoc"])
LegList_["SortByFoc"] = FocTimSort(LegList_["SortByFoc"])

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


def fixWeightFindMaxPoi(weight, fixTerm, lst):  # 指定重量最大韧性
    key = 0
    _searchRange = 89
    _TmpPlayerList = []
    _playerLimit = 50000
    for ChestKey in range(-len(ChestList_SortByPoiPerWgt) + 1, 0):
        if ChestList_SortByPoiPerWgt[-ChestKey].Wgt > weight:
            continue
        flagc = False
        if fixTerm["chest"] != -1:
            if ChestKey == -fixTerm["chest"]:
                flagc = True
            else:
                continue
        for LegKey in range(-len(LegList_SortByPoiPerWgt) + 1, 0):
            if LegList_SortByPoiPerWgt[-LegKey].Wgt + ChestList_SortByPoiPerWgt[-ChestKey].Wgt > weight:
                continue
            flagl = False
            if fixTerm["leg"] != -1:
                if LegKey == -fixTerm["leg"]:
                    flagcl = True
                else:
                    continue
            for GauntletKey in range(-len(GauntletList_SortByPoiPerWgt) + 1, 0):
                if GauntletList_SortByPoiPerWgt[-GauntletKey].Wgt + ChestList_SortByPoiPerWgt[-ChestKey].Wgt + \
                        LegList_SortByPoiPerWgt[-LegKey].Wgt > weight:
                    continue
                flagg = False
                if fixTerm["gauntlet"] != -1:
                    if GauntletKey == -fixTerm["gauntlet"]:
                        flagg = True
                    else:
                        continue
                for HelmKey in range(-len(HelmList_SortByPoiPerWgt) + 1, 0):
                    if HelmList_SortByPoiPerWgt[-HelmKey].Wgt > weight:
                        continue
                    flagh = False
                    if fixTerm["helm"] != -1:
                        if HelmKey == -fixTerm["helm"]:
                            flagh = True
                        else:
                            continue
                    _weight = HelmList_SortByPoiPerWgt[-HelmKey].Wgt + ChestList_SortByPoiPerWgt[-ChestKey].Wgt + \
                              GauntletList_SortByPoiPerWgt[-GauntletKey].Wgt + LegList_SortByPoiPerWgt[-LegKey].Wgt
                    _poi = HelmList_SortByPoiPerWgt[-HelmKey].Poi + ChestList_SortByPoiPerWgt[-ChestKey].Poi + \
                           GauntletList_SortByPoiPerWgt[-GauntletKey].Poi + LegList_SortByPoiPerWgt[-LegKey].Poi
                    if weight >= _weight >= lst:
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
                    if flagh:
                        break
                if flagg:
                    break
            if flagl:
                break
        if flagc:
            break
    return _TmpPlayerList


def fixWeightFindMaxAbs(weight, sortKey, lst):  # 指定重量最大抗性
    fixTerm = {"helm": -1, "chest": -1, "gauntlet": -1, "leg": -1}
    key = 0
    _TmpPlayerList = []
    _playerLimit = 30000
    for ChestKey in range(-len(HelmList_[sortKey]) + 1, 0):
        if ChestList_SortByPoiPerWgt[-ChestKey].Wgt > weight:
            continue
        flagc = False
        if fixTerm["chest"] != -1:
            if ChestKey == -fixTerm["chest"]:
                flagc = True
            else:
                continue
        for LegKey in range(-len(LegList_[sortKey]) + 1, 0):
            if LegList_SortByPoiPerWgt[-LegKey].Wgt + ChestList_SortByPoiPerWgt[-ChestKey].Wgt > weight:
                continue
            flagl = False
            if fixTerm["leg"] != -1:
                if LegKey == -fixTerm["leg"]:
                    flagcl = True
                else:
                    continue
            for GauntletKey in range(-len(GauntletList_[sortKey]) + 1, 0):
                if GauntletList_SortByPoiPerWgt[-GauntletKey].Wgt + ChestList_SortByPoiPerWgt[-ChestKey].Wgt + \
                        LegList_SortByPoiPerWgt[-LegKey].Wgt > weight:
                    continue
                flagg = False
                if fixTerm["gauntlet"] != -1:
                    if GauntletKey == -fixTerm["gauntlet"]:
                        flagg = True
                    else:
                        continue
                for HelmKey in range(-len(HelmList_[sortKey]) + 1, 0):
                    if HelmList_SortByPoiPerWgt[-HelmKey].Wgt > weight:
                        continue
                    flagh = False
                    if fixTerm["helm"] != -1:
                        if HelmKey == -fixTerm["helm"]:
                            flagh = True
                        else:
                            continue
                    _weight = HelmList_[sortKey][-HelmKey].Wgt + ChestList_[sortKey][-ChestKey].Wgt + \
                              GauntletList_[sortKey][-GauntletKey].Wgt + LegList_[sortKey][-LegKey].Wgt
                    if weight >= _weight >= lst:
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
                    if flagh:
                        break
                if flagh:
                    break
            if flagh:
                break
        if flagh:
            break
    return _TmpPlayerList


def fixWeightPoiFindMaxAbs(weight, fixTerm, tgtPoi, lst):  # 指定重量最大韧性
    key = 0
    _searchRange = 89
    _TmpPlayerList = []
    _playerLimit = 3000
    count = 0
    count1 = 0
    for ChestKey in range(-len(ChestList_SortByPoiPerWgt) + 1, 0):
        if ChestList_SortByPoiPerWgt[-ChestKey].Wgt > weight:
            continue
        flagc = False
        if fixTerm["chest"] != -1:
            if ChestKey == -fixTerm["chest"]:
                flagc = True
            else:
                continue
        for LegKey in range(-len(LegList_SortByPoiPerWgt) + 1, 0):
            if LegList_SortByPoiPerWgt[-LegKey].Wgt + ChestList_SortByPoiPerWgt[-ChestKey].Wgt > weight:
                continue
            flagl = False
            if fixTerm["leg"] != -1:
                if LegKey == -fixTerm["leg"]:
                    flagcl = True
                else:
                    continue
            for GauntletKey in range(-len(GauntletList_SortByPoiPerWgt) + 1, 0):
                if GauntletList_SortByPoiPerWgt[-GauntletKey].Wgt + ChestList_SortByPoiPerWgt[-ChestKey].Wgt + \
                        LegList_SortByPoiPerWgt[-LegKey].Wgt > weight:
                    continue
                flagg = False
                if fixTerm["gauntlet"] != -1:
                    if GauntletKey == -fixTerm["gauntlet"]:
                        flagg = True
                    else:
                        continue
                for HelmKey in range(-len(HelmList_SortByPoiPerWgt) + 1, 0):
                    if HelmList_SortByPoiPerWgt[-HelmKey].Wgt > weight:
                        continue
                    flagh = False
                    if fixTerm["helm"] != -1:
                        if HelmKey == -fixTerm["helm"]:
                            flagh = True
                        else:
                            continue
                    _weight = HelmList_SortByPoiPerWgt[-HelmKey].Wgt + ChestList_SortByPoiPerWgt[-ChestKey].Wgt + \
                              GauntletList_SortByPoiPerWgt[-GauntletKey].Wgt + LegList_SortByPoiPerWgt[-LegKey].Wgt
                    _poi = HelmList_SortByPoiPerWgt[-HelmKey].Poi + ChestList_SortByPoiPerWgt[-ChestKey].Poi + \
                           GauntletList_SortByPoiPerWgt[-GauntletKey].Poi + LegList_SortByPoiPerWgt[-LegKey].Poi
                    if weight >= _weight >= lst and _poi == tgtPoi:
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
                    if flagh:
                        break
                if flagh:
                    break
            if flagh:
                break
        if flagh:
            break
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
    PoiTimSort(Player)
    Player_SeparateByPoi = separateByPoi(Player)
    for k in Player_SeparateByPoi:
        print(k)
        Player_SeparateByPoi[k] = PhyTimSort(Player_SeparateByPoi[k])
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
    Player = fixWeightPoiFindMaxAbs(Weight, FixTerm, tgtPoi )
    print(len(Player))
    Player_SeparateByPoi = separateByPoi(Player)
    print(Player_SeparateByPoi)
    for key in Player_SeparateByPoi:
        Player_SeparateByPoi[key] = LitTimSort(Player_SeparateByPoi[key])
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


def calculateMod1(_totalWeight, _weaponAndRing, _ratio, _FixTerm, lst):
    # totalWeight = 77.8
    # weaponAndRing = 14.7
    # ratio = 0.699
    '''计算并显示负重前五'''
    Weight = calculateWeight(_totalWeight, _weaponAndRing, _ratio)
    lst = calculateWeight(lst, _weaponAndRing, _ratio)
    Player = fixWeightFindMaxPoi(Weight, _FixTerm, lst)
    print(len(Player), "/", len(HelmList) * len(ChestList) * len(GauntletList) * len(LegList))
    Player = PoiTimSort(Player)
    return separateByPoi(Player)


def calculateMod2(_totalWeight, _weaponAndRing, _ratio, _FixTerm, _tgtPoi, lst):
    # totalWeight = 77.8
    # weaponAndRing = 14.7
    # ratio = 0.699
    '''计算并显示负重前五'''
    Weight = calculateWeight(_totalWeight, _weaponAndRing, _ratio)
    lst = calculateWeight(lst, _weaponAndRing, _ratio)
    Player = fixWeightPoiFindMaxAbs(Weight, _FixTerm, _tgtPoi, lst)
    if len(Player) == 0:
        return -1
    print(len(Player))
    Player = PoiTimSort(Player)
    return separateByPoi(Player)


def calculateMod3(_totalWeight, _weaponAndRing, _ratio, sortKey, lst):
    # totalWeight = 77.8
    # weaponAndRing = 14.7
    # ratio = 0.699
    '''计算并显示负重前五'''
    Weight = calculateWeight(_totalWeight, _weaponAndRing, _ratio)
    lst = calculateWeight(lst, _weaponAndRing, _ratio)
    Player = fixWeightFindMaxAbs(Weight, sortKey, lst)
    if len(Player) == 0:
        return -1
    return Player


'''
    for k in Player_SeparateByPoi:
        print(k)
        Player_SeparateByPoi[k] = PhyTimSort(Player_SeparateByPoi[k])
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

if __name__=='__main__':
    pyglet.font.add_file("SourceSans3-Regular.ttf")
    pyglet.font.load("SourceSans3-Regular.ttf")

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")
    Player_SeparateByPoia = {}


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    Version = "Ver 0.1.3"

    zh_cn = {
        "title": "艾尔登法环护甲计算器",
        1: "胸甲ID",
        2: "头盔ID",
        3: "护手ID",
        4: "腿甲ID",
        5: "最大负重：",
        6: "当前负重：",
        7: "目标韧性：",
        8: "最大70%负重",
        9: "最大30%负重",
        10: "最大                        %负重 ",
        11: "护甲ID搜索",
        12: "排序选项",
        14: "物理(普通)抗性",
        15: "打击抗性",
        16: '斩击抗性',
        17: '突刺抗性',
        18: "魔抗性",
        19: "火抗性",
        20: '雷抗性',
        21: '圣抗性',
        22: '免疫',
        23: '健壮',
        24: '理智',
        25: "韧性",
        26: "护甲搭配组合",
        27:"最低预期："

    }

    en_us = {
        "title": "Elden Ring Armor Optimizer",
        1: "Chest ID",
        2: "Helm ID",
        3: "Gauntlet ID",
        4: "Leg ID",
        5: "MAX Wgt.:",
        6: "Current Wgt.:",
        7: "Tgt Poi.:",
        8: "Up to 70% Burden",
        9: "Up to 30% Burden",
        10: "Up to                        % Burden ",
        11: "Armor Finder",
        12: "Sort By",
        14: "Phy.Abs.",
        15: "VSStr.Abs.",
        16: 'VSSla.Abs.',
        17: 'VSPie.Abs.',
        18: "Mag.Abs.",
        19: "Fir.Abs.",
        20: 'Lit.Abs.',
        21: 'Hol.Abs',
        22: 'Imm.',
        23: 'Robu.',
        24: 'Foc.',
        25: "Poise",
        26: "Armor Sets",
        27:"Min.Ep.Wgt."
    }

    languageSet = zh_cn

    FixTerm = {"helm": -1, "chest": -1, "gauntlet": -1, "leg": -1}
    TreeDir = {}
    currentMode = 1
    window = Tk()
    window.title(languageSet["title"])

    winWidth = 1125
    winHeight = 566
    window.geometry("%dx%d"%(winWidth, winHeight))
    window.configure(bg="#252525")

    style = ttk.Style("darkly")

    canvas = Canvas(
        window,
        bg="#252525",
        height=winHeight,
        width=winWidth,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0,
        0.0,
        1924.9999999999999,
        1566.0,
        fill="#222222",
        outline="")

    canvas.create_rectangle(
        335.9999999999999,
        0.0,
        1225.9999999999999,
        1566.0,
        fill="#303030",
        outline="")

    canvas.create_text(
        5.999999999999886,
        41.00000000000001,
        anchor="nw",
        text="ARMOR OPTIMIZER",
        fill="#FCFCFC",
        font=("Source Sans 3", 24 * -1)
    )

    canvas.create_text(
        5.999999999999886,
        75.0,
        anchor="nw",
        text="Design for Elden Ring",
        fill="#FCFCFC",
        font=("Source Sans 3", 14 * -1)
    )

    canvas.create_text(
        200,
        55.0,
        anchor="nw",
        text=Version,
        fill="#aaaaaa",
        font=("Source Sans 3", 12 * -1)
    )

    canvas.create_text(
        493.9999999999999,
        50.00000000000001,
        anchor="nw",
        text=languageSet[1],
        fill="#979797",
        font=("Source Sans 3", 16 * -1)
    )

    canvas.create_text(
        353.9999999999999,
        50.00000000000001,
        anchor="nw",
        text=languageSet[2],
        fill="#979797",
        font=("Source Sans 3", 16 * -1)
    )
    '''
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        447.9999999999999,
        60.00000000000001,
        image=entry_image_1
    )
    '''
    HeadIDInputEntry = Entry(
        bd=0,
        bg="#383838",
        highlightthickness=0
    )
    HeadIDInputEntry.insert(0, "-1")
    HeadIDInputEntry.place(
        x=410.9999999999999,
        y=50.00000000000001,
        width=74.0,
        height=18.0
    )
    '''
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        587.9999999999999,
        60.00000000000001,
        image=entry_image_2
    )
    '''
    ChestIDInputEntry = Entry(
        bd=0,
        bg="#383838",
        highlightthickness=0
    )
    ChestIDInputEntry.insert(0, "-1")
    ChestIDInputEntry.place(
        x=550.9999999999999,
        y=50.00000000000001,
        width=74.0,
        height=18.0
    )
    '''
    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        727.9999999999999,
        60.00000000000001,
        image=entry_image_3
    )
    '''
    LegIDInputEntry = Entry(
        bd=0,
        bg="#383838",
        highlightthickness=0
    )
    LegIDInputEntry.insert(0, "-1")
    LegIDInputEntry.place(
        x=690.9999999999999,
        y=50.00000000000001,
        width=74.0,
        height=18.0
    )
    '''
    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        868.9999999999999,
        60.00000000000001,
        image=entry_image_4
    )
    '''
    GauntletIDInputEntry = Entry(
        bd=0,
        bg="#383838",
        highlightthickness=0
    )
    GauntletIDInputEntry.insert(0, "-1")
    GauntletIDInputEntry.place(
        x=831.9999999999999,
        y=50.00000000000001,
        width=74.0,
        height=18.0
    )
    '''
    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        868.9999999999999,
        28.000000000000007,
        image=entry_image_5
    )
    '''
    armorIDOutputEntry = Entry(
        bd=0,
        bg="#383838",
        highlightthickness=0,
    )
    armorIDOutputEntry.place(
        x=831.9999999999999,
        y=18.000000000000007,
        width=74.0,
        height=18.0
    )
    '''
    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        627.9999999999999,
        28.000000000000007,
        image=entry_image_6
    )
    '''
    armorNameInputEntry = Entry(
        bd=0,
        bg="#383838",
        highlightthickness=0
    )
    armorNameInputEntry.place(
        x=490.9999999999999,
        y=18.000000000000007,
        width=274.0,
        height=18.0
    )
    '''
    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        209.4999999999999,
        215.0,
        image=entry_image_7
    )
    '''
    MaxWgtInputEntry = Entry(
        bd=0,
        bg="#383838",
        highlightthickness=0
    )
    MaxWgtInputEntry.place(
        x=103.99999999999989,
        y=191.0,
        width=211.0,
        height=18.0
    )

    LstWgtInputEntry = Entry(
        bd=0,
        bg="#383838",
        highlightthickness=0
    )
    LstWgtInputEntry.insert(0, "-1")
    LstWgtInputEntry.place(
        x=103.99999999999989,
        y=218.0,
        width=211.0,
        height=18.0
    )


    '''
    entry_image_8 = PhotoImage(
        file=relative_to_assets("entry_8.png"))
    entry_bg_8 = canvas.create_image(
        112.49999999999989,
        157.0,
        image=entry_image_8
    )
    '''
    entry_8 = Entry(
        bd=0,
        bg="#383838",
        highlightthickness=0
    )
    entry_8.place(
        x=80.99999999999989,
        y=147.0,
        width=63.0,
        height=18.0
    )
    '''
    entry_image_9 = PhotoImage(
        file=relative_to_assets("entry_9.png"))
    entry_bg_9 = canvas.create_image(
        209.4999999999999,
        269.0,
        image=entry_image_9
    )
    '''
    PoiInputEntry = Entry(
        bd=0,
        bg="#383838",
        highlightthickness=0,
    )
    PoiInputEntry.place(
        x=103.99999999999989,
        y=273.0,
        width=211.0,
        height=18.0
    )
    '''
    entry_image_10 = PhotoImage(
        file=relative_to_assets("entry_10.png"))
    entry_bg_10 = canvas.create_image(
        209.4999999999999,
        242.0,
        image=entry_image_10
    )
    '''
    CurrentWgtInputEntry = Entry(
        bd=0,
        bg="#383838",
        highlightthickness=0
    )
    CurrentWgtInputEntry.place(
        x=103.99999999999989,
        y=246.0,
        width=211.0,
        height=18.0
    )

    canvas.create_rectangle(
        353.9999999999999,
        83.0,
        1108.9999999999999,
        86.0,
        fill="#515151",
        outline="")

    canvas.create_rectangle(
        5.999999999999886,
        68.0,
        65.99999999999989,
        70.0,
        fill="#00C192",
        outline="")

    canvas.create_rectangle(
        12.999999999999886,
        183.0,
        317.9999999999999,
        186.0,
        fill="#515151",
        outline="")

    canvas.create_rectangle(
        12.999999999999886,
        296.0,
        317.9999999999999,
        299.0,
        fill="#515151",
        outline="")

    canvas.create_rectangle(
        335.9999999999999,
        5.000000000000007,
        338.9999999999999,
        561.0,
        fill="#515151",
        outline="")

    canvas.create_text(
        633.9999999999999,
        51.00000000000001,
        anchor="nw",
        text=languageSet[4],
        fill="#979797",
        font=("Source Sans 3", 16 * -1)
    )

    canvas.create_text(
        774.9999999999999,
        51.00000000000001,
        anchor="nw",
        text=languageSet[3],
        fill="#979797",
        font=("Source Sans 3", 16 * -1)
    )

    canvas.create_text(
        12.999999999999886,
        190.0,
        anchor="nw",
        text=languageSet[5],
        fill="#979797",
        font=("Source Sans 3", 16 * -1)
    )

    canvas.create_text(
        12.999999999999886,
        218.0,
        anchor="nw",
        text=languageSet[27],
        fill="#979797",
        font=("Source Sans 3", 16 * -1)
    )

    canvas.create_text(
        40.999999999999886,
        147.0,
        anchor="nw",
        text=languageSet[10],
        fill="#979797",
        font=("Source Sans 3", 16 * -1)
    )

    canvas.create_text(
        40.999999999999886,
        101.0,
        anchor="nw",
        text=languageSet[8],
        fill="#979797",
        font=("Source Sans 3", 16 * -1)
    )

    canvas.create_text(
        40.999999999999886,
        124.0,
        anchor="nw",
        text=languageSet[9],
        fill="#979797",
        font=("Source Sans 3", 16 * -1)
    )

    canvas.create_text(
        353.9999999999999,
        18.000000000000007,
        anchor="nw",
        text=languageSet[11],
        fill="#979797",
        font=("Source Sans 3", 16 * -1)
    )

    canvas.create_text(
        12.999999999999886,
        247.0,
        anchor="nw",
        text=languageSet[6],
        fill="#979797",
        font=("Source Sans 3", 16 * -1)
    )

    canvas.create_text(
        12.999999999999886,
        274.0,
        anchor="nw",
        text=languageSet[7],
        fill="#979797",
        font=("Source Sans 3", 16 * -1)
    )

    canvas.create_text(
        12.999999999999886,
        316.0,
        anchor="nw",
        text=languageSet[12],
        fill="#979797",
        font=("Source Sans 3", 16 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        133.9999999999999,
        430.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: findArmor(),
        relief="flat"
    )
    button_1.place(
        x=769.9999999999999,
        y=17.000000000000007,
        width=57.0,
        height=22.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: calculateButtonFunction(),
        relief="flat"
    )
    button_2.place(
        x=12.999999999999886,
        y=528.0,
        width=157.0,
        height=24.0
    )

    sortbutton_image_3 = PhotoImage(
        file=relative_to_assets("sortbutton_3.png"))
    sortbutton_3 = Button(
        image=sortbutton_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: sort_st(),
        relief="flat"
    )
    sortbutton_3.place(
        x=177.9999999999999,
        y=528.0,
        width=77.0,
        height=24.0
    )


    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: changeModeTo1(),
        relief="flat"
    )
    button_3.place(
        x=65.99999999999989,
        y=7.105427357601002e-15,
        width=90.0,
        height=40.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: changeModeTo3(),
        relief="flat"
    )
    button_4.place(
        x=245.9999999999999,
        y=7.105427357601002e-15,
        width=90.0,
        height=40.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    DebugButton = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:
        printSomeThing(),
        relief="flat"
    )
    DebugButton.place(
        x=1.1368683772161603e-13,
        y=7.105427357601002e-15,
        width=66.0,
        height=40.0
    )

    modeText = ttk.Label(
        anchor="nw",
        text="当前模式:1",
        font=("Source Sans 3", 12 * -1)
    )
    modeText.place(x=265, y=50)

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: changeModeTo2(),
        relief="flat"
    )
    button_6.place(
        x=155.9999999999999,
        y=7.105427357601002e-15,
        width=90.0,
        height=40.0
    )

    selectedAbs = tk.StringVar()
    Abss = ((languageSet[14], 1),
            (languageSet[15], 2),
            (languageSet[16], 3),
            (languageSet[17], 4),
            (languageSet[18], 5),
            (languageSet[19], 6),
            (languageSet[20], 7),
            (languageSet[21], 8),
            (languageSet[22], 9),
            (languageSet[23], 10),
            (languageSet[24], 11)
            )
    key = 0
    for size in Abss:
        r = ttk.Radiobutton(
            text=size[0],
            value=size[1],
            variable=selectedAbs
        )
        if key <= 5:
            r.place(
                x=26,
                y=356 + 25 * key,
                height=20
            )
        else:
            r.place(
                x=126,
                y=356 + 25 * (key - 6),
                height=20
            )
        key = key + 1
    selectedAbs.set(1)

    selectedWgtPercentID = tk.StringVar()
    radiobutton = []
    WgtPercent = ("7", "3", "1")
    key1 = 0
    for size in WgtPercent:
        r = ttk.Radiobutton(
            value=size[0],
            variable=selectedWgtPercentID
        )
        r.place(
            x=14,
            y=102 + 22 * key1,
            height=20)
        key1 = key1 + 1
    selectedWgtPercentID.set(7)

    '''

    columns = ['护甲搭配组合']
    table = ttk.Treeview(
        height=24,  # 表格显示的行数,height行
        columns=columns,  # 显示的列
        show='headings',  # 隐藏首列
        yscrollcommand=yscroll.set,  # y轴滚动条
    selectmode = "browse",

    )

    table.heading(column='护甲搭配组合', text='护甲搭配组合', anchor=S,
                  command=lambda: print('护甲搭配组合'))  # 定义表头

    table.column('护甲搭配组合', width=740, minwidth=100, anchor=S, )  # 定义列
    table.anchor("center")
    table.place(
        x=354,
        y=100, )
    table.insert('', END, values=['头盔： Veteran\'s Helm 护甲： Veteran\'s Armor 手套： Gold'
                                  ' Bracelets 护腿： Veteran\'s Greaves 重量： 39.5 '])


    def treeviewClick(event):  # 单击
        for item in table.selection():
            item_text = table.item(item, "values")
            print(item_text)

    # 鼠标左键抬起
    table.bind('<ButtonRelease-1>', treeviewClick)

    # 鼠标选中一行回调
    def selectTree(event):
        for item in table.selection():
            item_text = table.item(item, "values")
            print(item_text)
    '''

    yscroll = Scrollbar(orient=VERTICAL)
    yscroll.place(
        x=1098,
        y=100,
        height=425
    )
    columns = ['1']
    tree = ttk.Treeview(height=23,
                        columns=columns,
                        yscrollcommand=yscroll.set,
                        )
    tree.heading(column='#0', text=languageSet[25], anchor=W,
                 command=lambda: print('护甲搭配组合'))
    tree.heading(column='1', text=languageSet[26], anchor=W,
                 command=lambda: print('护甲搭配组合'))
    tree.column("#0", anchor="w", width=80)
    tree.column("1", anchor="w", width=660)

    tree.anchor("center")
    tree.place(
        x=354,
        y=100, )
    '''
    myid = tree.insert("", "end", text="71", values=[])  # ""表示父节点是根
    myidx1 = tree.insert(myid, "end", text=" ", values=["头盔： Veteran\'s Helm 护甲： Veteran\'s Armor 手套： Gold\'Bracele"
                                                        "ts 护腿： Veteran\'s Greaves 重量： 39.5 "])
    myidx2 = tree.insert(myid, "end", text=" ", values=["头盔： Veteran\'s Helm 护甲： Veteran\'s Armor 手套： Gold\'Bracele"
                                                        "ts 护腿： Veteran\'s Greaves 重量： 39.5 "])
    myidx3 = tree.insert(myid, "end", text=" ", values=["头盔： Veteran\'s Helm 护甲： Veteran\'s Armor 手套： Gold\'Bracele"
                                                        "ts 护腿： Veteran\'s Greaves 重量： 39.5 "])
    myid4 = tree.insert("", "end", text="70", values=[])  # ""表示父节点是根
    myidx5 = tree.insert(myid4, "end", text=" ", values=["头盔： Veteran\'s Helm 护甲： Veteran\'s Armor 手套： Gold\'Bracele"
                                                         "ts 护腿： Veteran\'s Greaves 重量： 39.5 "])
    myidx6 = tree.insert(myid4, "end", text=" ", values=["头盔： Veteran\'s Helm 护甲： Veteran\'s Armor 手套： Gold\'Bracele"
                                                         "ts 护腿： Veteran\'s Greaves 重量： 39.5 "])
    myidx7 = tree.insert(myid4, "end", text=" ", values=["头盔： Veteran\'s Helm 护甲： Veteran\'s Armor 手套： Gold\'Bracele"
                                                         "ts 护腿： Veteran\'s Greaves 重量： 39.5 "])
    myid4 = tree.insert("", "end", text="69", values=[])  # ""表示父节点是根
    myid4 = tree.insert("", "end", text="68", values=[])  # ""表示父节点是根
    '''


    def selectTree(event):
        curItem = tree.focus()
        _dictionary = tree.item(curItem)
        if len(_dictionary["values"]) == 2:
            print(_dictionary["values"][0])
            print(_dictionary["values"][1])
            msgbox.showinfo("护甲信息", _dictionary["values"][1])


    # 选中行
    tree.bind('<<TreeviewSelect>>', selectTree)


    def changeModeTo1():
        modeText.config(text="当前模式:1")


    def changeModeTo2():
        modeText.config(text="当前模式:2")


    def changeModeTo3():
        modeText.config(text="当前模式:3")


    def printSomeThing():
        # print(selectedWgtPercentID.get())
        # print(entry_8.get())
        # print(getWgtPercent())
        # main.testfunction()
        # print(HeadIDInputEntry.get(), "1")
        # print(ChestIDInputEntry.get(), "2")
        # print(LegIDInputEntry.get(), "3")
        # print(GauntletIDInputEntry.get(), "4")
        # print(MaxWgtInputEntry.get(), "7")
        # print(entry_8.get(), "8")
        # print(PoiInputEntry.get(), "9")
        # print(CurrentWgtInputEntry.get(), "10")
        getFixTerm(FixTerm)
        print(FixTerm)
        print(modeText.cget("text")[-1])


    def getFixTerm(fixterm):
        fixterm["helm"] = int(HeadIDInputEntry.get())
        fixterm["chest"] = int(ChestIDInputEntry.get())
        fixterm["leg"] = int(LegIDInputEntry.get())
        fixterm["gauntlet"] = int(GauntletIDInputEntry.get())


    def findArmor():
        print("button_1 clicked")
        _ArmorName = armorNameInputEntry.get()
        armorIDOutputEntry.delete(0, END)
        armorIDOutputEntry.insert(0, main.findArmor(_ArmorName))


    def getWgtPercent():
        _id = selectedWgtPercentID.get()
        if _id == "7":
            return 0.699
        elif _id == "3":
            return 0.299
        elif _id == "1":
            if type(entry_8.get()) == str and 0 < float(entry_8.get()) < 100:
                return float(entry_8.get()) / 100
            else:
                return -1
        else:
            return -1


    def fillOutTreeMode1(doubleList):
        for k in doubleList:
            TreeDir[str(k) + "_parent"] = tree.insert("", "end", text=str(k), values=[])
            for i in range(0, len(doubleList[k])):
                # print(k,i,str(k) + "_" + str(i))
                # print(doubleList[k][i].Helm.Name)
                TreeDir[str(k) + "_" + str(i)] = tree.insert(TreeDir[str(k) + "_parent"], "end",
                                                             text=str(k) + "_" + str(i),
                                                             values=[("头盔：" + doubleList[k][i].Helm.Name
                                                                      + "  护甲：" + doubleList[k][i].Chest.Name
                                                                      + "  手套：" + doubleList[k][i].Gauntlet.Name
                                                                      + "  护腿：" + doubleList[k][i].Leg.Name
                                                                      + "  重量：" + str(round(doubleList[k][i].Wgt, 3))),
                                                                     "头盔：" + doubleList[k][i].Helm.Name +
                                                                     "\n护甲：" + doubleList[k][i].Chest.Name +
                                                                     "\n手套：" + doubleList[k][i].Gauntlet.Name +
                                                                     "\n护腿：" + doubleList[k][i].Leg.Name +
                                                                     "\n重量：" + str(round(doubleList[k][i].Wgt, 3)) +
                                                                     "\n物理：" + str(round(doubleList[k][i].Phy, 3)) +
                                                                     "\n打击抗性：" + str(round(doubleList[k][i].VSStr, 3)) +
                                                                     "\n斩击抗性：" + str(round(doubleList[k][i].VSSla, 3)) +
                                                                     "\n突刺抗性：" + str(round(doubleList[k][i].VSPie, 3)) +
                                                                     "\n魔力抗性：" + str(round(doubleList[k][i].Mag, 3)) +
                                                                     "\n火抗性：" + str(round(doubleList[k][i].Fir, 3)) +
                                                                     "\n雷抗性：" + str(round(doubleList[k][i].Lit, 3)) +
                                                                     "\n圣抗性：" + str(round(doubleList[k][i].Hol, 3)) +
                                                                     "\n免疫力：" + str(round(doubleList[k][i].Imm, 3)) +
                                                                     "\n健壮度：" + str(round(doubleList[k][i].Robu, 3)) +
                                                                     "\n理智度：" + str(round(doubleList[k][i].Foc, 3)) +
                                                                     "\n抗死度：" + str(round(doubleList[k][i].Vita, 3)) +
                                                                     "\n韧性：" + str(round(doubleList[k][i].Poi, 3)) +
                                                                     "\n韧重比：" + str(round(doubleList[k][i].PoiPerWgt, 3)) +
                                                                     "\n实际韧性：" + str(round(doubleList[k][i].Poi, 3) / 10) +
                                                                     "\n实际韧性为游戏内部计算时使用值"
                                                                     ])


    def sort(playerList, sortID, revert=True):
        if sortID == "1":
            for k in playerList:
                playerList[k] = main.PhyTimSort(playerList[k], rever=revert)
        elif sortID == "2":
            for k in playerList:
                playerList[k] = main.VSStrTimSort(playerList[k], rever=revert)
        elif sortID == "3":
            for k in playerList:
                playerList[k] = main.VSSlaTimSort(playerList[k], rever=revert)
        elif sortID == "4":
            for k in playerList:
                playerList[k] = main.VSPieTimSort(playerList[k], rever=revert)
        elif sortID == "5":
            for k in playerList:
                playerList[k] = main.MagTimSort(playerList[k], rever=revert)
        elif sortID == "6":
            for k in playerList:
                playerList[k] = main.FirTimSort(playerList[k], rever=revert)
        elif sortID == "7":
            for k in playerList:
                playerList[k] = main.LitTimSort(playerList[k], rever=revert)
        elif sortID == "8":
            for k in playerList:
                playerList[k] = main.HolTimSort(playerList[k], rever=revert)
        elif sortID == "9":
            for k in playerList:
                playerList[k] = main.ImmTimSort(playerList[k], rever=revert)
        elif sortID == "10":
            for k in playerList:
                playerList[k] = main.RobuTimSort(playerList[k], rever=revert)
        elif sortID == "11":
            for k in playerList:
                playerList[k] = main.FocTimSort(playerList[k], rever=revert)


    def getSortKey(sortID):
        if sortID == "1":
            return "SortByPhy"
        elif sortID == "2":
            return "SortByVSStr"
        elif sortID == "3":
            return "SortByVSSla"
        elif sortID == "4":
            return "SortByVSPie"
        elif sortID == "5":
            return "SortByMag"
        elif sortID == "6":
            return "SortByFir"
        elif sortID == "7":
            return "SortByLit"
        elif sortID == "8":
            return "SortByHol"
        elif sortID == "9":
            return "SortByImm"
        elif sortID == "10":
            return "SortByRobu"
        elif sortID == "11":
            return "SortByFoc"

    def getMinExpectWgt():
        if float(LstWgtInputEntry.get()) != -1:
            return float(LstWgtInputEntry.get())
        else:
            return float(MaxWgtInputEntry.get())*0.95


    def calculateMode_1():
        global Player_SeparateByPoia
        x = tree.get_children()
        for item in x:
            tree.delete(item)
        _totalWeight = float(MaxWgtInputEntry.get())
        _weaponAndRing = float(CurrentWgtInputEntry.get())
        _ratio = getWgtPercent()
        getFixTerm(FixTerm)
        Player_SeparateByPoi = main.calculateMod1(_totalWeight, _weaponAndRing, _ratio, FixTerm,
                                                  float(LstWgtInputEntry.get()))
        sortID = selectedAbs.get()
        sort(Player_SeparateByPoi, sortID)
        Player_SeparateByPoia = {}
        for k in Player_SeparateByPoi:
            Player_SeparateByPoia[k] = []
            while len(Player_SeparateByPoi[k]) > 8:
                Player_SeparateByPoia[k].append(Player_SeparateByPoi[k].pop())
            for i in Player_SeparateByPoi[k]:
                Player_SeparateByPoia[k].append(Player_SeparateByPoi[k][-1])
        fillOutTreeMode1(Player_SeparateByPoi)


    def calculateMode_2():
        global Player_SeparateByPoia
        x = tree.get_children()
        for item in x:
            tree.delete(item)
        _totalWeight = float(MaxWgtInputEntry.get())
        _weaponAndRing = float(CurrentWgtInputEntry.get())
        _ratio = getWgtPercent()
        _tgtPoi = float(PoiInputEntry.get())
        getFixTerm(FixTerm)
        Player_SeparateByPoi = main.calculateMod2(_totalWeight, _weaponAndRing, _ratio, FixTerm, _tgtPoi,
                                                  float(LstWgtInputEntry.get()))
        if Player_SeparateByPoi == -1:
            msgbox.showinfo("警告", "无法根据输入数据找到护甲组合！\n请更换数据后尝试!")
            return
        sortID = selectedAbs.get()
        sort(Player_SeparateByPoi, sortID)
        Player_SeparateByPoia = Player_SeparateByPoi
        for k in Player_SeparateByPoi:
            while len(Player_SeparateByPoi[k]) > 8:
                Player_SeparateByPoi[k].pop()
        fillOutTreeMode1(Player_SeparateByPoi)


    def calculateMode_3():
        global Player_SeparateByPoia
        x = tree.get_children()
        for item in x:
            tree.delete(item)
        _totalWeight = float(MaxWgtInputEntry.get())
        _weaponAndRing = float(CurrentWgtInputEntry.get())
        Player_SeparateByPoi = {}
        _ratio = getWgtPercent()
        sortID = selectedAbs.get()
        _sortKey = getSortKey(sortID)
        Player = main.calculateMod3(_totalWeight, _weaponAndRing, _ratio, _sortKey, float(LstWgtInputEntry.get()))
        Player_SeparateByPoi["nil"] = Player
        sort(Player_SeparateByPoi, sortID)
        Player_SeparateByPoi["nil"].reverse()
        Player_SeparateByPoia = Player_SeparateByPoi
        while len(Player_SeparateByPoi["nil"]) > 100:
            Player_SeparateByPoi[k].pop()
        fillOutTreeMode1(Player_SeparateByPoi)


    def calculateButtonFunction():
        mode = modeText.cget("text")
        if mode[-1] == "1":
            calculateMode_1()
        elif mode[-1] == "2":
            calculateMode_2()
        elif mode[-1] == "3":
            calculateMode_3()

    def sort_st():
        global Player_SeparateByPoia
        x = tree.get_children()
        for item in x:
            tree.delete(item)
        sortID = selectedAbs.get()
        sort(Player_SeparateByPoia, sortID ,revert=False)
        for k in Player_SeparateByPoia:
            Player_SeparateByPoia[k].reverse()
            while len(Player_SeparateByPoia[k]) > 8:
                Player_SeparateByPoia[k].pop()
        fillOutTreeMode1(Player_SeparateByPoia)


    def showInfo():
        msgbox.showinfo("说明", """
    最低预期指可以接受的装备加武器加戒指的总重量下限，用于过滤与目标相差过大的目标。低可用负重的情况下或许需要进行修改。默认值-1为95%最大负重。

    模式1:
    给定可用负重，计算最大韧性的护甲搭配：
    给出一个从高到低排序的韧性列表，同一种韧性可能有多种护甲搭配组合。
    对于同韧性的不同搭配组合，按选择的抗性种类从高到低排序。
    （一般情况，韧性越高越好）

    模式2：
    给定负重和目标韧性值，计算出合适的护甲搭配：
    计算出搭配组合后，按照选择的抗性种类，抗性从高到低排序。
    （适用于特定规则下限制韧性或只堆韧到韧性质变点）

    以上两种模式都支持护甲自选功能：
    固定1到3个部位的护甲，进行以上两种最优化计算。
    在护甲搜索框内输入护甲全名，点击搜索获取护甲id，将护甲id输入对应的护甲id输入框中。
    默认值-1为不固定该部位护甲。

    模式3：
    给定负重情况下不考虑韧性，计算最高属性抗性套装：
    输出表格为选定抗性从高到低排序。
        """)


    def openWeb():
        webbrowser.open('https://github.com/Acquity2/EldenRingArmorOptimizer')


    '''
    radiobutton_1 = ttk.Radiobutton(text="Phy.abs", value=1, variable=selected)
    radiobutton_1.place(
        x=26,
        y=356,
        height=20
    )
    '''
    canvas.create_rectangle(
        244.9999999999999,
        2.000000000000007,
        246.9999999999999,
        38.00000000000001,
        fill="#151515",
        outline="")

    canvas.create_rectangle(
        154.9999999999999,
        2.000000000000007,
        156.9999999999999,
        38.00000000000001,
        fill="#151515",
        outline="")

    canvas.create_rectangle(
        64.99999999999989,
        2.000000000000007,
        66.99999999999989,
        38.00000000000001,
        fill="#151515",
        outline="")

    button_7 = ttk.Button(
        text="说明",
        command=lambda: showInfo(),
        bootstyle="info-outline"
    )

    button_7.place(
        x=265,
        y=529.0,
        width=60.0,
        height=24.0,

    )

    button_8 = ttk.Button(
        text="https://github.com/Acquity2/EldenRingArmorOptimizer",
        command=lambda: openWeb(),
        style="link-light"
    )

    button_8.place(
        x=339, y=540,
        width=785.0,
        height=26.0,
    )

    canvas.create_rectangle(
        353.9999999999999,
        537.0,
        1108.9999999999999,
        540.0,
        fill="#515151",
        outline="")
    """
    someInfo = ttk.Label(
        anchor="nw",
        text="""

    """
        font=("Source Sans 3", 12 * -1),
        background="#303030",
        foreground="#979797",
    )
    someInfo.place(x=500, y=50)
    """

    window.resizable(False, False)
    window.mainloop()
