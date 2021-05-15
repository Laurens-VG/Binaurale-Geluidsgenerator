import scipy.io.wavfile
import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fft, ifft
from parameters import ITD, IID


def read_input(fname):
    rate, data = scipy.io.wavfile.read(fname)  # data: numpy array
    sample_count = len(data)
    # print(type(data))
    # print(data.dtype)
    return rate, data, sample_count


def stereo2mono(fname):
    rate, data, sample_count = read_input(fname)

    scipy.io.wavfile.write("sounds\channel1.wav", rate, data[:, 0])
    scipy.io.wavfile.write("sounds\channel2.wav", rate, data[:, 1])

    # print("wavfile splitted into \"channel1.wav\" en \"channel2.wav\"")


def mono2stereo(channel1, channel2):
    rate, dataChannel1, sample_countChannel1 = read_input(channel1)
    rate, dataChannel2, sample_countChannel2 = read_input(channel2)

    result = np.vstack((dataChannel1, dataChannel2)).T

    scipy.io.wavfile.write("sounds\stereo.wav", rate, result)
    # print("wavfile \"stereo.wav\" created from two channels: \"channel1.wav\" en \"channel2.wav\"")


def add_azimut(fname, delay, freq_mask_left, freq_mask_right):
    stereo2mono(fname)

    rate, dataChannel1, sample_count = read_input("sounds\channel1.wav")
    rate, dataChannel2, sample_count = read_input("sounds\channel2.wav")

    delayframes = int(delay * rate)
    samples = sample_count + delayframes

    for s in range(samples):
        if s < delayframes:
            dataChannel1 = np.insert(dataChannel1, 0, 0)  # array, place, value , row
        if s >= samples-delayframes:
            dataChannel2 = np.insert(dataChannel2, s-1, 0)

    half = fft(dataChannel1)  # Left
    half = half * freq_mask_left
    dataChannel1 = ifft(half)

    # audio_fft_mag = np.absolute(half)  # spectral magnitude
    # freq = np.linspace(0, 44100, len(audio_fft_mag))  # frequency variable
    # plt.plot(freq[:100000], audio_fft_mag[:100000])  # magnitude spectrum, 22050 als sf= 44100
    # plt.xlabel('Frequency')
    # plt.show()

    half = fft(dataChannel2)  # Right
    half = half * freq_mask_right
    dataChannel2 = ifft(half)

    # audio_fft_mag = np.absolute(half)  # spectral magnitude
    # freq = np.linspace(0, 44100, len(audio_fft_mag))  # frequency variable
    # plt.plot(freq[:100000], audio_fft_mag[:100000])  # magnitude spectrum, 22050 als sf= 44100
    # plt.xlabel('Frequency')
    # plt.show()

    scipy.io.wavfile.write("sounds\channel1.wav", rate, dataChannel1.astype(dtype='int16'))
    scipy.io.wavfile.write("sounds\channel2.wav", rate, dataChannel2.astype(dtype='int16'))

    mono2stereo("sounds\channel1.wav", "sounds\channel2.wav")


if __name__ == "__main__":

    # for i in range(90):
    #     delay = ITD(600, i, 30)
    #     if i == 0:
    #         add_azimut("heli_outside.wav", delay)
    #     else:
    #         add_azimut("stereo.wav", delay)

    degree = 50  # azimut
    freq = 600
    delay = ITD(freq, degree, 30)
    H_left = IID(freq, degree, "left")
    H_right = IID(freq, degree, "right")
    print("delay:", delay)
    print("h_left:", H_left)
    print("h_right:", H_right)
    add_azimut("./sounds/Tetris.wav", delay, H_left, H_right)

    # rate, original, sample_count = read_input("stereo.wav")
    # rate, data, sample_count = read_input("sounds/stereo.wav")
    # plt.plot(original[100:1024])
    # plt.show()
    # plt.plot(data[100:1024])
    # plt.show()

    print("DONE")
