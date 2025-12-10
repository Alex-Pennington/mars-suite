#!/usr/bin/env python3
"""
Basic example of using MARS Suite for signal processing.

This example demonstrates:
- Creating a signal processor
- Generating a test signal
- Normalizing and windowing the signal
- Computing FFT
"""

import numpy as np
import matplotlib.pyplot as plt
from mars_suite.core import SignalProcessor


def main():
    # Initialize signal processor
    sample_rate = 48000
    processor = SignalProcessor(sample_rate=sample_rate)
    
    # Generate a test signal (440 Hz sine wave)
    duration = 1.0  # seconds
    t = np.linspace(0, duration, int(sample_rate * duration))
    frequency = 440  # A4 note
    signal = np.sin(2 * np.pi * frequency * t)
    
    # Add some noise
    noise = np.random.normal(0, 0.1, signal.shape)
    noisy_signal = signal + noise
    
    # Normalize the signal
    normalized = processor.normalize(noisy_signal)
    
    # Apply a window
    windowed = processor.apply_window(normalized, 'hann')
    
    # Compute FFT
    freqs, magnitudes = processor.compute_fft(windowed)
    
    # Find peak frequency
    peak_idx = np.argmax(magnitudes)
    peak_freq = freqs[peak_idx]
    
    print(f"Sample rate: {sample_rate} Hz")
    print(f"Signal duration: {duration} s")
    print(f"Original frequency: {frequency} Hz")
    print(f"Detected peak frequency: {peak_freq:.2f} Hz")
    
    # Optional: Plot if matplotlib is available
    try:
        fig, axes = plt.subplots(2, 1, figsize=(10, 8))
        
        # Time domain
        axes[0].plot(t[:1000], normalized[:1000])
        axes[0].set_xlabel('Time (s)')
        axes[0].set_ylabel('Amplitude')
        axes[0].set_title('Normalized Signal (first 1000 samples)')
        axes[0].grid(True)
        
        # Frequency domain
        axes[1].plot(freqs, magnitudes)
        axes[1].set_xlabel('Frequency (Hz)')
        axes[1].set_ylabel('Magnitude')
        axes[1].set_title('FFT Magnitude Spectrum')
        axes[1].set_xlim(0, 2000)
        axes[1].grid(True)
        
        plt.tight_layout()
        plt.savefig('signal_processing_example.png')
        print("\nPlot saved to signal_processing_example.png")
    except ImportError:
        print("\nMatplotlib not available, skipping plot generation")


if __name__ == "__main__":
    main()
