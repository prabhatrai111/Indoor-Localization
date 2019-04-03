import numpy 
import scipy
import math

pi=3.14125;




#Pt=input("type");
#Gt=input("type");
#Gr=input("type");
#hb=input("type");
#hm=input("type");
#n=input("type");
#pref
#dref
#f=input("type");
c=300000000;


RSSI=[0.0048 ,0.0067, 0.0079,0.0023 ,0.0055, 0.0059 , 0.005356];
#after cnversion from binary file to float values the rssi values are coming like this
#which approximately resembles the actual distance 
N=numpy.size(RSSI);

#Pr=numpy.zeros(N);
d=[];
a=[];
Pt=6.0;#in dbm
#Gr=45.0;
f=1900.0; # using wifi signal in mega hertz
hb=1.2; #height of bs

#hm=1.1; height of ms
#Pr=float(Pr);
#k=math.log((4.0*pi*f/c),10);
#print(k);

#alpha=Pt+Gt+Gr-20*k+180;# free space model
#alpha=36+43.7-20*math.log(f,10)+20*math.log(hb,10)+10*math.log(hm,10);#egli model

alpha=Pt+65.15-26.16*math.log(f,10)-5.83*math.log(hb,10);#okamura hata model
n=4.49-6.65*math.log(hb);



for i in range (0,N):
    Pr=10*math.log(RSSI[i],10)+30;
    #print (Pr);
    a=(alpha-Pr)/(10*n);
    d=math.pow(10,a);
    #print (a);
    print (d);

# we have to average the value for all d , that will be our actual distance ie add all the values and divide by total no of rssi
#In our case the values are 17 cm 20 cm etc , which after averaging will be the actual distance

    
