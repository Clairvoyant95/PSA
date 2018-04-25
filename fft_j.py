import wave
import numpy
import scipy

my_file = wave.open('<sciezka>', 'rb') # otwieranie pliku


organy = range(16, 15804)
fortepian = range(27, 4186)
kontrabas = range(41, 220)
skrzypce = range(196, 4186)
gitara = range(82, 1047)
saksofon_tenorowy = range(51, 670)
flet = range(261, 2093)
flet_piccolo = range(587, 4186)

instrument_list = [organy, fortepian, kontrabas, skrzypce, gitara, saksofon_tenorowy, flet, flet_piccolo]

fregiencies_in_my_signal = numpy.fft.freq...(my_file)

min_freq = fregiencies_in_my_signal.min
max_freq = max(fregiencies_in_my_signal)

my_signal_range = range(min_freq, max_freq)

if my_signal_range in organy:
    print "da sie zagrac na organach"
elif my_signal_range in fortepian:
    print "da sie zagrac na fortepianie"
elif my_signal_range in kontrabas:
    print "da sie zagrac na kontrabasie"
elif my_signal_range in skrzypce:
    print "da sie zagrac na skrzypcach"
elif my_signal_range in gitara:
    print "da sie zagrac na gitarze"
elif my_signal_range in saksofon_tenorowy:
    print "da sie zagrac na saksofonie tenorowym"
elif my_signal_range in flet:
    print "da sie zagrac na flecie"
elif my_signal_range in flet_piccolo:
    print "da sie zagrac na flecie piccolo"



for instrument in instrument_list:
    if my_signal_range in instrument_list[:value]
        print "da sie zagrac na instrumencie " + instrument[key:]
