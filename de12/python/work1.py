from sqlite3 import ProgrammingError
from isort import place_module
from matplotlib import docstring
from numpy import place
from sympy import ff
from zmq import PLAIN_SERVER


name="fbh"
waist=46
age=40

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

name="aaa"
place_=3007
doing=ff

print(name, "さんは今", place_, "で",doing, "していますね")