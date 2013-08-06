from nose.tools import *
from numpy import testing as np
from StringIO import StringIO
from smsls import file_ops 

def create_out_files_test():
    basename = 'test'
    outfile = StringIO(file_ops.create_out_files(basename))

def get_which_pixels_test():
    peaks = file_ops.get_which_pixels('peaks')
    rolloff = file_ops.get_which_pixels('rolloff')
    np.assert_array_equal(peaks, (20, 89, 155, 221, 285, 351, 418, 486))
    np.assert_array_equal(rolloff[:,0], 
            (5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35)) 

def read_temp_header_test():
##learn how to simulat the presence of this file
    header = '''Header Size:  7
Version:  2
Sampling Interval:  1
Sampling Rate:  1
Sample Count:  55595
Device Serial Number:  0
Sample Number, Data/Time, CHANNEL0, CHANNEL1, CHANNEL2, CHANNEL3, CHANNEL4, CHANNEL5, CHANNEL6, CHANNEL7, Events
         1,   08/02/2013 06:13:15.432 PM, 29.1881, 29.9276, 30.9153, 30.8196, 28.8607, 28.6462, 29.2038, 31.0845, DAQ Start, LOG Start
         2,   08/02/2013 06:13:16.432 PM, 29.1855, 29.9356, 30.9201, 30.8183, 28.8586, 28.6402, 29.2059, 31.0803
         3,   08/02/2013 06:13:17.432 PM, 29.1826, 29.9354, 30.9173, 30.8254, 28.8483, 28.6494, 29.2125, 31.0769
    '''
    f = StringIO(header)
    header, column = file_ops.read_temp_header(f)
    assert_equal( int(header['Sampling Interval']), 1)
    assert_equal( int(header['Sampling Rate']), 1)
    assert_equal( int(header['Sample Count']), 55595)
    assert_items_equal(column, ('Sample Number', 'Data/Time', 'CHANNEL0',
        'CHANNEL1', 'CHANNEL2', 'CHANNEL3', 'CHANNEL4', 'CHANNEL5', 
        'CHANNEL6', 'CHANNEL7', 'Events'))
