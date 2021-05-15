import time
import cv2
from input_binaural import add_azimut
from split_sound import split
from headtracking_distance import headtracking_image
from parameters import ITD, IID, change_radius
import winsound
# import pygame


def main(fname):
    starttime = time.time()
    teller = 0
    sec = 3
    j = sec
    i = 0
    k = -180
    for x in range(0, 100):
        if x % sec == 0:
            split(x, j, fname, teller)
            j += sec
            teller += 1

    while True:
        fname = "sounds\splitted\\" + "newSong" + str(i) + ".wav"
        # if(switch):
        distance, degree, elevation = headtracking_image()
        # else:
        #   distance, degree, elevation = returnParameters()
        print("distance: " + str(distance))
        print("degree: " + str(degree))
        print("elevation: " + str(elevation))
        implement_parameters(fname, distance, degree, elevation, 600)
        play_sound()
        time.sleep(float(sec) - ((time.time() - starttime) % float(sec)))
        i += 1


def implement_parameters(fname, distance, degree, elevation, freq):
    # implement parameters
    delay = ITD(freq, degree, elevation)
    H_left = IID(freq, degree, "left")
    H_right = IID(freq, degree, "right")
    print("delay:", delay)
    print("h_left:", H_left)
    print("h_right:", H_right)
    add_azimut(fname, delay, H_left, H_right)
    change_radius("sounds\stereo.wav", distance)


def play_sound():
    # pygame.init()
    # pygame.mixer.music.load("sounds/changed.wav")
    # pygame.mixer.music.play()
    # pygame.event.wait()
    winsound.PlaySound("sounds\changed.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)


if __name__ == "__main__":
    main("sounds\Tetris.wav")
