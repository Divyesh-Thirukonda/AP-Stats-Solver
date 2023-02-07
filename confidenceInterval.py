import math
from scipy.stats import *


cLevel = float(input("confidence level (ex 90, 95, 99 etc): "))
meanOrProp = input("m for Mean and p for Proportion: ")

if meanOrProp.lower().strip() == "m":
    populationOrSampleSD = input("pop for population SD and sam for sample SD: ")
    if populationOrSampleSD.lower().strip() == "pop":
        popSD = float(input("population SD: "))
    elif populationOrSampleSD.lower().strip() == "sam":
        samSD = float(input("sample SD: "))
    sampleSize = float(input("sample size: "))
    testStatistic = float(input("x-bar value: "))
elif meanOrProp.lower().strip() == "p":
    testStatistic = float(input("p-hat: "))
    sampleSize = float(input("sample size: "))

degFree = sampleSize - 1
standardError = None
critValue = None

def confidenceInterval():

    if meanOrProp.lower().strip() == "p":
        standardError = math.sqrt((testStatistic * (1-testStatistic)) / sampleSize)
    elif meanOrProp.lower().strip() == "m":
        if populationOrSampleSD.lower().strip() == "pop":
            standardError = popSD/(math.sqrt(sampleSize))
        elif populationOrSampleSD.lower().strip() == "sam":
            standardError = samSD/(math.sqrt(sampleSize))

    if meanOrProp.lower().strip() == "p":
        critValue = math.sqrt(norm.ppf(((100 - cLevel) / 100) / 2) * norm.ppf(((100 - cLevel) / 100) / 2))
    elif meanOrProp.lower().strip() == "m":
        if populationOrSampleSD.lower().strip() == "pop":
            critValue = math.sqrt(norm.ppf(((100 - cLevel) / 100) / 2) * norm.ppf(((100 - cLevel) / 100) / 2))
        elif populationOrSampleSD.lower().strip() == "sam":
            critValue = math.sqrt(t.ppf(((100 - cLevel) / 100) / 2, degFree) * t.ppf(((100 - cLevel) / 100) / 2, degFree))

    interval = [testStatistic - (critValue * standardError), testStatistic + (critValue * standardError)]
    print(interval[0], ", ", interval[1])
    print("test statistic: ", testStatistic, "critical value: ", critValue, "standard error: ", standardError)

confidenceInterval()



