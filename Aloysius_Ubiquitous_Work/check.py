NOTE_FREQUENCIES = {"E2": 82, "A2": 110, "D3": 147, "G3": 196, "B4": 247, "F4": 349.23, "E4": 330}

# Change this to the user's desired frequency.
desired_note = "E2"

def check(closest_note, estimated_frequency):
    if closest_note != desired_note:
        difference =  NOTE_FREQUENCIES[desired_note] - estimated_frequency
        if difference > 0:
            print("Tighten string")
        else:
            print("Loosen string")
    else:
        print("The string is tuned!")

