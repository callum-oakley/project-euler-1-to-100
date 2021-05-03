import os
import re
import sh
import sys
import time


def test(file):
    n = file[8:11]
    print(f"{n}: ", end="")
    start = time.time()
    result = sh.python3(file)
    elapsed = time.time() - start
    answer = open(file).read().splitlines()[-1].lstrip("# ")
    if result != answer + "\n":
        print(f"WRONG expected {answer} but got {result.strip()}")
        sys.exit(1)
    elif elapsed > 60:
        print("SLOW took {round(elapsed)}s")
        sys.exit(1)
    else:
        print("OK")


if len(sys.argv[1:]) > 0:
    test_files = sys.argv[1:]
else:
    test_files = os.listdir()

for f in sorted(test_files):
    if re.match(r"problem_\d{3}\.py", f):
        test(f)
