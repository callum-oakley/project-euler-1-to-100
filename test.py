import json
import os
import re
import sh
import time
import multiprocessing


def test(file):
    n = file[8:11]
    if n not in answers:
        print('\nMISSING: no test for {}'.format(file))
        return
    start = time.time()
    result = sh.python(file)
    elapsed = time.time() - start
    if result != answers[n] + '\n':
        print('\nWRONG: expected {} but got {} ({})'.format(
            answers[n], result.strip(), file))
    elif elapsed > 60:
        print('\nSLOW: {} took {}s to run'.format(file, round(elapsed)))
    else:
        print('.', end='', flush=True)


answers = json.loads(open('answers.json').read())
with multiprocessing.Pool() as p:
    p.map(test, (f for f in os.listdir() if re.match(r'problem_\d{3}\.py', f)))
