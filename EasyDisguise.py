import pyautogui, keyboard, os, random
from pynput.keyboard import Key, Controller
import time

def checkClasses():
    global cList
    global dBind
    global numOfClasses
    global strClasses
    numOfClasses = 0
    strClasses = str(numOfClasses)
    cList = [
     0]
    haveZero = 0
    print('Developed by Caleb Jackson ;)')
    print('What is your disguise bind choice? ex:  q')
    dBind = input('Disguise with = ')
    list_of_files = os.listdir()
    if 'Classes' in list_of_files:
        file1 = open('Classes', 'r')
        verify = file1.read().splitlines()
        print('Working')
        print("Pulling settings from 'Classes' file ")
        print('-------')
        if 'Scout 1' in verify:
            print('scout enabled')
            numOfClasses += 1
            cList.extend([1])
            if haveZero in cList:
                cList.remove(0)
        if 'Scout 0' in verify:
            print('Scout disabled')
        if 'Solier 1' in verify:
            print('Soldier enabled')
            numOfClasses += 1
            cList.extend([2])
            if haveZero in cList:
                cList.remove(0)
        if 'Solier 0' in verify:
            print('Soldier disabled')
        if 'Pyro 1' in verify:
            print('Pyro enabled')
            numOfClasses += 1
            cList.extend([3])
            if haveZero in cList:
                cList.remove(0)
        if 'Pyro 0' in verify:
            print('Pyro disabled')
        if 'Demoman 1' in verify:
            print('Demoman enabled')
            numOfClasses += 1
            cList.extend([4])
            if haveZero in cList:
                cList.remove(0)
        if 'Demoman 0' in verify:
            print('Demoman disabled')
        if 'Heavy 1' in verify:
            print('Heavy enabled')
            numOfClasses += 1
            cList.extend([5])
            if haveZero in cList:
                cList.remove(0)
        if 'Heavy 0' in verify:
            print('Heavy disabled')
        if 'Engineer 1' in verify:
            print('Engineer enabled')
            numOfClasses += 1
            cList.extend([6])
            if haveZero in cList:
                cList.remove(0)
        if 'Enginner 0' in verify:
            print('Engineer disabled')
        if 'Medic 1' in verify:
            print('Medic enabled')
            numOfClasses += 1
            cList.extend([7])
            if haveZero in cList:
                cList.remove(0)
        if 'Medic 0' in verify:
            print('Medic disabled')
        if 'Sniper 1' in verify:
            print('Sniper enabled')
            numOfClasses += 1
            cList.extend([8])
            if haveZero in cList:
                cList.remove(0)
        if 'Sniper 0' in verify:
            print('Sniper disabled')
    elif 'Spy 1' in verify:
        print('Spy enabled')
        numOfClasses += 1
        cList.extend([9])
        if haveZero in cList:
            cList.remove(0)
        if 'Spy 0' in verify:
            print('Spy disabled')
        checker = random.choice(cList)
        if checker == 0:
            print('ERROR!!! Are all classes disabled?... Please be sure you enable at least one class')
    else:
        Disguiser()


def Disguiser():
    ran = random.choice(cList)
    key = keyboard.read_key()
    scout = 1
    soldier = 2
    pyro = 3
    demo = 4
    heavy = 5
    engineer = 6
    medic = 7
    sniper = 8
    spy = 9
    if ran == scout:
        print('SCOUT')
        if key == dBind:
            print('worked')
            time.sleep(0.2)
            keyboard.press('4')
            keyboard.release('4')
            time.sleep(0.2)
            keyboard.press('1')
            keyboard.release('1')
            Disguiser()
        else:
            Disguiser()
    else:
        if ran == soldier:
            print('SOLDIER')
            if key == dBind:
                print('worked')
                time.sleep(0.2)
                keyboard.press('4')
                keyboard.release('4')
                time.sleep(0.2)
                keyboard.press('2')
                keyboard.release('2')
                Disguiser()
            else:
                Disguiser()
        else:
            if ran == pyro:
                print('PYRO')
                if key == dBind:
                    print('worked')
                    time.sleep(0.2)
                    keyboard.press('4')
                    keyboard.release('4')
                    time.sleep(0.2)
                    keyboard.press('3')
                    keyboard.release('3')
                    Disguiser()
                else:
                    Disguiser()
            else:
                if ran == demo:
                    print('DEMO')
                    if key == dBind:
                        print('worked')
                        time.sleep(0.2)
                        keyboard.press('4')
                        keyboard.release('4')
                        time.sleep(0.2)
                        keyboard.press('4')
                        keyboard.release('4')
                        Disguiser()
                    else:
                        Disguiser()
                else:
                    if ran == heavy:
                        print('HEAVY')
                        if key == dBind:
                            print('worked')
                            time.sleep(0.2)
                            keyboard.press('4')
                            keyboard.release('4')
                            time.sleep(0.2)
                            keyboard.press('5')
                            keyboard.release('5')
                            Disguiser()
                        else:
                            Disguiser()
                    if ran == medic:
                        print('MEDIC')
                        if key == dBind:
                            print('worked')
                            time.sleep(0.2)
                            keyboard.press('4')
                            keyboard.release('4')
                            time.sleep(0.2)
                            keyboard.press('7')
                            keyboard.release('7')
                            Disguiser()
                        else:
                            Disguiser()
                if ran == engineer:
                    print('ENGINEER')
                    if key == dBind:
                        print('worked')
                        time.sleep(0.2)
                        keyboard.press('4')
                        keyboard.release('4')
                        time.sleep(0.2)
                        keyboard.press('6')
                        keyboard.release('6')
                        Disguiser()
                    else:
                        Disguiser()
            if ran == sniper:
                print('SNIPER')
                if key == dBind:
                    print('worked')
                    time.sleep(0.2)
                    keyboard.press('4')
                    keyboard.release('4')
                    time.sleep(0.2)
                    keyboard.press('8')
                    keyboard.release('8')
                    Disguiser()
                else:
                    Disguiser()
        if ran == spy:
            print('SPY')
            if key == dBind:
                print('worked')
                time.sleep(0.2)
                keyboard.press('4')
                keyboard.release('4')
                time.sleep(0.2)
                keyboard.press('9')
                keyboard.release('9')
                Disguiser()
            else:
                Disguiser()


checkClasses()
