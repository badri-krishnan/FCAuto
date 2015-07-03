#!/usr/bin/python2.7
import os
import wave
import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

def save(path, ext='png', close=True, verbose=False):
    verbose = False
    """Save a figure from pyplot.

    Parameters
    ----------
    path : string
        The path (and filename, without the extension) to save the
        figure to.

    ext : string (default='png')
        The file extension. This must be supported by the active
        matplotlib backend (see matplotlib.backends module).  Most
        backends support 'png', 'pdf', 'ps', 'eps', and 'svg'.

    close : boolean (default=True)
        Whether to close the figure after saving.  If you want to save
        the figure multiple times (e.g., to multiple formats), you
        should NOT close it in between saves or you will have to
        re-plot it.

    verbose : boolean (default=True)
        Whether to print information about when and where the image
        has been saved.

    """

    # Extract the directory and filename from the given path
    directory = os.path.split(path)[0]
    filename = "%s.%s" % (os.path.split(path)[1], ext)
    if directory == '':
        directory = '.'

    # If the directory does not exist, create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    # The final path to save to
    savepath = os.path.join(directory, filename)

    if verbose:
        print("Saving figure to '%s'..." % savepath),

    # Actually save the figure
    plt.savefig(savepath)

    # Close it
    if close:
        plt.close()

    if verbose:
        print("Done")

def plot(tval, filtered, xlabel, ylabel,title, plotpath):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.plot(tval, filtered)
    save(plotpath, ext="png", close=False, verbose=True)
    plt.close()

def min_filter_automata(signal,sig_len,plotpath,rate,wave_path):
    filtered = np.zeros(sig_len)
    prev_val = filtered[0] = float(signal[0])
    max_sigval = max(signal)

    title = 'MinFilteredSignal'
    xlabel = 'Time t'
    ylabel = 'Min Filter Signal'
    plotpath = plotpath + "/" + "min_filter"
    wave_path = plotpath + ".wav"

    for x in xrange(sig_len):
        if(x >= sig_len-2):
            break
        min_3 = float(min(filtered[x],signal[x+1],signal[x+2]))
        filtered[x+1]= min_3
        prev_val = min_3
    filtered[sig_len-1]= (float(signal[sig_len-1]))

    tval = np.arange(0,sig_len)
    plot(tval, filtered, xlabel, ylabel, title, plotpath)
    wav.write(wave_path,rate,filtered)

def min_cellular_automata(signal,sig_len,plotpath,rate,wave_path):
    title = 'MinFilteredSignal'
    xlabel = 'Time t'
    ylabel = 'Min Cellular Signal'
    plotpath = plotpath + "/" + "min_cellular_filter"
    wave_path = plotpath + ".wav"

    filtered = np.zeros(sig_len)
    filtered[0] = float(signal[0])
    for x in xrange(sig_len):
        if(x >= sig_len-2):
            break
        min_3 = float(min(signal[x],signal[x+1],signal[x+2]))
        filtered[x+1]= min_3
    filtered[sig_len-1]= float(signal[sig_len-1])

    tval = np.arange(0,sig_len)
    plot(tval, filtered, xlabel, ylabel, title, plotpath)
    wav.write(wave_path,rate,filtered)

def max_filter_automata(signal,sig_len,plotpath,rate,wave_path):
    title = 'MaxFilteredSignal'
    xlabel = 'Time t'
    ylabel = 'Max Filtered Signal'
    plotpath = plotpath + "/" + "Max_filtered"
    wave_path = plotpath + ".wav"

    filtered = np.zeros(sig_len)
    filtered[0] = float(signal[0])
    for x in xrange(sig_len):
        if(x >= sig_len-2):
            break
        max_3 = float(max(filtered[x],signal[x+1],signal[x+2]))
        filtered[x+1]= max_3
    filtered[sig_len-1]= float(signal[sig_len-1])

    tval = np.arange(0,sig_len)
    plot(tval, filtered, xlabel, ylabel, title, plotpath)
    wav.write(wave_path,rate,filtered)


def max_cellular_automata(signal,sig_len,plotpath,rate,wave_path):
    title = 'MaxCellularSignal'
    xlabel = 'Time t'
    ylabel = 'Max Cellular Signal'
    plotpath = plotpath + "/" + "max_cellular"
    wave_path = plotpath + ".wav"
    filtered = np.zeros(sig_len)
    prev_val = filtered[0] = float(signal[0])
    for x in xrange(sig_len):
        if(x >= sig_len-2):
            break
        max_3 = float(max(prev_val,signal[x+1],signal[x+2]))
        filtered[x+1]= max_3
        prev_val = max_3
    filtered[sig_len-1]= float(signal[sig_len-1])

    tval = np.arange(0,sig_len)
    plot(tval, filtered, xlabel, ylabel, title, plotpath)
    wav.write(wave_path,rate,filtered)


def ave_cellular_automata(signal,sig_len,plotpath,rate,wave_path):
    title = 'AveCellularSignal'
    xlabel = 'Time t'
    ylabel = 'Ave Cellular Signal'
    plotpath = plotpath + "/" + "ave_cellular"
    wave_path = plotpath + ".wav"

    sig_len = len(signal)
    filtered = np.zeros(sig_len)
    filtered[0] = float(signal[0])
    for x in xrange(sig_len):
        if(x >= sig_len-2):
            break

        ave_3 = float(signal[x]+signal[x+1]+signal[x+2])/3
        filtered[x+1] = ave_3
    filtered[sig_len-1] = float(signal[sig_len-1])

    tval = np.arange(0,sig_len)
    plot(tval, filtered, xlabel, ylabel, title, plotpath)
    wav.write(wave_path,rate,filtered)


def ave_filter_automata(signal,sig_len,plotpath,rate,wave_path):
    prev_val = 0
    title = 'AveFilterSignal'
    xlabel = 'Time t'
    ylabel = 'Ave Filter Signal'
    plotpath = plotpath + "/" + "ave_filter"
    wave_path = plotpath + ".wav"

    sig_len = len(signal)
    filtered = np.zeros(sig_len)
    prev_val = filtered[0] = float(signal[0])
    for x in xrange(sig_len):
        if(x >= sig_len-2):
            break
        ave_3 = (float(prev_val + signal[x+1] + signal[x+2])/3)
        filtered[x+1] = ave_3
        prev_val = ave_3
    filtered[sig_len-1]= float(signal[sig_len-1])

    tval = np.arange(0,sig_len)
    plot(tval, filtered, xlabel, ylabel, title, plotpath)
    wav.write(wave_path,rate,filtered)


def parse_wav(file_name):
    file_string = file_name.split('/')
    length_f = len(file_string)
    title = file_string[length_f-1].split(".")
    title = title[0]
    rate, sample = wav.read(file_name)
    plot_save_path = "/Users/badrikrishnan/Data_structures/FI_automata/plots/" + title + "/"
    newwave_save_path = "/Users/badrikrishnan/Data_structures/FI_automata/filtered_wav/" + title + "/"
    sample_save_path = "/Users/badrikrishnan/Data_structures/FI_automata/plots/" + "sample" + "/"

    sig_len= len(sample)


    tval = np.arange(0,sig_len)
    plt.xlabel('Time t')
    plt.ylabel('Original  Signal')
    plt.title('Original Signal vs t')
    plt.plot(tval, sample)
    plotpath = plot_save_path + "/" + "OriginalSignal"
    save(plotpath, ext="png", close=False, verbose=True)
    plt.close()

    """signal = np.array([3,1,2,2,1,3,4,2])
    sig_len_2 = len(signal)
    tval = np.arange(0,sig_len_2)
    plt.xlabel('Time t')
    plt.ylabel('Original  Signal')
    plt.title('Original Signal vs t')
    plt.plot(tval, signal)
    plotpath = sample_save_path + "/" + "OriginalSignal"

    save(plotpath, ext="png", close=False, verbose=True)
    plt.close()

    max_cellular_automata(signal,sig_len_2,sample_save_path)
    max_filter_automata(signal,sig_len_2,sample_save_path)
    ave_cellular_automata(signal,sig_len_2,sample_save_path)
    ave_filter_automata(signal,sig_len_2,sample_save_path)
    min_cellular_automata(signal,sig_len_2,sample_save_path)
    min_filter_automata(signal,sig_len_2,sample_save_path)
    """

    max_cellular_automata(sample, sig_len,plot_save_path,rate,newwave_save_path)
    max_filter_automata(sample,sig_len,plot_save_path,rate,newwave_save_path)
    ave_cellular_automata(sample,sig_len,plot_save_path,rate,newwave_save_path)
    ave_filter_automata(sample,sig_len,plot_save_path,rate,newwave_save_path)
    min_cellular_automata(sample,sig_len,plot_save_path,rate,newwave_save_path)
    min_filter_automata(sample,sig_len,plot_save_path,rate,newwave_save_path)

def main():

    for i in range(1,31):
        input_file = "/Users/badrikrishnan/Data_structures/FI_automata/wavesample/s" + str(i) + ".wav"
        parse_wav(input_file)

if __name__ == '__main__':
    main()
