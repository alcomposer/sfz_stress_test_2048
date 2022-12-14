# sfz_stress_test_2048

- [x] Single note, creates 2048 sfz <region> objects, playing 2048 sfz layers
- [x] Each region from its own sample, 48000, mono, one minute long (unlooped)
- [x] Pitch transpose up one semitone (avoid skipping interpolation, avoid cache artificial boost when downsampling)
- [x] Each region enables a 4P LPF, 3 bands of peaking EQ. No _oncc for the filters nor eqs.
- [x] 6-point AHDSR enabled for filter cutoff, amp
- [x] Sine wave LFO enabled, assigned to pitch, 1 semitone depth, 4 hz for all layers
- [x] RAM loading

Using the test:
* Host settings for test: SR = 48kHz, block size = 128, fixed
* Interpolation as sinc, 7-points (equivalent to the one in the original SFZ plugin)

Test passes if:
* No dropouts in the resulting audio. 2010 hardware achieved 70% CPU utilization.
* No dropouts on note-on.
* Audio binary compare perfect of consecutive runs

**Usage**

* `chmod +x st_gen.py st_wav_copy.py`
* `mkdir samples`
* generate samples in samples directory: `./st_wav_copy.py` (11.8 GB needed for copies, possibly use links? Not sure if all sfz players support)
* generate stress test sfz file: `./st_gen.py > stress_test.sfz`
* load stress_test.sfz in sfz sampler & test
