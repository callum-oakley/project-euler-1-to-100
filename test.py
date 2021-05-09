import os
import re
import sys
import time
import importlib


def test(file):
    m = re.match(r"problem_\d{3}", file)
    if not m:
        return
    module = m.group()
    print(f"{module}: ", end="")
    start = time.time()
    result = str(importlib.import_module(module).main())
    elapsed = round(time.time() - start)
    expected = open(file).readlines()[-1].strip("# \n")
    if result != expected:
        print(f"WRONG expected {expected} but got {result}")
        sys.exit(1)
    elif elapsed >= 60:
        print(f"SLOW {elapsed}s")
        sys.exit(1)
    else:
        print(f"OK {elapsed}s")


def main():
    if len(sys.argv[1:]) > 0:
        test_files = [f"problem_{n}.py" for n in sys.argv[1:]]
    else:
        test_files = os.listdir()
    for f in sorted(test_files):
        test(f)


if __name__ == "__main__":
    main()
