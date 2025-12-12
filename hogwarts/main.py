import sys
import os
hogwarts_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(hogwarts_root)

from chapters.chapter_1 import *
from chapters.chapter_2 import *
from chapters.chapter_3 import *
from chapters.chapter_4 import *
from universe.character import *
from universe.house import *

start_chapter_1()