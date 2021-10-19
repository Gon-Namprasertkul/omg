#!/usr/bin/env python
# file path is 'sys.argv[0]'


import time as t
from time import sleep
import random
import os, sys
import os.path
import getch

#INTERFACE INFORMATION FOR INTERFACE DEVELOPMENT
name = 'Default-improved(Official)'
version = '1.0'
author = 'foresterblox'



def cal():
    os.system('clear')
    calc = input('Enter calculation: ')
    print("Answer = " + str(eval(calc)))
    print("Press any key to go back")
    getch.getch()
    mainmenu()


def gradecal():
    os.system('clear')
    print('Welcome to grade calculator')
    print('[1] Grade 1-4')
    print('[2] Grade A-F')
    print('[0] Quit')
    print("Enter your choice", end="")
    pls = getch.getch()
    yea = int(pls)
    if yea == 1:
        score = input('Please enter your score: ')
        rs = int(score)
        if rs >= 80:
            print('Grade 4')
        elif rs >= 70:
            print('Grade 3')
        elif rs >= 60:
            print('Grade 2')
        elif rs >= 50:
            print('Grade 1')
        else:
            print('Grade 0')
        print("Press any key to go back")
        getch.getch()
        print('')
        gradecal()
    elif yea == 2:
        afscore = input('Enter your score: ')
        ras = int(afscore)
        if ras >= 90:
            print('Grade A')
        elif ras >= 85:
            print('Grade B+')
        elif ras >= 80:
            print('Grade B')
        elif ras >= 75:
            print('Grade C+')
        elif ras >= 70:
            print('Grade C')
        elif ras >= 65:
            print('Grade D+')
        elif ras >= 60:
            print('Grade D')
        else:
            print('Grade F')
        print("Press any key to go back")
        getch.getch()
        print('')
        gradecal()
    elif yea == 0:
        mainmenu()
    else:
        print("It's not a choice")
        gradecal()


def rand():
    os.system('clear')
    least = input('Please enter the least number: ')
    most = input('Please enter the most number: ')
    result = random.randint(int(least), int(most))
    print('the number is ' + str(result))
    print("Press any key to go back")
    pls = getch.getch()
    print('')
    mainmenu()


def credit():
    os.system('clear')
    print('----------------------------------------------')
    print('')
    print('version 2.0.5')
    print (f'interface: {name}')
    print (f'interface version: {version}')
    print (f'interface author: {author}')
    print('language used:Python')
    print('ascii powered by RoboTech')
    print('RoboTech made by Tech co')
    print('RoboTech: https://top.gg/bot/865927980353716234')
    print('Python link: https://python.org')
    print('')
    print('----------------------------------------------')
    print("Press any key to go back")
    getch.getch()
    mainmenu()

def cdtm():
    os.system('clear')
    seconds = int(input('How many seconds to countdown: '))
    for i in range(seconds):
        print(str(seconds - i) + 'seconds left')
        t.sleep(1)
    print("Press any key to go back")
    pls = getch.getch()


def cmd():
    os.system('clear')
    print('Welcome to terminal')
    while True:
        cmdline = input('Please enter a command: ')
        if cmdline == 'help':
            print('---------------------------------------------------')
            print('')
            print('List of commands:')
            print('1.Help (this command)')
            print('2.exit is a command to go back to menu')
            print('3.shutdown is a command for shutting down the stupidOS')
            print('4.sudo is a sudo command')
            print('5.randnum is a command to open random number generator')
            print('6.cal is a command to open calculator')
            print('7.grade is a command to open grade calculator')
            print('')
            print('---------------------------------------------------')
            sudo = input()
        elif cmdline == 'exit':
            mainmenu()
        elif cmdline == 'shutdown':
            quit()
        elif cmdline == 'sudo':
            sudo = input('Please enter a sudo command: ')
            if sudo == '-h':
                print('---------------------------------------------------')
                print('')
                print('ABOUT SUDO')
                print('sudo is a command for admin')
                print('you can use sudo command to use admin commands')
                print('LIST OF COMMANDS')
                print('1.-h (this command)')
                print('2.-k is a command to uninstall stupidOS')
                print('3.-o is a command to open a file')
                print('')
                print('---------------------------------------------------')
            elif sudo == '-k':
                yorno = input('Are you sure you want to kill stupidOS?(y/n): ')
                if yorno == 'y':
                    os.remove(sys.argv[0])
                elif yorno == 'n':
                    cmd()
            elif sudo == '-o':
                findfile = input('Please enter a file path')
                os.startfile(findfile)
        elif cmdline == 'calc':
            cal()
        elif cmdline == 'grade':
            gradecal()
        elif cmdline == 'randnum':
            rand()
        elif cmdline == 'countdown':
            cdtm()
        elif cmdline == 'credit':
            credit()
        elif cmdline == 'ping':
            web = input('Please enter url: ')
            os.system(f'ping {web}')
        elif cmdline == 'clear':
            os.system('clear')
        else:
            print('command not found')


def mainmenu():
    os.system('clear')
    print('Welcome to stupidOS')
    print('[1] Calculator')
    print('[2] Grade calculator')
    print('[3] Random number generator')
    print('[4] Countdown timer')
    print('[5] Terminal')
    print('[6] Credit')
    print('[0] Quit')
    print("Press your choice", end="")
    option = getch.getch()
    choice = int(option)
    print("")
    if choice == 1:
        cal()
    elif choice == 2:
        gradecal()
    elif choice == 0:
        print('Thank you for using!')
        print('Closing..')
        quit()
    elif choice == 3:
        rand()
    elif choice == 4:
        cdtm()
    elif choice == 5:
        cmd()
    elif choice == 6:
        credit()
    else:
        print("It's not a choice!")
        print("Press any key to go back")
        getch.getch()
        mainmenu()

def passcode():
    heyhey = input('Enter the passcode: ')
    heyhey1 = int(heyhey)
    if heyhey1 == (3958):
        mainmenu()
    else:
        print('Invalid passcode')
        passcode()


def start():
    print('      _               _     _  ___  ____  ')
    print('  ___| |_ _   _ _ __ (_) __| |/ _ \/ ___| ')
    print(" / __| __| | | | '_ \| |/ _` | | | \___ \ ")
    print(' \__ \ |_| |_| | |_) | | (_| | |_| |___) |')
    print(' |___/\__|\__,_| .__/|_|\__,_|\___/|____/ ')
    print('               |_|                        ')


start()
passcode()

# this is development version
