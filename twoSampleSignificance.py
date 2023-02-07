import math
import numpy
import scipy
from scipy.stats import *

alphaLevel = float(input("alpha level (ex .05, .01, etc): "))
meanOrProp = input("m for Mean and p for Proportion: ")

if meanOrProp.lower().strip() == "m":
    populationOrSampleSD = input("pop for population SD and sam for sample SD: ")
    if populationOrSampleSD.lower().strip() == "pop":
        popSD1 = float(input("population SD1: "))
        popSD2 = float(input("population SD2: "))
    elif populationOrSampleSD.lower().strip() == "sam":
        samSD1 = float(input("sample SD1: "))
        samSD2 = float(input("sample SD2: "))
    statistic1 = float(input("x-bar1 value: "))
    sampleSize1 = float(input("sample1 size: "))
    parameter1 = float(input("hypothesized population mean (usually 0): "))
    statistic2 = float(input("x-bar2 value: "))
    sampleSize2 = float(input("sample2 size: "))
    parameter2 = float(input("hypothesized population mean (usually 0): "))

elif meanOrProp.lower().strip() == "p":
    statistic1 = float(input("p-hat1: "))
    sampleSize1 = float(input("sample1 size: "))
    parameter1 = float(input("parameter1 (usually 0): "))
    statistic2 = float(input("p-hat2: "))
    sampleSize2 = float(input("sample2 size: "))
    parameter2 = float(input("parameter2 (usually 0): "))

if sampleSize1 < sampleSize2:
    degFree = sampleSize1 - 1
elif sampleSize2 < sampleSize1:
    degFree = sampleSize2 - 1
standardError = None
testStatistic = None
pValue = None

def significanceTest():

    statistic = statistic1 - statistic2
    parameter = parameter1 - parameter2

    if meanOrProp.lower().strip() == "p":
        testStatistic = (statistic - parameter)/math.sqrt((statistic1 * (1-statistic1) / sampleSize1) + (statistic2 * (1-statistic2) / sampleSize2))
        pValue = norm.cdf(testStatistic)
    elif meanOrProp.lower().strip() == "m":
        if populationOrSampleSD.lower().strip() == "pop":
            testStatistic = (statistic - parameter)/math.sqrt(((popSD1 * popSD1)/sampleSize1) + ((popSD2 * popSD2)/sampleSize2))
            pValue = norm.cdf(testStatistic)
        if populationOrSampleSD.lower().strip() == "sam":
            testStatistic = (statistic - parameter)/math.sqrt(((samSD1 * samSD1)/sampleSize1) + ((samSD2 * samSD2)/sampleSize2))
            pValue = t.sf(testStatistic, degFree)

    print("1 sided test statistic = ", testStatistic)
    print("P-value = ", pValue)
    if pValue <= alphaLevel:
        print("Reject the null hypothesis")
    elif pValue >= alphaLevel:
        print("Fail to reject the null hypothesis")

significanceTest()