
# Real-Time Guitar Tuner

A Python-based guitar tuner built on a Raspberry Pi that uses digital signal processing (DSP) to detect guitar notes in real time and provide intuitive tuning feedback.

## Overview
This project applies signal processing techniques to convert raw audio input from a microphone into clear tuning instructions for guitar players. Unlike basic tuner apps, this system leverages FFT, Harmonic Product Spectrum (HPS), and octave-band noise filtering to deliver accurate pitch detection, even in noisy environments.

The system maps detected frequencies to the closest musical notes (E, A, D, G, B, E) and provides simple tuning instructions: tighten, loosen, or tuned.

## Structure

main.py – Entry point, handles audio input stream

extractFeatures2.py – Core pitch detection and feature extraction pipeline

findClosestNote.py – Maps detected frequencies to musical notes

computeMagnitudeSpectrum.py – Computes FFT-based magnitude spectrum

octaveBands.py – Noise filtering using octave bands

updateSampleBuffer.py – Maintains rolling audio buffer

check.py – Provides tuning feedback (tighten, loosen, tuned)

## Features

Real-time audio input with Python and sounddevice

FFT and Harmonic Product Spectrum for frequency estimation

Octave-band noise filtering for robustness

Mapping of frequencies to the nearest guitar notes

User feedback system for beginner-friendly tuning

## Requirements

Audio input device

Python libraries: numpy, scipy, sounddevice

## Installing dependencies

pip install numpy scipy sounddevice
