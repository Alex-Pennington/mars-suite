#!/usr/bin/env python3
"""
Basic example of using the modem functionality.

This example demonstrates:
- Creating a modem instance
- Modulating data
- Setting carrier frequency
"""

import numpy as np
from mars_suite.modem import Modem


def main():
    # Initialize modem with PSK31 mode
    modem = Modem(mode='PSK31', sample_rate=48000)
    
    print(f"Modem mode: {modem.mode}")
    print(f"Sample rate: {modem.sample_rate} Hz")
    print(f"Carrier frequency: {modem.carrier_freq} Hz")
    
    # Set a custom carrier frequency
    modem.set_carrier_frequency(1500)
    print(f"New carrier frequency: {modem.carrier_freq} Hz")
    
    # Modulate some test data
    test_message = b"CQ CQ CQ DE KY4OLB KY4OLB KY4OLB K"
    print(f"\nModulating message: {test_message.decode('ascii')}")
    
    modulated_signal = modem.modulate(test_message)
    print(f"Modulated signal length: {len(modulated_signal)} samples")
    print(f"Duration: {len(modulated_signal) / modem.sample_rate:.3f} seconds")
    
    # Demodulate (placeholder in current implementation)
    demodulated_data = modem.demodulate(modulated_signal)
    print(f"\nDemodulated data: {demodulated_data}")
    
    print("\nNote: This is a placeholder implementation.")
    print("Full PSK31, RTTY, and other mode implementations coming soon!")


if __name__ == "__main__":
    main()
