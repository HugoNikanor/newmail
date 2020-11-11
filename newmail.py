#!/usr/bin/env python3
import os
import time
import argparse

mailroot = "/var/mail/hugo"

def p(path):
    """prettify path"""
    return path[len(mailroot) + 1:]

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

    for (path, count) in sorted(accounts, key=lambda p: p[0]):
        print(f"{c(count)}{count:>6}\x1b[m {p(path)}")

    l = len(accounts)
    print(f"\nNew mail in {c(l)}{l}\x1b[m mailbox{plural(l)}.")

parser = argparse.ArgumentParser()
parser.add_argument('--watch', action="store_true")
args = parser.parse_args()

if __name__ == "__main__":
    if args.watch:
        os.system("tput civis") # setterm --cursor off
        while True:
            print("\033[H\033[J", end="")
            print(time.ctime())
            print("")
            newmail()
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                break
        os.system("tput cnorm") # setterm --cursor on
    else:
        newmail()
