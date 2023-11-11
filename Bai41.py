note = input("Enter the note name: ")
letter=note[0]
if len(note) == 2:
    octave = int(note[1])
else:
    octave = int(note[1:])
if letter == 'C':
    frequency = 261.63 / (2 ** (4 - octave))
elif letter == 'D':
    frequency = 293.66 / (2 ** (4 - octave))
elif letter == 'E':
    frequency = 329.63 / (2 ** (4 - octave))
elif letter == 'F':
    frequency = 349.23 / (2 ** (4 - octave))
elif letter == 'G':
    frequency = 392.00 / (2 ** (4 - octave))
elif letter == 'A':
    frequency = 440.00 / (2 ** (4 - octave))
elif letter == 'B':
    frequency = 493.88 / (2 ** (4 - octave))
print("The frequency of", note, "is", round(frequency, 2), "Hz.")