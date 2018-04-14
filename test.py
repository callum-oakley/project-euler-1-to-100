import json
import os
import re
import sh
import time


class Reporter:
    good = True

    def report(self, msg=None):
        if msg:
            if self.good:
                print()
                self.good = False
            print(msg)
        else:
            print('.', end='', flush=True)


def test(answers):
    reporter, ok = Reporter(), True
    files = sorted(
        f for f in os.listdir() if re.match(r'problem_\d{3}\.py', f))
    for file in files:
        n = file[8:11]
        if n not in answers:
            ok = False
            reporter.report('MISSING: no test for {}'.format(file))
            continue
        start = time.time()
        result = sh.python(file)
        elapsed = time.time() - start
        if result != answers[n] + '\n':
            ok = False
            reporter.report('WRONG: expected {} but got {} ({})'.format(
                answers[n], result.strip(), file))
        elif elapsed > 60:
            ok = False
            reporter.report('SLOW: {} took {}s to run'.format(
                file, round(elapsed)))
        else:
            reporter.report()
    if ok:
        print('\nOK')


test(json.loads(open('answers.json').read()))
