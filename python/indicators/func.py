def sma(avlist):
    return sum(i for i in avlist) /len(avlist)

def ema(avg, new_sample, n_length=10):
    a = 2/(n_length+1)
    k_t = new_sample
    prev_ema = avg
    new_ema = (1-a) * prev_ema+ a*k_t
    return new_ema


def macd(short_ema, long_ema, signal_ema, new_sample, n_shortema=3, n_longema=8, n_signal_ema=3):
    '''

    :param short_ema: value of the short ema
    :param long_ema: value of the long ema
    :param signal_ema: value of the signal ema
    :param new_sample: new value of price
    :param n_shortema: number of samples used for short ema
    :param n_longema: number of samples used for long ema
    :param n_signal_ema: number of samples for the signal ema
    :return: macd value and signal_vale, along with short_ema value and long_ema value
    '''
    new_longema = ema(long_ema, new_sample,n_longema)
    new_shortema = ema(short_ema, new_sample, n_shortema)
    macd = new_shortema - new_longema
    new_signalema = ema(signal_ema, macd, n_signal_ema)


    return macd, new_signalema, new_shortema, new_longema