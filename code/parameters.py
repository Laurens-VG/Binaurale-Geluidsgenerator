from pydub import AudioSegment
import math


# AZIMUT AND ELEVATION #####################################################


def ITD(freq, azimut_value, elevation_value):
    head_radius = 0.075
    azimut_value = azimut_value * math.pi/180  # degree to radian
    elevation_value = elevation_value * math.pi/180

    if freq < 500:
        ITD = (head_radius / 343) * 2 * (math.sin(azimut_value))  # 343 is speed of sound
    else:
        ITD = (head_radius / 343) * (math.asin(math.cos(azimut_value)*math.sin(elevation_value)) + (math.cos(elevation_value)*math.sin(azimut_value)))
    return ITD


def IID(freq, azimut_value, side):
    head_radius = 0.075
    beta = (2 * 434) / head_radius
    azimut_value = azimut_value * math.pi / 180

    if side == "left":
        H = ((1 + math.cos(azimut_value + math.pi/2)) * freq + beta) / (freq + beta)
    elif side == "right":
        H = ((1 + math.cos(azimut_value - math.pi/2)) * freq + beta) / (freq + beta)
    else:
        print("No side selected")
        return None
    return H


# RADIUS #####################################################


def change_radius(fname, distance, reference_distance=0.5):
    song = AudioSegment.from_wav(fname)
    print("rms: ", song.rms)
    # print("data: ", song._data)
    rel_dist = float(reference_distance) / float(distance)
    radiusdB = 20.0 * (math.log(rel_dist) / math.log(10))
    print("radius", radiusdB)
    # change sound
    song = song + radiusdB
    # save the output
    song.export("sounds\changed.wav", "wav")


# MAIN #####################################################


if __name__ == "__main__":
    print("Parameters:")
    fname = "./sounds/Joey.wav"
    # change_radius(fname, 2, 1.0)
    # change_radius(fname, 2, 1.0)
    # play_sound()
    # IID(600, 0.0005, "right")
    # IID(600, 0.0005, "left")
    change_radius(fname, 1)
