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
print("How many pitches are in the scale?")
NumberOfPitches = int(input("Enter a number between 5 and 9: "))

#User inputs note names for the original scale.  Later, take away the conversion, so the user can check their scale first.
UserScaleNoteNames = []
ScaleDegreeCounter = ("2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th")
i = 0
UserScaleNoteNames.append(str(input("Enter the root: ")))
for x in range(NumberOfPitches-1):
    UserScaleNoteNames.append(str(input("Enter the " + ScaleDegreeCounter[i] + " scale degree: ")))
    i+=1

#User checks that scale is correct, if not program is ended.  Later, add feature to redo the input instead.
print("Is this your scale?")
print(UserScaleNoteNames)
userAnswer = input("Y/n:")
if userAnswer == "N" or userAnswer == "n":
    exit()

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
print(TransposedUserScalePitchClasses)

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
chordQualitiesToAnalyze = int(input("0 = Major and Minor Triads | 1 = All Triads | 2 = All Seventh Chords : "))

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
print(AntiScaleNoteNames)
print(AntiScaleChords)

#Reevluate variable names to be more clear