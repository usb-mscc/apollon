
def create(form):
    txtDm = form["durchmesser"]
    grading = form["Differenzierung"]
    lokalisation = form["Lokalisation"]
    tiefe = form["Infiltrationstiefe"] 
    lkpos = int(form["lymphknoten_x"])
    lkneg = form["lymphknoten_y"]
    
    if grading == "Gut":
        grading = "Gut differenziertes "
    elif grading == "Mässig":
        grading = "Mässig differenziertes "
    else:
        grading = "Gering differenziertes "

    pT = 0
    if tiefe == "Submukosa":
        tiefe = "Tumorinfiltration bis in die Submukosa. "
        pT = "pT1"
    elif tiefe == "Muscularis":
        tiefe = "Tumorinfiltration bis in die Muscularis propria. "
        pT = "pT2"
    elif tiefe == "Perikolisches":
        tiefe = "Tumorinfiltration aller Wandschichten bis in das subserosale Fettgewebe. "
        pT = "pT3"
    else:
        tiefe = "Tumorinfiltration aller Wandschichten mit Durchbruch durch die Serosa. "
        pT = "pT4a"   

    rro = form.get("randoral", "")
    rro1 = 0
    rra = form.get("randaboral", "")
    rrt = form.get("randtief", "")
    if rro == "" and rra == "" and rrt == "":
        rro = "Tumorfreier oraler, aboraler und tiefer Resektionsrand."
        rro1 = "R0 (lokal)"
        rro2 = "Tumorfreie Resektionsränder."
    elif rro == "on" and rra == "" and rrt == "":
        rro = "Tumorinfiltration in den oralen Resektionsrand. Tumorfreier aboraler und tiefer Resektionsrand."
        rro1 = "R1"
        rro2 = "Tumornachweis bis in den Resektionsrand."
    elif rro == "" and rra == "on" and rrt == "":
        rro = "Tumorinfiltration in den aboralen Resektionsrand. Tumorfreier oraler und tiefer Resektionsrand."
        rro1 = "R1"
        rro2 = "Tumornachweis bis in den Resektionsrand."
    elif rro == "" and rra == "" and rrt == "on":
        rro = "Tumorinfiltration in den tiefen Resektionsrand. Tumorfreier oraler und aboraler Resektionsrand."
        rro1 = "R1"
        rro2 = "Tumornachweis bis in den Resektionsrand."
    elif rro == "on" and rra == "on" and rrt == "":
        rro = "Tumorinfiltration in den oralen und aboralen Resektionsrand. Tumorfreier tiefer Resektionsrand."
        rro1 = "R1"
        rro2 = "Tumornachweis bis in den Resektionsrand."
    elif rro == "" and rra == "on" and rrt == "on":
        rro = "Tumorinfiltration in den tiefen und aboralen Resektionsrand. Tumorfreier oraler Resektionsrand."
        rro1 = "R1"
        rro2 = "Tumornachweis bis in den Resektionsrand."
    else:
        rro = "Tumorinfiltration in den tiefen, oralen und aboralen Resektionsrand."
        rro2 = "Tumornachweis bis in den Resektionsrand."
        rro1 = "R1"

    tb = float(form["Tumorbuds"])
    objectiv = form["Objektiv"]
    if objectiv == "23":
        tb = tb/1.323
    elif objectiv == "24":
        tb = tb/1.440
    else:
        tb = tb/1.563
    
    tb1 = 0
    if tb <= 4:
        tb1 = "Tumorbudding : Bd1 (low), "
    elif tb > 4 and tb < 10:
        tb1 = "Tumorbudding : Bd2 (intermediate), "
    else:
        tb1 = "Tumorbudding : Bd3 (high), "

    pn1 = form.get("perineuralscheideninfiltration", "")
    pn2 = 0
    if pn1 == "on":
        pn1 = "Perineuralscheideninfiltration. "
        pn2 = "Pn1, "
    else:
        pn1 = ""
        pn2 = "Pn0, "

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

    if lkpos == 0:
        lkp = "pN0"
    elif lkpos == 1:
        lkp = "pN1a"
    elif lkpos > 1 and lkpos <= 3:
        lkp = "pN1b"
    elif lkpos > 3 and lkpos <= 6:
        lkp = "pN2a"
    else:
        lkp = "pN2b"

    mss = form["MSS"]

    if mss == "MSS+":
        mss = "Mikrosatellitenstabil (MSS)"
    elif mss == "MSS-":
        mss = "Mikrosatelliteninstabil (MSI)"
    else:
        mss = "Bestimmung der Mikrosatelliten folgt"

    sentense1 = "Colon " + lokalisation +  " (Ektomie):\n" + grading + "Adenokarzinom des Colon " + lokalisation + "(maximaler Tumordurchmesser: " + str(txtDm) + " mm). " + tiefe + lymphangiosis1 + und1 + hämangiosis1 + ca + pn1 + "\n\n" + tb1 + '{:.2}'.format(tb) + " Buds/0.785 mm^2" + "\n\n" + rro 
    
    sentense2 = grading + "Adenokarzinom des Colon " + lokalisation + " (maximaler Tumordurchmesser: " + str(txtDm) + " mm). " + rro2 + "\n\nTNM-Klassifikation (8. Auflage, UICC):\n" + pT + ", " + lkp + "(" + str(lkpos) + "/" + str(lkneg) + "), " + l1 + v1 + pn2 + rro1 + "\n\n" + tb1 + '{:.2}'.format(tb) + " Buds/0.785 mm^2\n\n" + mss
    return sentense1, sentense2