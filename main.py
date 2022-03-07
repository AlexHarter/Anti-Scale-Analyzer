"""
The purpose of this program is to generate an anti-scale, 
that is, a complimentary set with an invariable root and possibly fifth depending on user preferences.
It will then analyze the anti-scale for possible chords.
There is no plan to add a GUI.
The features of this program will eventually be transplanted to the larger Scale Architect, with will have a GUI.
"""
import PitchClassConverter
import ChordAnalyzer
#import re

#Use re.split() function so that user can input all notes at once

#User specifies number of pitches in the scale.
#This is limited based on the presupposition that the smallest meaningful number of notes a scale can have is 5.
while True:
    print("How many pitches are in the scale?")
    while True:
        while True:
            UserInputNumberOfPitches = str(input("Enter a number between 5 and 9: "))
            if [A-z] in NumberOfPitches:
                print("That is not a number between 5 and 9.")
            else:
                NumberOfPitches = int(UserInputNumberOfPitches)
                break
        if NumberOfPitches >= 5 and NumberOfPitches <= 9:
            break
        else: print("That is not a number between 5 and 9.")

    #User inputs note names for the original scale.  Later, take away the conversion, so the user can check their scale first.
    UserScaleNoteNames = []
    ScaleDegreeCounter = ("2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th")
    PossibleNoteNames = ("C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B")
    i = 0
    UserScaleNoteNames.append(str(input("Enter the root: ")))
    for x in range(NumberOfPitches-1):
        while True:
            userInputNoteName = str(input("Enter note name of the " + ScaleDegreeCounter[i] + " scale degree: "))
            if PossibleNoteNames.count(userInputNoteName) == 1:
                UserScaleNoteNames.append(userInputNoteName)
                i+=1
                break
            else: print("That is not a note name.")

    #User confirms that scale is correct
    print("Is this your scale?")
    print(UserScaleNoteNames)
    userAnswer = input("Y/n:")
    if userAnswer.lower() != "n":
        break

#User specifies invariable pitches.
invariableFifth = ""
print("Would you like the anti-scale to contain an invariable perfect fifth from the root?")
invariableFifth = str(input("Y/n:"))
if invariableFifth.lower() == "n":
    invariableFifth = False
else: invariableFifth = True

#Convert UserScaleNoteNames to UserScalePitchClasses
UserScalePitchClasses = []
for x in UserScaleNoteNames:
    UserScalePitchClasses.append(PitchClassConverter.NoteNameToPitchClass(x))

#Transpose UserScalePitchClasses to 0 level
TransposedUserScalePitchClasses = PitchClassConverter.TransposePitchClassSetToZero(UserScalePitchClasses)

#generate Anti-Scale pitch classes
ChromaticScalePitchClasses = (0,1,2,3,4,5,6,7,8,9,10,11)
TransposedAntiScalePitchClasses = list(ChromaticScalePitchClasses)
for x in range(12):
    if x == 7 and invariableFifth == True:
        pass
    elif TransposedUserScalePitchClasses.count(x) == 1 and x != 0:
        TransposedAntiScalePitchClasses.remove(x)

#Transpose AntiScale Pitch Classes to User's Original level
transpositionFactor = UserScalePitchClasses[0]
AntiScalePitchClasses = PitchClassConverter.TransposePitchClassSet(TransposedAntiScalePitchClasses, transpositionFactor)

#user specify desired chord qualities to check for
print("What chord qualities would you like to anaylze?")
print("0 = Major and Minor Triads | 1 = All Triads | 2 = All Seventh Chords")
while True:
    chordQualitiesToAnalyze = int(input("0, 1, or 2: "))
    if chordQualitiesToAnalyze >= 0 and chordQualitiesToAnalyze <= 2:
        break
    else: print("That is not 0, 1, or 2")

#Analyze for user-specified chord qualities
AntiScaleChords = []
if chordQualitiesToAnalyze == 0:
    AntiScaleChords = ChordAnalyzer.IdentifyMajorAndMinorTriads(AntiScalePitchClasses)
elif chordQualitiesToAnalyze == 1:
    AntiScaleChords = ChordAnalyzer.IdentifyAllTriads(AntiScalePitchClasses)
elif chordQualitiesToAnalyze == 2:
    AntiScaleChords = ChordAnalyzer.IdentifyAllSeventhChords(AntiScalePitchClasses)

#convert new pitch class set to note names (see NoteNameConverter)
AntiScaleNoteNames = []
for x in range(len(AntiScalePitchClasses)):
    AntiScaleNoteNames.append(PitchClassConverter.PitchClassToNoteName(AntiScalePitchClasses[x]))

#Print Anti-scale with chord possibilities
if invariableFifth == True:
    print ("Here is the anti-scale (with an invariable perfect fifth)")
else: print("Here is your anti-scale:")
print(AntiScaleNoteNames)
print(AntiScaleChords)

#Reevaluate variable names to be more clear