#1
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else: pass
elif place == "cave":
    print("You find a hidden treasure!")
    action2 = input("light a torch or proceed in the dark ")
    if action2 == "light a torch":
        print("There are giant spiders cowering from the light!")
    elif action2 == "proceed in the dark":
        print("You are attcked by giant spiders!")
    else: pass
else: pass

#2
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
venue = venue + " with an audio system" if attendees > 75 else venue
venue = venue + " and a projector" if attendees > 150 else venue

print(venue)

veg = input("Would you like vegetarian food? ")
if veg == "yes":
    print("We recommend Veggie Delight Caterers")
else:
    print("We recommend Gourmet Meals Cateres")