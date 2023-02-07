import math
import time
import pyautogui
import numpy
import scipy
from scipy.stats import *


time.sleep(10800)
pyautogui.typewrite("ok now")
pyautogui.keyDown('enter')


randomMet = input("Are the samples taken randomly? yes or no: ")
if randomMet.lower().strip() == "yes":
    print("Random samples have been taken")
    meanOrProp = input("m for Mean and p for Proportion: ")
else:
    print("proceed with caution")
    meanOrProp = input("m for Mean and p for Proportion: ")

if meanOrProp.lower().strip() == "m":
    sampleSize = float(input("sample size: "))
    popSize = float(input("population size: "))
elif meanOrProp.lower().strip() == "p":
    pHat = float(input("p-hat: "))
    sampleSize = float(input("sample size: "))
    popSize = float(input("population size: "))

def conditionsForInference():
    if meanOrProp.lower().strip() == "m":
        if sampleSize >= 30:
            print("Normality has been met")
        else:
            print("Normality has not been met")
        if (10 * sampleSize) <= popSize:
            print("Independence has been established")
        else:
            print("Independence has not been established")
    if meanOrProp.lower().strip() == "p":
        if sampleSize*pHat >= float(10):
            if sampleSize*(1-pHat) >= float(10):
                print("Normality has been established")
        else:
            print("Normality has not been met")
        if (10 * sampleSize) <= popSize:
            print("Independence has been met")
        else:
            print("Independence has not been established")

conditionsForInference()
