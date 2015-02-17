#!/usr/bin/env python

import subprocess

base_host = '127.0.0.'

for i in range(1,254):
    host = base_host + str(i)
    ping = subprocess.Popen(
        ["ping", "-c", "2", host],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )

    out, error = ping.communicate()
    print out
