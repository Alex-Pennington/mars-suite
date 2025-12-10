# Phoenix Nest MARS Communications Suite

[![Python CI](https://github.com/Alex-Pennington/mars-suite/workflows/Python%20CI/badge.svg)](https://github.com/Alex-Pennington/mars-suite/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Open-source HF digital communications tools for Military Auxiliary Radio System (MARS) operations.

**Developer:** Alex Pennington (KY4OLB, formerly AAR4TE / NNN0VO)  
**Project Site:** [www.organicengineer.com/projects](https://www.organicengineer.com/projects)  
**Contact:** projects@organicengineer.com

## Features

- 🎯 **Signal Processing**: Advanced DSP operations optimized for HF communications
- 📡 **Digital Modes**: Support for PSK31, RTTY, MFSK, and other MARS digital modes
- 🔧 **Modular Design**: Easy-to-use components that can be combined for custom applications
- 🧪 **Well Tested**: Comprehensive test suite ensuring reliability
- 📚 **Documented**: Clear documentation and examples

## Installation

### From Source

```bash
git clone https://github.com/Alex-Pennington/mars-suite.git
cd mars-suite
pip install -e .
```

### For Development

```bash
git clone https://github.com/Alex-Pennington/mars-suite.git
cd mars-suite
pip install -r requirements-dev.txt
pip install -e .
```

## Quick Start

```python
from mars_suite.core import SignalProcessor
from mars_suite.modem import Modem
import numpy as np

# Signal processing
processor = SignalProcessor(sample_rate=48000)
signal = np.sin(2 * np.pi * 440 * np.linspace(0, 1, 48000))
normalized = processor.normalize(signal)
freqs, magnitudes = processor.compute_fft(normalized)

# Modem operations
modem = Modem(mode='PSK31')
modem.set_carrier_frequency(1500)
audio_signal = modem.modulate(b"CQ CQ DE KY4OLB K")
```

## Project Structure

```
mars-suite/
├── src/mars_suite/          # Main package source code
│   ├── core/                # Signal processing core
│   ├── modem/               # Modem implementations
│   ├── protocols/           # Protocol implementations
│   └── utils/               # Utility functions
├── tests/                   # Test suite
│   ├── unit/                # Unit tests
│   └── integration/         # Integration tests
├── examples/                # Usage examples
├── docs/                    # Documentation
└── scripts/                 # Utility scripts
```

## Documentation

Full documentation is available in the [docs/](docs/) directory. See [docs/README.md](docs/README.md) for a complete guide.

## Examples

Check out the [examples/](examples/) directory for complete working examples:

- **signal_processing_example.py**: Signal processing operations
- **modem_example.py**: Modem usage and modulation
- **utils_example.py**: Utility functions demonstration

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=mars_suite

# Run specific test file
pytest tests/unit/test_core.py
```

## Development

### Code Style

This project uses:
- **Black** for code formatting
- **Flake8** for linting
- **mypy** for type checking

```bash
# Format code
black src/ tests/

# Lint
flake8 src/ tests/

# Type check
mypy src/
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This software is intended for educational and amateur radio use. Users are responsible for ensuring compliance with all applicable regulations, including:

- FCC Part 97 Rules (Amateur Radio Service)
- MARS operating procedures and directives
- International telecommunications regulations

## Contact & Support

- **Email:** projects@organicengineer.com
- **Issues:** [GitHub Issues](https://github.com/Alex-Pennington/mars-suite/issues)
- **Website:** [www.organicengineer.com/projects](https://www.organicengineer.com/projects)

## Acknowledgments

Special thanks to the amateur radio and MARS communities for their continued support and feedback.

---

**73 de KY4OLB**
