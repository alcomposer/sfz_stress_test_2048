#!/usr/bin/env python3

group_settings = """
<group>
ampeg_attack=1
ampeg_hold=0.5
ampeg_decay=1
ampeg_sustain=100
ampeg_release=1

resonance=6
cutoff=2000
fil_type=lpf_4p
fileg_attack=1
fileg_hold=1
fileg_decay=2
fileg_sustain=100
fileg_release=0.5

transpose=1

lfo1_pitch=100
lfo1_freq=4

eq1_freq=500
eq1_bw=0.1
eq1_gain=24

eq2_freq=800
eq2_bw=0.1
eq2_gain=24

eq3_freq=1200
eq3_bw=0.1
eq3_gain=24
"""

print(group_settings)

for x in range(2048):
    #print("<region> sample=st_sample.wav")
    print("<region> sample=samples/st_sample_" + str(x) + ".wav")
