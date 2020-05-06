import os
import sys
import pytest

current_file_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(
                current_file_dir, '..')))
