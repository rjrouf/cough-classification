from __future__ import division
import numpy 
import pickle
import os
import sys
import math
import code
from scipy.signal import lfilter
import speechproc
from copy import deepcopy


def getVad(finwav):

    winlen, ovrlen, pre_coef, nfilter, nftt = 0.025, 0.01, 0.97, 20, 512
    ftThres=0.5; vadThres=0.4
    opts=1

    fs, data = speechproc.speech_wave(finwav)   
    ft, flen, fsh10, nfr10 =speechproc.sflux(data, fs, winlen, ovrlen, nftt)


    # --spectral flatness --
    pv01=numpy.zeros(nfr10)
    pv01[numpy.less_equal(ft, ftThres)]=1 
    pitch=deepcopy(ft)

    pvblk=speechproc.pitchblockdetect(pv01, pitch, nfr10, opts)


    # --filtering--
    ENERGYFLOOR = numpy.exp(-50)
    b=numpy.array([0.9770,   -0.9770])
    a=numpy.array([1.0000,   -0.9540])
    fdata=lfilter(b, a, data, axis=0)


    #--pass 1--
    noise_samp, noise_seg, n_noise_samp=speechproc.snre_highenergy(fdata, nfr10, flen, fsh10, ENERGYFLOOR, pv01, pvblk)

    #sets noisy segments to zero
    for j in range(n_noise_samp):
        fdata[range(int(noise_samp[j,0]),  int(noise_samp[j,1]) +1)] = 0 


    vad_seg=speechproc.snre_vad(fdata,  nfr10, flen, fsh10, ENERGYFLOOR, pv01, pvblk, vadThres)
    
    return vad_seg
    