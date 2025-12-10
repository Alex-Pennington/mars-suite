# MARS Suite Documentation

Welcome to the Phoenix Nest MARS Communications Suite documentation.

## Overview

MARS Suite is an open-source toolkit for HF digital communications, specifically designed for Military Auxiliary Radio System (MARS) operations. It provides tools for signal processing, modulation/demodulation, and protocol implementation.

## Features

- **Signal Processing**: Core DSP operations for HF communications
- **Modem Support**: Digital mode encoding/decoding (PSK31, RTTY, MFSK, etc.)
- **Protocol Implementation**: MARS-specific protocols (coming soon)
- **Utilities**: Helper functions for RF and signal analysis

## Installation

### From PyPI (when published)

```bash
pip install mars-suite
```

### From Source

```bash
git clone https://github.com/Alex-Pennington/mars-suite.git
cd mars-suite
pip install -e .
```

### Development Installation

```bash
git clone https://github.com/Alex-Pennington/mars-suite.git
cd mars-suite
pip install -r requirements-dev.txt
pip install -e .
```

## Quick Start

### Signal Processing

```python
from mars_suite.core import SignalProcessor
import numpy as np

# Create a processor
processor = SignalProcessor(sample_rate=48000)

# Generate a test signal
t = np.linspace(0, 1, 48000)
signal = np.sin(2 * np.pi * 440 * t)

# Normalize and window
normalized = processor.normalize(signal)
windowed = processor.apply_window(normalized, 'hann')

# Compute FFT
freqs, magnitudes = processor.compute_fft(windowed)
```

### Modem Usage

```python
from mars_suite.modem import Modem

# Create a PSK31 modem
modem = Modem(mode='PSK31', sample_rate=48000)

# Set carrier frequency
modem.set_carrier_frequency(1500)

# Modulate data
message = b"CQ CQ CQ DE KY4OLB K"
signal = modem.modulate(message)
```

### Utilities

```python
from mars_suite.utils import db_to_linear, linear_to_db, snr_estimate

# Convert between dB and linear
power_linear = db_to_linear(10)  # 10 dB to linear
power_db = linear_to_db(100)      # 100 linear to dB

# Estimate SNR
snr = snr_estimate(signal, noise)
print(f"SNR: {snr:.2f} dB")
```

## Modules

### Core Module (`mars_suite.core`)

- `SignalProcessor`: Main class for signal processing operations
  - `normalize()`: Normalize signals
  - `apply_window()`: Apply window functions (Hann, Hamming, Blackman)
  - `compute_fft()`: Compute FFT

### Modem Module (`mars_suite.modem`)

- `Modem`: Base class for digital mode modems
  - `modulate()`: Convert data to audio signal
  - `demodulate()`: Convert audio signal to data
  - `set_carrier_frequency()`: Set carrier frequency

### Utilities Module (`mars_suite.utils`)

- `db_to_linear()`: Convert dB to linear scale
- `linear_to_db()`: Convert linear scale to dB
- `snr_estimate()`: Estimate signal-to-noise ratio

## Examples

See the `examples/` directory for complete working examples:
- `signal_processing_example.py`: Signal processing demonstration
- `modem_example.py`: Modem usage demonstration
- `utils_example.py`: Utility functions demonstration

## Development

### Running Tests

```bash
pytest
```

With coverage:
```bash
pytest --cov=mars_suite
```

### Code Style

We use Black for code formatting:
```bash
black src/ tests/
```

And Flake8 for linting:
```bash
flake8 src/ tests/
```

### Type Checking

```bash
mypy src/
```

## Contributing

Please see [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See [LICENSE](../LICENSE) for details.

## Contact

- Developer: Alex Pennington (KY4OLB)
- Email: projects@organicengineer.com
- Website: www.organicengineer.com/projects

## Acknowledgments

This project is developed for the amateur radio and MARS communities. Special thanks to all contributors and operators who provide feedback and support.

## Disclaimer

This software is provided for educational and amateur radio use. Users are responsible for ensuring compliance with all applicable regulations, including FCC Part 97 rules and MARS operating procedures.
