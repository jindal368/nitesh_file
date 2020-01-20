import csv
import math
def min_geo(partner_list,loc):
    #partner_list is 2d array
    #loc is 1d array 
    w1=0
    w2=0
    dif_w=0
    dif_l=0
    a=0
    darr=[]
    for i in range(len(partner_list[0])):
        w1=math.radians(float(partner_list[i][1]))
        w2=math.radians(loc[0])
        dif_w=w2-w1
        dif_l=math.radians(loc[1]-float(partner_list[i][2]))
        a=pow(math.sin(dif_w/2),2)+math.cos(w1)*math.cos(w2)*pow(math.sin(dif_l/2),2)
        c=math.atan2(math.sqrt(a),math.sqrt(1-a))*2
        d=c*6371
        d=round(d,2)
        darr.append(d)

    return darr    








partner_list=[]
with open("file.csv","r") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        partner_list.append(row)



print(partner_list)
#want to write the data
for i in range(len(partner_list[0])):
    print(partner_list[i])

loc=[28.9380, 77.5290]
final_lis=min_geo(partner_list,loc)
print(final_lis)


#hence final list is the distance in km
#select that distance whose have in range of 30km
index=[]
for i in range(len(final_lis)):
    if final_lis[i]<30:
        index.append(i)


print(index)

notification_bhej=[]
for i in range(len(index)):
    notification_bhej.append(partner_list[index[i]])


print(notification_bhej)    



