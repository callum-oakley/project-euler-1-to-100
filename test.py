#! /usr/bin/env python3

import json
import os
import re
import sh
import sys
import time


def test(file):
    n = file[8:11]
    print("{}: ".format(n), end="")
    if n not in answers:
        print("MISSING ANSWER".format(file))
        sys.exit(1)
    start = time.time()
    result = sh.python3(file)
    elapsed = time.time() - start
    if result != answers[n] + "\n":
        print("WRONG expected {} but got {}".format(answers[n], result.strip()))
        sys.exit(1)
    elif elapsed > 60:
        print("SLOW took {}s".format(round(elapsed)))
        sys.exit(1)
    else:
        print("OK")


answers = json.loads(open("answers.json").read())

if len(sys.argv[1:]) > 0:
    test_files = sys.argv[1:]
else:
    test_files = os.listdir()

for f in sorted(test_files):
    if re.match(r"problem_\d{3}\.py", f):
        test(f)
