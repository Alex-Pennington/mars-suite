#!/usr/bin/env python3
"""
Example demonstrating utility functions.

This example shows:
- dB/linear conversions
- SNR estimation
"""

import numpy as np
from mars_suite.utils import db_to_linear, linear_to_db, snr_estimate


def main():
    print("=== dB/Linear Conversions ===")
    
    # Convert some common dB values to linear
    db_values = [0, 3, 6, 10, 20, -3, -6, -10]
    print("\ndB to Linear:")
    for db in db_values:
        linear = db_to_linear(db)
        print(f"  {db:+4.0f} dB = {linear:.4f} linear")
    
    # Convert back
    print("\nLinear to dB:")
    linear_values = [1.0, 2.0, 4.0, 10.0, 0.5, 0.25]
    for linear in linear_values:
        db = linear_to_db(linear)
        print(f"  {linear:6.2f} linear = {db:+6.2f} dB")
    
    print("\n=== SNR Estimation ===")
    
    # Create test signals with known SNR
    np.random.seed(42)
    
    # Signal with 10 dB SNR
    signal_power = 1.0
    noise_power = db_to_linear(-10)  # 10 dB below signal
    
    signal = np.random.normal(0, np.sqrt(signal_power), 10000)
    noise = np.random.normal(0, np.sqrt(noise_power), 10000)
    
    estimated_snr = snr_estimate(signal, noise)
    print(f"\nExpected SNR: ~10 dB")
    print(f"Estimated SNR: {estimated_snr:.2f} dB")
    
    # Clean signal (very high SNR)
    clean_signal = np.ones(1000) * 1.0
    tiny_noise = np.random.normal(0, 0.001, 1000)
    
    high_snr = snr_estimate(clean_signal, tiny_noise)
    print(f"\nHigh SNR case: {high_snr:.2f} dB")


if __name__ == "__main__":
    main()
