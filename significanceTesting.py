import math
import numpy
import scipy
from scipy.stats import *

alphaLevel = float(input("alpha level (ex .05, .01, etc): "))
meanOrProp = input("m for Mean and p for Proportion: ")

if meanOrProp.lower().strip() == "m":
    populationOrSampleSD = input("pop for population SD and sam for sample SD: ")
    if populationOrSampleSD.lower().strip() == "pop":
        popSD = float(input("population SD: "))
    elif populationOrSampleSD.lower().strip() == "sam":
        samSD = float(input("sample SD: "))
    parameter = float(input("hypothesized population mean: "))
    statistic = float(input("x-bar: "))
    sampleSize = float(input("sample size: "))

elif meanOrProp.lower().strip() == "p":
    parameter = float(input("hypothesized population proportion (.25, .73, etc): "))
    statistic = float(input("p-hat (.25, .73, etc): "))
    sampleSize = float(input("sample size: "))

degFree = sampleSize - 1
standardError = None
testStatistic = None
pValue = None

def significanceTest():

    if meanOrProp.lower().strip() == "p":
        testStatistic = (statistic - parameter)/(math.sqrt((parameter * (1-parameter)) / sampleSize))
        pValue = norm.cdf(testStatistic)

    elif meanOrProp.lower().strip() == "m":
        if populationOrSampleSD.lower().strip() == "pop":
            testStatistic = (statistic - parameter)/(popSD / (math.sqrt(sampleSize)))
            pValue = norm.cdf(testStatistic)
        if populationOrSampleSD.lower().strip() == "sam":
            testStatistic = (statistic - parameter)/(samSD / (math.sqrt(sampleSize)))
            pValue = t.sf(testStatistic, degFree)

    print("1 sided test statistic = ", testStatistic)
    print("P-value = ", pValue)
    if pValue <= alphaLevel:
        print("Reject the null hypothesis")
    elif pValue >= alphaLevel:
        print("Fail to reject the null hypothesis")

significanceTest()