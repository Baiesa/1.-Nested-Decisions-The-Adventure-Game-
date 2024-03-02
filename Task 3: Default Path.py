place = input("Choose a place: forest or cave? ")
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        if place == "river":
            pass
        
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You can see clearly and find an ancient artifact!")
    elif action == "proceed in the dark":
        print("You stumble in the darkness and trip over something.")
        print("Fortunately, you find a hidden stash of gems!")
        