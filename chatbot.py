import re
class RuleBasedChatbot:
      def __init__(self):
           self.rules=[(re.compile(r"hello",re.IGNORECASE),"hello there!how can i help you"),
                        (re.compile(r"hi",re.IGNORECASE),"hello there!how can i help you"),
                       (re.compile(r"hii",re.IGNORECASE),"hello there!how can i help you"),
                       (re.compile(r"helo",re.IGNORECASE),"hello there!how can i help you"),
  		       (re.compile(r"bye",re.IGNORECASE),"Goodbye!have a great day!"),
		     (re.compile(r"how are you",re.IGNORECASE),"Iam doing good!and how about you"),
                      (re.compile(r"what is your name",re.IGNORECASE),"Iam open based Ai,and what is your name"),
		     (re.compile(r"have you eat",re.IGNORECASE),"iam just a bot"),
		     (re.compile(r"what is your name",re.IGNORECASE),"iam chatbot"),
                     (re.compile(r"help me",re.IGNORECASE),"sure! iam here to help!what do you need to assist with"),
		     (re.compile(r"thank you",re.IGNORECASE),"you're welcom!if you have any questions or need further assistance,feel free to ask"),
		     (re.compile(r"thanks",re.IGNORECASE),"you're welcom!if you have any questions or need further assistance,feel free to ask"),]
      def get_response(self,user_input):
           for pattern,respons in self.rules:
                if pattern.search(user_input):
                    return respons
           return "iam sorry,i don't understand that."
if __name__=="__main__":
    bot= RuleBasedChatbot()
    while True:
        user_input = input("you: ")
        
        if user_input.lower()in["exit","quit","bye"]:
            print("Bot: Goodbye! Have a great day!")
            break
        response = bot.get_response(user_input)
        print(f"Bot: {response}")