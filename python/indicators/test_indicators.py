from .func import *
import numpy as np

def ExpMovingAverage(values, window):
    """ Numpy implementation of EMA
    """
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    a =  np.convolve(values, weights, mode='full')[:len(values)]
    a[:window] = a[window]
    return a

def test_sma():
    values = [i for i in range(20)]
    average = sma(values[9:19])
    assert(sum(values[9:19])/10 == average)

def test_ema():
    values = [i for i in range(20)]
    average=0
    for i in values:
        average=ema(average, i )

    values.append(20)
    assert(abs(14.59939377261759 - average)< 0.001)

def test_macd():
    values = [i for i in range(20)]
    shortaverage = 0
    longaverage = 0
    macdlongaverage = 0
    macdshortaverage = 0
    signalema = 0
    for i in values:
        shortaverage=ema(shortaverage, i, 3  )
        longaverage = ema(longaverage, i, 8)
        macdvalue, signalema, macdshortaverage, macdlongaverage = macd(macdshortaverage,macdlongaverage,signalema, i)
        assert( abs(macdvalue-(shortaverage-longaverage)) < 0.001)
