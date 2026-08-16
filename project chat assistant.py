# Rule Based python chatbot
import datetime
import time
name=input("Wel come ! Enter your name : ")
presentHour=datetime.datetime.now().hour
if 1<=presentHour <=12:
    print(f"Good Morning !, {name}")
elif 12<=presentHour<=17:
    print(f"Good Afternoon !,{name}")
elif 17<=presentHour<=20:
    print(f"Good Evening !,{name}")
else:
    print(f"Good night !,{name}")
    
print("Namaskaram ! Wel come to your Chat assistant")
print("you can ask basic questions about python , Type 'bye' to exit from chat assistant")

#Memory (dictionary of responses)
responses = {
      "hello" : "Hi ,wel come ! Howw can I help you ?",
      "how are you " : "I'm very fine, How about you ?",
      "i'm fine" :"Oh! that's great !",
      "i am good":"Oh! that's nice ",
      "i not fine":"Oh! everything will be alright soon .",
      "who are you ?":"I am your chatbot",
      "what is python ?":"Python is an interperted programming language .",
      "what are the uses of python ?":"It is useful for web development,software development,Machine             learning",
      "how python differ from other programming languages ?":"Python has a simple syntax and easy to          learn",
      "thank you":"My pleasure"
   }
      
# Method or function to get response from the chat assistant

def getResponsesofBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
            
    return "Sorry , I haven't get you , I will go through it"
            
            # take user input
while True :
                userInput = input("please ask you question : " )
                reply=getResponsesofBot(userInput)
                print("Bot Response :",reply)
                if "bye" in userInput.lower():
                    break

      
      
      
      
      
