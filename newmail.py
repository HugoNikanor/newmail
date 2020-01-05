#!/usr/bin/env python3
import os

mailroot = "/home/hugo/mail"

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

if __name__ == "__main__":
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
