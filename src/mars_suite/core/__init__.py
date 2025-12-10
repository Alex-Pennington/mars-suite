"""
Core signal processing functionality for MARS Suite.
"""

import numpy as np
from typing import Optional


class SignalProcessor:
    """
    Base class for signal processing operations.
    
    Handles common DSP operations for HF digital communications.
    """
    
    def __init__(self, sample_rate: int = 48000):
        """
        Initialize the signal processor.
        
        Args:
            sample_rate: Sample rate in Hz (default: 48000)
        """
        self.sample_rate = sample_rate
    
    def normalize(self, signal: np.ndarray) -> np.ndarray:
        """
        Normalize a signal to the range [-1, 1].
        
        Args:
            signal: Input signal array
            
        Returns:
            Normalized signal array
        """
        max_val = np.max(np.abs(signal))
        if max_val > 0:
            return signal / max_val
        return signal
    
    def apply_window(self, signal: np.ndarray, window_type: str = 'hann') -> np.ndarray:
        """
        Apply a window function to a signal.
        
        Args:
            signal: Input signal array
            window_type: Type of window ('hann', 'hamming', 'blackman')
            
        Returns:
            Windowed signal array
        """
        window_funcs = {
            'hann': np.hanning,
            'hamming': np.hamming,
            'blackman': np.blackman
        }
        
        if window_type not in window_funcs:
            raise ValueError(f"Unknown window type: {window_type}")
        
        window = window_funcs[window_type](len(signal))
        return signal * window
    
    def compute_fft(self, signal: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """
        Compute the FFT of a signal.
        
        Args:
            signal: Input signal array
            
        Returns:
            Tuple of (frequencies, magnitudes)
        """
        fft = np.fft.fft(signal)
        freqs = np.fft.fftfreq(len(signal), 1/self.sample_rate)
        magnitudes = np.abs(fft)
        
        return freqs[:len(freqs)//2], magnitudes[:len(magnitudes)//2]
