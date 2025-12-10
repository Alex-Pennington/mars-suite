"""
Utility functions for MARS Suite.
"""

import numpy as np
from typing import Union


def db_to_linear(db: float) -> float:
    """
    Convert decibels to linear scale.
    
    Args:
        db: Value in decibels
        
    Returns:
        Linear scale value
    """
    return 10 ** (db / 10)


def linear_to_db(linear: float) -> float:
    """
    Convert linear scale to decibels.
    
    Args:
        linear: Linear scale value
        
    Returns:
        Value in decibels
    """
    if linear <= 0:
        return -np.inf
    return 10 * np.log10(linear)


def snr_estimate(signal: np.ndarray, noise: np.ndarray) -> float:
    """
    Estimate signal-to-noise ratio.
    
    Args:
        signal: Signal array
        noise: Noise array
        
    Returns:
        SNR in dB
    """
    signal_power = np.mean(signal ** 2)
    noise_power = np.mean(noise ** 2)
    
    if noise_power == 0:
        return np.inf
    
    return linear_to_db(signal_power / noise_power)
