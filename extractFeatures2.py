import numpy as np

from findClosestNote import find_closest_note
from octaveBands import octave_bands
from updateSampleBuffer import update_sample_buffer
from computeMagnitudeSpectrum import compute_magnitude_spectrum
from check import check

SAMPLE_FREQ = 20500
WINDOW_SIZE = 48000  # window size of the DFT in samples
HANN_WINDOW = np.hanning(WINDOW_SIZE)

def extract_features(indata, frames, window, status):
    NUM_HPS = 5  # Max number of harmonic product spectrums
    MIN_FREQ_HZ = 62  # Minimum frequency to keep in spectrum

    # Initialise persistent attributes if not already present
    if not hasattr(extract_features, "sample"):
        extract_features.sample = np.zeros(WINDOW_SIZE)
    if not hasattr(extract_features, "buffer"):
        extract_features.buffer = ["1", "2"]

    # Check for status
    if status:
        print(status)
        return

    # Check for data present
    if not any(indata):
        print("no input")
        return

    # Append new data and maintain fixed sample window
    new_data = indata[:, 0]
    extract_features.sample = update_sample_buffer(extract_features.sample, new_data)

    spectrum = compute_magnitude_spectrum(extract_features.sample, SAMPLE_FREQ, MIN_FREQ_HZ)

    # Apply octave band filter
    spectrum = octave_bands(spectrum, SAMPLE_FREQ / WINDOW_SIZE)

    # Interpolate and normalise magnitude spectrum
    interp_points = np.arange(0, len(spectrum), 1 / NUM_HPS)
    interp_spectrum = np.interp(interp_points, np.arange(len(spectrum)), spectrum)
    interp_spectrum /= np.linalg.norm(interp_spectrum, ord=2)

    # Compute Harmonic Product Spectrum (HPS)
    hps_spectrum = interp_spectrum.copy()
    for i in range(1, NUM_HPS):
        step = i + 1
        hps_product = hps_spectrum[:len(interp_spectrum[::step])] * interp_spectrum[::step]
        if not np.any(hps_product):
            break
        hps_spectrum = hps_product

    # Estimate frequency
    max_index = np.argmax(hps_spectrum)
    estimated_freq = max_index * (SAMPLE_FREQ / WINDOW_SIZE) / NUM_HPS

    # Get closest musical note
    closest_note, reference_pitch = find_closest_note(estimated_freq)

    # Round for display
    estimated_freq = round(estimated_freq, 1)
    reference_pitch = round(reference_pitch, 1)

    # Update rolling note buffer
    extract_features.buffer.insert(0, closest_note)
    extract_features.buffer.pop()

    # Display result
    if extract_features.buffer.count(extract_features.buffer[0]) == len(extract_features.buffer):
        output = f"{closest_note} {estimated_freq}/{reference_pitch}"

        # Check estimated frequency against desired frequency
        check(closest_note, estimated_freq)
    else:
        output = "..."

    print(f"Closest note: {output}")