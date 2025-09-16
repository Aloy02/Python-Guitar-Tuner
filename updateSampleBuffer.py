import numpy as np

WINDOW_SIZE = 48000  # window size of the DFT in samples

def update_sample_buffer(existing_samples, new_data):
    combined = np.concatenate((existing_samples, new_data))
    return combined[-WINDOW_SIZE:]