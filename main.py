"""
The purpose of this program is to generate an anti-scale, 
that is, a complimentary set with an invariable root and possibly fifth depending on user preferences.
It will then analyze the anti-scale for possible user-specified chords.
"""
import PitchClassConverter as pcc
import ChordAnalyzer as ca

ScaleDegreeCounter = ("2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th")
AllNoteNames = ("c", "c#", "db", "d", "d#", "eb", "e", "f", "f#", "gb", "g", "g#", "ab", "a", "a#", "bb", "b")

#User inputs scale
while True:
    #User specifies number of pitches in the scale.
    #This is limited to between 5 and 9 based on the presupposition that the smallest meaningful number of notes a scale can have is 5.
    #And a scale of 9 pitches would yield an anti-scale of 5 pitches.
    UserScaleNoteNames = []
    print("How many pitches are in the scale?")
    while True:
        try: NumberOfPitches = int(input("Enter a number between 5 and 9, inclusive: "))
        except: print("That is not an integer.")
        else:
            if NumberOfPitches >= 5 and NumberOfPitches <= 9: break
            else: print("That is not a number between 5 and 9.")

    #User inputs note names for the original scale.
    #Before input is added to Scale list, check to ensure that it is
    #a valid note name; not a duplicate (not for root); and ascending (not for root).
    i = -1
    for x in range(NumberOfPitches):
        while True:
            scaleValidity = True
            if i == -1:
                userInputNoteName = str(input("Enter the note name of the root: ")).lower()
                if AllNoteNames.count(userInputNoteName) is 0:
                    print("That is not a note name.")
                else:
                    UserScaleNoteNames.append(userInputNoteName)
                    i+=1
                    break
            elif i >= 0:
                userInputNoteName = str(input("Enter the note name of the " + ScaleDegreeCounter[i] + " scale degree: ")).lower()
                if AllNoteNames.count(userInputNoteName) is 0:
                    print("That is not a note name.")
                elif UserScaleNoteNames.count(userInputNoteName) is 1:
                    print("That is a duplicate pitch.")
                    #BUG this doesn't account for enharmonic spellings.
                elif pcc.NoteNameToPitchClass(userInputNoteName) > ((pcc.NoteNameToPitchClass(UserScaleNoteNames[i])+4)%12):
                        #based on the presupposition that a scale would not contain an interval greater than a Major Third.
                        print("The pitches should be entered in ascending order.")
                else:
                    UserScaleNoteNames.append(userInputNoteName)
                    i+=1
                    break

    #Note name capitilization is corrected.
    i = 0
    for x in UserScaleNoteNames:
        if len(x) is 1: UserScaleNoteNames[i] = x[0].upper()
        elif len(x) is 2: UserScaleNoteNames[i] = x[0].upper() + x[1]
        i+=1

    #User confirms that scale is correct. If not, restart process.
    print("Is this your scale?")
    print(UserScaleNoteNames)
    userAnswer = input("Y/n:")
    if userAnswer.lower() != "n": break

#User specifies invariable pitches.
print("Would you like the anti-scale to contain an invariable perfect fifth from the root?")
invariableFifth = input("Y/n: ")
if invariableFifth.lower() is "n": invariableFifth = False
else: invariableFifth = True

#Converts UserScaleNoteNames to UserScalePitchClasses
#TODO implement this to happen at the same time as building UserScaleNoteNames so that duplicate pitches can be checked.
UserScalePitchClasses = []
for x in UserScaleNoteNames:
    UserScalePitchClasses.append(pcc.NoteNameToPitchClass(x))

#Transposes UserScalePitchClasses to 0 level
TransposedUserScalePitchClasses = pcc.TransposePitchClassSetToZero(UserScalePitchClasses)

#generates Anti-Scale pitch classes
AllPitchClasses = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
TransposedAntiScalePitchClasses = list(AllPitchClasses)
for x in range(12):
    if x == 7 and invariableFifth is True: pass
    elif TransposedUserScalePitchClasses.count(x) == 1 and x != 0:
        TransposedAntiScalePitchClasses.remove(x)

#Transposes AntiScale Pitch Classes to User's Original level
transpositionFactor = UserScalePitchClasses[0]
AntiScalePitchClasses = pcc.TransposePitchClassSet(TransposedAntiScalePitchClasses, transpositionFactor)

#User specifies desired chord qualities to analyze
print("What chord qualities would you like to anaylze?")
print("0 = Major and Minor Triads | 1 = All Triads | 2 = All Seventh Chords")
while True:
    try:
        chordQualities = int(input("0, 1, or 2: "))
        if chordQualities >= 0 and chordQualities <= 2: break
        else: print("That is not 0, 1, or 2")
    except: print("That is not an integer.")

#Analyzes for user-specified chord qualities
AntiScaleChords = []
match chordQualities:
    case 0: AntiScaleChords = ca.IdentifyMajorAndMinorTriads(AntiScalePitchClasses)
    case 1: AntiScaleChords = ca.IdentifyAllTriads(AntiScalePitchClasses)
    case 2: AntiScaleChords = ca.IdentifyAllSeventhChords(AntiScalePitchClasses)

#convert new pitch class set to note names (see NoteNameConverter)
AntiScaleNoteNames = []
for x in range(len(AntiScalePitchClasses)):
    AntiScaleNoteNames.append(pcc.PitchClassToNoteName(AntiScalePitchClasses[x]))

#Print Anti-scale
match invariableFifth:
    case True: print("Here is your anti-scale (with an invariable perfect fifth):")
    case False: print("Here is your anti-scale (without an invariable perfect fifth):")
print(AntiScaleNoteNames)

#Print chord possibilities
match chordQualities:
    case 0: chordsAnalyzed = "Major and Minor Triads"
    case 1: chordsAnalyzed = "Triads"
    case 2: chordsAnalyzed = "Seventh Chords"
print("Here are the possible " + chordsAnalyzed + " that can be made with your anti-scale:")
print(AntiScaleChords)