#!/usr/bin/env perl

use strict;
use warnings;

use JSON::XS;

my $json = JSON::XS->new->canonical;

&printResult(&dispatch(@ARGV));

sub printResult {
    my $result = shift;
    print "$result";
}

sub dispatch {
    if(scalar(@_) == 0){
        &usage();
    }

    my $cmd = shift;
    my $result = undef;

    my %cmds = (test => \&call_test, er => \&call_er);

    if($cmd eq '-h' || $cmd eq '-?' || $cmd eq '--help' || $cmd eq '?'){
        &usage();
    }

    if(exists($cmds{$cmd})){
        $result = $cmds{$cmd}(@_);
    } else {
        print STDERR "Command '$cmd' not found\n";
        &usage();
    }

    return $result;
}


sub usage{
    print STDERR "The following commands are exported:\n";
    print STDERR "  test\n";
    print STDERR q{    param 1: Num}, "\n";
    print STDERR q{    return: Num}, "\n";
    print STDERR "  er\n";
    print STDERR q{    param 1: Num}, "\n";
    print STDERR q{    return: Num}, "\n";
    exit 0;
}



sub call_test{
    if(scalar(@_) != 1){
        print STDERR "Expected 1 arguments to 'test', given " . 
        scalar(@_) . "\n";
        exit 1;
    }
    return `python3 pool.py 14 '$_[0]'`;
}


sub call_er{
    if(scalar(@_) != 1){
        print STDERR "Expected 1 arguments to 'er', given " . 
        scalar(@_) . "\n";
        exit 1;
    }
    return `python3 pool.py 15 '$_[0]'`;
}


