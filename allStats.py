import math
from scipy.stats import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QCheckBox, QLineEdit
from PyQt5.QtCore import Qt

class PyQtApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        #Setting up the app
        self.setWindowTitle("Statistics")
        self.setWindowIcon(QtGui.QIcon("Path/to/Your/image/file.png"))
        self.setMinimumWidth(resolution.width() / 3)
        self.setMinimumHeight(resolution.height() / 1.5)
        self.setStyleSheet(
            "QWidget {background-color: rgba(45,45,45,255);} QScrollBar:horizontal {width: 1px; height: 1px;"
            "background-color: rgba(45,45,45,255);} QScrollBar:vertical {width: 1px; height: 1px;"
            "background-color: rgba(45,45,45,255);}")
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(20)
        font.setWeight(100)

        #textbox for confidence level
        self.cLevel = QtWidgets.QTextEdit(self)
        self.cLevel.setPlaceholderText("Confidence Level:")
        self.cLevel.setStyleSheet(
            "margin: 1px; padding: 7px; background-color: rgba(0,0,0,100); color: rgba(0,90,255,255);"
            "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,140,255,255);")
        self.cLevel.setFont(font)

        self.meanorprop = QtWidgets.QComboBox(self)
        self.meanorprop.addItems(["mean", "proportion"])
        self.meanorprop.setStyleSheet(
            "margin: 1px; padding: 7px; background-color: rgba(0,0,0,100); color: rgba(0,90,255,255);"
            "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,140,255,255);")
        self.meanorprop.setFont(font)


        #grid layout for all inputsx
        self.grid1 = QtWidgets.QGridLayout()
        self.grid1.addWidget(self.cLevel, 10, 2, 2, 2)
        self.grid1.addWidget(self.meanorprop, 20, 2, 2, 2)
        self.grid1.setContentsMargins(10, 10, 400, 550)
        self.setLayout(self.grid1)


import sys
app = QtWidgets.QApplication(sys.argv)
desktop = QtWidgets.QApplication.desktop()
resolution = desktop.availableGeometry()
myapp = PyQtApp()
myapp.setWindowOpacity(0.95)
myapp.show()
myapp.move(resolution.center() - myapp.rect().center())
sys.exit(app.exec_())


def confidenceInterval():
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


def significanceTest():
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


def twoConfidenceInterval():
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


def twoSignificanceTest():
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


def conditionsForInference():
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




'''
whichPerformance = input("What chapter? 7 through 10.2: ")
if whichPerformance.lower().strip() == "7":
    conditionsForInference()
    randomMet = input("Are the samples taken randomly? yes or no: ")
if whichPerformance.lower().strip() == "8":
    confidenceInterval()
if whichPerformance.lower().strip() == "9":
    significanceTest()
if whichPerformance.lower().strip() == "10.1":
    twoConfidenceInterval()
if whichPerformance.lower().strip() == "10.2":
    twoSignificanceTest()
'''