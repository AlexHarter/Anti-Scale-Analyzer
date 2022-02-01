
"""
I could do a series of elseif statements, but that seems kind of dinosaur
Or, I could use a dictionary?
Or, perhaps I should use a similar method to my FizzBuzz program and start with the array or list then modify
"""

def NameToPitchClass(noteName):
    if noteName.lower() == "c":
        return 0
    elif noteName.lower() == "c#" or noteName.lower() == "db":
        return 1
    elif noteName.lower() == "d":
        return 2
    elif noteName.lower() == "d#" or noteName.lower() == "eb":
        return 3
    elif noteName.lower() == "e":
        return 4
    elif noteName.lower() == "f":
        return 5
    elif noteName.lower() == "f#" or noteName.lower() == "gb":
        return 6
    elif noteName.lower() == "g":
        return 7
    elif noteName.lower() == "g#" or noteName.lower() == "ab":
        return 8
    elif noteName.lower() == "a":
        return 9
    elif noteName.lower() == "a#" or noteName.lower() == "bb":
        return 10
    elif noteName.lower() == "b":
        return 11
    else:
        return -1


def PitchClassToName(pitchClass):
    if pitchClass == 0:
        return "C"
    elif pitchClass == 1:
        return "C#"
    elif pitchClass == 2:
        return "D"
    elif pitchClass == 3:
        return "D#"
    elif pitchClass == 4:
        return "E"
    elif pitchClass == 5:
        return "F"
    elif pitchClass == 6:
        return "F#"
    elif pitchClass == 7:
        return "G"
    elif pitchClass == 8:
        return "G#"
    elif pitchClass == 9:
        return "A"
    elif pitchClass == 10:
        return "A#"
    elif pitchClass == 11:
        return "B"
    else:
        return "error"

