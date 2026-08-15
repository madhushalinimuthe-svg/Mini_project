# Content production tracker
contentlist = [  ] #list of details about content created and posted by you

while True :
    print("========<<<<<<MENU>>>>>>========")
    print("1. Add information")
    print("2. View total creations ")
    print("3. View total spending")
    print("4. view total earnings")
    print("5. EXIT")
    choice=int(input("please choose : "))
#1.Add information
    if (choice==1):
        date=input("please enter date of upload : ")
        category=input("enter what type of content are you creating?(long form,short form,photo post): ")
        category_in_editing=input("enter what software you are using ?(premierpro,adobe,VN,Vita : " )
        category_in_content =input("enter what kind of content(study,productivity,self care) : ")
        Total_Amount_of_spending=int(input("enter how much you spent : "))
        Total_Amount_earned=int(input("enter how much you earned : "))
    	
        info={ 
                     "date" : date,
                     "category" : category,
                     "category_in_editing" : category_in_editing,
                     "category_in_content" : category_in_content,
                     "Total_Amount_of_spending" : Total_Amount_of_spending,
                     "Total_Amount_earned" : Total_Amount_earned
        }
    	
        contentlist.append(info)
        print("DONE DUDE.Entered successfully")
#2.View total creations
    elif (choice==2):
        if (len(contentlist)==0):
            print("Not yet uploaded")
        else:
            print("======>>>>>here is your history<<<<<======")
            count=1
            for eachupload in contentlist :
                print(f"post Number{count} -->{eachupload["date"]},{eachupload["category"]},{eachupload["category_in_editing"]},{eachupload["category_in_content"]},{eachupload["Total_Amount_of_spending"]},{eachupload["Total_Amount_earned"]}")
                count=count+1
#3.View total spending
    elif(choice==3):
        total=0
        for eachupload in contentlist :
            total=total+eachupload["Total_Amount_of_spending"]
            print("Total spending : ",total)
#4.View total earings
    elif(choice==4):
        Total_Amount_earned =0
        for eachupload in contentlist :
            Total_Amount_earned =eachupload["Total_Amount_earned"]
            print("Total earned :",Total_Amount_earned)
#5.EXIT
    elif (choice==5):
     print("THANK YOU ")
     break
    else:
        print(INVALID,"Enter information properly")
        
   
 