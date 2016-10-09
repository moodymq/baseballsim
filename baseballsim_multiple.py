# -*- coding: utf-8 -*-
"""
Created on Sun Oct 09 12:51:25 2016

@author: moodymq
"""

#Part of a larger project to predict baseball outcomes.
#Will consist of two parts in the end: a baseball simulator in Python (this code) which will simulate seasons and a
#a second, data science, based part to predict performance in the future (to be written largely in R)

from __future__ import division
import random as rdm
import numpy as np

no_sims = 100000
no_innings = 9
home_half = 2
no_stats = 7
first_base = 0
second_base = 0
third_base = 0

teams = np.zeros((home_half,no_stats),dtype = np.float64)
runs = np.zeros((2),dtype = np.int16)
runs_per_inning = np.zeros((2,200),dtype = np.int16)
wins = np.zeros((2),dtype = np.int64)

teams[0,0] = 99/699
teams[0,1] = 35/699
teams[0,2] = 3/699
teams[0,3] = 39/699
teams[0,4] = 75/699
teams[0,5] = 18/699
teams[0,6] = (699-99-35-3-39-75-18)/699

teams[1,0] = 91/676
teams[1,1] = 43/676
teams[1,2] = 4/676
teams[1,3] = 32/676
teams[1,4] = 74/676
teams[0,5] = 16/676
teams[1,6] = (676-91-43-4-32-74-16)/676

i = 0

for thissim in xrange(no_sims):
    while i < no_innings:
        for j in xrange(home_half):
            #if runs[1] > runs[0] and i == 8 and j == 1:
            #    break
            outs = 0
            first_base = 0
            second_base = 0
            third_base = 0
            while outs < 3:
                if runs[1] > runs[0] and i == 8 and j == 1:
                    break
                pa = rdm.uniform(0,1)
                #print '%s' %pa
                k = 0
                while pa > 0 and k < no_stats:
                    pa = pa - teams[j,k]
                    #print '%s' % pa
                    k = k + 1
                    #print '%s' % k
                if k == 1:
                    if third_base == 1:
                        third_base = 0
                        runs[j] = runs[j] + 1
                        runs_per_inning[j,i] = runs_per_inning[j,i] + 1
                    if second_base == 1:
                        second_base = 0
                        runs[j] = runs[j] + 1
                        runs_per_inning[j,i] = runs_per_inning[j,i] + 1
                    if first_base == 1:
                        third_base = 1
                        first_base = 0
                    first_base = 1
                if k == 2:
                    if third_base == 1:
                        third_base = 0
                        runs[j] = runs[j] + 1
                        runs_per_inning[j,i] = runs_per_inning[j,i] + 1
                    if second_base == 1:
                        second_base = 0
                        runs[j] = runs[j] + 1
                        runs_per_inning[j,i] = runs_per_inning[j,i] + 1
                    if first_base == 1:
                        first_base = 0
                        runs[j] = runs[j] + 1
                        runs_per_inning[j,i] = runs_per_inning[j,i] + 1
                    second_base = 1
                if k == 3:
                    if third_base == 1:
                        third_base = 0
                        runs[j] = runs[j] + 1
                        runs_per_inning[j,i] = runs_per_inning[j,i] + 1
                    if second_base == 1:
                        second_base = 0
                        runs[j] = runs[j] + 1
                        runs_per_inning[j,i] = runs_per_inning[j,i] + 1
                    if first_base == 1:
                        first_base = 0
                        runs[j] = runs[j] + 1
                        runs_per_inning[j,i] = runs_per_inning[j,i] + 1
                    third_base = 1
                if k == 4:
                    if third_base == 1:
                        third_base = 0
                        runs[j] = runs[j] + 1
                        runs_per_inning[j,i] = runs_per_inning[j,i] + 1
                    if second_base == 1:
                        second_base = 0
                        runs[j] = runs[j] + 1
                        runs_per_inning[j,i] = runs_per_inning[j,i] + 1
                    if first_base == 1:
                        first_base = 0
                        runs[j] = runs[j] + 1
                        runs_per_inning[j,i] = runs_per_inning[j,i] + 1
                    runs[j] = runs[j] + 1
                    runs_per_inning[j,i] = runs_per_inning[j,i] + 1
                if k == 5:
                    if third_base == 1:
                        if second_base == 1:
                            if first_base == 1:
                                runs[j]=runs[j] + 1
                                runs_per_inning[j,i] = runs_per_inning[j,i] + 1
                                continue
                    if second_base == 1:
                        if first_base == 1:
                            third_base = 1
                            continue
                    if first_base == 1:
                        second_base = 1
                        continue
                    first_base = 1
                if k == 6:
                    if third_base == 1:
                        if second_base == 1:
                            if first_base == 1:
                                runs[j]=runs[j] + 1
                                runs_per_inning[j,i] = runs_per_inning[j,i] + 1
                                continue
                    if second_base == 1:
                        if first_base == 1:
                            third_base = 1
                            continue
                    if first_base == 1:
                        second_base = 1
                        continue
                    first_base = 1
                if k == 7:
                    outs = outs + 1
        if i >= 8 and runs[0] == runs [1]:
            no_innings = no_innings + 1
        i = i + 1
    #print 'H: ' + str(runs[1]) + ', A ' + str(runs[0]) + '; ' + str(i) + ' innings'
    if runs[0] > runs[1]:
        wins[0] = wins[0] + 1
    if runs[1] > runs[0]:
        wins[1] = wins[1] + 1
    i = 0
    no_innings = 9
    runs[0] = 0
    runs[1] = 0