## Create a  sample train ticket generator using file handling methode


def book_ticket():
    
   try:
       
        file = open("data.txt",'a+')
        file.seek(0)   ##set the position to start of file.
        old_data = file.readlines()
        last_tkt = old_data[-2][-11:]
        # print(last_tkt)
        current_num=last_tkt[-5:]
        current_num=int(current_num)
        # print(num)
        file.close()
        
        ## check if the limit of ticket is exceeded
        if current_num == 9999:
            print("sorry!!, no ticket is available")
        
        else:
        ##details of passenger    
            name = input("Enter your name :").upper()
            age = int(input("enter your age :"))
            travel_from = input("Enter your starting station :").upper()
            travel_to = input("Enter your destination :").upper()

            ## ticket format is defined
            format = "TKTxxx"

            ##for auto generation of ticket
            current_num =current_num+1
            zero=(9-len(format))*'0'
            temp=format+str(zero)+str(current_num)
            if len(temp)>10:     ##to set the ticket format(length) to be constant
                zero=(10-((len(str(current_num))+len(format))))*'0'
                temp=format+str(zero)+str(current_num)
                    
                
            ##Data is saved in the file
            file = open("data.txt",'a+')
            file.write(f"Name : {name}\nAge : {age}\nTravel from :{travel_from}\nTravel to : {travel_to}\nTicket number : {temp}\n")
            file.write('--------------------------------------------------------------\n')
            file.close()
        
   except IndexError:
       
        name = input("Enter your name :").upper()
        age = int(input("enter your age :"))
        travel_from = input("Enter your starting station :").upper()
        travel_to = input("Enter your destination :").upper()
        
        format = "TKTxxx"
        num = 1
        zero=(9-len(format))*'0'
        temp=format+str(zero)+str(num)
        
        new_file = open("data.txt",'a+')
        new_file.write(f"Name : {name}\nAge : {age}\nTravel from :{travel_from}\nTravel to : {travel_to}\nTicket number : {temp}\n")
        new_file.write('--------------------------------------------------------------\n')
        new_file.close()
        
   except ValueError:
       print("Oops! please check your age. try again.")
       
    
   finally:
       print("Thank you for using book_ticket.")
       
   
book_ticket()




    