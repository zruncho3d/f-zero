#!/usr/bin/python3
# Script to compute standard deviation from the output of BED_MESH_OUTPUT with Klipper
# Copy/paste into a file the list of points after 'Mesh Leveling Probed Z positions'...
# The inputs can be split across multiple lines.
# Paste it into a file and the pipe that as input, e.g.:
#   cat data.txt | ./bed_mesh_stats.py
import statistics
import sys
f = sys.stdin
data = ([float(x) for x in f.read().replace('\n', ' ').split()])
s = statistics.stdev(data)
median = statistics.median(data)
print("Min: %0.3f" % min(data))
print("Max: %0.3f" % max(data))
print("Median: %0.3f" % median)
print("Standard Deviation: %0.3f" % s)


