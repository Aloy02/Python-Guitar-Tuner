import numpy as np
import scipy.fftpack

WINDOW_SIZE = 48000  # window size of the DFT in samples
HANN_WINDOW = np.hanning(WINDOW_SIZE)

def compute_magnitude_spectrum(samples, sample_rate, min_freq_hz):
    windowed = samples * HANN_WINDOW
    spectrum = np.abs(scipy.fftpack.fft(windowed)[:len(windowed) // 2])
    freq_step = sample_rate / len(samples)
    spectrum[:int(min_freq_hz / freq_step)] = 0
    return spectrum