#!/usr/bin/env python3
"""
Setup script for quick development environment setup.
"""

import subprocess
import sys
import os


def run_command(cmd, description):
    """Run a command and print status."""
    print(f"\n{'='*60}")
    print(f"  {description}")
    print(f"{'='*60}")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        if e.stderr:
            print(e.stderr)
        return False


def main():
    """Main setup function."""
    print("Phoenix Nest MARS Suite - Development Environment Setup")
    print("=" * 60)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required")
        sys.exit(1)
    
    print(f"Python version: {sys.version}")
    
    # Upgrade pip
    run_command(
        f"{sys.executable} -m pip install --upgrade pip",
        "Upgrading pip"
    )
    
    # Install development dependencies
    if os.path.exists("requirements-dev.txt"):
        run_command(
            f"{sys.executable} -m pip install -r requirements-dev.txt",
            "Installing development dependencies"
        )
    
    # Install package in editable mode
    run_command(
        f"{sys.executable} -m pip install -e .",
        "Installing mars-suite in editable mode"
    )
    
    # Run tests to verify installation
    print("\n" + "="*60)
    print("  Running tests to verify installation")
    print("="*60)
    
    try:
        import pytest
        exit_code = pytest.main(["-v", "tests/"])
        if exit_code == 0:
            print("\n" + "="*60)
            print("  ✓ Setup completed successfully!")
            print("="*60)
            print("\nYou can now:")
            print("  - Run examples: python examples/signal_processing_example.py")
            print("  - Run tests: pytest")
            print("  - Import the package: from mars_suite import *")
        else:
            print("\nWarning: Some tests failed. Please review the output above.")
    except ImportError:
        print("\nPytest not installed. Skipping test verification.")
        print("Install with: pip install pytest")


if __name__ == "__main__":
    main()
