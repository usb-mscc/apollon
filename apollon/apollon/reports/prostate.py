
def create(form):
    txtDm = form["durchmesser"]
    gl1 = form["gleason_x"]
    gl2 = form["gleason_y"]
    lkpos = form["lymphknoten_x"]
    lkneg = form["lymphknoten_y"]

    gls = 0

    if gl1 == 3 and gl2 == 3:
        isup = "1 "
        gls = "6"
    elif gl1 == 3 and gl2 == 4:
        gls = "7"
        isup = "2 "
    elif gl1 == 4 and gl2 == 3:
        isup = "3 "
        gls = "7"
    elif gl1 == 4 and gl2 == 4:
        isup = "4 "
        gls = "8"
    elif gl1 == 5 and gl2 == 3:
        isup = "4 "
        gls = "8"
    elif gl1 == 3 and gl2 == 5:
        isup = "4 "
        gls = "8"
    else:
        isup = "5 "
        gls = "9"

    lappen = form["lappen"]

    if lappen == "links":
        lappen = ", im linken Prostatalappen"
    elif lappen == "rechts":
        lappen = ", im rechten Prostatalappen"
    else:
        lappen = ", in beiden Prostatalappen"


    pn1 = form.get("perineuralscheideninfiltration", "")
    pn2 = 0
    if pn1 == "on":
        pn1 = "Perineuralscheideninfiltration. "
        pn2 = "Pn1, "
    else:
        pn1 = ""
        pn2 = "Pn0, "



    sabla = form.get("tumorfreie_sabla", "")
    sablapt3b = 0

    if sabla == "on":
        sabla = "Tumorfreie Samenblase. "
        sablapt3b = 0
    else:
        sabla = "Infiltration der Samenblase. "
        sablapt3b = 1


    ep = form.get("extraprostatisches_wachstum", "")
    ep1 = 0
    if ep == "on":
        ep = "Extraprostatisches Wachstum. "
        ep1 = 1
    else:
        ep = "Kein Extraprostatisches Wachstum. "
        ep1 = 0


    lymphangiosis = 0
    hämangiosis = 0
    lymphangiosis = form.get("lymphangiose", "")
    hämangiosis = form.get("haengiose", "")
    l1 = 0
    v1 = 0
    und1 = 0

    if lymphangiosis == "on" and hämangiosis == "on":
        und1 = "und "
    else:
        und1 = ""


    if lymphangiosis == "on":
        lymphangiosis1 = "Lymphangiosis "
        l1 = "L1, "
    else:
        lymphangiosis1 = ""
        l1 = "L0, "



    if hämangiosis == "on":
        hämangiosis1 = "Hämangiosis "
        v1 = "V1, "
    else:
        hämangiosis1 = ""
        v1 = "V0, "


    ca = 0
    if lymphangiosis == "on" or hämangiosis == "on":
        ca = "carcinomatosa. "
    else:
        ca = ""

    lkp = 0

    if lkpos == 0:
        lkp = "pN0"
    else:
        lkp = "pN1"


    rr = form.get("rr_tumorfrei", "")
    rro1 = 0

    rrlok = form["rr_wo"]
    rrmm = form["rr_strecke"]



    if rr == 1:
        rr = "Tumorfreie Resektionsränder. Minimaler Abstand zum Resektionsrand: " + str(rrmm) + "mm " + "(" + str(rrlok) + ")."
        rro1 = "R0 (lokal)"
    else:
        rr = "Tumor bis in Resektionsrand " + str(rrlok) + "über eine Strecke von " + str(rrmm) + "."
        rro1 = "R1"



    pT = form["lappen"]
    if pT == "links" or pT == "rechts":
        pT = "pT2b"
    elif pT == "beide":
        pT = "pT2c"


    if ep1 == "on": # extra wachstum
        pT = "pT3a"
    else:
        pT

    if sablapt3b == "on": # tumorfrei sabla
        pT = "pT3b"
    else:
        pT

    sentense1 = "Prostata (Ektomie):\nAdenokarzinom der Prostata, Gleason " + gls + " (" + str(gl1) + "+" + str(gl2) + "), WHO/ISUP Grad " + isup + "(maximaler Tumordurchmesser: " + str(txtDm) + " mm). " + pn1 + sabla + lymphangiosis1 + und1 + hämangiosis1 + ca + ep + rr

    sentense2 = "Adenokarzinom der Prostata, Gleason " + gls + " (" + str(gl1) + "+" + str(gl2) + "), WHO/ISUP Grad " + isup + "(maximaler Tumordurchmesser: " + str(txtDm) + " mm). " + rr + "\n\nTNM-Klassifikation (8. Auflage, UICC):\n" + pT + ", " + lkp + "(" + str(lkpos) + "/" + str(lkneg) + "), " + l1 + v1 + pn2 + rro1

    return sentense1, sentense2