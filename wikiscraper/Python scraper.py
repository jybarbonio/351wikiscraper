"""
John Barbonio
Professor Jiang
CS 351
21 April 2022
"""

import re
from selenium import webdriver

def scraper():
        # driver/automated parser
        driver = webdriver.Chrome("C:\\Users\John\Desktop\wikiscraper\chromedriver.exe")
        driver.get("https://en.wikipedia.org/wiki/List_of_California_locations_by_income")

        # narrow downs
        county_name = driver.find_elements_by_xpath('//table[@class="wikitable sortable jquery-tablesorter"][1]/tbody/tr/td[1]')
        county_pops = driver.find_elements_by_xpath('//table[@class="wikitable sortable jquery-tablesorter"][1]/tbody/tr/td[2]')
        county_density = driver.find_elements_by_xpath('//table[@class="wikitable sortable jquery-tablesorter"][1]/tbody/tr/td[3]')
        county_percapita = driver.find_elements_by_xpath('//table[@class="wikitable sortable jquery-tablesorter"][1]/tbody/tr/td[4]')

        # regPop = re.compile("\d+,\d+")
        regDensity = re.compile("\d+\.\d+")
        lstPop = []

        for c in county_density:    # alternatively use county_pops
            if(regDensity.search(c.text)):
                lstPop.append(re.sub(",", "", c.text))
                print(re.sub(",", "", c.text))
            else:
                print("no match")
        
        return lstPop

def newSVG(list):
    regRGB = re.compile('style=\"fill:#.+\"')

    with open('Blank_California_Map.svg', 'r') as f:
        f_lines = f.readlines()
        count = 0

        for line in f_lines:
            s = regRGB.search(line)
            if(regRGB.search(line)):
                newRGB = rgbCalcDensity(list[count])
                newline = line.replace(s.group(), 'style=\"fill:#' + newRGB + "\"")
                with open('Blank_California_Map_NEW.svg', 'a') as wf:
                    wf.writelines(newline)
                print("found-> replaced")
                count += 1
            else:
                with open('Blank_California_Map_NEW.svg', 'a') as wf:
                    wf.writelines(line)
                print("skip-> copying same line over to new file")
            
        f.close()
        wf.close()

def rgbCalcPop(value):
    if(float(value) > 1000.0):
        return "FF0000"
    elif(float(value) > 100.0):
        return "FF8000"
    elif(float(value) > 10.0):
        return "FFFF00"
    else:
        return "80FF00"

def rgbCalcDensity(value):
    if(float(value) > 1000.0):
        return "FF0000"
    elif(float(value) > 100.0):
        return "FF8000"
    elif(float(value) > 10.0):
        return "FFFF00"
    else:
        return "80FF00"

def rgbCalcCapita(value):
    if(float(value) > 1000.0):
        return "FF0000"
    elif(float(value) > 100.0):
        return "FF8000"
    elif(float(value) > 10.0):
        return "FFFF00"
    else:
        return "80FF00"

if __name__ == '__main__':
    lstPop = scraper()
    print(lstPop)
    newSVG(lstPop)