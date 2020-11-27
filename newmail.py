#!/usr/bin/env python3
import os
import re
import time
import argparse

mailroot = "/var/mail/hugo"

def p(path):
    """prettify path"""
    return re.sub('INBOX', '\x1b[1mINBOX\x1b[m', path[len(mailroot) + 1:])

def c(count):
    if count < 10:
        color = 2 # green
    elif count < 100:
        color = 3 # yellow
    else:
        color = 1 # red

    return f"\x1b[1;3{color}m"

def plural(count):
    return "es" if count != 0 else ""

def newmail():
    gen = os.walk(mailroot, topdown=True)
    accounts = []
    for (path, dirs, files) in gen:
        # print(path, sorted(dirs))
        if sorted(dirs) == ["cur", "new", "tmp"]:
            dirs.remove("cur")
            dirs.remove("tmp")

            (_, _, files) = next(gen)
            count = len(files)
            if count != 0:
                accounts.append((path, count))


    output = '\n'.join(f"{c(count)}{count:>6}\x1b[m {p(path)}" for (path, count) in sorted(accounts, key=lambda p: p[0]))
    l = len(accounts)
    output += f"\n\nNew mail in {c(l)}{l}\x1b[m mailbox{plural(l)}."
    return output

parser = argparse.ArgumentParser()
parser.add_argument('--watch', action="store_true")
args = parser.parse_args()

if __name__ == "__main__":
    if args.watch:
        # set terminal title
        print("\x1b]0;Newmail\007")
        os.system("tput civis") # setterm --cursor off
        while True:
            output = newmail()
            now = time.ctime()
            print(f"\033[H\033[J{now}\n\n{output}")
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                break
        os.system("tput cnorm") # setterm --cursor on
    else:
        print(newmail())
