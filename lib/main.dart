import 'package:flutter/material.dart';
import 'package:flutter_application_1/jsondata.dart';
import 'package:window_manager/window_manager.dart';
import 'dart:convert';
import '../../assets/lang/language.dart';
import '../../ui/export.dart';
import 'package:flutter_treeview/flutter_treeview.dart';
import 'package:url_launcher/url_launcher.dart';

Map languageMap = language1.ZH;
String languageString = 'ZH';
bool nameChanged = false;
String calculateMode = "1";
int wgtPercentStatue = 1;
String? sortMode = "Phy.Abs.";
late ArmorData armorData;
late Map<String, String> ArmorSetNameAttribute = {};
final _globalKey = GlobalKey();
bool _wearGoat = true;
bool _poiInputEnable = false;

List<Node> testnodes = [
  const Node(label: 'documents', key: 'docs', children: [
    const Node(label: 'documents', key: 'docs3', icon: Icons.input),
    Node(
      label: 'documents',
      key: 'docs14',
      icon: Icons.input,
    ),
  ]),
  const Node(label: 'documents', key: 'docs1', icon: Icons.folder_open_outlined)
];

class Armor {
  String name = "";
  late double wgt;
  double phy = 0;
  double vSStr = 0;
  double vSSla = 0;
  double vSPie = 0;
  double mag = 0;
  double fir = 0;
  double lit = 0;
  double hol = 0;
  double imm = 0;
  double robu = 0;
  double foc = 0;
  double vita = 0;
  double poi = 0;
  double poiPerWgt = 0;

  Armor(var object) {
    name = object["Name"];
    wgt = object["Wgt"];
    phy = object["Phy"];
    vSStr = object["VSStr"];
    vSSla = object["VSSla"];
    vSPie = object["VSPie"];
    mag = object["Mag"];
    fir = object["Fir"];
    lit = object["Lit"];
    hol = object["Hol"];
    imm = object["Imm"];
    robu = object["Robu"];
    foc = object["Foc"];
    vita = object["Vita"];
    poi = object["Poi"];
    poiPerWgt = poi / wgt;
  }

  stringInfo() {
    return ("$name\n 重量：$wgt\n 物理：$phy\n 打击抗性：$vSStr\n 斩击抗性："
        "$vSSla\n 突刺抗性：$vSPie\n 魔力抗性：$mag\n 火抗性：$fir\n 雷抗性："
        "$lit\n 圣抗性：$hol\n 免疫力：$imm\n 健壮度：$robu\n 理智度：$foc"
        "\n 抗死度：$vita\n 韧性：$poi\n 韧重比：$poiPerWgt");
  }
}

class ArmorData {
  List<Armor> helms = [];
  List<Armor> chests = [];
  List<Armor> legs = [];
  List<Armor> gauntlets = [];
  ArmorData(helmJsonStr, chestJsonStr, legJsonStr, gauntletJsonStr) {
    List map = json.decode(helmJsonStr);
    for (var i = 0; i < map.length; i++) {
      helms.add(Armor(map[i]));
    }
    map = json.decode(chestJsonStr);
    for (var i = 0; i < map.length; i++) {
      chests.add(Armor(map[i]));
    }
    map = json.decode(legJsonStr);
    for (var i = 0; i < map.length; i++) {
      legs.add(Armor(map[i]));
    }
    map = json.decode(gauntletJsonStr);
    for (var i = 0; i < map.length; i++) {
      gauntlets.add(Armor(map[i]));
    }
  }
  reverse() {
    helms = helms.reversed.toList();
    chests = chests.reversed.toList();
    legs = legs.reversed.toList();
    gauntlets = gauntlets.reversed.toList();
  }

  ArmorData SortbyPoiPerWgt() {
    helms.sort((a, b) => a.poiPerWgt.compareTo(b.poiPerWgt));
    chests.sort((a, b) => a.poiPerWgt.compareTo(b.poiPerWgt));
    legs.sort((a, b) => a.poiPerWgt.compareTo(b.poiPerWgt));
    gauntlets.sort((a, b) => a.poiPerWgt.compareTo(b.poiPerWgt));
    reverse();
    return this;
  }

  ArmorData SortbyPhy() {
    helms.sort((a, b) => a.phy.compareTo(b.phy));
    chests.sort((a, b) => a.phy.compareTo(b.phy));
    legs.sort((a, b) => a.phy.compareTo(b.phy));
    gauntlets.sort((a, b) => a.phy.compareTo(b.phy));
    reverse();
    return this;
  }

  ArmorData SortbyVSStr() {
    helms.sort((a, b) => a.vSStr.compareTo(b.vSStr));
    chests.sort((a, b) => a.vSStr.compareTo(b.vSStr));
    legs.sort((a, b) => a.vSStr.compareTo(b.vSStr));
    gauntlets.sort((a, b) => a.vSStr.compareTo(b.vSStr));
    return this;
  }

  ArmorData SortbyVSSla() {
    helms.sort((a, b) => a.vSSla.compareTo(b.vSSla));
    chests.sort((a, b) => a.vSSla.compareTo(b.vSSla));
    legs.sort((a, b) => a.vSSla.compareTo(b.vSSla));
    gauntlets.sort((a, b) => a.vSSla.compareTo(b.vSSla));
    reverse();
    return this;
  }

  ArmorData SortbyVSPie() {
    helms.sort((a, b) => a.vSPie.compareTo(b.vSPie));
    chests.sort((a, b) => a.vSPie.compareTo(b.vSPie));
    legs.sort((a, b) => a.vSPie.compareTo(b.vSPie));
    gauntlets.sort((a, b) => a.vSPie.compareTo(b.vSPie));
    reverse();
    return this;
  }

  ArmorData SortbyMag() {
    helms.sort((a, b) => a.mag.compareTo(b.mag));
    chests.sort((a, b) => a.mag.compareTo(b.mag));
    legs.sort((a, b) => a.mag.compareTo(b.mag));
    gauntlets.sort((a, b) => a.mag.compareTo(b.mag));
    reverse();
    return this;
  }

  ArmorData SortbyFir() {
    helms.sort((a, b) => a.fir.compareTo(b.fir));
    chests.sort((a, b) => a.fir.compareTo(b.fir));
    legs.sort((a, b) => a.fir.compareTo(b.fir));
    gauntlets.sort((a, b) => a.fir.compareTo(b.fir));
    reverse();
    return this;
  }

  ArmorData SortbyHol() {
    helms.sort((a, b) => a.hol.compareTo(b.hol));
    chests.sort((a, b) => a.hol.compareTo(b.hol));
    legs.sort((a, b) => a.hol.compareTo(b.hol));
    gauntlets.sort((a, b) => a.hol.compareTo(b.hol));
    reverse();
    return this;
  }

  ArmorData SortbyLit() {
    helms.sort((a, b) => a.lit.compareTo(b.lit));
    chests.sort((a, b) => a.lit.compareTo(b.lit));
    legs.sort((a, b) => a.lit.compareTo(b.lit));
    gauntlets.sort((a, b) => a.lit.compareTo(b.lit));
    reverse();
    return this;
  }

  ArmorData SortbyImm() {
    helms.sort((a, b) => a.imm.compareTo(b.imm));
    chests.sort((a, b) => a.imm.compareTo(b.imm));
    legs.sort((a, b) => a.imm.compareTo(b.imm));
    gauntlets.sort((a, b) => a.imm.compareTo(b.imm));
    reverse();
    return this;
  }

  ArmorData SortbyRobu() {
    helms.sort((a, b) => a.robu.compareTo(b.robu));
    chests.sort((a, b) => a.robu.compareTo(b.robu));
    legs.sort((a, b) => a.robu.compareTo(b.robu));
    gauntlets.sort((a, b) => a.robu.compareTo(b.robu));
    reverse();
    return this;
  }

  ArmorData SortbyFoc() {
    helms.sort((a, b) => a.foc.compareTo(b.foc));
    chests.sort((a, b) => a.foc.compareTo(b.foc));
    legs.sort((a, b) => a.foc.compareTo(b.foc));
    gauntlets.sort((a, b) => a.foc.compareTo(b.foc));
    reverse();
    return this;
  }

  ArmorData SortbyVita() {
    helms.sort((a, b) => a.vita.compareTo(b.vita));
    chests.sort((a, b) => a.vita.compareTo(b.vita));
    legs.sort((a, b) => a.vita.compareTo(b.vita));
    gauntlets.sort((a, b) => a.vita.compareTo(b.vita));
    reverse();
    return this;
  }
}

class ArmorSet {
  Armor helm;
  Armor chest;
  Armor leg;
  Armor gauntlet;
  late double wgt;
  double phy = 0;
  double vSStr = 0;
  double vSSla = 0;
  double vSPie = 0;
  double mag = 0;
  double fir = 0;
  double lit = 0;
  double hol = 0;
  double imm = 0;
  double robu = 0;
  double foc = 0;
  double vita = 0;
  double poi = 0;

  ArmorSet(this.helm, this.chest, this.leg, this.gauntlet, this.poi) {
    wgt = helm.wgt + chest.wgt + leg.wgt + gauntlet.wgt;
    phy = 100 -
        100 *
            (1 - helm.phy / 100) *
            (1 - chest.phy / 100) *
            (1 - gauntlet.phy / 100) *
            (1 - leg.phy / 100);
    vSStr = 100 -
        100 *
            (1 - helm.vSStr / 100) *
            (1 - chest.vSStr / 100) *
            (1 - gauntlet.vSStr / 100) *
            (1 - leg.vSStr / 100);
    vSSla = 100 -
        100 *
            (1 - helm.vSSla / 100) *
            (1 - chest.vSSla / 100) *
            (1 - gauntlet.vSSla / 100) *
            (1 - leg.vSSla / 100);
    vSPie = 100 -
        100 *
            (1 - helm.vSPie / 100) *
            (1 - chest.vSPie / 100) *
            (1 - gauntlet.vSPie / 100) *
            (1 - leg.vSPie / 100);
    mag = 100 -
        100 *
            (1 - helm.mag / 100) *
            (1 - chest.mag / 100) *
            (1 - gauntlet.mag / 100) *
            (1 - leg.mag / 100);
    fir = 100 -
        100 *
            (1 - helm.fir / 100) *
            (1 - chest.fir / 100) *
            (1 - gauntlet.fir / 100) *
            (1 - leg.fir / 100);
    lit = 100 -
        100 *
            (1 - helm.lit / 100) *
            (1 - chest.lit / 100) *
            (1 - gauntlet.lit / 100) *
            (1 - leg.lit / 100);
    hol = 100 -
        100 *
            (1 - helm.hol / 100) *
            (1 - chest.hol / 100) *
            (1 - gauntlet.hol / 100) *
            (1 - leg.hol / 100);
    imm = helm.imm + chest.imm + leg.imm + gauntlet.imm;
    robu = helm.robu + chest.robu + leg.robu + gauntlet.robu;
    foc = helm.foc + chest.foc + leg.foc + gauntlet.foc;
    vita = helm.vita + chest.vita + leg.vita + gauntlet.vita;
  }

  String getName() {
    return "${languageMap["Helm:"]}${helm.name} | "
        "${languageMap["Chest:"]}${chest.name} | "
        "${languageMap["Gauntlet:"]}${gauntlet.name} | "
        "${languageMap["Leg:"]}${leg.name} | "
        "${languageMap["Weight:"]}${wgt.toStringAsFixed(2)}";
  }

  String getAttributes() {
    return "${languageMap["Weight:"]}${wgt.toStringAsFixed(2)}\n"
        "${languageMap["Phy.Abs."]}: ${phy.toStringAsFixed(2)}\n"
        "${languageMap["VSStr.Abs."]}: ${vSStr.toStringAsFixed(2)}\n"
        "${languageMap["VSSla.Abs."]}: ${vSSla.toStringAsFixed(2)}\n"
        "${languageMap["VSPie.Abs."]}: ${vSPie.toStringAsFixed(2)}\n"
        "${languageMap["Mag.Abs."]}: ${mag.toStringAsFixed(2)}\n"
        "${languageMap["Fir.Abs."]}: ${fir.toStringAsFixed(2)}\n"
        "${languageMap["Lit.Abs.1"]}: ${lit.toStringAsFixed(2)}\n"
        "${languageMap["Hol.Abs"]}: ${hol.toStringAsFixed(2)}\n"
        "${languageMap["Imm."]}: ${imm.toStringAsFixed(0)}\n"
        "${languageMap["Robu."]}: ${robu.toStringAsFixed(0)}\n"
        "${languageMap["Foc."]}: ${foc.toStringAsFixed(0)}\n"
        "${languageMap["Vita."]}: ${vita.toStringAsFixed(0)}\n"
        "${languageMap["Poi."]}: ${poi.toStringAsFixed(0)}\n";
  }
}

var helmdata = JsonData['helm'];
var chestdata = JsonData['chest'];
var legdata = JsonData['leg'];
var gauntletdata = JsonData['gauntlet'];
var armorNameData = JsonData['ArmorName'];

var ArmorFixList = {
  // Key:    Value
  'helm': 'nil',
  'chest': 'nil',
  'leg': 'nil',
  'gauntlet': 'nil'
};

List<String> HelmList = [];
List<String> ChestList = [];
List<String> LegList = [];
List<String> GauntletList = [];

final weightPercentInput = TextEditingController();
final maxWgtInput = TextEditingController();
final currentWgtInput = TextEditingController();
final tgtPoiInput = TextEditingController();
final minWgtInput = TextEditingController();

class PoiInputBox extends StatefulWidget {
  const PoiInputBox(Key? key) : super(key: key);

  @override
  State<PoiInputBox> createState() => _PoiInputBoxState();
}

class _PoiInputBoxState extends State<PoiInputBox> {
  String hint_Text = 'AVL In Mode.2';
  @override
  Widget build(BuildContext context) {
    return TextFormField(
      controller: tgtPoiInput,
      enabled: _poiInputEnable,
      textAlign: TextAlign.start,
      decoration: InputDecoration(
        contentPadding: const EdgeInsets.symmetric(vertical: 0, horizontal: 2),
        filled: true,
        fillColor: FvColors.edittext55Background,
        hintText: hint_Text,
        hintStyle: TextStyle(color: Color.fromARGB(255, 104, 104, 104)),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(3),
          borderSide: const BorderSide(style: BorderStyle.none, width: 0),
        ),
      ),
      style: const TextStyle(
          color: FvColors.button49FontColor,
          fontSize: 16,
          fontWeight: FontWeight.w400),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();
}

class WeightRadioButtonColum extends StatefulWidget {
  const WeightRadioButtonColum({Key? key}) : super(key: key);
  @override
  State<WeightRadioButtonColum> createState() => _WeightRadioButtonColumState();
}

class _WeightRadioButtonColumState extends State<WeightRadioButtonColum> {
  Key key = GlobalKey();
  int status = 1;
  bool flag = true;
  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        SizedBox(
          height: 25,
          width: 25,
          child: Transform.scale(
            scale: 0.9,
            child: Radio(
              value: 1,
              onChanged: (value) {
                setState(() {
                  this.status = 1;
                });
                print(this.status);
                wgtPercentStatue = status;
              },
              groupValue: status,
              activeColor: const Color.fromARGB(255, 153, 153, 153),
              materialTapTargetSize: MaterialTapTargetSize.padded,
            ),
          ),
        ),
        SizedBox(
          height: 25,
          width: 25,
          child: Transform.scale(
            scale: 0.9,
            child: Radio(
              value: 2,
              onChanged: (value) {
                setState(() {
                  status = 2;
                });
                print(this.status);
                wgtPercentStatue = status;
              },
              groupValue: status,
              activeColor: const Color.fromARGB(255, 153, 153, 153),
              materialTapTargetSize: MaterialTapTargetSize.padded,
            ),
          ),
        ),
        SizedBox(
          height: 25,
          width: 25,
          child: Transform.scale(
            scale: 0.9,
            child: Radio(
              value: 3,
              onChanged: (value) {
                setState(() {
                  status = 3;
                });
                print(this.status);
                wgtPercentStatue = status;
              },
              groupValue: status,
              activeColor: const Color.fromARGB(255, 153, 153, 153),
              materialTapTargetSize: MaterialTapTargetSize.padded,
            ),
          ),
        ),
      ],
    );
  }
}

class ArmorInputWidget extends StatelessWidget {
  const ArmorInputWidget({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
        width: 905,
        height: 86,
        child:
            Column(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
          SizedBox(
              width: 905,
              child: Text(
                languageMap["Armor Finder:"],
                overflow: TextOverflow.visible,
                textAlign: TextAlign.left,
                style: const TextStyle(
                    fontSize: 17,
                    fontWeight: FontWeight.w400,
                    color: FvColors.button49FontColor,
                    wordSpacing: 1.0),
              )),
          Row(mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [
            Stack(children: [
              SizedBox(
                width: 215,
                child: Text(
                  languageMap["Helm:"],
                  style: const TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.w400,
                      color: FvColors.button49FontColor,
                      wordSpacing: 1.0),
                ),
              ),
              Positioned(
                  top: -14,
                  left: 55,
                  child: Stack(children: [
                    Positioned(
                        left: 3,
                        top: 14,
                        child: Container(
                          height: 19,
                          width: 154,
                          color: FvColors.edittext55Background,
                        )),
                    SizedBox(
                        height: 35,
                        width: 160,
                        child: Transform.scale(
                            scale: 0.95,
                            child: (Autocomplete<String>(
                                key: const ValueKey("Helm"),
                                optionsBuilder:
                                    (TextEditingValue textEditingValue) {
                                  if (textEditingValue.text == '') {
                                    return const Iterable<String>.empty();
                                  }
                                  return HelmList.where((String option) {
                                    return option.toLowerCase().contains(
                                        textEditingValue.text.toLowerCase());
                                  });
                                },
                                onSelected: (String selection) {
                                  ArmorFixList["helm"] = selection;
                                  print('You just selected $selection');
                                  print(ArmorFixList["helm"]);
                                })))),
                  ]))
            ]),
            Stack(children: [
              SizedBox(
                width: 215,
                child: Text(
                  languageMap["Chest:"],
                  style: const TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.w400,
                      color: FvColors.button49FontColor,
                      wordSpacing: 1.0),
                ),
              ),
              Positioned(
                  top: -14,
                  left: 55,
                  child: Stack(children: [
                    Positioned(
                        left: 3,
                        top: 14,
                        child: Container(
                          height: 19,
                          width: 154,
                          color: FvColors.edittext55Background,
                        )),
                    SizedBox(
                        height: 35,
                        width: 160,
                        child: Transform.scale(
                            scale: 0.95,
                            child: (Autocomplete<String>(
                                key: const ValueKey("Chest"),
                                optionsBuilder:
                                    (TextEditingValue textEditingValue) {
                                  if (textEditingValue.text == '') {
                                    return const Iterable<String>.empty();
                                  }
                                  return ChestList.where((String option) {
                                    return option.toLowerCase().contains(
                                        textEditingValue.text.toLowerCase());
                                  });
                                },
                                onSelected: (String selection) {
                                  ArmorFixList["chest"] = selection;
                                  print('You just selected $selection');
                                  print(ArmorFixList["chest"]);
                                })))),
                  ]))
            ]),
            Stack(children: [
              SizedBox(
                width: 215,
                child: Text(
                  languageMap["Leg:"],
                  style: const TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.w400,
                      color: FvColors.button49FontColor,
                      wordSpacing: 1.0),
                ),
              ),
              Positioned(
                  top: -14,
                  left: 55,
                  child: Stack(children: [
                    Positioned(
                        left: 3,
                        top: 14,
                        child: Container(
                          height: 19,
                          width: 154,
                          color: FvColors.edittext55Background,
                        )),
                    SizedBox(
                        height: 35,
                        width: 160,
                        child: Transform.scale(
                            scale: 0.95,
                            child: (Autocomplete<String>(
                                key: const ValueKey("Leg"),
                                optionsBuilder:
                                    (TextEditingValue textEditingValue) {
                                  if (textEditingValue.text == '') {
                                    return const Iterable<String>.empty();
                                  }
                                  return LegList.where((String option) {
                                    return option.toLowerCase().contains(
                                        textEditingValue.text.toLowerCase());
                                  });
                                },
                                onSelected: (String selection) {
                                  ArmorFixList["leg"] = selection;
                                  debugPrint('You just selected $selection');
                                  print(ArmorFixList["leg"]);
                                })))),
                  ]))
            ]),
            Stack(children: [
              SizedBox(
                width: 215,
                child: Text(
                  languageMap["Gauntlet:"],
                  style: const TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.w400,
                      color: FvColors.button49FontColor,
                      wordSpacing: 1.0),
                ),
              ),
              Positioned(
                  top: -14,
                  left: 55,
                  child: Stack(children: [
                    Positioned(
                        left: 3,
                        top: 14,
                        child: Container(
                          height: 19,
                          width: 154,
                          color: FvColors.edittext55Background,
                        )),
                    SizedBox(
                        height: 35,
                        width: 160,
                        child: Transform.scale(
                            scale: 0.95,
                            child: (Autocomplete<String>(
                                key: const ValueKey("Gauntlet"),
                                optionsBuilder:
                                    (TextEditingValue textEditingValue) {
                                  if (textEditingValue.text == '') {
                                    return const Iterable<String>.empty();
                                  }
                                  return GauntletList.where((String option) {
                                    return option.toLowerCase().contains(
                                        textEditingValue.text.toLowerCase());
                                  });
                                },
                                onSelected: (String selection) {
                                  ArmorFixList["gauntlet"] = selection;
                                  debugPrint('You just selected $selection');
                                  print(ArmorFixList["gauntlet"]);
                                })))),
                  ]))
            ])
          ]),
        ]));
  }
}

class SortRadioWidget extends StatefulWidget {
  const SortRadioWidget({Key? key}) : super(key: key);

  @override
  State<SortRadioWidget> createState() => _SortRadioWidgetState();
}

class _SortRadioWidgetState extends State<SortRadioWidget> {
  static const List<String> absList = [
    "Phy.Abs.",
    "VSStr.Abs.",
    "VSSla.Abs.",
    "VSPie.Abs.",
    "Mag.Abs.",
    "Fir.Abs.",
    "Lit.Abs.",
    "Hol.Abs",
    "Imm.",
    "Robu.",
    "Foc.",
  ];
  String? groupValue1 = "Phy.Abs.";
  String status = '';
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceAround,
      children: [
        Column(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  SizedBox(
                      height: 25,
                      width: 25,
                      child: Transform.scale(
                          scale: 0.9,
                          child: Radio(
                            value: absList[0],
                            groupValue: groupValue1,
                            activeColor:
                                const Color.fromARGB(255, 153, 153, 153),
                            onChanged: (value) {
                              setState(() {
                                this.status = absList[0];
                              });
                              print(this.status);
                              sortMode = value as String?;
                              groupValue1 = value as String?;
                            },
                          ))),
                  Text(languageMap["Phy.Abs."])
                ],
              ),
              Row(
                children: [
                  SizedBox(
                      height: 25,
                      width: 25,
                      child: Transform.scale(
                          scale: 0.9,
                          child: Radio(
                            value: absList[1],
                            groupValue: groupValue1,
                            activeColor:
                                const Color.fromARGB(255, 153, 153, 153),
                            onChanged: (value) {
                              setState(() {
                                this.status = absList[1];
                              });
                              print(this.status);
                              sortMode = value as String?;
                              groupValue1 = value as String?;
                            },
                          ))),
                  Text(languageMap["VSStr.Abs."])
                ],
              ),
              Row(
                children: [
                  SizedBox(
                      height: 25,
                      width: 25,
                      child: Transform.scale(
                          scale: 0.9,
                          child: Radio(
                            value: absList[2],
                            groupValue: groupValue1,
                            activeColor:
                                const Color.fromARGB(255, 153, 153, 153),
                            onChanged: (value) {
                              setState(() {
                                this.status = absList[2];
                              });
                              print(this.status);
                              sortMode = value as String?;
                              groupValue1 = value as String?;
                            },
                          ))),
                  Text(languageMap["VSSla.Abs."])
                ],
              ),
              Row(
                children: [
                  SizedBox(
                      height: 25,
                      width: 25,
                      child: Transform.scale(
                          scale: 0.9,
                          child: Radio(
                            value: absList[3],
                            groupValue: groupValue1,
                            activeColor:
                                const Color.fromARGB(255, 153, 153, 153),
                            onChanged: (value) {
                              setState(() {
                                this.status = absList[3];
                              });
                              print(this.status);
                              sortMode = value as String?;
                              groupValue1 = value as String?;
                            },
                          ))),
                  Text(languageMap["VSPie.Abs."])
                ],
              ),
              Row(
                children: [
                  SizedBox(
                      height: 25,
                      width: 25,
                      child: Transform.scale(
                          scale: 0.9,
                          child: Radio(
                            value: absList[4],
                            groupValue: groupValue1,
                            activeColor:
                                const Color.fromARGB(255, 153, 153, 153),
                            onChanged: (value) {
                              setState(() {
                                this.status = absList[4];
                              });
                              print(this.status);
                              sortMode = value as String?;
                              groupValue1 = value as String?;
                            },
                          ))),
                  Text(languageMap["Mag.Abs."])
                ],
              ),
              Row(
                children: [
                  SizedBox(
                      height: 25,
                      width: 25,
                      child: Transform.scale(
                          scale: 0.9,
                          child: Radio(
                            value: absList[5],
                            groupValue: groupValue1,
                            activeColor:
                                const Color.fromARGB(255, 153, 153, 153),
                            onChanged: (value) {
                              setState(() {
                                this.status = absList[5];
                              });
                              print(this.status);
                              sortMode = value as String?;
                              groupValue1 = value as String?;
                            },
                          ))),
                  Text(languageMap["Fir.Abs."])
                ],
              ),
            ]),
        Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                SizedBox(
                    height: 25,
                    width: 25,
                    child: Transform.scale(
                        scale: 0.9,
                        child: Radio(
                          value: absList[6],
                          groupValue: groupValue1,
                          activeColor: const Color.fromARGB(255, 153, 153, 153),
                          onChanged: (value) {
                            setState(() {
                              this.status = absList[6];
                            });
                            print(this.status);
                            sortMode = value as String?;
                            groupValue1 = value as String?;
                          },
                        ))),
                Text(languageMap["Lit.Abs."])
              ],
            ),
            Row(
              children: [
                SizedBox(
                    height: 25,
                    width: 25,
                    child: Transform.scale(
                        scale: 0.9,
                        child: Radio(
                          value: absList[7],
                          groupValue: groupValue1,
                          activeColor: const Color.fromARGB(255, 153, 153, 153),
                          onChanged: (value) {
                            setState(() {
                              this.status = absList[7];
                            });
                            print(this.status);
                            sortMode = value as String?;
                            groupValue1 = value as String?;
                          },
                        ))),
                Text(languageMap["Hol.Abs"])
              ],
            ),
            Row(
              children: [
                SizedBox(
                    height: 25,
                    width: 25,
                    child: Transform.scale(
                        scale: 0.9,
                        child: Radio(
                          value: absList[8],
                          groupValue: groupValue1,
                          activeColor: const Color.fromARGB(255, 153, 153, 153),
                          onChanged: (value) {
                            setState(() {
                              this.status = absList[8];
                            });
                            print(this.status);
                            sortMode = value as String?;
                            groupValue1 = value as String?;
                          },
                        ))),
                Text(languageMap["Imm."])
              ],
            ),
            Row(
              children: [
                SizedBox(
                    height: 25,
                    width: 25,
                    child: Transform.scale(
                        scale: 0.9,
                        child: Radio(
                          value: absList[9],
                          groupValue: groupValue1,
                          activeColor: const Color.fromARGB(255, 153, 153, 153),
                          onChanged: (value) {
                            setState(() {
                              this.status = absList[9];
                            });
                            print(this.status);
                            sortMode = value as String?;
                            groupValue1 = value as String?;
                          },
                        ))),
                Text(languageMap["Robu."])
              ],
            ),
            Row(
              children: [
                SizedBox(
                    height: 25,
                    width: 25,
                    child: Transform.scale(
                        scale: 0.9,
                        child: Radio(
                          value: absList[10],
                          groupValue: groupValue1,
                          activeColor: const Color.fromARGB(255, 153, 153, 153),
                          onChanged: (value) {
                            setState(() {
                              this.status = absList[10];
                            });
                            print(this.status);
                            sortMode = value as String?;
                            groupValue1 = value as String?;
                          },
                        ))),
                Text(languageMap["Foc."])
              ],
            ),
            const SizedBox(
              height: 25,
              width: 25,
            )
          ],
        ),
      ],
    );
  }
}

class ModeSelectButton extends StatefulWidget {
  const ModeSelectButton({Key? key}) : super(key: key);

  @override
  State<ModeSelectButton> createState() => _ModeSelectButtonState();
}

class _ModeSelectButtonState extends State<ModeSelectButton> {
  static const Color deactiveColor = Color.fromRGBO(58, 45, 45, 1);
  static const Color activeColor = Color.fromRGBO(0, 193, 146, 1);
  static const Color deactiveTextColor = FvColors.button49FontColor;
  static const Color activeTextColor = Color.fromARGB(255, 255, 255, 255);
  List<Color> activeStatue = [activeColor, deactiveColor, deactiveColor];
  List<Color> activeTextStatue = [
    activeTextColor,
    deactiveTextColor,
    deactiveTextColor
  ];

  void pressButton(int index) {
    calculateMode = (index).toString();
    setState(() {
      for (int i = 0; i < 3; i++) {
        if (i == index - 1) {
          activeStatue[i] = activeColor;
          activeTextStatue[i] = activeTextColor;
        } else {
          activeStatue[i] = deactiveColor;
          activeTextStatue[i] = deactiveTextColor;
        }
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      alignment: Alignment.bottomLeft,
      child: Row(
        children: [
          SizedBox(
              width: 90,
              height: 40,
              child: TextButton(
                style: TextButton.styleFrom(
                  padding: EdgeInsets.zero,
                  backgroundColor: activeStatue[0],
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(0),
                    side: const BorderSide(
                      width: 0,
                      color: Colors.transparent,
                    ),
                  ),
                ),
                onPressed: () {
                  _poiInputEnable = false;
                  (_globalKey.currentState as _PoiInputBoxState).hint_Text =
                      'AVL In Mode.2';
                  (_globalKey.currentState as _PoiInputBoxState)
                      .setState(() {});
                  pressButton(1);
                },
                child: Text('Mode.1',
                    overflow: TextOverflow.visible,
                    style: TextStyle(
                      fontSize: 16,
                      color: activeTextStatue[0],
                      fontWeight: FontWeight.w400,
                    )),
              )),
          SizedBox(
              width: 90,
              height: 40,
              child: TextButton(
                style: TextButton.styleFrom(
                  padding: EdgeInsets.zero,
                  backgroundColor: activeStatue[1],
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(0),
                    side: const BorderSide(
                      width: 0,
                      color: Colors.transparent,
                    ),
                  ),
                ),
                onPressed: () {
                  _poiInputEnable = true;
                  (_globalKey.currentState as _PoiInputBoxState).hint_Text =
                      'Expected Poise';
                  (_globalKey.currentState as _PoiInputBoxState)
                      .setState(() {});
                  pressButton(2);
                },
                child: Text('Mode.2',
                    overflow: TextOverflow.visible,
                    style: TextStyle(
                      fontSize: 16,
                      color: activeTextStatue[1],
                      fontWeight: FontWeight.w400,
                    )),
              )),
          SizedBox(
              width: 90,
              height: 40,
              child: TextButton(
                style: TextButton.styleFrom(
                  padding: EdgeInsets.zero,
                  backgroundColor: activeStatue[2],
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(0),
                    side: const BorderSide(
                      width: 0,
                      color: Colors.transparent,
                    ),
                  ),
                ),
                onPressed: () {
                  _poiInputEnable = false;
                  (_globalKey.currentState as _PoiInputBoxState).hint_Text =
                      'AVL In Mode.2';
                  (_globalKey.currentState as _PoiInputBoxState)
                      .setState(() {});
                  pressButton(3);
                },
                child: Text('Mode.3',
                    overflow: TextOverflow.visible,
                    style: TextStyle(
                      fontSize: 16,
                      color: activeTextStatue[2],
                      fontWeight: FontWeight.w400,
                    )),
              )),
        ],
      ),
    );
  }
}

class _HomePageState extends State<HomePage> {
  String _selectedNode = "";
  late List<Node> _nodes;
  late TreeViewController _treeViewController;
  ExpanderPosition _expanderPosition = ExpanderPosition.start;
  ExpanderType _expanderType = ExpanderType.plusMinus;
  ExpanderModifier _expanderModifier = ExpanderModifier.none;
  bool docsOpen = true;
  bool deepExpanded = true;
  bool _allowParentSelect = false;
  bool _supportParentDoubleTap = false;
  late Map<double, List<ArmorSet>> armorSetSepreateByPoiseMap;

  void initState() {
    _nodes = [];
    _treeViewController = TreeViewController(
      children: _nodes,
      selectedKey: _selectedNode,
    );

    super.initState();
  }

  Widget build(BuildContext context) {
    double width = MediaQuery.of(context).size.width;
    double height = MediaQuery.of(context).size.height;

    TreeViewTheme _treeViewTheme = TreeViewTheme(
      expanderTheme: ExpanderThemeData(
          type: _expanderType,
          modifier: _expanderModifier,
          position: _expanderPosition,
          // color: Colors.grey.shade800,
          size: 20,
          color: const Color.fromARGB(255, 108, 130, 148)),
      labelStyle: const TextStyle(
        fontSize: 16,
        fontWeight: FontWeight.w400,
        color: FvColors.button49FontColor,
      ),
      parentLabelStyle: const TextStyle(
        fontSize: 16,
        fontWeight: FontWeight.w400,
        color: FvColors.button49FontColor,
      ),
      iconTheme: IconThemeData(
        size: 18,
        color: Colors.grey.shade800,
      ),
      colorScheme: Theme.of(context).colorScheme,
    );

    return Scaffold(
      backgroundColor: FvColors.container53Background,
      body: SizedBox(
        width: width,
        height: height,
        child: Stack(
          alignment: Alignment.center,
          clipBehavior: Clip.none,
          children: [
            SingleChildScrollView(
              scrollDirection: Axis.vertical,
              child: Stack(children: [
                const SizedBox(height: 566, width: 1425),
//-- Component frame_Container_3 --//
                Positioned(
                  left: 335,
                  top: 86,
                  child: Container(
                    width: 589,
                    height: 480,
                    decoration: BoxDecoration(
                      color: FvColors.container6Background,
                      borderRadius: BorderRadius.circular(0),
                    ),
                    child: Stack(
                        alignment: Alignment.center,
                        clipBehavior: Clip.none,
                        children: [
//-- Component Rectangle_Container_4 --//
                          Positioned(
                            left: 3,
                            top: 0,
                            child: Container(
                                width: 936,
                                height: 480,
                                decoration: BoxDecoration(
                                  color: FvColors.container6Background,
                                  borderRadius: BorderRadius.circular(0),
                                ),
                                alignment: Alignment.topCenter,
                                child: Column(children: [
                                  SizedBox(
                                      width: 910,
                                      height: 450,
                                      child: Card(
                                          color: FvColors.edittext55Background,
                                          child: TreeView(
                                            controller: _treeViewController,
                                            allowParentSelect:
                                                _allowParentSelect,
                                            supportParentDoubleTap:
                                                _supportParentDoubleTap,
                                            onExpansionChanged:
                                                (key, expanded) =>
                                                    _expandNode(key, expanded),
                                            onNodeTap: (key) {
                                              debugPrint('Selected: $key');
                                              showDialog(
                                                  context: context,
                                                  builder: (context) {
                                                    return AlertDialog(
                                                      title: Text("Details"),
                                                      content: Text(
                                                          getArmorSetDetails(
                                                              key)),
                                                    );
                                                  });
                                              setState(() {
                                                _selectedNode = key;
                                                _treeViewController =
                                                    _treeViewController
                                                        .copyWith(
                                                            selectedKey: key);
                                              });
                                            },
                                            theme: _treeViewTheme,
                                          ))),
                                  SizedBox(
                                      width: 905,
                                      child: OutlinedButton(
                                          onPressed: () {
                                            const url =
                                                "https://github.com/Acquity2/EldenRingArmorOptimizer";
                                            launch(url);
                                            print("PRESSED");
                                          },
                                          child: const Text(
                                              "https://github.com/Acquity2/EldenRingArmorOptimizer"))),
                                ])),
                          ),

//-- End Rectangle_Container_4 --//
//-- Component Rectangle_Container_5 --//
                          Positioned(
                            left: 0,
                            top: 0,
                            child: Container(
                              width: 3,
                              height: 480,
                              decoration: BoxDecoration(
                                color: FvColors.container42Background,
                                borderRadius: BorderRadius.circular(0),
                              ),
                            ),
                          ),

//-- End Rectangle_Container_5 --//
                        ]),
                  ),
                ),

//-- End frame_Container_3 --//
//-- Component frame_Container_6 --//
                Positioned(
                  left: 335,
                  top: 0,
                  child: Container(
                    width: 939,
                    height: 86,
                    decoration: BoxDecoration(
                      color: FvColors.container6Background,
                      borderRadius: BorderRadius.circular(0),
                    ),
                    child: Stack(
                        alignment: Alignment.center,
                        clipBehavior: Clip.none,
                        children: [
//-- Component Rectangle_Container_7 --//
                          Positioned(
                            left: 0,
                            top: 0,
                            child: Container(
                              width: 589,
                              height: 86,
                              decoration: BoxDecoration(
                                color: FvColors.container6Background,
                                borderRadius: BorderRadius.circular(0),
                              ),
                            ),
                          ),

//-- End Rectangle_Container_7 --//
//-- Component Rectangle_Container_8 --//
                          Positioned(
                            left: 18,
                            top: 83,
                            child: Container(
                              width: 905,
                              height: 3,
                              decoration: BoxDecoration(
                                color: FvColors.container42Background,
                                borderRadius: BorderRadius.circular(1),
                              ),
                            ),
                          ),

//-- End Rectangle_Container_8 --//
                          const Positioned(
                            left: 17,
                            top: 0,
                            child: ArmorInputWidget(),
                          ),

//-- Component Rectangle_Container_20 --//
                          Positioned(
                            left: 0,
                            top: 0,
                            child: Container(
                              width: 3,
                              height: 86,
                              decoration: BoxDecoration(
                                color: FvColors.container42Background,
                                borderRadius: BorderRadius.circular(0),
                              ),
                            ),
                          ),

//-- End Rectangle_Container_20 --//
                        ]),
                  ),
                ),

//-- End frame_Container_6 --//
//-- Component frame_Container_21 --//
                Positioned(
                  left: 0,
                  top: 181,
                  child: Container(
                    width: 336,
                    height: 385,
                    decoration: BoxDecoration(
                      color: FvColors.container53Background,
                      borderRadius: BorderRadius.circular(0),
                    ),
                    child: Stack(
                        alignment: Alignment.center,
                        clipBehavior: Clip.none,
                        children: [
//-- Component Rectangle_Container_22 --//
                          Positioned(
                            left: 0,
                            top: 0,
                            child: Container(
                              width: 336,
                              height: 385,
                              decoration: BoxDecoration(
                                color: FvColors.container53Background,
                                borderRadius: BorderRadius.circular(0),
                              ),
                            ),
                          ),

//-- End Rectangle_Container_22 --//
//-- Component Rectangle_Container_23 --//
                          Positioned(
                            left: 12,
                            top: 121,
                            child: Container(
                              width: 305,
                              height: 3,
                              decoration: BoxDecoration(
                                color: FvColors.container42Background,
                                borderRadius: BorderRadius.circular(1),
                              ),
                            ),
                          ),

//-- End Rectangle_Container_23 --//
//-- Component TextBox_Container_24 Max weight input--//

                          Positioned(
                              left: 100,
                              top: 12,
                              child: SizedBox(
                                  width: 217,
                                  height: 23,
                                  child: TextFormField(
                                    key: const ValueKey(1),
                                    controller: maxWgtInput,
                                    textAlign: TextAlign.start,
                                    decoration: InputDecoration(
                                      contentPadding:
                                          const EdgeInsets.symmetric(
                                              vertical: 0, horizontal: 2),
                                      filled: true,
                                      fillColor: FvColors.edittext55Background,
                                      hintText: 'Upper Weight Limit',
                                      hintStyle: const TextStyle(
                                          color: Color.fromARGB(
                                              255, 104, 104, 104)),
                                      border: OutlineInputBorder(
                                        borderRadius: BorderRadius.circular(3),
                                        borderSide: const BorderSide(
                                            style: BorderStyle.none, width: 0),
                                      ),
                                    ),
                                    style: const TextStyle(
                                        color: FvColors.button49FontColor,
                                        fontSize: 16,
                                        fontWeight: FontWeight.w400),
                                  ))),
//-- End TextBox_Container_24 --//
//-- Component Text_TextView_25 --//
                          Positioned(
                              left: 12,
                              top: 12,
                              child: Text(
                                languageMap["MAX. Wgt.:"],
                                overflow: TextOverflow.visible,
                                textAlign: TextAlign.left,
                                style: const TextStyle(
                                    fontSize: 16,
                                    fontWeight: FontWeight.w400,
                                    backgroundColor:
                                        FvColors.scrollcontainer2Background,
                                    color: FvColors.button49FontColor,
                                    wordSpacing: 1.0),
                              )),
//-- End Text_TextView_25 --//
//-- Component TextBox_Container_26   target poise input--//

                          Positioned(
                              left: 100,
                              top: 87,
                              child: SizedBox(
                                  width: 217,
                                  height: 23,
                                  child: TextFormField(
                                    key: const ValueKey(2),
                                    controller: minWgtInput,
                                    textAlign: TextAlign.start,
                                    decoration: InputDecoration(
                                      contentPadding:
                                          const EdgeInsets.symmetric(
                                              vertical: 0, horizontal: 2),
                                      filled: true,
                                      fillColor: FvColors.edittext55Background,
                                      hintText: 'Def:90%->Mode.1 60%->Mode.3',
                                      hintStyle: const TextStyle(
                                          color: Color.fromARGB(
                                              255, 104, 104, 104)),
                                      border: OutlineInputBorder(
                                        borderRadius: BorderRadius.circular(3),
                                        borderSide: const BorderSide(
                                            style: BorderStyle.none, width: 0),
                                      ),
                                    ),
                                    style: const TextStyle(
                                        color: FvColors.button49FontColor,
                                        fontSize: 16,
                                        fontWeight: FontWeight.w400),
                                  ))),
//-- End TextBox_Container_26 --//
//-- Component Text_TextView_27 --//
                          Positioned(
                              left: 12,
                              top: 87,
                              child: Text(
                                languageMap["Min. Wgt.:"],
                                overflow: TextOverflow.visible,
                                textAlign: TextAlign.left,
                                style: const TextStyle(
                                    fontSize: 16,
                                    fontWeight: FontWeight.w400,
                                    color: FvColors.button49FontColor,
                                    wordSpacing: 1.0),
                              )),
//-- End Text_TextView_27 --//
//-- Component TextBox_Container_28 current weight input--//

                          Positioned(
                              left: 100,
                              top: 37,
                              child: SizedBox(
                                  width: 217,
                                  height: 23,
                                  child: TextFormField(
                                    key: const ValueKey(3),
                                    controller: currentWgtInput,
                                    textAlign: TextAlign.start,
                                    decoration: InputDecoration(
                                      contentPadding:
                                          const EdgeInsets.symmetric(
                                              vertical: 0, horizontal: 2),
                                      filled: true,
                                      fillColor: FvColors.edittext55Background,
                                      hintText: 'Max Weight Without Armor',
                                      hintStyle: const TextStyle(
                                          color: Color.fromARGB(
                                              255, 104, 104, 104)),
                                      border: OutlineInputBorder(
                                        borderRadius: BorderRadius.circular(3),
                                        borderSide: const BorderSide(
                                            style: BorderStyle.none, width: 0),
                                      ),
                                    ),
                                    style: const TextStyle(
                                        color: FvColors.button49FontColor,
                                        fontSize: 16,
                                        fontWeight: FontWeight.w400),
                                  ))),
//-- End TextBox_Container_28 --//
//-- Component Text_TextView_29 --//
                          Positioned(
                              left: 12,
                              top: 37,
                              child: Text(
                                languageMap["Current Wgt.:"],
                                overflow: TextOverflow.visible,
                                textAlign: TextAlign.left,
                                style: const TextStyle(
                                    fontSize: 16,
                                    fontWeight: FontWeight.w400,
                                    color: FvColors.button49FontColor,
                                    wordSpacing: 1.0),
                              )),
//-- End Text_TextView_29 --//
//-- Component TextBox_Container_30 min weight input--//

                          Positioned(
                              left: 100,
                              top: 62,
                              child: Row(children: [
                                SizedBox(
                                  width: 110,
                                  height: 23,
                                  child: PoiInputBox(_globalKey),
                                ),
                                SizedBox(
                                    width: 23,
                                    height: 23,
                                    child: Checkbox(
                                        value: _wearGoat,
                                        activeColor: FvColors.button49FontColor,
                                        onChanged: (value) {
                                          setState(() {
                                            _wearGoat = value!;
                                            print(_wearGoat);
                                          });
                                        })),
                                SizedBox(
                                  width: 100,
                                  height: 24,
                                  child: Text(
                                    languageMap["Goat Tail"],
                                    style: const TextStyle(
                                        fontSize: 16,
                                        fontWeight: FontWeight.w400,
                                        color: FvColors.button49FontColor,
                                        wordSpacing: 1.0),
                                  ),
                                )
                              ])),
//-- End TextBox_Container_30 --//
//-- Component Text_TextView_31 --//
                          Positioned(
                              left: 12,
                              top: 62,
                              child: Text(
                                languageMap["Tgt.Poi.:"],
                                overflow: TextOverflow.visible,
                                textAlign: TextAlign.left,
                                style: const TextStyle(
                                    fontSize: 16,
                                    fontWeight: FontWeight.w400,
                                    color: FvColors.button49FontColor,
                                    wordSpacing: 1.0),
                              )),
//-- End Text_TextView_31 --//
//-- Component SortBy_TextView_32 --//
                          Positioned(
                              left: 12,
                              top: 135,
                              child: Text(
                                languageMap["Sort By"],
                                overflow: TextOverflow.visible,
                                textAlign: TextAlign.left,
                                style: const TextStyle(
                                    fontSize: 16,
                                    fontWeight: FontWeight.w400,
                                    color: FvColors.button49FontColor,
                                    wordSpacing: 1.0),
                              )),
//-- End SortBy_TextView_32 --//
//-- Component Image_Container_33 --//
                          Positioned(
                            left: 12,
                            top: 165,
                            child: Container(
                              width: 305,
                              height: 168,
                              decoration: BoxDecoration(
                                color: FvColors.edittext55Background,
                                borderRadius: BorderRadius.circular(9),
                              ),
                              child: const SortRadioWidget(),
                            ),
                          ),

//-- End Image_Container_33 --//
//-- Component Calculatebutton_Container_34 --//
                          Positioned(
                              left: 12,
                              top: 347,
                              child: SizedBox(
                                  width: 212,
                                  height: 24,
                                  child: TextButton(
                                    style: TextButton.styleFrom(
                                      padding: EdgeInsets.zero,
                                      backgroundColor:
                                          FvColors.button34Background,
                                      shape: RoundedRectangleBorder(
                                        borderRadius: BorderRadius.circular(2),
                                        side: const BorderSide(
                                          width: 0,
                                          color: Colors.transparent,
                                        ),
                                      ),
                                    ),
                                    onPressed: () {
                                      setState(() {
                                        calculateMain();
                                      });
                                    },
                                    child: Text(languageMap['Calculate'],
                                        overflow: TextOverflow.visible,
                                        style: const TextStyle(
                                          fontSize: 16,
                                          color: FvColors.button37FontColor,
                                          fontWeight: FontWeight.w400,
                                        )),
                                  ))),
//-- End Calculatebutton_Container_34 --//
//-- Component ReSortbutton_Container_37 --//
                          Positioned(
                              left: 240,
                              top: 347,
                              child: SizedBox(
                                  width: 77,
                                  height: 24,
                                  child: TextButton(
                                    style: TextButton.styleFrom(
                                      padding: EdgeInsets.zero,
                                      backgroundColor:
                                          FvColors.button37Background,
                                      shape: RoundedRectangleBorder(
                                        borderRadius: BorderRadius.circular(2),
                                        side: const BorderSide(
                                          width: 0,
                                          color: Colors.transparent,
                                        ),
                                      ),
                                    ),
                                    onPressed: () {
                                      setState(() {
                                        resultReSort();
                                      });
                                    },
                                    child: Text(languageMap['ReSort'],
                                        overflow: TextOverflow.visible,
                                        style: const TextStyle(
                                          fontSize: 16,
                                          color: FvColors.button37FontColor,
                                          fontWeight: FontWeight.w400,
                                        )),
                                  ))),
//-- End ReSortbutton_Container_37 --//
                        ]),
                  ),
                ),

//-- End frame_Container_21 --//
//-- Component frame_Container_40 --//
                Positioned(
                  left: 0,
                  top: 0,
                  child: Container(
                    width: 336,
                    height: 181,
                    decoration: BoxDecoration(
                      color: FvColors.container53Background,
                      borderRadius: BorderRadius.circular(0),
                    ),
                    child: Stack(
                        alignment: Alignment.center,
                        clipBehavior: Clip.none,
                        children: [
//-- Component Rectangle_Container_41 --//
                          Positioned(
                            left: 0,
                            top: 0,
                            child: Container(
                              width: 336,
                              height: 181,
                              decoration: BoxDecoration(
                                color: FvColors.container53Background,
                                borderRadius: BorderRadius.circular(0),
                              ),
                            ),
                          ),

//-- End Rectangle_Container_41 --//
//-- Component Rectangle_Container_42 --//
                          Positioned(
                            left: 12,
                            top: 178,
                            child: Container(
                              width: 305,
                              height: 3,
                              decoration: BoxDecoration(
                                color: FvColors.container42Background,
                                borderRadius: BorderRadius.circular(1),
                              ),
                            ),
                          ),

//-- End Rectangle_Container_42 --//
//-- Component ARMOROPTIMIZER_TextView_43 --//
                          const Positioned(
                              left: 5,
                              top: 41,
                              child: SizedBox(
                                  child: Text(
                                "ARMOR OPTIMIZER",
                                overflow: TextOverflow.visible,
                                textAlign: TextAlign.left,
                                style: TextStyle(
                                    fontSize: 24,
                                    fontWeight: FontWeight.w400,
                                    backgroundColor:
                                        FvColors.scrollcontainer2Background,
                                    color: FvColors.textview44FontColor,
                                    wordSpacing: 1.0),
                              ))),
//-- End ARMOROPTIMIZER_TextView_43 --//
//-- Component DesignforEldenRing_TextView_44 --//
                          const Positioned(
                              left: 5,
                              top: 71,
                              child: Text(
                                "Design for Elden Ring",
                                overflow: TextOverflow.visible,
                                textAlign: TextAlign.left,
                                style: TextStyle(
                                    fontSize: 14,
                                    fontWeight: FontWeight.w400,
                                    color: FvColors.textview44FontColor,
                                    wordSpacing: 1.0),
                              )),
//-- End DesignforEldenRing_TextView_44 --//
//-- Component Rectangle_Container_45 --//
                          Positioned(
                            left: 5,
                            top: 68,
                            child: Container(
                              width: 60,
                              height: 2,
                              decoration: BoxDecoration(
                                color: FvColors.container48Background,
                                borderRadius: BorderRadius.circular(1),
                              ),
                            ),
                          ),

//-- End Rectangle_Container_45 --//

                          Positioned(
                              left: 65, top: 0, child: ModeSelectButton()),

//-- Component debugbutton_Container_48 --//
                          Positioned(
                            left: 0,
                            top: 0,
                            child: SizedBox(
                              width: 66,
                              height: 40,
                              child: TextButton(
                                style: TextButton.styleFrom(
                                  padding: EdgeInsets.zero,
                                  backgroundColor:
                                      FvColors.container48Background,
                                  shape: RoundedRectangleBorder(
                                    borderRadius: BorderRadius.circular(0),
                                    side: const BorderSide(
                                      width: 1,
                                      color: Color.fromARGB(88, 0, 166, 196),
                                    ),
                                  ),
                                ),
                                onPressed: () => {
                                  setState(() {
                                    for (var Elements
                                        in _treeViewController.children) {
                                      _treeViewController = TreeViewController(
                                          children: _treeViewController
                                              .deleteNode(Elements.key));
                                    }
                                    debugButton();

                                    //  _treeViewController =
                                    //      TreeViewController(children: testnodes);
                                  })

                                  //futureArmorNameMap
                                  //    .then((value) => {print(value)}),
                                },
                                child: const Text('',
                                    overflow: TextOverflow.visible,
                                    style: TextStyle(
                                      fontSize: 16,
                                      color: FvColors.button49FontColor,
                                      fontWeight: FontWeight.w400,
                                    )),
                              ),
                            ),
                          ),

//-- End debugbutton_Container_48 --//

//-- Component Rectangle_Container_50 --//
                          Positioned(
                            left: 244,
                            top: 2,
                            child: Container(
                              width: 2,
                              height: 36,
                              decoration: BoxDecoration(
                                color: FvColors.container52Background,
                                borderRadius: BorderRadius.circular(2),
                              ),
                            ),
                          ),

//-- End Rectangle_Container_50 --//
//-- Component Rectangle_Container_51 --//
                          Positioned(
                            left: 154,
                            top: 2,
                            child: Container(
                              width: 2,
                              height: 36,
                              decoration: BoxDecoration(
                                color: FvColors.container52Background,
                                borderRadius: BorderRadius.circular(2),
                              ),
                            ),
                          ),

//-- End Rectangle_Container_51 --//
//-- Component Rectangle_Container_52 --//
                          Positioned(
                            left: 64,
                            top: 2,
                            child: Container(
                              width: 2,
                              height: 36,
                              decoration: BoxDecoration(
                                color: FvColors.container52Background,
                                borderRadius: BorderRadius.circular(2),
                              ),
                            ),
                          ),

//-- End Rectangle_Container_52 --//
                        ]),
                  ),
                ),

//-- End frame_Container_40 --//
//-- Component frame_Container_53 --//
                Positioned(
                  left: 12,
                  top: 91,
                  child: Container(
                    width: 305,
                    height: 81,
                    decoration: BoxDecoration(
                      color: FvColors.container53Background,
                      borderRadius: BorderRadius.circular(0),
                    ),
                    child: Stack(
                        alignment: Alignment.center,
                        clipBehavior: Clip.none,
                        children: [
//-- Component Rectangle_Container_54 --//
                          Positioned(
                            left: 0,
                            top: 0,
                            child: Container(
                              width: 305,
                              height: 81,
                              decoration: BoxDecoration(
                                color: FvColors.container53Background,
                                borderRadius: BorderRadius.circular(0),
                              ),
                              child: Stack(children: [
                                const Positioned(
                                  left: 0,
                                  top: 4,
                                  child: WeightRadioButtonColum(),
                                ),
                                Positioned(
                                    left: 30,
                                    top: 6,
                                    child: Column(
                                      mainAxisAlignment:
                                          MainAxisAlignment.center,
                                      children: [
                                        SizedBox(
                                          height: 25,
                                          width: 300,
                                          child: Text(
                                            languageMap["Up to 70% Burdern"],
                                            style: const TextStyle(
                                              fontSize: 16,
                                              color: FvColors.button49FontColor,
                                              fontWeight: FontWeight.w400,
                                            ),
                                          ),
                                        ),
                                        SizedBox(
                                          height: 25,
                                          width: 300,
                                          child: Text(
                                            languageMap["Up to 30% Burdern"],
                                            style: const TextStyle(
                                              fontSize: 16,
                                              color: FvColors.button49FontColor,
                                              fontWeight: FontWeight.w400,
                                            ),
                                          ),
                                        ),
                                        SizedBox(
                                          height: 25,
                                          width: 300,
                                          child: Text(
                                            languageMap[
                                                "Up to                      % Burdern"],
                                            style: const TextStyle(
                                              fontSize: 16,
                                              color: FvColors.button49FontColor,
                                              fontWeight: FontWeight.w400,
                                            ),
                                          ),
                                        ),
                                      ],
                                    )),
                              ]),
                            ),
                          ),

//-- End Rectangle_Container_54 --//
//-- Component TextBox_Container_55 --//

                          Positioned(
                              left: 70,
                              top: 58,
                              child: SizedBox(
                                  width: 63,
                                  height: 20,
                                  child: TextFormField(
                                    controller: weightPercentInput,
                                    textAlign: TextAlign.start,
                                    decoration: InputDecoration(
                                      contentPadding:
                                          const EdgeInsets.symmetric(
                                              vertical: -3, horizontal: 2),
                                      filled: true,
                                      fillColor: FvColors.edittext55Background,
                                      hintText: ' ',
                                      hintStyle: const TextStyle(
                                          color: FvColors.button49FontColor),
                                      border: OutlineInputBorder(
                                        borderRadius: BorderRadius.circular(3),
                                        borderSide: const BorderSide(
                                            style: BorderStyle.none, width: 0),
                                      ),
                                    ),
                                    style: const TextStyle(
                                        color: FvColors.button49FontColor,
                                        fontSize: 16,
                                        fontWeight: FontWeight.w400),
                                  ))),
//-- End TextBox_Container_55 --//
                        ]),
                  ),
                ),

//-- End frame_Container_53 --//
              ]),
            ),
//-- Component ScrollContainer --//
//-- End ScrollContainer --//
          ],
        ),
      ),
    );
  }

  _expandNode(String key, bool expanded) {
    String msg = '${expanded ? "Expanded" : "Collapsed"}: $key';
    debugPrint(msg);
    Node? node = _treeViewController.getNode(key);
    if (node != null) {
      List<Node> updated;
      if (key == 'docs') {
        updated = _treeViewController.updateNode(
            key,
            node.copyWith(
              expanded: expanded,
              icon: expanded ? Icons.folder_open : Icons.folder,
            ));
      } else {
        updated = _treeViewController.updateNode(
            key, node.copyWith(expanded: expanded));
      }
      setState(() {
        if (key == 'docs') docsOpen = expanded;
        _treeViewController = _treeViewController.copyWith(children: updated);
      });
    }
  }

  Map<double, List<ArmorSet>> deepCopyMap(Map<double, List<ArmorSet>> map) {
    Map<double, List<ArmorSet>> newMap = {};
    for (double key in map.keys) {
      newMap[key] = List.from(map[key]!);
    }
    return newMap;
  }

  calculateMode1() {
    List<ArmorSet> armorSetList = fixWeightFindMaxPoise();
    if (armorSetList.length == 0) {
      showDialog(
          context: context,
          builder: (context) {
            return AlertDialog(
              title: Text(languageMap["Alert!"]),
              content: Text(languageMap["No armor set found!"]),
            );
          });
      return;
    }
    armorSetSepreateByPoiseMap = sepreateByPoi(armorSetList);
    Map<double, List<ArmorSet>> _armorSetSepreateByPoiseMap =
        deepCopyMap(armorSetSepreateByPoiseMap);
    for (double key in _armorSetSepreateByPoiseMap.keys) {
      _armorSetSepreateByPoiseMap[key] =
          armorSetListSort(_armorSetSepreateByPoiseMap[key]!, sortMode!);
    }
    _armorSetSepreateByPoiseMap.forEach((key, value) {
      while (value.length > 10) {
        value.removeLast();
      }
    });
    List<Node> nodes = convertToNodes(_armorSetSepreateByPoiseMap);
    _treeViewController = TreeViewController(children: nodes);
  }

  calculateMode2() {
    List<ArmorSet> armorSetList = fixWeightPoiseFindMaxAbs();
    if (armorSetList.length == 0) {
      showDialog(
          context: context,
          builder: (context) {
            return AlertDialog(
              title: Text(languageMap["Alert!"]),
              content: Text(languageMap["No armor set found!"]),
            );
          });
      return;
    }
    armorSetSepreateByPoiseMap = sepreateByPoi(armorSetList);
    Map<double, List<ArmorSet>> _armorSetSepreateByPoiseMap =
        deepCopyMap(armorSetSepreateByPoiseMap);
    for (double key in _armorSetSepreateByPoiseMap.keys) {
      _armorSetSepreateByPoiseMap[key] =
          armorSetListSort(_armorSetSepreateByPoiseMap[key]!, sortMode!);
    }
    _armorSetSepreateByPoiseMap.forEach((key, value) {
      while (value.length > 20) {
        value.removeLast();
      }
    });
    List<Node> nodes = convertToNodes(_armorSetSepreateByPoiseMap);

    _treeViewController = TreeViewController(children: nodes);
  }

  calculateMode3() {
    List<ArmorSet> armorSetList = fixWeightFindMaxAbs();
    if (armorSetList.length == 0) {
      showDialog(
          context: context,
          builder: (context) {
            return AlertDialog(
              title: Text(languageMap["Alert!"]),
              content: Text(languageMap["No armor set found!"]),
            );
          });
      return;
    }
    armorSetSepreateByPoiseMap = {-1: armorSetList};
    Map<double, List<ArmorSet>> _armorSetSepreateByPoiseMap =
        deepCopyMap(armorSetSepreateByPoiseMap);
    _armorSetSepreateByPoiseMap.forEach((key, value) {
      while (value.length > 30) {
        value.removeLast();
      }
    });
    List<Node> nodes = convertToNodes(_armorSetSepreateByPoiseMap);
    _treeViewController = TreeViewController(children: nodes);
  }

  resultReSort() {
    Map<double, List<ArmorSet>> _armorSetSepreateByPoiseMap =
        deepCopyMap(armorSetSepreateByPoiseMap);
    for (double key in _armorSetSepreateByPoiseMap.keys) {
      _armorSetSepreateByPoiseMap[key] =
          armorSetListSort(_armorSetSepreateByPoiseMap[key]!, sortMode!);
    }
    _armorSetSepreateByPoiseMap.forEach((key, value) {
      while (value.length > 10) {
        value.removeLast();
      }
    });
    List<Node> nodes = convertToNodes(_armorSetSepreateByPoiseMap);
    _treeViewController = TreeViewController(children: nodes);
  }

  calculateMain() {
    if (calculateMode == "1") {
      calculateMode1();
    } else if (calculateMode == "2") {
      calculateMode2();
    } else if (calculateMode == "3") {
      calculateMode3();
    }
  }

  void debugButton() {
    //print(69.75 ~/ 1 + 1);
    //print((double.parse(tgtPoiInput.text) / 4 * 3) ~/ 1 + 1);
    //  print('debug button pressed');
    //  print(weightPercentInput.text);
    //  print(wgtPercentStatue);
    //  print("minwgt " + minWgtInput.text);
    //  print("maxwgt " + maxWgtInput.text);
    //  print("tgtpoi " + tgtPoiInput.text);
    //  print("crtwgt " + currentWgtInput.text);
    //  print(ArmorFixList);
    //print(calculateMode);
    //print(sortMode);
    //  print(calculateAvilableWeight());
    //  List<ArmorSet> testList = fixWeightFindMaxPoise();
    //  Map<double, List<ArmorSet>> testSepreateByPoiseMap =
    //      sepreateByPoi(testList);
    //  for (double key in testSepreateByPoiseMap.keys) {
    //    testSepreateByPoiseMap[key] =
    //        armorSetListSort(testSepreateByPoiseMap[key]!, sortMode!);
    //  }
    //  testSepreateByPoiseMap.forEach((key, value) {
    //    while (value.length > 10) {
    //      value.removeLast();
    //    }
    //  });
    //  testSepreateByPoiseMap.forEach((key, value) {
    //    print(key.toString() + "  " + value.length.toString());
    //  });
    //  List<Node> nodes = convertToNodes(testSepreateByPoiseMap);
    //  _treeViewController = TreeViewController(children: nodes);
  }

  Map<String, int> getArmorFixID(Map armorFixNameList, ArmorData armorData) {
    Map<String, int> armorFixIDMap = {};
    if (armorFixNameList["helm"] == "nil") {
      armorFixIDMap["helm"] = -1;
    } else {
      armorFixIDMap["helm"] = armorData.helms
          .indexWhere((element) => element.name == armorFixNameList["helm"]);
    }
    if (armorFixNameList["chest"] == "nil") {
      armorFixIDMap["chest"] = -1;
    } else {
      armorFixIDMap["chest"] = armorData.chests
          .indexWhere((element) => element.name == armorFixNameList["chest"]);
    }
    //leg
    if (armorFixNameList["leg"] == "nil") {
      armorFixIDMap["leg"] = -1;
    } else {
      armorFixIDMap["leg"] = armorData.legs
          .indexWhere((element) => element.name == armorFixNameList["leg"]);
    }
    //gauntlets
    if (armorFixNameList["gauntlet"] == "nil") {
      armorFixIDMap["gauntlet"] = -1;
    } else {
      armorFixIDMap["gauntlet"] = armorData.gauntlets.indexWhere(
          (element) => element.name == armorFixNameList["gauntlet"]);
    }

    return armorFixIDMap;
  }

  double calculateAvilableWeight() {
    double availableWeight = 0;
    if (maxWgtInput.text == "" || currentWgtInput.text == "") {
      return -1;
    }
    if (wgtPercentStatue == 1) {
      availableWeight = double.parse(maxWgtInput.text) * 0.695 -
          double.parse(currentWgtInput.text);
    } else if (wgtPercentStatue == 2) {
      availableWeight = double.parse(maxWgtInput.text) * 0.295 -
          double.parse(currentWgtInput.text);
    } else if (wgtPercentStatue == 3) {
      availableWeight = double.parse(maxWgtInput.text) *
              double.parse(weightPercentInput.text) /
              100 -
          double.parse(currentWgtInput.text);
    }
    return availableWeight;
  }

  List<ArmorSet> armorSetListSort(List<ArmorSet> armorSetList, String sortID) {
    List<ArmorSet> tmpList = armorSetList;
    if (sortID == "Poi") {
      //sort tmpList by element.poi
      tmpList.sort((a, b) => b.poi.compareTo(a.poi));
    } else if (sortID == "Phy.Abs.") {
      tmpList.sort((a, b) => b.phy.compareTo(a.phy));
    } else if (sortID == "VSStr.Abs.") {
      tmpList.sort((a, b) => b.vSStr.compareTo(a.vSStr));
    } else if (sortID == "VSSla.Abs.") {
      tmpList.sort((a, b) => b.vSSla.compareTo(a.vSSla));
    } else if (sortID == "VSPie.Abs.") {
      tmpList.sort((a, b) => b.vSPie.compareTo(a.vSPie));
    } else if (sortID == "Mag.Abs") {
      tmpList.sort((a, b) => b.mag.compareTo(a.mag));
    } else if (sortID == "Fir.Abs.") {
      tmpList.sort((a, b) => b.fir.compareTo(a.fir));
    } else if (sortID == "Lit.Abs.") {
      tmpList.sort((a, b) => b.lit.compareTo(a.lit));
    } else if (sortID == "Hol.Abs.") {
      tmpList.sort((a, b) => b.hol.compareTo(a.hol));
    } else if (sortID == "Imm.") {
      tmpList.sort((a, b) => b.imm.compareTo(a.imm));
    } else if (sortID == "Robu.") {
      tmpList.sort((a, b) => b.robu.compareTo(a.robu));
    } else if (sortID == "Foc.") {
      tmpList.sort((a, b) => b.foc.compareTo(a.foc));
    }
    return tmpList;
  }

  Map<double, List<ArmorSet>> sepreateByPoi(List<ArmorSet> armorSetList) {
    Map<double, List<ArmorSet>> seperateByPoi = {};
    double initPoi = armorSetList[0].poi;
    seperateByPoi[initPoi] = [];
    //seperateByPoi[initPoi]!.add(armorSetList[0]);
    int count = 1;
    for (int i = 0; i < armorSetList.length; i++) {
      if (armorSetList[i].poi == initPoi) {
        seperateByPoi[armorSetList[i].poi]!.add(armorSetList[i]);
      } else {
        count += 1;
        if (count > 16) {
          break;
        }
        initPoi = armorSetList[i].poi;
        seperateByPoi[armorSetList[i].poi] = [];
        seperateByPoi[armorSetList[i].poi]!.add(armorSetList[i]);
      }
    }
    return seperateByPoi;
  }

  List<ArmorSet> fixWeightFindMaxPoise() {
    double avilableWeight = calculateAvilableWeight();
    if (avilableWeight == -1) {
      nullInputAlert(context);
      throw Error();
    }
    double minWgtPercent = 0;
    if (minWgtInput.text == "") {
      minWgtPercent = 0.90;
    } else {
      minWgtPercent = double.parse(minWgtInput.text) / 100;
    }
    armorData.SortbyPoiPerWgt();
    List<ArmorSet> armorSetList = [];
    Map ArmorSetID = getArmorFixID(ArmorFixList, armorData);
    int key = 0;
    int limit = 200000;
    double tmpWeight = 0;
    for (int ic = 0; ic < armorData.chests.length; ic++) {
      if (ArmorSetID["chest"] != -1 && ic != ArmorSetID["chest"]) {
        continue;
      }
      tmpWeight = armorData.chests[ic].wgt;
      if (tmpWeight > avilableWeight) {
        continue;
      }
      for (int il = 0; il < armorData.legs.length; il++) {
        if (ArmorSetID["leg"] != -1 && il != ArmorSetID["leg"]) {
          continue;
        }

        if (armorData.chests[ic].wgt + armorData.legs[il].wgt >
            avilableWeight) {
          continue;
        }
        for (int ih = 0; ih < armorData.helms.length; ih++) {
          if (ArmorSetID["helm"] != -1 && ih != ArmorSetID["helm"]) {
            continue;
          }
          if (armorData.helms[ih].wgt +
                  armorData.chests[ic].wgt +
                  armorData.legs[il].wgt >
              avilableWeight) {
            continue;
          }
          for (int ig = 0; ig < armorData.gauntlets.length; ig++) {
            if (ArmorSetID["gauntlet"] != -1 && ig != ArmorSetID["gauntlet"]) {
              continue;
            }
            if (armorData.gauntlets[ig].wgt +
                        armorData.helms[ih].wgt +
                        armorData.chests[ic].wgt +
                        armorData.legs[il].wgt <=
                    avilableWeight &&
                armorData.gauntlets[ig].wgt +
                        armorData.helms[ih].wgt +
                        armorData.chests[ic].wgt +
                        armorData.legs[il].wgt >
                    avilableWeight * minWgtPercent) {
              double poi = 0.1;
              if (_wearGoat == true) {
                poi = (armorData.gauntlets[ig].poi +
                        armorData.helms[ih].poi +
                        armorData.chests[ic].poi +
                        armorData.legs[il].poi) /
                    3 *
                    4 *
                    100 ~/
                    1 /
                    100;
              } else {
                poi = armorData.gauntlets[ig].poi +
                    armorData.helms[ih].poi +
                    armorData.chests[ic].poi +
                    armorData.legs[il].poi;
              }
              armorSetList.add(ArmorSet(
                  armorData.helms[ih],
                  armorData.chests[ic],
                  armorData.legs[il],
                  armorData.gauntlets[ig],
                  poi));
              key++;
            }
            if (key >= limit) {
              return armorSetListSort(armorSetList, "Poi");
            }
          }
        }
      }
    }
    return armorSetListSort(armorSetList, "Poi");
  }

  List<ArmorSet> fixWeightPoiseFindMaxAbs() {
    double avilableWeight = calculateAvilableWeight();
    double targetPoise = 0;
    if (tgtPoiInput.text == "") {
      nullInputAlert(context);
      throw Error();
    }
    if (_wearGoat == true) {
      targetPoise = (double.parse(tgtPoiInput.text) / 4 * 3) ~/ 1 + 1;
    } else {
      targetPoise = double.parse(tgtPoiInput.text);
    }

    if (avilableWeight == -1) {
      nullInputAlert(context);
      throw Error();
    }
    double minWgtPercent = 0;
    if (minWgtInput.text == "") {
      minWgtPercent = 0.90;
    } else {
      minWgtPercent = double.parse(minWgtInput.text) / 100;
    }
    armorData.SortbyPoiPerWgt();
    List<ArmorSet> armorSetList = [];
    Map armorSetID = getArmorFixID(ArmorFixList, armorData);
    int key = 0;
    int limit = 9000000;
    int limit2 = 50000000;
    int count = 0;
    for (int ic = 0; ic < armorData.chests.length; ic++) {
      if (armorSetID["chest"] != -1 && ic != armorSetID["chest"]) {
        continue;
      }
      if (armorData.chests[ic].wgt > avilableWeight ||
          armorData.chests[ic].poi > targetPoise) {
        continue;
      }
      for (int il = 0; il < armorData.legs.length; il++) {
        if (armorSetID["leg"] != -1 && il != armorSetID["leg"]) {
          continue;
        }

        if (armorData.chests[ic].wgt + armorData.legs[il].wgt >
                avilableWeight ||
            armorData.chests[ic].poi + armorData.legs[il].poi > targetPoise) {
          continue;
        }
        for (int ih = 0; ih < armorData.helms.length; ih++) {
          if (armorSetID["helm"] != -1 && ih != armorSetID["helm"]) {
            continue;
          }
          if (armorData.helms[ih].wgt +
                      armorData.chests[ic].wgt +
                      armorData.legs[il].wgt >
                  avilableWeight ||
              armorData.helms[ih].poi +
                      armorData.chests[ic].poi +
                      armorData.legs[il].poi >
                  targetPoise) {
            continue;
          }
          for (int ig = 0; ig < armorData.gauntlets.length; ig++) {
            if (armorSetID["gauntlet"] != -1 && ig != armorSetID["gauntlet"]) {
              continue;
            }
            if (armorData.gauntlets[ig].wgt +
                        armorData.helms[ih].wgt +
                        armorData.chests[ic].wgt +
                        armorData.legs[il].wgt <=
                    avilableWeight &&
                armorData.gauntlets[ig].poi +
                        armorData.helms[ih].poi +
                        armorData.chests[ic].poi +
                        armorData.legs[il].poi ==
                    targetPoise) {
              double poi = 0.1;
              if (_wearGoat == true) {
                poi = (armorData.gauntlets[ig].poi +
                        armorData.helms[ih].poi +
                        armorData.chests[ic].poi +
                        armorData.legs[il].poi) /
                    3 *
                    4 *
                    100 ~/
                    1 /
                    100;
              } else {
                poi = armorData.gauntlets[ig].poi +
                    armorData.helms[ih].poi +
                    armorData.chests[ic].poi +
                    armorData.legs[il].poi;
              }
              armorSetList.add(ArmorSet(
                  armorData.helms[ih],
                  armorData.chests[ic],
                  armorData.legs[il],
                  armorData.gauntlets[ig],
                  poi));
              key++;
              count = 0;
            } else {
              count++;
            }
            if (key >= limit || count >= limit2) {
              return armorSetListSort(armorSetList, "Poi");
            }
          }
        }
      }
    }
    return armorSetListSort(armorSetList, "Poi");
  }

  List<ArmorSet> fixWeightFindMaxAbs() {
    double avilableWeight = calculateAvilableWeight();
    if (avilableWeight == -1) {
      nullInputAlert(context);
      throw Error();
    }
    double minWgtPercent = 0;
    if (minWgtInput.text == "") {
      minWgtPercent = 0.60;
    } else {
      minWgtPercent = double.parse(minWgtInput.text) / 100;
    }
    if (sortMode == "Phy.Abs.") {
      armorData.SortbyPhy();
    } else if (sortMode == "VSStr.Abs.") {
      armorData.SortbyVSStr();
    } else if (sortMode == "VSSla.Abs.") {
      armorData.SortbyVSSla();
    } else if (sortMode == "VSPie.Abs.") {
      armorData.SortbyVSPie();
    } else if (sortMode == "Mag.Abs") {
      armorData.SortbyMag();
    } else if (sortMode == "Fir.Abs.") {
      armorData.SortbyFir();
    } else if (sortMode == "Lit.Abs.") {
      armorData.SortbyLit();
    } else if (sortMode == "Hol.Abs.") {
      armorData.SortbyHol();
    } else if (sortMode == "Imm.") {
      armorData.SortbyImm();
    } else if (sortMode == "Robu.") {
      armorData.SortbyRobu();
    } else if (sortMode == "Foc.") {
      armorData.SortbyFoc();
    }
    List<ArmorSet> armorSetList = [];
    Map ArmorSetID = getArmorFixID(ArmorFixList, armorData);
    int key = 0;
    int limit = 400000;
    int limit2 = 100000;
    int count = 0;
    for (int ic = 0; ic < armorData.chests.length; ic++) {
      if (ArmorSetID["chest"] != -1 && ic != ArmorSetID["chest"]) {
        continue;
      }
      if (armorData.chests[ic].wgt > avilableWeight) {
        continue;
      }
      for (int il = 0; il < armorData.legs.length; il++) {
        if (ArmorSetID["leg"] != -1 && il != ArmorSetID["leg"]) {
          continue;
        }

        if (armorData.chests[ic].wgt + armorData.legs[il].wgt >
            avilableWeight) {
          continue;
        }
        for (int ih = 0; ih < armorData.helms.length; ih++) {
          if (ArmorSetID["helm"] != -1 && ih != ArmorSetID["helm"]) {
            continue;
          }
          if (armorData.helms[ih].wgt +
                  armorData.chests[ic].wgt +
                  armorData.legs[il].wgt >
              avilableWeight) {
            continue;
          }
          for (int ig = 0; ig < armorData.gauntlets.length; ig++) {
            if (ArmorSetID["gauntlet"] != -1 && ig != ArmorSetID["gauntlet"]) {
              continue;
            }
            if (armorData.gauntlets[ig].wgt +
                        armorData.helms[ih].wgt +
                        armorData.chests[ic].wgt +
                        armorData.legs[il].wgt <=
                    avilableWeight &&
                armorData.gauntlets[ig].wgt +
                        armorData.helms[ih].wgt +
                        armorData.chests[ic].wgt +
                        armorData.legs[il].wgt >
                    avilableWeight * minWgtPercent) {
              double poi = 0.1;
              if (_wearGoat == true) {
                poi = (armorData.gauntlets[ig].poi +
                        armorData.helms[ih].poi +
                        armorData.chests[ic].poi +
                        armorData.legs[il].poi) /
                    3 *
                    4 *
                    100 ~/
                    1 /
                    100;
              } else {
                poi = armorData.gauntlets[ig].poi +
                    armorData.helms[ih].poi +
                    armorData.chests[ic].poi +
                    armorData.legs[il].poi;
              }
              armorSetList.add(ArmorSet(
                  armorData.helms[ih],
                  armorData.chests[ic],
                  armorData.legs[il],
                  armorData.gauntlets[ig],
                  poi));
              key++;
              count = 0;
            } else {
              count++;
            }

            if (key >= limit || count > limit2) {
              return armorSetListSort(armorSetList, sortMode!);
            }
          }
        }
      }
    }
    return armorSetListSort(armorSetList, sortMode!);
  }

  List<Node> convertToNodes(
      Map<double, List<ArmorSet>> armorSetsSepreateByPoiseMap) {
    List<Node> nodes = [];
    int poisekey = 0;
    int count = 0;
    armorSetsSepreateByPoiseMap.forEach((key, value) {
      List<Node> tmpchildrenList = [];
      value.forEach((ArmorSet armorSet) {
        ArmorSetNameAttribute[count.toString()] = armorSet.getAttributes();
        tmpchildrenList.add(Node(
          label: armorSet.getName(),
          key: count.toString(),
          icon: Icons.input,
          iconColor: Color.fromARGB(255, 165, 54, 46),
        ));
        count++;
      });
      nodes.add(
        Node(
            label: "Poise:$key",
            key: "Poise:$key",
            children: tmpchildrenList,
            icon: Icons.folder_open_outlined,
            iconColor: Color.fromARGB(255, 134, 134, 134)),
      );
    });
    return nodes;
  }

  String getArmorSetDetails(String key) {
    String? string = ArmorSetNameAttribute[key];
    if (string != null) {
      return string;
    } else {
      return "";
    }
  }

  void nullInputAlert(BuildContext context) {
    var alert = AlertDialog(
      title: const Text("Alert"),
      content: Text(languageMap["Please input all the fields"]),
    );

    showDialog(
        context: context,
        builder: (BuildContext context) {
          return alert;
        });
  }
}

void main() async {
  armorData = ArmorData(helmdata, chestdata, legdata, gauntletdata);
  Map ArmorNameMap = jsonDecode(armorNameData!);
  print(armorData);
  print(ArmorNameMap);
  for (var i = 0; i < armorData.helms.length; i++) {
    HelmList.add(armorData.helms[i].name);
  }
  for (var i = 0; i < armorData.chests.length; i++) {
    ChestList.add(armorData.chests[i].name);
  }
  for (var i = 0; i < armorData.legs.length; i++) {
    LegList.add(armorData.legs[i].name);
  }
  for (var i = 0; i < armorData.gauntlets.length; i++) {
    GauntletList.add(armorData.gauntlets[i].name);
  }

  if (languageString == 'ZH' && nameChanged == false) {
    for (var i = 0; i < HelmList.length; i++) {
      armorData.helms[i].name = ArmorNameMap[armorData.helms[i].name];
      HelmList[i] = ArmorNameMap[HelmList[i]];
    }
    for (var i = 0; i < ChestList.length; i++) {
      armorData.chests[i].name = ArmorNameMap[armorData.chests[i].name];
      ChestList[i] = ArmorNameMap[ChestList[i]];
    }
    for (var i = 0; i < LegList.length; i++) {
      armorData.legs[i].name = ArmorNameMap[armorData.legs[i].name];
      LegList[i] = ArmorNameMap[LegList[i]];
    }
    for (var i = 0; i < GauntletList.length; i++) {
      armorData.gauntlets[i].name = ArmorNameMap[armorData.gauntlets[i].name];
      GauntletList[i] = ArmorNameMap[GauntletList[i]];
    }
    nameChanged == true;
  }
  HelmList.add("nil");
  ChestList.add("nil");
  LegList.add("nil");
  GauntletList.add("nil");

  WidgetsFlutterBinding.ensureInitialized();
  // 必须加上这一行。
  await windowManager.ensureInitialized();
  WindowOptions windowOptions = const WindowOptions(
    title: "Elden Ring Armor Optimizer",
    size: Size(1285, 605),
    center: true,
    backgroundColor: Colors.transparent,
    skipTaskbar: false,
    titleBarStyle: TitleBarStyle.normal,
  );
  windowManager.setResizable(false);
  windowManager.waitUntilReadyToShow(windowOptions, () async {
    await windowManager.show();
    await windowManager.focus();
  });

  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        theme: ThemeData(
          brightness: Brightness.dark,
          primaryColor: Colors.lightBlue[800],
          fontFamily: 'SourceSans3',
        ),
        home: const HomePage());
  }
}
