#!/usr/bin/python3
"""Cprofile test to optimise python scripts"""

import cProfile
import palingrams_optimised
cProfile.run('palingrams_optimised.find_palingrams()')
