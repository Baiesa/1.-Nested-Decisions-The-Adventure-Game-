attendees = float(input ("Enter number of attendees:"))
venue = str(input("do you prefer audio system/projector"))
food = str(input("do you want vegetarian food? yes/no "))
if attendees > 100:
        print("confrence room")
else:
        print("large hall")
        
if venue == ("projector"):
        print("wow nice view")

if venue == ("audio system"):
         print("enjoy from nice voice")
        
if food == ("yes"):
            print("veggie delight caterers")
elif food == ("no"):
         print("gourmet meals caterers")

else:
    print("we have place for attendees")