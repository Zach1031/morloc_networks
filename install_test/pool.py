#!/usr/bin/env python

import sys
import subprocess
import json
from pymorlocinternals import (mlc_serialize, mlc_deserialize)
from collections import OrderedDict

sys.path = ["/Users/zachdefazio/.morloc/src"] + sys.path

from pybase.core import *
from pybase.data import *

def _morloc_foreign_call(args):
    try:
        sysObj = subprocess.run(
            args,
            stdout=subprocess.PIPE,
            check=True
        )
    except subprocess.CalledProcessError as e:
        sys.exit(str(e))

    return(sysObj.stdout.decode("ascii"))

def m9(x0):
    a0 = mlc_deserialize(x0, ("float",None));
    a1 = mlc_add(a0, 1.0)
    a2 = mlc_serialize(a1, ("float",None))
    return(a2)

if __name__ == '__main__':
    try:
        cmdID = int(sys.argv[1])
    except IndexError:
        sys.exit("Internal error in {}: no manifold id found".format(sys.argv[0]))
    except ValueError:
        sys.exit("Internal error in {}: expected integer manifold id".format(sys.argv[0]))
    try:
        dispatch = {
            9: m9,
        }
        f = dispatch[cmdID]
    except KeyError:
        sys.exit("Internal error in {}: no manifold found with id={}".format(sys.argv[0], cmdID))

    result = f(*sys.argv[2:])

    print(result)
