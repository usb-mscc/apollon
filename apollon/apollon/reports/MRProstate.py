
def create(form):

    #date = form["date"]

    if date == "********":
        date = "Zum Vergleich leigen die Voraufnahmen vom ******** vor"
    else date == "":
        date = "Es liegen keine Voraufnahmen zum Vergleich vor"


    artefakte = form.get("artefakte", "")
    if artefakte == "on":
        artefakte = "Eingeschränkte Beurteilbarkeit bei ausgeprägten Bewegungsartefakten."
    else:
        artefakte = ""

    ap = int(form["ap"])
    axial = int(form["axial"])
    cc = int(form["cc"])
    volumen = 0
    volumen = ap*axial*cc*0.52

    #Base rechts
    AFSbaserechts = form.get("AFSbaserechts", "")
    if AFSbaserechts == "on":
        AFSbaserechts = "Prostatabasis anteriores fibromuskulares Stroma rechts"
    else:
        AFSbaserechts = ""

    TZabaserechts = form.get("TZabaserechts", "")
    if TZabaserechts == "on":
        TZabaserechts = "Prostatabasis anteriore Transitionalzone rechts"
    else:
        TZabaserechts = ""

    PZabaserechts = form.get("PZabaserechts", "")
    if PZabaserechts == "on":
        PZabaserechts = "Prostatabasis anteriore Peripherzone rechts"
    else:
        PZabaserechts = ""

    TZpbaserechts = form.get("TZpbaserechts", "")
    if TZpbaserechts == "on":
        TZpbaserechts = "Prostatabasis posteriore Transitionalzone rechts"
    else:
        TZpbaserechts = ""
    
    PZpbaserechts = form.get("PZpbaserechts", "")
    if PZpbaserechts == "on":
        PZpbaserechts = "Prostatabasis posteriore Peripherzone rechts"
    else:
        PZpbaserechts = ""

    CZbaserechts = form.get("CZbaserechts", "")
    if CZbaserechts == "on":
        CZbaserechts = "Prostatabasis posteriore Zentralzone rechts"
    else:
        CZbaserechts = ""

    #Base links
    AFSbaselinks = form.get("AFSbaselinks", "")
    if AFSbaselinks == "on":
        AFSbaselinks = "Prostatabasis anteriores fibromuskulares Stroma links"
    else:
        AFSbaselinks = ""

    TZabaselinks = form.get("TZabaselinks", "")
    if TZabaselinks == "on":
        TZabaselinks = "Prostatabasis anteriore Transitionalzone links"
    else:
        TZabaselinks = ""

    PZabaselinks = form.get("PZabaselinks", "")
    if PZabaselinks == "on":
        PZabaselinks = "Prostatabasis anteriore Peripherzone links"
    else:
        PZabaselinks = ""

    TZpbaselinks = form.get("TZpbaselinks", "")
    if TZpbaselinks == "on":
        TZpbaselinks = "Prostatabasis posteriore Transitionalzone links"
    else:
        TZpbaselinks = ""
    
    PZpbaselinks = form.get("PZpbaselinks", "")
    if PZpbaselinks == "on":
        PZpbaselinks = "Prostatabasis posteriore Peripherzone links"
    else:
        PZpbaselinks = ""

    CZbaselinks = form.get("CZbaselinks", "")
    if CZbaselinks == "on":
        CZbaselinks = "Prostatabasis posteriore Zentralzone links"
    else:
        CZbaselinks = ""

    #Mid rechts
    AFSmidrechts = form.get("AFSmidrechts", "")
    if AFSmidrechts == "on":
        AFSmidrechts = "Mittlere Prostata anteriores fibromuskulares Stroma rechts"
    else:
        AFSmidrechts = ""

    TZamidrechts = form.get("TZamidrechts", "")
    if TZamidrechts == "on":
        TZamidrechts = "Mittlere Prostata anteriore Transitionalzone rechts"
    else:
        TZamidrechts = ""

    PZamidrechts = form.get("PZamidrechts", "")
    if PZamidrechts == "on":
        PZamidrechts = "Mittlere Prostata anteriore Peripherzone rechts"
    else:
        PZamidrechts = ""

    TZpmidrechts = form.get("TZpmidrechts", "")
    if TZpmidrechts == "on":
        TZpmidrechts = "Mittlere Prostata posteriore Transitionalzone rechts"
    else:
        TZpmidrechts = ""
    
    PZpmidrechts = form.get("PZpmidrechts", "")
    if PZpmidrechts == "on":
        PZpmidrechts = "Mittlere Prostata posteriore Peripherzone rechts"
    else:
        PZpmidrechts = ""

    PZmmiderechts = form.get("PZmmiderechts", "")
    if PZmmiderechts == "on":
        PZmmiderechts = "Mittlere Prostata posteriore Zentralzone rechts"
    else:
        PZmmiderechts = ""

    #Mid links
    AFSmidlinks = form.get("AFSmidlinks", "")
    if AFSmidlinks == "on":
        AFSmidlinks = "Mittlere Prostata anteriores fibromuskulares Stroma links"
    else:
        AFSmidlinks = ""

    TZamidlinks = form.get("TZamidlinks", "")
    if TZamidlinks == "on":
        TZamidlinks = "Mittlere Prostata anteriore Transitionalzone links"
    else:
        TZamidlinks = ""

    PZamidlinks = form.get("PZamidlinks", "")
    if PZamidlinks == "on":
        PZamidlinks = "Mittlere Prostata anteriore Peripherzone links"
    else:
        PZamidlinks = ""

    TZpmidlinks = form.get("TZpmidlinks", "")
    if TZpmidlinks == "on":
        TZpmidlinks = "Mittlere Prostata posteriore Transitionalzone links"
    else:
        TZpmidlinks = ""
    
    PZpmidlinks = form.get("PZpmidlinks", "")
    if PZpmidlinks == "on":
        PZpmidlinks = "Mittlere Prostata posteriore Peripherzone links"
    else:
        PZpmidlinks = ""

    PZmmidlinks = form.get("PZmmidlinks", "")
    if PZmmidlinks == "on":
        PZmmidlinks = "Mittlere Prostata posteriore Zentralzone links"
    else:
        PZmmidlinks = ""

    #Apex rechts
    AFSapexrechts = form.get("AFSapexrechts", "")
    if AFSapexrechts == "on":
        AFSapexrechts = "Prostataapex anteriores fibromuskulares Stroma rechts"
    else:
        AFSapexrechts = ""

    TZaapexrechts = form.get("TZaapexrechts", "")
    if TZaapexrechts == "on":
        TZaapexrechts = "Prostataapex anteriore Transitionalzone rechts"
    else:
        TZaapexrechts = ""

    PZaapexrechts = form.get("PZaapexrechts", "")
    if PZaapexrechts == "on":
        PZaapexrechts = "Prostataapex anteriore Peripherzone rechts"
    else:
        PZaapexrechts = ""

    TZpapexrechts = form.get("TZpapexrechts", "")
    if TZpapexrechts == "on":
        TZpapexrechts = "Prostataapex posteriore Transitionalzone rechts"
    else:
        TZpapexrechts = ""
    
    PZpapexrechts = form.get("PZpapexrechts", "")
    if PZpapexrechts == "on":
        PZpapexrechts = "Prostataapex posteriore Peripherzone rechts"
    else:
        PZpapexrechts = ""

    PZmapexrechts = form.get("PZmapexrechts", "")
    if PZmapexrechts == "on":
        PZmapexrechts = "Prostataapex posteromedial Zentralzone rechts"
    else:
        PZmapexrechts = ""

    #Apex links
    AFSapexlinks = form.get("AFSapexlinks", "")
    if AFSapexlinks == "on":
        AFSapexlinks = "Prostataapex anteriores fibromuskulares Stroma links"
    else:
        AFSapexlinks = ""

    TZaapexlinks = form.get("TZaapexlinks", "")
    if TZaapexlinks == "on":
        TZaapexlinks = "Prostataapex anteriore Transitionalzone links"
    else:
        TZaapexlinks = ""

    PZaapexlinks = form.get("PZaapexlinks", "")
    if PZaapexlinks == "on":
        PZaapexlinks = "Prostataapex anteriore Peripherzone links"
    else:
        PZaapexlinks = ""

    TZpapexlinks = form.get("TZpapexlinks", "")
    if TZpapexlinks == "on":
        TZpapexlinks = "Prostataapex posteriore Transitionalzone links"
    else:
        TZpapexlinks = ""
    
    PZpapexlinks = form.get("PZpapexlinks", "")
    if PZpapexlinks == "on":
        PZpapexlinks = "Prostataapex posteriore Peripherzone links"
    else:
        PZpapexlinks = ""

    PZmapexlinks = form.get("PZmapexlinks", "")
    if PZmapexlinks == "on":
        PZmapexlinks = "Prostataapex posteromedial Zentralzone links"
    else:
        PZmapexlinks = ""

    txtDm = form["durchmesser"]

    ADC = form["ADC"]
    if ADC == "ADC1":
        ADC = ""
    elif ADC == "ADC2":
        ADC = "mit geringer Diffusionsrestriktion"
    elif ADC == "ADC3":
        ADC = "mit fokaler Diffusionsrestriktion"
    else:
        ADC = "mit flächiger Diffusionsrestriktion"

    DWI = form["DWI"]
    if DWI == "DWI1":
        DWI = ""
    else DWI == "DWI2":
        DWI = "Undeutlich hyperintens in der DWI"

    DWIMessung = form["DWIMessung"]

    T2w = form["T2w"]
    if T2w == "T2w1":
        T2w = ""
    elif T2w == "T2w2":
        T2w = "Nodulär hypointens"
    elif T2w == "T2w3":
        T2w = "Unscharf hypointens"
    else:
        T2w = "Linsenförmig hypointens"

    sabla = form.get("tumorfreie_sabla", "")
    sablapt3b = 0

    #if sabla == "on":
    #    sabla = "Tumorfreie Samenblase. "
    #    sablapt3b = 0
    #else:
    #    sabla = "Infiltration der Samenblase. "
    #    sablapt3b = 1
#
#
    #ep = form.get("extraprostatisches_wachstum", "")
    #ep1 = 0
    #if ep == "on":
    #    ep = "Extraprostatisches Wachstum. "
    #    ep1 = 1
    #else:
    #    ep = "Kein Extraprostatisches Wachstum. "
    #    ep1 = 0
#
    sentense1 = "Befund\n" + "\n\nProstatavolumen: " + str(ap) + " (ap) " + str(axial) + " (axial) " + str(cc) + " (cc) " \
        + " = " + volumen + "(Normwert: < 30 ml).\n\nLäsionen\nLokalisation: " + AFSbaserechts + TZabaserechts + PZabaserechts + TZpbaserechts + PZpbaserechts + CZbaserechts + AFSbaselinks + TZabaselinks + PZabaselinks + TZpbaselinks + PZpbaselinks + CZbaselinks  + AFSmidrechts + TZamidrechts + PZamidrechts + TZpmidrechts + PZpmidrechts + PZmmiderechts + AFSmidlinks + TZamidlinks + PZamidlinks + TZpmidlinks + PZpmidlinks + PZmmidlinks + AFSapexrechts + TZaapexrechts + PZaapexrechts + TZpapexrechts + PZpapexrechts + PZmapexrechts + AFSapexlinks + TZaapexlinks + PZaapexlinks + TZpapexlinks + PZpapexlinks + PZmapexlinks\
        + txtDm + ADC + ADCMessung + DWI + DWIMessung + T2w

    return sentense1