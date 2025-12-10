# MARS Suite Examples

This directory contains example scripts demonstrating how to use the MARS Suite library.

## Examples

### signal_processing_example.py
Demonstrates basic signal processing operations:
- Creating a signal processor
- Generating and normalizing signals
- Applying window functions
- Computing FFT

Run with:
```bash
python signal_processing_example.py
```

### modem_example.py
Demonstrates modem functionality:
- Creating a modem instance
- Modulating data
- Setting carrier frequencies

Run with:
```bash
python modem_example.py
```

### utils_example.py
Demonstrates utility functions:
- dB/linear conversions
- SNR estimation

Run with:
```bash
python utils_example.py
```

## Requirements

Make sure you have installed the package first:

```bash
pip install -e ..
```

Or install the requirements:

```bash
pip install -r ../requirements.txt
```

## Optional Dependencies

For visualization in the signal processing example:
```bash
pip install matplotlib
```
