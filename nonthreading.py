# -*- coding: utf-8 -*-

import time
import random
import keyboard
import pyautogui
import sys


class Main:  # PEP8: `CamelCaseNames` for classes

    def __init__(self):
        self.run = True
        # Used to stop the while true click loop
        keyboard.add_hotkey('n', self.stop)

        self.main()

    def main(self):
        # Time delay for mouse movement
        pyautogui.PAUSE = 0.01
        # Used for when to press alt and shift
        z=1
        # Coordinates on screen to click for monsters
        coords = [(327, 200),
                  (313, 309),
                  (307, 440),
                  (439, 440),
                  (561, 440),
                  (560, 320),
                  (428, 322),
                  (324, 198),
                  (437, 203),
                  (587, 222)
                  ]
        # Used for getting coordinates on screen for leveling up abilities based on class
        def grab_coordinates(classType):
            if classType == 'Feeder':
                  main_coord = (765,395)
                  second_coord = (815,420)
            elif classType == 'Samurai':
                  main_coord = (765,395)
                  second_coord = (815,420)
            elif classType == 'Paladin':
                  main_coord = (765,395)
                  second_coord = (815,420)
            elif classType == 'Monk':
                  main_coord = (765,395)
                  second_coord = (720,420)
            elif classType == 'Ninja':
                  main_coord = (765,395)
                  second_coord = (815,420)
            elif classType == 'Warlock':
                  main_coord = (720,500)
                  second_coord = (815,500)
            elif classType == 'Headhunter':
                  main_coord = (765,395)
                  second_coord = (815,420)
            elif classType == 'Alchemist':
                  main_coord = (720,500)
                  second_coord = (815,500)
            return main_coord, second_coord
        
        classType = grab_coordinates(sys.argv[1])
        skillType = sys.argv[2]
        statType = sys.argv[3]

        # Append class abilities to coords list
        if skillType == 'Main':
            coords.append(list(classType[0]))
        else:
            coords.append(list(classType[1]))

        # Append class attributes to coords list
        if statType == 'Str':
            coords.append((780,260))
        elif statType == 'Dex':
            coords.append((780,275))
        elif statType == 'Intel':
            coords.append((780,296))
        else:
            coords.append((780,316))

        while self.run:
            # Click randomly with coords list
            random.shuffle(coords)
            
            # Move to coordinates and click
            for x, y in coords:
                pyautogui.moveTo(x, y, 0.01, pyautogui.easeInOutQuad)
                pyautogui.click(clicks=1, interval=0.015)
                if not self.run:
                    return  # directly exit function `main()`

            # Trying to time when it is best to press shift and alt for ability cast
            if z % 7 == 0:
                pyautogui.press('shift')
            elif z % 9 == 0:
                pyautogui.press('alt')

            z += 1

    def stop(self):
        self.run = False
        
program = Main()