import math
from scipy.stats import *

cLevel = float(input("confidence level (ex 90, 95, 99 etc): "))
meanOrProp = input("m for Mean and p for Proportion: ")

if meanOrProp.lower().strip() == "m":
    populationOrSampleSD = input("pop for population SD and sam for sample SD: ")
    if populationOrSampleSD.lower().strip() == "pop":
        popSD1 = float(input("population SD1: "))
        popSD2 = float(input("population SD2: "))
    elif populationOrSampleSD.lower().strip() == "sam":
        samSD1 = float(input("sample SD1: "))
        samSD2 = float(input("sample SD2: "))
    testStatistic1 = float(input("x-bar1 value: "))
    sampleSize1 = float(input("sample1 size: "))
    testStatistic2 = float(input("x-bar2 value: "))
    sampleSize2 = float(input("sample2 size: "))
elif meanOrProp.lower().strip() == "p":
    testStatistic1 = float(input("p-hat1: "))
    sampleSize1 = float(input("sample1 size: "))
    testStatistic2 = float(input("p-hat2: "))
    sampleSize2 = float(input("sample2 size: "))

if sampleSize1 < sampleSize2:
    degFree = sampleSize1 - 1
elif sampleSize2 < sampleSize1:
    degFree = sampleSize2 - 1
testStatistic = None
standardError = None
critValue = None

def twoConfidenceInterval():
    #test statistic computation
    testStatistic = testStatistic1 - testStatistic2
    #computes the standard error based on whether it is a mean or proportion sample and whether given a sample or population SD
    if meanOrProp.lower().strip() == "p":
        standardError = math.sqrt(((testStatistic1 * (1-testStatistic1)) / sampleSize1) + ((testStatistic2 * (1-testStatistic2)) / sampleSize2))
    elif meanOrProp.lower().strip() == "m":
        if populationOrSampleSD.lower().strip() == "pop":
            standardError = math.sqrt(((popSD1 * popSD1) / sampleSize1) + ((popSD2 * popSD2) / sampleSize2))
        if populationOrSampleSD.lower().strip() == "sam":
            standardError = math.sqrt(((samSD1 * samSD1) / sampleSize1) + ((samSD2 * samSD2) / sampleSize2))
    #computes the critical value based on whether it is a mean or proportion sample and whether given a sample or population SD
    if meanOrProp.lower().strip() == "p":
        critValue = math.sqrt(norm.ppf(((100 - cLevel) / 100) / 2) * norm.ppf(((100 - cLevel) / 100) / 2))
    elif meanOrProp.lower().strip() == "m":
        if populationOrSampleSD.lower().strip() == "pop":
            critValue = math.sqrt(norm.ppf(((100 - cLevel) / 100) / 2) * norm.ppf(((100 - cLevel) / 100) / 2))
        if populationOrSampleSD.lower().strip() == "sam":
            critValue = math.sqrt(t.ppf(((100 - cLevel) / 100) / 2, degFree) * t.ppf(((100 - cLevel) / 100) / 2, degFree))

    #calculates the interval based on the statistics given through input and prior computation
    interval = [testStatistic - (critValue * standardError), testStatistic + (critValue * standardError)]
    print(interval[0], ", ", interval[1])
    print("test statistic: ", testStatistic, "critical value: ", critValue, "standard error: ", standardError)

twoConfidenceInterval()