import subprocess
import setup_util
import multiprocessing
import os

bin_dir = os.path.expanduser('~/FrameworkBenchmarks/installs/pypy/bin')
NCPU = multiprocessing.cpu_count()

proc = None


def start(args):
    global proc
    proc = subprocess.Popen([
        bin_dir + "/gunicorn",
        "app:app",
        '-k', 'tornado',
        "-b", "0.0.0.0:8080",
        '-w', str(NCPU*3),
        "--log-level=critical"],
        cwd="falcon")
    return 0

def stop():
    global proc
    if proc is None:
        return 0
    proc.terminate()
    proc = None
    return 0
