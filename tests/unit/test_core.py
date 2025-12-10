"""
Unit tests for core signal processing functionality.
"""

import numpy as np
import pytest
from mars_suite.core import SignalProcessor


class TestSignalProcessor:
    """Test cases for SignalProcessor class."""
    
    def test_initialization(self):
        """Test processor initialization with default sample rate."""
        processor = SignalProcessor()
        assert processor.sample_rate == 48000
    
    def test_initialization_custom_rate(self):
        """Test processor initialization with custom sample rate."""
        processor = SignalProcessor(sample_rate=44100)
        assert processor.sample_rate == 44100
    
    def test_normalize_signal(self):
        """Test signal normalization."""
        processor = SignalProcessor()
        signal = np.array([0.5, 1.0, -0.5, -1.0])
        normalized = processor.normalize(signal)
        
        assert np.max(np.abs(normalized)) == pytest.approx(1.0)
        assert normalized.shape == signal.shape
    
    def test_normalize_zero_signal(self):
        """Test normalization of zero signal."""
        processor = SignalProcessor()
        signal = np.zeros(100)
        normalized = processor.normalize(signal)
        
        assert np.all(normalized == 0)
    
    def test_apply_hann_window(self):
        """Test applying Hann window."""
        processor = SignalProcessor()
        signal = np.ones(100)
        windowed = processor.apply_window(signal, 'hann')
        
        assert windowed.shape == signal.shape
        assert windowed[0] == pytest.approx(0.0, abs=1e-10)
        assert windowed[-1] == pytest.approx(0.0, abs=1e-10)
    
    def test_apply_hamming_window(self):
        """Test applying Hamming window."""
        processor = SignalProcessor()
        signal = np.ones(100)
        windowed = processor.apply_window(signal, 'hamming')
        
        assert windowed.shape == signal.shape
    
    def test_invalid_window_type(self):
        """Test that invalid window type raises ValueError."""
        processor = SignalProcessor()
        signal = np.ones(100)
        
        with pytest.raises(ValueError, match="Unknown window type"):
            processor.apply_window(signal, 'invalid')
    
    def test_compute_fft(self):
        """Test FFT computation."""
        processor = SignalProcessor(sample_rate=1000)
        # Create a simple sine wave at 10 Hz
        t = np.linspace(0, 1, 1000)
        signal = np.sin(2 * np.pi * 10 * t)
        
        freqs, magnitudes = processor.compute_fft(signal)
        
        assert len(freqs) == len(magnitudes)
        assert len(freqs) == 500  # Half of input length
        assert np.all(freqs >= 0)
