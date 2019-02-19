
def create(form):

    date = form.get("date")
    date1=0
    if date == "":
        date1 = "Es liegen keine Voraufnahmen zum Vergleich vor"
    else:
        date1 = "Zum Vergleich leigen die Voraufnahmen vom " + date + " vor."

    artefakte = form.get("artefakte", "")
    if artefakte == "on":
        artefakte = "Eingeschränkte Beurteilbarkeit bei ausgeprägten Bewegungsartefakten." + "\n\n"
    else:
        artefakte = ""

    Postinterventionell = form.get("Postinterventionell", "")
    if Postinterventionell == "on":
        Postinterventionell = "Postinterventionelle Veränderungen in..."
    else:
        Postinterventionell = "Kein Nachweiß postinterventioneller Veränderungen in der T1 nativ"

    ap = int(form["ap"])
    axial = int(form["axial"])
    cc = int(form["cc"])
    volumen = 0
    volumen = ap*axial*cc*0.52

    #Base rechts
    AFSbaserechts = form.get("AFSbaserechts", "")
    TZabaserechts = form.get("TZabaserechts", "")
    PZabaserechts = form.get("PZabaserechts", "")
    TZpbaserechts = form.get("TZpbaserechts", "")
    PZpbaserechts = form.get("PZpbaserechts", "")
    CZbaserechts = form.get("CZbaserechts", "")

    #Base links
    AFSbaselinks = form.get("AFSbaselinks", "")
    TZabaselinks = form.get("TZabaselinks", "")
    PZabaselinks = form.get("PZabaselinks", "")
    TZpbaselinks = form.get("TZpbaselinks", "")
    PZpbaselinks = form.get("PZpbaselinks", "")
    CZbaselinks = form.get("CZbaselinks", "")
    #Mid rechts
    AFSmidrechts = form.get("AFSmidrechts", "")
    TZamidrechts = form.get("TZamidrechts", "")
    PZamidrechts = form.get("PZamidrechts", "")
    TZpmidrechts = form.get("TZpmidrechts", "")
    PZpmidrechts = form.get("PZpmidrechts", "")
    PZmmidrechts = form.get("PZmmidrechts", "")
    #Mid links
    AFSmidlinks = form.get("AFSmidlinks", "")
    TZamidlinks = form.get("TZamidlinks", "")
    PZamidlinks = form.get("PZamidlinks", "")
    TZpmidlinks = form.get("TZpmidlinks", "")
    PZpmidlinks = form.get("PZpmidlinks", "")
    PZmmidlinks = form.get("PZmmidlinks", "")
    #Apex rechts
    AFSapexrechts = form.get("AFSapexrechts", "")
    TZaapexrechts = form.get("TZaapexrechts", "")
    PZaapexrechts = form.get("PZaapexrechts", "")
    TZpapexrechts = form.get("TZpapexrechts", "")
    PZpapexrechts = form.get("PZpapexrechts", "")
    PZmapexrechts = form.get("PZmapexrechts", "")
    #Apex links
    AFSapexlinks = form.get("AFSapexlinks", "")
    TZaapexlinks = form.get("TZaapexlinks", "")
    PZaapexlinks = form.get("PZaapexlinks", "")
    TZpapexlinks = form.get("TZpapexlinks", "")
    PZpapexlinks = form.get("PZpapexlinks", "")
    PZmapexlinks = form.get("PZmapexlinks", "")


    basis = 0
    if AFSbaserechts == "on" or TZabaserechts == "on" or PZabaserechts == "on" or TZpbaserechts == "on" or PZpbaserechts == "on" or CZbaserechts == "on" or AFSbaselinks == "on" or TZabaselinks == "on" or PZabaselinks == "on" or TZpbaselinks == "on" or PZpbaselinks == "on" or CZbaselinks:
        basis = 1
    else:
        basis = 0

    mitte = 0
    if AFSmidrechts == "on" or TZamidrechts == "on" or PZamidrechts == "on" or TZpmidrechts == "on" or PZpmidrechts == "on" or PZmmidrechts == "on" or AFSmidlinks == "on" or TZamidlinks == "on" or PZamidlinks == "on" or TZpmidlinks == "on" or PZpmidlinks == "on" or PZmmidlinks:
        mitte = 2
    else:
        mitte = 0

    apex = 0
    if AFSapexrechts == "on" or TZaapexrechts == "on" or PZaapexrechts == "on" or TZpapexrechts == "on" or PZpapexrechts == "on" or PZmapexrechts == "on" or AFSapexlinks == "on" or TZaapexlinks == "on" or PZaapexlinks == "on" or TZpapexlinks == "on" or PZpapexlinks == "on" or PZmapexlinks:
        apex = 4
    else:
        apex = 0

    high=0
    high = basis+mitte+apex

    if high == 1:
        high = " auf Höhe der Prostatabasis "
    elif high == 2:
        high = " auf Höhe der Prostatamitte "
    elif high == 4:
        high = " auf Höhe des Prostataapex "
    elif high == 3:
        high = " auf Höhe der Prostatamitte bis Basis "
    elif high == 6:
        high = " auf Höhe der Prostatamitte bis Apex "
    else:
        high = " auf Höhe der der Prostatabasis bis Apex "

    rechts = 0
    if AFSbaserechts == "on" or TZabaserechts == "on" or PZabaserechts == "on" or TZpbaserechts == "on" or PZpbaserechts == "on" or CZbaserechts == "on" or AFSmidrechts == "on" or TZamidrechts == "on" or PZamidrechts == "on" or TZpmidrechts == "on" or PZpmidrechts == "on" or PZmmidrechts == "on" or AFSapexrechts == "on" or TZaapexrechts == "on" or PZaapexrechts == "on" or TZpapexrechts == "on" or PZpapexrechts == "on" or PZmapexrechts == "on":
        rechts = " links "
    else:
        rechts = ""
    
    links=0
    if AFSbaselinks == "on" or TZabaselinks == "on" or PZabaselinks == "on" or TZpbaselinks == "on" or PZpbaselinks == "on" or CZbaselinks == "on" or AFSmidlinks == "on" or TZamidlinks == "on" or PZamidlinks == "on" or TZpmidlinks == "on" or PZpmidlinks == "on" or PZmmidlinks == "on" or AFSapexlinks == "on" or TZaapexlinks == "on" or PZaapexlinks == "on" or TZpapexlinks == "on" or PZpapexlinks == "on" or PZmapexlinks == "on":
        links = " rechts "
    else:
        links = ""

    beidseits=0
    if rechts == " rechts " and links == " links ":
        rechts=""
        links=""
        beidseits=" beidseits "
    else:
        beidseits=""


    TZ=0
    if TZabaserechts == "on" or TZpbaserechts == "on" or TZabaselinks == "on" or TZpbaselinks == "on" or TZamidlinks == "on"  or TZpmidlinks == "on" or TZamidrechts == "on"  or TZpmidrechts == "on" or TZpapexrechts == "on" or TZaapexrechts == "on" or TZpapexlinks == "on" or TZaapexlinks == "on":
        TZ = 1
    else:
        TZ =0

    PZ=0
    if PZabaserechts == "on" or PZpbaserechts == "on" or PZabaselinks == "on" or PZpbaselinks == "on" or PZamidlinks == "on"  or PZpmidlinks == "on" or PZamidrechts == "on"  or PZpmidrechts == "on" or PZpapexrechts == "on" or PZaapexrechts == "on" or PZpapexlinks == "on" or PZaapexlinks == "on" or PZmapexlinks == "on" or PZmapexrechts == "on" or PZmmidrechts == "on" or PZmmidlinks == "on":
        PZ = 3
    else:
        PZ =0

    CZ=0
    if CZbaselinks == "on" or CZbaserechts == "on":
        CZ = 5
    else:
        CZ =0

    AFS=0
    if AFSbaserechts == "on" or AFSbaselinks == "on" or AFSmidlinks == "on"  or AFSmidrechts == "on" or AFSapexlinks == "on" or AFSapexrechts == "on":
        AFS = 7
    else:
        AFS =0
    
    anterior=0
    if PZabaselinks == "on" or PZabaserechts == "on" or TZabaselinks == "on" or TZabaserechts == "on" or PZamidlinks == "on" or PZamidrechts == "on" or TZamidlinks == "on" or TZamidrechts == "on" or PZaapexlinks == "on" or PZaapexrechts == "on" or TZaapexlinks == "on" or TZaapexrechts == "on":
        anterior = 1
    else:
        anterior = 0

    posterior=0
    if PZpbaselinks == "on" or PZpbaserechts == "on" or TZpbaselinks == "on" or TZpbaserechts == "on" or PZpmidlinks == "on" or PZpmidrechts == "on" or TZpmidlinks == "on" or TZpmidrechts == "on" or PZpapexlinks == "on" or PZpapexrechts == "on" or TZpapexlinks == "on" or TZpapexrechts == "on":
        posterior = 3
    else:
        posterior = 0

    medial=0
    if PZmapexlinks == "on" or PZmapexrechts == "on" or PZmmidrechts == "on" or PZmmidlinks == "on":
        medial = 5
    else: 
        medial = 0
    
    direction=0
    direction=anterior+posterior+medial
    if direction==1:
        direction= " Anteriore "
    elif direction==3:
        direction= " Posteriore "
    elif direction==5:
        direction= " Posteromediale "
    else:
        direction= " Anteriore und posteriore "

    zone=0
    zone=TZ+PZ+CZ+AFS
    if zone == 1:
        zone = " Transitionalzone "
    elif zone == 3:
        zone = " periphere Zone "
    elif zone == 5:
        zone = " zentrale Zone "
    elif zone == 7:
        zone = " Anteriores fibromuskuläres Stroma "
        direction = ""
    elif zone == 4:
        zone = " periphere- und Transitionalzone "
    elif zone == 8:
        zone = " periphere und zentrale Zone "
    elif zone == 6:
        zone = " zentrale- und Transitionalzone "
    else:
        zone = " Prostatalappen "

    Lokalisation = direction + zone + rechts + links + beidseits + high
    

    txtDm = int(form["durchmesser"])

    serie = form["serie"]

    image = form["image"]

    ADCMessung = form["ADCMessung"]
    PIRADSP=0
    
    ADC = form["ADC"]
    if ADC == "ADC1":
        ADC = "Keine Diffusionsrestriktion (ADC: " + str(ADCMessung) + "mm2/s). "
        PIRADSP=1
    elif ADC == "ADC2":
        ADC = "Geringe Diffusionsrestriktion (ADC: " + str(ADCMessung) + "mm2/s). "
        PIRADSP=2
    elif ADC == "ADC3":
        ADC = "Fokale Diffusionsrestriktion (ADC: " + str(ADCMessung) + "mm2/s). "
        PIRADSP=3
    else:
        ADC = "Flächige Diffusionsrestriktion (ADC: " + str(ADCMessung) + "mm2/s). "
        PIRADSP=4

    DWIMessung = form["DWIMessung"]

    DWI = form["DWI"]
    if DWI == "DWI1":
        DWI = " Keine Hyperintensität in der DWI (DWI: " + str(DWIMessung) + "mm2/s). "
    else:
        DWI = " Undeutlich hyperintens in der DWI (DWI: " + str(DWIMessung) + "mm2/s). "

    DWIMessung = form["DWIMessung"]

    PIRADSZ=0

    T2w = form["T2w"]
    if T2w == "T2w1":
        T2w = "Normales Signalverhalten in der T2w. "
        PIRADSZ = 1
    elif T2w == "T2w2":
        T2w = "Nodulär hypointens in der T2w. "
        PIRADSZ = 2
    elif T2w == "T2w3":
        T2w = "Unscharf hypointens in der T2w. "
        PIRADSZ = 3
    else:
        T2w = "Linsenförmig hypointens in der T2w. "
        PIRADSZ = 4

    if PIRADSP == 4 and txtDm > 1.4:
        PIRADSP = 5

    if PIRADSZ == 4 and txtDm > 1.4:
        PIRADSZ = 5

    if PZ==0:
        PIRADSP= ""
    else:
        PIRADSZ= ""

    #sabla = form.get("tumorfreie_sabla", "")
    #sablapt3b = 0

    #if sabla == "on":
    #    sabla = "Tumorfreie Samenblase. "
    #    sablapt3b = 0
    #else:
    #    sabla = "Infiltration der Samenblase. "
    #    sablapt3b = 1


    #ep = form.get("extraprostatisches_wachstum", "")
    #ep1 = 0
    #if ep == "on":
    #    ep = "Extraprostatisches Wachstum. "
    #    ep1 = 1
    #else:
    #    ep = "Kein Extraprostatisches Wachstum. "
    #    ep1 = 0

    sentense1 = "Befund\n" + date1 + "\n\n" + artefakte + Postinterventionell + "\n\nProstatavolumen: " + str(ap) + " cm (ap) " + str(axial) + " cm (axial) " + str(cc) + " cm (cc)" \
        + " = " + str(volumen) + "  (Normwert: < 30 ml).\n\nLäsion (PIRADS "+ str(PIRADSP) + str(PIRADSZ) + ")\nLokalisation: " + Lokalisation + "(Serie " + str(serie) + "/ Image " + str(image) + "). \nMorphologie: " + str(txtDm) + " mm Durchmesser. Signalverhalten: " \
        + ADC + DWI + T2w

    sentense2 =""

    return sentense1, sentense2