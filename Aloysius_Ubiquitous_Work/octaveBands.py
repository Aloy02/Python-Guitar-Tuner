import numpy as np

bands = [50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]
noise_thresh = 0.2 # everything under WHITE_NOISE_THRESH*avg_energy_per_freq is cut off

def octave_bands(magnitude_spec, change_in_freq):

    for j in range(len(bands) - 1):
        ind_start = int(bands[j] / change_in_freq)
        ind_end = int(bands[j + 1] / change_in_freq)
        if not len(magnitude_spec) > ind_end:
            ind_end = len(magnitude_spec)
        avg_energy_per_freq = (np.linalg.norm(magnitude_spec[ind_start:ind_end], ord=2, axis=0) ** 2) / (
                    ind_end - ind_start)
        avg_energy_per_freq = avg_energy_per_freq ** 0.75
        for i in range(ind_start, ind_end):
            magnitude_spec[i] = magnitude_spec[i] if magnitude_spec[i] > noise_thresh * avg_energy_per_freq else 0
    return magnitude_spec