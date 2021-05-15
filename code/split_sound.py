import wave
from pydub import AudioSegment
import math


def split(t1, t2, fname, teller):
    t1 = t1 * 1000  # Works in milliseconds
    t2 = t2 * 1000
    newAudio = AudioSegment.from_wav(fname)
    newAudio = newAudio[t1:t2]
    newAudio.export('sounds\splitted\\newSong' + str(teller) + '.wav', format="wav")


if __name__ == "__main__":
    fname = "./sounds/Joey.wav"
    j = 1
    for x in range(0, 5):
        split(x, j, fname)
        j += 1

