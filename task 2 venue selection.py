attendees = float(input ("Enter number of attendees:"))
venue = str(input("do you prefer audio system/projector"))
if attendees > 50:
    print("large hall")
    if venue == ("audio system"):
        print("enjoy from nice voice")
    elif venue == ("projector"):
        print("wow nice view")
elif attendees < 50:
    print("small hall")
else:
    print("we have place for attendees")
    