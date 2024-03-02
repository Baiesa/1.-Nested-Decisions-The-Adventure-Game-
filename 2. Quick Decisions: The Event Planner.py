attendees = float(input ("Enter number of attendees:"))
venue = "large hall" 
if attendees > 50:
    print("large hall")
elif attendees < 50:
    print("small hall")
else:
    print("we have place for attendees")