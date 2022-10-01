#!/usr/bin/env python3

group_settings = """
<group>
ampeg_attack=1
ampeg_hold=0.5
ampeg_decay=1
ampeg_sustain=100
ampeg_release=1
"""

print(group_settings)

for x in range(2048):
    #print("<region> sample=st_sample.wav")
    print("<region> sample=samples/st_sample_" + str(x) + ".wav")