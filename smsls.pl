#!/usr/bin/perl -w
#$Id$
use strict;
use constant DEBUGGING => 0;
use constant HOME => "/home/cmcfaul/Documents/"; #these should change
use constant DATADIR => "/home/cmcfaul/data/"; #with the machine

my @cell_center = (20, 89, 155, 221, 285, 351, 418, 486); # one point for each cell
my @range = -10..10;
my $step = 3;
my $cell = 1;
my @pixels = ();
#my @pixels = 1..39; # for cell 01
#my @pixels = 202..240; # for cell 04
#my @pixels = 467..505; # for cell 08
foreach (@range) {
	 my $test = $cell_center[$cell - 1] + $_*$step;
	 push(@pixels, $test) unless ($test < 0 || $test > 511);
}
@pixels = @cell_center; #to use one point for each cell

print "Created by $Id$\n ";
my $files = 0;
my @offset = (0);
while(<>) {
	my @data = split /\t/, $_;
	my $num = @data;
	if ($num == 1) { }
	elsif ($data[0] =~ /Time/) {
		unless ($files) {
			print $data[0] . "\t";
			foreach (@pixels) {
				print $data[$_] . "\t";
			}
			print "\n";
		}	
		$files ++;
	}
	else {
		print $data[0] + $offset[$files-1] . "\t";
		foreach (@pixels) {
			print $data[$_] . "\t";
		}
	print "\n";
	$offset[$files] = $offset[$files-1] + $data[0];
	}
}
