from cowin_api import CoWinAPI
import json
import re
import webbrowser

f = open("dist.txt", "r")
g = open("wb_dist.txt", "r")
d_id = input("Do you know your district id?\nType \'wb\' to see district id of West Bengal \nOr type \'ost\' to see district id of all states\nLeave blank otherwise: ")

if d_id=='ost':
    for x in f:
          print(x)
          
elif d_id=="wb":
    for x in g:
        print(x)
    
district_id = input("Enter the district id: ")  # put the district id

date=""
date = input('Enter a date in this format -> (dd-mm-yyyy) (Optional. Takes today\'s date by default): ')  # Optional. Takes today's date by default

# Optional. By default returns centers without filtering by min_age_limit
min_age = input("Enter minimum age (Optional. By default returns centers without filtering by minimum age limit): ")

try:
    min_age_limit=int(min_age)
except:
    min_age_limit=0

cowin = CoWinAPI()
if date=="" and min_age_limit==0:
    available_centers = cowin.get_availability_by_district(district_id)
elif date=="":
    available_centers = cowin.get_availability_by_district(district_id, min_age_limit)
elif min_age_limit==0:
    available_centers = cowin.get_availability_by_district(district_id, date)
else:
    available_centers = cowin.get_availability_by_district(district_id, date, min_age_limit)
result = json.dumps(available_centers)
r1 = re.findall(r"\bavailable_capacity\w*....", result.strip())

flag=0
for i in r1:
    if i[-1:] != '0':
        print("Slot available")
        ch = input("type \'y\' if you want to go to cowin portal. leave blank otherwise: ")
        if ch == 'y':
            url = 'https://www.cowin.gov.in/home'
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)
        flag=1
        break
if flag!=1:
    print("No slot available")
