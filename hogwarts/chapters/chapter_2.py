import sys
import os
hogwarts_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, hogwarts_root)
    
from utils.input_utils import *
from universe.character import *
from chapters.chapter_1 import *
