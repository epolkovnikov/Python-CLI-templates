#!/usr/bin/env python
"""loc2log template v.0.2
Template for a simple command line script, Python 2.6.

Usage:
    <script_name> [-hvd]
 
    -v, --verbose
        Verbose output
    -d, --debug
        Debug level
    -h, --help
        This usage screen
"""
import traceback
import os
import sys
import subprocess
import getopt
import datetime
import re

is_verbose = False
debug_level = 0

def usage(rc):
    """Show usage from 'About', then exit."""
    print globals()['__doc__']
    sys.exit(rc)

def do(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    (std, err) = p.communicate()
    # rc = p.returncode
    return std

def main():
    try:
        optlist, arglist = getopt.getopt(sys.argv[1:],
                                         'hvd:',
                                         ['help','h','verbose', 'debug'])
    except Exception, e:
        print >>sys.stderr, "[ERROR] Unexpected input."
        usage(1)

    if len(optlist) == 0:
        print >>sys.stderr, "[ERROR] Missing input parameters."
        usage(1)

    for opt, arg in optlist:
        if opt in ('-h','--help'):
            print 'Help:'
            usage(0)
        elif opt in ('-v', '--verbose'):
            is_verbose = True
        elif opt in ('-d', '--debug'):
            debug_level = int(arg)
            print "debug_level=" + str(arg)
        else:
            print >>sys.stderr, "[ERROR] Unknown input parameter(s)."
            usage(1) 

if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except KeyboardInterrupt:
        print("Keyboard interrupt.")
        sys.exit(0)
    except SystemExit:
        sys.exit(0)
    except Exception, e:
        print str(e)
        traceback.print_exc()
        sys.exit(1)
