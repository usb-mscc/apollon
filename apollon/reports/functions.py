#Abfrage Auswahl
A = form.get("A", None)
B = form.get("B", None)
C = form.get("C", None)
D = form.get("D", None)

# Minimale Anzahl an Sets bilden. Kein Item wurde ausgewählt vs Mindestens 1 Item wurde ausgewählt
SetRechts = {A, B, C}
if len(SetRechts) == 0:
    SetRechts = None
else:
    SetRechts = "Rechts"

SetRechts = "Rechts" if any(SetRechts)

SetLinks = {D}
if len(SetLinks) == 0:
    SetLinks = None
else:
    SetLinks = "Links"

# Abfrage Überlappungen bei Mehrfachauswahl. Keine Überlappung. Überlappung überschreibt Einzelausgabe
SetBeidseits = {SetRechts, SetLinks}
if len(SetBeidseits) == 0:
    SetRechts = None
    SetLinks = None
else:
    SetRechts = "Beidseits"
    SetLinks = None

Sentence = SetRechts, SetLinks, SetBeidseits...