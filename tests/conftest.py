"""
Test configuration and shared fixtures.
"""

import pytest
import numpy as np


@pytest.fixture
def sample_rate():
    """Standard sample rate for tests."""
    return 48000


@pytest.fixture
def test_signal(sample_rate):
    """Generate a test signal."""
    duration = 1.0  # seconds
    t = np.linspace(0, duration, int(sample_rate * duration))
    frequency = 440  # A4 note
    signal = np.sin(2 * np.pi * frequency * t)
    return signal
