"""
Unit tests for utility functions.
"""

import numpy as np
import pytest
from mars_suite.utils import db_to_linear, linear_to_db, snr_estimate


class TestUtilities:
    """Test cases for utility functions."""
    
    def test_db_to_linear(self):
        """Test decibel to linear conversion."""
        assert db_to_linear(0) == pytest.approx(1.0)
        assert db_to_linear(10) == pytest.approx(10.0)
        assert db_to_linear(20) == pytest.approx(100.0)
        assert db_to_linear(-10) == pytest.approx(0.1)
    
    def test_linear_to_db(self):
        """Test linear to decibel conversion."""
        assert linear_to_db(1.0) == pytest.approx(0.0)
        assert linear_to_db(10.0) == pytest.approx(10.0)
        assert linear_to_db(100.0) == pytest.approx(20.0)
        assert linear_to_db(0.1) == pytest.approx(-10.0)
    
    def test_linear_to_db_zero(self):
        """Test linear to dB with zero input."""
        result = linear_to_db(0)
        assert result == -np.inf
    
    def test_linear_to_db_negative(self):
        """Test linear to dB with negative input."""
        result = linear_to_db(-1)
        assert result == -np.inf
    
    def test_snr_estimate(self):
        """Test SNR estimation."""
        signal = np.ones(100) * 2.0
        noise = np.ones(100) * 0.2
        
        snr = snr_estimate(signal, noise)
        expected_snr = linear_to_db(4.0 / 0.04)  # signal_power / noise_power
        
        assert snr == pytest.approx(expected_snr)
    
    def test_snr_estimate_zero_noise(self):
        """Test SNR estimation with zero noise."""
        signal = np.ones(100)
        noise = np.zeros(100)
        
        snr = snr_estimate(signal, noise)
        assert snr == np.inf
