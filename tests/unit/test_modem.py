"""
Unit tests for modem functionality.
"""

import numpy as np
import pytest
from mars_suite.modem import Modem


class TestModem:
    """Test cases for Modem class."""
    
    def test_initialization_default(self):
        """Test modem initialization with defaults."""
        modem = Modem()
        assert modem.mode == 'PSK31'
        assert modem.sample_rate == 48000
        assert modem.carrier_freq == 1000
    
    def test_initialization_custom(self):
        """Test modem initialization with custom parameters."""
        modem = Modem(mode='RTTY', sample_rate=44100)
        assert modem.mode == 'RTTY'
        assert modem.sample_rate == 44100
    
    def test_set_carrier_frequency(self):
        """Test setting carrier frequency."""
        modem = Modem()
        modem.set_carrier_frequency(1500)
        assert modem.carrier_freq == 1500
    
    def test_set_invalid_carrier_frequency(self):
        """Test that invalid carrier frequency raises ValueError."""
        modem = Modem(sample_rate=48000)
        
        with pytest.raises(ValueError):
            modem.set_carrier_frequency(-100)
        
        with pytest.raises(ValueError):
            modem.set_carrier_frequency(50000)  # Above Nyquist
    
    def test_modulate(self):
        """Test modulation produces audio signal."""
        modem = Modem()
        data = b"TEST"
        signal = modem.modulate(data)
        
        assert isinstance(signal, np.ndarray)
        assert len(signal) > 0
    
    def test_demodulate(self):
        """Test demodulation produces bytes."""
        modem = Modem()
        signal = np.random.randn(1000)
        data = modem.demodulate(signal)
        
        assert isinstance(data, bytes)
