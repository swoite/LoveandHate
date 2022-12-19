import math

def freq_to_note(freq):
    '''Converts frequency to musical note and octave based on function found at
    https://en.wikipedia.org/wiki/Piano_key_frequencies
    '''
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    note_number = 12 * math.log2(freq / 440) + 49  
    note_number = round(note_number)

    note = (note_number - 1 ) % len(notes)
    note = notes[note]
 
    octave = (note_number + 8 ) // len(notes)
  
    return note, octave


if __name__ == '__main__':
    print(freq_to_note(440))
