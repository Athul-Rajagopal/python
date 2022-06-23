## tring to create a train ticket generator using file handling methode

num = 1
def book_ticket():
    
    name = input("Enter your name :").upper()
    age = int(input("enter your age :"))
    travel_from = input("Enter your starting station :").upper()
    travel_to = input("Enter your destination :").upper()

    ## ticket format is defined
    format = "TKTxxx"

    #for auto generation of ticket
    current_num =num+1
    zero=(9-len(format))*'0'
    temp=format+str(zero)+str(current_num)
    if len(temp)>10:     ##to set the ticket format(length) to be constant
        zero=(10-((len(str(1))+len(format))))*'0'
        temp=format+str(zero)+str(current_num)
        
        
##file opened and writed
    file = open("data.txt",'w+')
    file.write(f"Name : {name}\nAge : {age}\nTravel from :{travel_from}\nTravel to : {travel_to}\nTicket number : {temp}\n")
    file.write('--------------------------------------------------------------\n')
    file.close()
    
    file=open("data.txt",'r+')

    print(file.read())
    file.close()

book_ticket()




    