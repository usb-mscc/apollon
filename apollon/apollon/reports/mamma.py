def create(form):
    #Seite
    seite = form["seite"]
    seite2 = 0
    if seite == "rechts":
        seite = "rechten "
        seite2 = "rechts"
    else:
        seite = "linken "
        seite2 = "links"

    #Differenzierung Karzinom
    typ = form["typ"]
    differenzierung = form["typ"]

    if differenzierung == "ductal":
        differenzierung = "invasiv duktales Mammakarzinom "
    else:
        differenzierung = "invasiv lobuläres Mammakarzinom "

    #BRE-Score
    tubform = int(form["tubform"])
    kernpleo = int(form["kernpleo"])
    mitosis = int(form["mitosis"])
    BREscore = tubform+kernpleo+mitosis
    BREa1 = 0
    BREa2 = 0
    grading = 0

    if BREscore > 2 and BREscore < 6:
        BREa1 = "(BRE-Grad 1; Score " + str(BREscore) + ":" + str(BRE1) + "," + str(BRE2) + "," + str(BRE3) + ") "
        BREa2 = "BRE-Grad 1, "
        grading = "Gut differenziertes, "
    elif BREscore > 5 and BREscore < 8:
        BREa1 = "(BRE-Grad 2; Score " + str(BREscore) + ":" + str(BRE1) + "," + str(BRE2) + "," + str(BRE3) + ") "
        BREa2 = "BRE-Grad 2, "
        grading = "Mässig differenziertes, "
    elif BREscore > 7:
        BREa1 = "(BRE-Grad 3; Score " + str(BREscore) + ":" + str(BRE1) + "," + str(BRE2) + "," + str(BRE3) + ") "
        BREa2 = "BRE-Grad 3, "
        grading = "Schlecht differenziertes, "
    else:
        BREa1 = ""
        BREa2 = ""

    #Durchmesser pT
    txtDm = int(form["durchmesser"])
    pT = 0    
    if txtDm <= 1:
        pT = "pT1mi"
    elif txtDm > 1 and txtDm <=5:
        pT = "pT1a"
    elif txtDm > 5 and txtDm <=10:
        pT = "pT1b"
    elif txtDm > 10 and txtDm <=20:
        pT = "pT1c"
    elif txtDm > 20 and txtDm <=50:
        pT = "pT2"
    else:
        pT = "pT3"

    #RR Invasiv
    cran = int(form["cranial"])
    caud = int(form["caudal"])
    med = int(form["medial"])
    lat = int(form["lateral"])
    vent = int(form["ventral"])
    dors = int(form["dorsal"])
    cran1 = 0
    if cran == 0:
        cran1 = "\n- nach kranial in den Resektionsrand reichend."
    elif cran > 0 and cran < 5:
        cran1 = "\n- nach kranial: " + str(cran) + " mm"
    else:
        cran1 = ""

    caud1 = 0
    if caud == 0:
        caud1 = "\n- nach kaudal in den Resektionsrand reichend."
    elif caud > 0 and caud < 5:
        caud1 = "\n- nach kaudal: " + str(caud) + " mm"
    else:
        caud1 = ""

    med1 = 0
    if med == 0:
        med1 = "\n- nach medial in den Resektionsrand reichend."
    elif med > 0 and med < 5:
        med1 = "\n- nach medial: " + str(med) + " mm"
    else:
        med1 = ""

    lat1 = 0
    if lat == 0:
        lat1 = "\n- nach lateral in den Resektionsrand reichend."
    elif lat > 0 and lat < 5:
        lat1 = "\n- nach lateral: " + str(lat) + " mm"
    else:
        lat1 = ""

    vent1 = 0
    if vent == 0:
        vent1 = "\n- nach ventral in den Resektionsrand reichend."
    elif vent > 0 and vent < 5:
        vent1 = "\n- nach ventral: " + str(vent) + " mm"
    else:
        vent1 = ""

    dors1 = 0
    if dors == 0:
        dors1 = "\n- nach dorsal in den Resektionsrand reichend."
    elif dors > 0 and dors < 5:
        dors1 = "\n- nach dorsal: " + str(dors) + " mm"
    else:
        dors1 = ""
    
    r1 = 0
    
    if cran > 0 and caud > 0 and med > 0 and lat > 0 and dors > 0 and vent > 0:
        r1 = "R0 (lokal)"
    else:
        r1 = "R1"

    allc = 0
    if cran > 5 and caud > 5 and med > 5 and vent > 5 and lat > 5 and dors > 5:
        alldc = "\n- zu allen Resektionsrändern > 5mm."
    else:
        allc = "\n- zu den restlichen Resektionsrändern > 5mm."

    #Lymph/Haemangiosis
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

    #DCISAusmaß
    DCISAusmaß = form["Ausmaß"]

    #DCISLokalisation
    intratumoral = form["intratumoral"]
    peritumoral = form["peritumoral"]

    if intratumoral == "intratumoral" and peritumoral == "peritumoral":
        und = "und "
    else:
        und = ""

    #DCISGrading
    DCISgrading = form["DCIS-Grading"]
    if DCISgrading == "G1":
        DCISgrading = "Geringer Kernmalignitätsgrad "
    elif DCISgrading == "G2":
        DCISgrading = "Intermediärer Kernmalignitätsgrad "
    elif DCISgrading == "G3":
        DCISgrading = "Hocher Kernmalignitätsgrad "
    else:
        DCISgrading = ""

    #DCISRR#
    crandc = int(form["dccran"])
    cauddc = int(form["dccaud"])
    meddc = int(form["dcmed"])
    latdc = int(form["dclat"])
    ventdc = int(form["dcvent"])
    dorsdc = int(form["dcdors"])

    cran2 = 0
    if crandc == 0:
        cran2 = "\n- nach kranial in den Resektionsrand reichend,"
    elif crandc > 0 and crandc < 5:
        cran2 = "\n- nach kranial: " + str(cran) + " mm,"
    else:
        cran2 = ""

    caud2 = 0
    if cauddc == 0:
        caud2 = "\n- nach kaudal in den Resektionsrand reichend,"
    elif cauddc > 0 and cauddc < 5:
        caud2 = "\n- nach kaudal: " + str(caud) + " mm,"
    else:
        caud2 = ""

    med2 = 0
    if meddc == 0:
        med2 = "\n- nach medial in den Resektionsrand reichend,"
    elif meddc > 0 and meddc < 5:
        med2 = "\n- nach medial: " + str(med) + " mm,"
    else:
        med2 = ""

    lat2 = 0
    if latdc == 0:
        lat2 = "\n- nach lateral in den Resektionsrand reichend,"
    elif latdc > 0 and latdc < 5:
        lat2 = "\n- nach lateral: " + str(lat) + " mm,"
    else:
        lat2 = ""

    vent2 = 0
    if ventdc == 0:
        vent2 = "\n- nach ventral in den Resektionsrand reichend,"
    elif ventdc > 0 and ventdc < 5:
        vent2 = "\n- nach ventral: " + str(vent) + " mm,"
    else:
        vent2 = ""

    dors2 = 0
    if dorsdc == 0:
        dors2 = "\n- nach dorsal in den Resektionsrand reichend,"
    elif dorsdc > 0 and dorsdc < 5:
        dors2 = "\n- nach dorsal: " + str(dors) + " mm,"
    else:
        dors2 = ""
        
    alldc = 0
    if crandc > 5 and cauddc > 5 and meddc > 5 and ventdc > 5 and latdc > 5 and dorsdc > 5:
        alldc = "\n- zu allen Resektionsrändern > 5mm."
    else:
        alldc = "\n- zu den restlichen Resektionsrändern > 5mm."

    #Prädiktive marker
    ER = int(form["ER"])
    PR = int(form["PR"])
    HER = int(form["HER2"])
    KI = int(form["Ki67"])
    ERf = 0

    if ER == 0:
        ERf = "negativ"
    else:
        ERf = "positiv"

    PRf = 0

    if PR == 0:
        PRf = "negativ"
    else:
        PRf = "positiv"

    HERf = 0

    if HER == 0:
        HERf = "negativ"
    elif HER == 1:
        HERf = "negativ"
    elif HER == 2:
        HERf = "equivocal"
    elif HER == 3:
        HERf = "positiv"
    else:
        HERf = ""

    #Lymphknoten
    lkpos = int(form["lymphknoten_x"])
    lkneg = int(form["lymphknoten_y"])
    lkp = 0
    
    if lkpos == 0:
        lkp = "pN0"
    elif lkpos > 0 and lkpos <= 3:
        lkp = "pN1"
    elif lkpos > 3 and lkpos <= 9:
        lkp = "pN2"
    elif lkpos > 9:
        lkp = "pN3"
    else :
        lkp = ""

    #Extras
    fd = form["fd"]
    am = form["am"]
    mp = form["mp"]
    udh = form["udh"]
    miazdb = form["miazdb"]
    #li = [fd, am, udh, miazdb, mp]
    #s_li = sorted(li)
    
    #Sentence
    sentense1 = "Mamma, " + seite2 + " (Exzision):\n" + "1. " + grading + differenzierung + BREa1 + "der " + seite + "Mamma. Maximaler Tumordurchmesser: " + str(txtDm) + " mm. " + lymphangiosis1 + und1 + hämangiosis1 + ca + tfh\
        + "\nMinimaler Abstand des invasiven Karzinoms zu den Resektionsrändern:" + cran1 + caud1 + med1 + lat1 + vent1 + dors1 + allc \
        +"\n\n" "2. " + DCISAusmaß + intratumoral + und + peritumoral + " duktales Carcinoma in situ (DCIS) mit" + DCISgrading1 + " Kernmalignitätsgrad" + "(" + DCISgrading2 + ksubtyp + stkomma + ssubtyp + komedonekrosen + mikrokalk + ")." \
        +"\nMinimaler Abstand des invasiven Karzinoms zu den Resektionsrändern:" + cran2 + caud2 + med2 + lat2 + vent2 + dors2 + alldc \
        + "\n\n3. Übriges Mammaparenchym mit " + fd + k1 + am + k2 + udh + k3 + miazdb + k4 + mp + "."

        #sentense2 = grading + differenzierung + "(maximaler Tumordurchmesser: " + str(txtDm) + " mm) der " + seite + " Mamma.\n\nTNM-Klassifikation (8. Auflage, UICC):\n" + pT + ", " + lkp + "(" + str(lkpos) + "/" + str(lkneg) + "), "\
        #+ BREa2 + l1 + v1 + r1 + "\n\nER: " + ERf + "(" + str(ER) + "%), " + "PR: " + PRf + "(" + str(PR) + "%), " + "Her2/neu: " + HERf + " " + str(HER) + "+ (IHC), Proliferationsindex (Ki-67): " + str(KI) + " %"
