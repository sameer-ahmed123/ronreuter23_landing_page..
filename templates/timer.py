
import time
from django.shortcuts import render
from django.views import View

import datetime



    # date = Brand.objects.all()
last_date = 5
#last_date= Brand.day_left
    # counter = 1
    # print(counter)
print(last_date)
while True:
    # database se last_date get karo us par while loop lagao 86400 seconds ka which is (24 hours)
    # and or jab data change hoga usko form me save karo or database me send kardo

    # change hota hua data database me send karo or usko  refresh kar k dihkahao html par
    # data ko form.save ki format me send karte han ??????





    #  yahan par 86400 s insert karna ha joh 24hours equal ha
    time.sleep(1)
    # counter += 1
    # print(counter)

    # or yahan par har 86400 seconds k baad ik value kam hojay gi joh k 1 date k end hone k equal ha
    last_date -= 1

    print(last_date)
    if last_date < 1:
        print("time ended/ yah phir stock unavalable")
        break
    #this adds one to the counter every 60 seconds


