import NoteNameConversion

ListOfChords = []

#Major Triads
def IdentifyMajorTriads(PitchClassSet):
    for x in PitchClassSet:
        if (x+4)%12 in PitchClassSet and (x+7)%12 in PitchClassSet:
            ListOfChords.append(str(NoteNameConversion.PitchClassToNoteName(x) + " Major"))
    return ListOfChords

#Test:
#SamplePitchClassSet = [0, 2, 4, 5, 7, 9, 11]
#print(IdentifyMajorTriads(SamplePitchClassSet))


#Minor Triads

def IdentifyMinorTriads(PitchClassSet):
    for x in PitchClassSet:
        if (x+3)%12 in PitchClassSet and (x+7)%12 in PitchClassSet:
            ListOfChords.append(str(NoteNameConversion.PitchClassToNoteName(x) + " Minor"))
    return ListOfChords


#Diminished Triads

def IdentifyDiminishedTriads(PitchClassSet):
    for x in PitchClassSet:
        if (x+3)%12 in PitchClassSet and (x+6)%12 in PitchClassSet:
            ListOfChords.append(str(NoteNameConversion.PitchClassToNoteName(x) + " Diminished"))
    return ListOfChords


#Augmented Triads

def IdentifyAugmentedTriads(PitchClassSet):
    for x in PitchClassSet:
        if (x+4)%12 in PitchClassSet and (x+8)%12 in PitchClassSet:
            ListOfChords.append(str(NoteNameConversion.PitchClassToNoteName(x) + " Augmented"))
    return ListOfChords


#Minor and Major Triads

def IdentifyMajorAndMinorTriads(PitchClassSet):
    for x in PitchClassSet:
        if (x+4)%12 in PitchClassSet and (x+7)%12 in PitchClassSet:
            ListOfChords.append(str(NoteNameConversion.PitchClassToNoteName(x) + " Major"))
        if (x+3)%12 in PitchClassSet and (x+7)%12 in PitchClassSet:
            ListOfChords.append(str(NoteNameConversion.PitchClassToNoteName(x) + " Minor"))
        else: 
            ListOfChords = "No Major or Minor Triads"
    return ListOfChords


#All Triads
def IdentifyAllTriads(PitchClassSet):
    for x in PitchClassSet:
            if (x+4)%12 in PitchClassSet and (x+7)%12 in PitchClassSet:
                ListOfChords.append(str(NoteNameConversion.PitchClassToNoteName(x) + " Major"))
            if (x+3)%12 in PitchClassSet and (x+7)%12 in PitchClassSet:
                ListOfChords.append(str(NoteNameConversion.PitchClassToNoteName(x) + " Minor"))
            if (x+3)%12 in PitchClassSet and (x+6)%12 in PitchClassSet:
                ListOfChords.append(str(NoteNameConversion.PitchClassToNoteName(x) + " Diminished"))
            if (x+4)%12 in PitchClassSet and (x+8)%12 in PitchClassSet:
                ListOfChords.append(str(NoteNameConversion.PitchClassToNoteName(x) + " Augmented"))
            else:
                ListOfChords = "No Triads"
    return ListOfChords

#All Seventh Chords

"""
Secundal Triads & Tetrads (How to label?)
Tertian Triads & Tetrads
Quartal Triads & Tetrads (How to label?)
Quintal Triads & Tetrads (Redundant?)
"""