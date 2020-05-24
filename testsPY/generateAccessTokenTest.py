#Used for calling classes in parent directory
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from classes.snookeyCore import *

core = snookeyCore()

core.generateAccessTokenLink()
