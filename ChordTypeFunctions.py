import NoteNameConverter

"""
#Major Triads
def IdentifyMajorTriads(PitchClassSet):
    for x in PitchClassSet:
        if (x+4)%12 in PitchClassSet and (x+7)%12 in PitchClassSet:
            ListOfChords.append(str(NoteNameConverter.PitchClassToNoteName(x) + " Major"))
    return ListOfChords

#Test:
#SamplePitchClassSet = [0, 2, 4, 5, 7, 9, 11]
#print(IdentifyMajorTriads(SamplePitchClassSet))


#Minor Triads

def IdentifyMinorTriads(PitchClassSet):
    for x in PitchClassSet:
        if (x+3)%12 in PitchClassSet and (x+7)%12 in PitchClassSet:
            ListOfChords.append(str(NoteNameConverter.PitchClassToNoteName(x) + " Minor"))
    return ListOfChords


#Diminished Triads

def IdentifyDiminishedTriads(PitchClassSet):
    for x in PitchClassSet:
        if (x+3)%12 in PitchClassSet and (x+6)%12 in PitchClassSet:
            ListOfChords.append(str(NoteNameConverter.PitchClassToNoteName(x) + " Diminished"))
    return ListOfChords


#Augmented Triads

def IdentifyAugmentedTriads(PitchClassSet):
    for x in PitchClassSet:
        if (x+4)%12 in PitchClassSet and (x+8)%12 in PitchClassSet:
            ListOfChords.append(str(NoteNameConverter.PitchClassToNoteName(x) + " Augmented"))
    return ListOfChords
"""
ListOfChords = []

#Minor and Major Triads
def IdentifyMajorAndMinorTriads(PitchClassSet):
    for x in PitchClassSet:
        if (x+4)%12 in PitchClassSet and (x+7)%12 in PitchClassSet:
            ListOfChords.append(NoteNameConverter.PitchClassToNoteName(x) + " Major")
        if (x+3)%12 in PitchClassSet and (x+7)%12 in PitchClassSet:
            ListOfChords.append(NoteNameConverter.PitchClassToNoteName(x) + " Minor")
    if ListOfChords == "":    
        ListOfChords.append("No Major or Minor Triads")
    return ListOfChords

#All Triads
def IdentifyAllTriads(PitchClassSet):
    for x in PitchClassSet:
        if (x+4)%12 in PitchClassSet and (x+7)%12 in PitchClassSet:
            ListOfChords.append(str(NoteNameConverter.PitchClassToNoteName(x) + " Major"))
        if (x+3)%12 in PitchClassSet and (x+7)%12 in PitchClassSet:
            ListOfChords.append(str(NoteNameConverter.PitchClassToNoteName(x) + " Minor"))
        if (x+3)%12 in PitchClassSet and (x+6)%12 in PitchClassSet:
            ListOfChords.append(str(NoteNameConverter.PitchClassToNoteName(x) + " Diminished"))
        if (x+4)%12 in PitchClassSet and (x+8)%12 in PitchClassSet:
            ListOfChords.append(str(NoteNameConverter.PitchClassToNoteName(x) + " Augmented"))
    if ListOfChords == "": 
        ListOfChords.append("No Triads")
    return ListOfChords

#All Seventh Chords
def IdentifyAllSeventhChords(PitchClassSet):
    for x in PitchClassSet:
        #Major 7
        if (x+4)%12 in PitchClassSet and (x+7)%12 and (x+11)%12 in PitchClassSet:
                ListOfChords.append(str(NoteNameConverter.PitchClassToNoteName(x) + " Major 7"))
        #Dominant 7
        if (x+4)%12 in PitchClassSet and (x+7)%12 and (x+10)%12 in PitchClassSet:
                ListOfChords.append(str(NoteNameConverter.PitchClassToNoteName(x) + " Dominant 7"))
        #Minor 7
        if (x+3)%12 in PitchClassSet and (x+7)%12 and (x+10)%12 in PitchClassSet:
                ListOfChords.append(str(NoteNameConverter.PitchClassToNoteName(x) + " Minor 7"))
        #Minor-Major 7
        if (x+3)%12 in PitchClassSet and (x+7)%12 and (x+11)%12 in PitchClassSet:
                ListOfChords.append(str(NoteNameConverter.PitchClassToNoteName(x) + " Minor-Major 7"))
        #Half-Dimished 7
        if (x+3)%12 in PitchClassSet and (x+6)%12 and (x+10)%12 in PitchClassSet:
                ListOfChords.append(str(NoteNameConverter.PitchClassToNoteName(x) + " Half-Dimished 7"))
        #Fully Diminished 7
        if (x+3)%12 in PitchClassSet and (x+7)%12 and (x+9)%12 in PitchClassSet:
                ListOfChords.append(str(NoteNameConverter.PitchClassToNoteName(x) + " Fully-Diminished 7"))
        #Augmented 7
        if (x+4)%12 in PitchClassSet and (x+8)%12 and (x+11)%12 in PitchClassSet:
                ListOfChords.append(str(NoteNameConverter.PitchClassToNoteName(x) + " Augmented 7"))
    if ListOfChords == "": 
        ListOfChords.append("No Seventh Chords")
    return ListOfChords


"""
Secundal Triads & Tetrads (How to label?)
Tertian Triads & Tetrads
Quartal Triads & Tetrads (How to label?)
Quintal Triads & Tetrads (Redundant?)
"""