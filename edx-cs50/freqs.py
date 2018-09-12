from math import pow
from sys import argv
from collections import defaultdict
import json

fname = argv[1]
notes = {"C": 1, "C#": 2, "D": 3, "D#": 4, "E": 5, "F": 6,
         "F#": 7, "G": 8, "G#": 9, "A": 10, "A#": 11, "B": 12}


def to_freqs(note):
    tmp_letter = note.split('@')[0]
    letter = tmp_letter[:-1]
    octave = int(tmp_letter[-1])
    if letter in notes:
        semitone = notes[letter]
        tmp_freq = round(pow(2.0, (semitone - 10.0)/12) * 440, 0)
    return letter, pow(2.0, (octave - 4)) * tmp_freq


with open(fname) as f:
    frequencies = defaultdict(list)
    count = defaultdict(int)
    for line in f:
        note, freq = to_freqs(line.rstrip())
        frequencies[note].append(freq)
    for k, v in frequencies.items():
        count[k] = len(v)
    print("Frequencies: {0!s}".format(json.dumps(frequencies)))
    print("Amount of frequencies per note: {0!s}".format(json.dumps(count)))
