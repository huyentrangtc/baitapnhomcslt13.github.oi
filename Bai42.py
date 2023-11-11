f=float(input(""))
if 260.63<=f<=262.3:
    note="C4"
elif 292.66<=f<=293.63:
    note="D4"
elif 328.63<=f<=330.63:
    note="E4"
elif 348.23<=f<=350.23:
    note="F4"
elif 391.00<=f<=323.:
    note="G4"
elif 439.00<=f<=441.00:
    note="A4"
elif 492.88<=f<=494.88:
    note="B4"
else:
    note="There is no need to consider notes from other octaves"
print(note)