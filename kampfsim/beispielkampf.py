# -*- coding: utf-8 -*- 
from kampf import Kampf
from archetypen import *	
from waffen import *
from ruestung import *
import pprint
from copy import deepcopy
import logging

# import cProfile
Testkampf = Kampf(10)

logging.basicConfig(level=logging.DEBUG,format = '%(message)s')
Testkampf.Arena([Aderion, Cederion], [Bederion, Wulfhard])

#Testkampf.Arena(Cederion, Sialdis)

