import wave
import numpy
import scipy

my_file = wave.open("", rb) # otwieranie pliku

instrument_list = ['organy':range(16, 15804),
                   'fortepian':range(27, 4186),
                   'kontrabas':range(41, 220),
                   'skrzypce':range(196, 4186),
                   'gitara':range(82,1047),
                   'saksofon tenorowy':range(51,670),
                   'flet':range(261,2093),
                   'flet piccolo':range(587,4186)]

# organy = (16 - 15804)
# fortepian = (27 - 4186)
# kontrabas = (41 - 220)
# skrzypce = (196 - 4186)
# gitara = (82 - 1047)
# saksofon_tenorowy = (51 - 670)
# flet = (261 - 2093)
# flet_piccolo = (587 - 4186)

fregiencies_in_my_signal = numpy.fft.freq...(my_file)

min_freq = fregiencies_in_my_signal.min
max_freq = max(fregiencies_in_my_signal)

my_signal_range = range(min_freq, max_freq)

#if my_signal_range in organy:
#    print "da sie zagrac na organach"
#elif: my_signal_range


for instrument in instrument_list:
    if my_signal_range in instrument_list[:value]
        print "da sie zagrac na instrumencie " + instrument[key:]
