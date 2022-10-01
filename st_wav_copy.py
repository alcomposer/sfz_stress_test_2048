#!/usr/bin/env python3

import shutil

for x in range(2048):
    shutil.copy2("st_sample.wav", "samples/st_sample_" + str(x) + ".wav")