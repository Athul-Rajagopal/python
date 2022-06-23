## tring to create a train ticket generator using file handling methode

from numpy import true_divide


# name = input("Enter your name :").capitalize()
# age = int(input("enter your age :"))
# travel_from = input("Enter your starting station :").capitalize()
# travel_to = input("Enter your destination :").capitalize()
# file = open("data.txt",'w')
# file.write(f"Name : {name}\nAge : {age}\nTravel from :{travel_from}\nTravel to : {travel_to}\n")
# file.write('--------------------------------------------------------------\n')
# file.close()



##ticket number
num=90 
while num<=110:
    format = "tktxxx"
    zero=(9-len(format))*'0'
    temp=format+str(zero)+str(num)
    
    if len(temp)>10:
        # zero=(8-len(format))*'0'
        zero=(10-((len(str(num))+len(format))))*'0'
        temp=format+str(zero)+str(num)
    
    print(temp)
    num+=1

        
    
