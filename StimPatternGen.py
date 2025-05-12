# Noah Williams 
# Sharf Lab, UCSC
# May 12, 2025
# My coffee is cold and I am sad

'''
This should give a 
'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
import os
from braindance.core.stim_commands import generate_stimulations


class simplePatternGenerator:
    '''
    skeleton to build on 
    '''

    def __init__(self,
                 electrodes = [], 
                 phase_width_ms=200,
                 amplitude_mv=400,
                 delay_ms=20):
        
        self.phase_width = phase_width_ms 
        self.amplitude = amplitude_mv
        self.electrodes = electrodes
        self.delay = delay_ms
        self.training_pattern = []
        self.sub_pattern = self._generate_sub_pattern()

    def _generate_sub_pattern(self):
        '''
        Generates a simple pattern, constant amplitude and frequency

        Note: 
            - alternates between electrodes in order of array
            - [[0,1,2],4] will stim 0,1,2 as a group, then 4
        Returns: list of tuples [([electrode(s)], amplitude, phase_width), ...]
        '''
        self.sub_pattern = generate_stimulations(
            electrode_inds=self.electrodes, 
            amp=self.amplitude, 
            phase_width=self.phase_width)
        return self.sub_pattern
    
    def _tie_to_electrodes(self, pattern):
        '''
        Adds keywords to commands ('stim', 'delay')
        Adds in specified delay between stim commands
        Returns: list of tuples [('stim', [electrode(s)], amplitude, phase_width), ('delay', delay_time), ...] 
        '''
        tied_pattern = []
        pattern_len = len(pattern)
        for i in range(pattern_len):
            electrode, amplitude, phase_width = pattern[i]
            tied_pattern.append(('stim', electrode, amplitude, phase_width))
            tied_pattern.append(('delay', self.delay))
        return tied_pattern 

    def generate_training_pattern(self):
        '''
        Meat of the function is _tie_to_electrodes, this is just a wrapper
            to make end result code more readable
        '''
        # Assert that sub_pattern has been generated
        assert self.sub_pattern, 'Must generate sub_pattern first'
        self.training_pattern = []   # Reset the pattern
        self.training_pattern = self._tie_to_electrodes(self.sub_pattern) 
        return self.training_pattern

    def log_patterns(self, path):
        '''
        Saves the training to a directory, very helpful 
        '''
        None

    def plot_spatial_pattern(self):
        '''
        This is cool to show, can supply more code if needed

        Maxwell MaxOne array: 26,400 electrodes, 3.85 x 2.10 mm² → 220 x 120 electrodes
        '''
        None


def simple_unit_test1():
    '''
    Simple test to check if the class is working
    '''

    # Come up with some tests for your program
    # Check if the files are there
    # remove the files

    print('Simple test passed!')



if __name__ == '__main__':

    pattern = simplePatternGenerator(
        electrodes=[0, 1, 2, 3, 4], 
        phase_width_ms=200,
        amplitude_mv=400,
        delay_ms=20
    )
    pattern.generate_training_pattern()
    print(pattern.training_pattern)



