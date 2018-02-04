import aiml

#creating kernel
kernel = aiml.Kernel()
BOT_INFO = {
    "name": "Jarvis",
    "birthday": "July 13th 2017",
    "location": "Banglore",
    "master": "Avinash",
    "website":"follow me on twitter",
    "gender": "Male",
    "age": "21",
    "size": "0",
    "religion": "Humanity",
    "party": "All night !"
}

kernel.learn("/home/avinash/chatbot-college-query/aiml/standard/std-startup.xml")
kernel.respond("LOAD AIML B")
for key,val in BOT_INFO.items():
	kernel.setBotPredicate(key,val)

# Press CTRL-C to break this loop
while True:
    print(kernel.respond(input("Enter your message >> ")))
