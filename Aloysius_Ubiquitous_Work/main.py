import sounddevice as sd
import time
from extractFeatures2 import extract_features

ALL_NOTES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

try:
    print("Starting guitar tuner...")
    with sd.InputStream(channels=1, callback=extract_features, blocksize=12000, samplerate=20500):
        while True:
            time.sleep(1)
except Exception as exc:
    print(str(exc))
