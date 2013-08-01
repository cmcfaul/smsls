from nose.tools import *
from smsls import file_ops 

def create_out_files_test():
    basename = 'test'
    outfile = file_ops.create_out_files(basename)
    assert_is_instance(outfile[0], file)
    assert_equal(outfile[0].mode, 'w')
    assert_equal(outfile[0].name, 'test_c1.dat')

def get_which_pixels_test():
    peaks = file_ops.get_which_pixels('peaks')
    rolloff = file_ops.get_which_pixels('rolloff')
    assert_equal(peaks[4], 285)
    assert_equal(rolloff[0][5], 336)

#def read_temp_header_test():
##learn how to simulat the presence of this file
#    f, header, column = file_ops.read_temp_header('test.txt')
#    assert_is_instance(f, file)
#    assert_equal(f.mode, 'r')
#    assert_equal(f.name, 'test.txt')
#    period = int(header['Sampling Interval'])
#    freq = int(header['Sampling Rate'])
#    assert_equal(period*freq, 1)
    
