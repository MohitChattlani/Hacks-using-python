import os,sys

from flask import Flask, request

from pymessenger import Bot

app= Flask(__name__)

PAGE_ACCESS_TOKEN="EAAD9QYZB5rbYBACI6i6qbGhGehq6bCPZCkFbXibyZCHGRHyaI4IHNEMoMPZA7WPFThm5WNMppS2auPbxJKzZAdia8vhxNOjm98MTPDwuPQ6c0KxNwPkhfoTcRJNvWyP6NZA1zZASqZC7cBEG1JEdScWumaLZBHhFMdehjcg7zWwDSQaOSCozX2ZBdZAQL8GF9Ce5nEZD"

#creating a bot instance
bot=Bot(PAGE_ACCESS_TOKEN)

# Facebook API Will send a http get request on this address
@app.route('/', methods=['GET'])

def verify():

        #Webhook verification
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == "hello":
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Hello worlds", 200

@app.route('/',methods=['POST'])
def webhook():

    #inorder to retrieve data from a post request
    data=request.get_json()
    log(data)

    if(data['object']=='page'):
            for entry in data["entry"]:
                    for messaging_event in entry["messaging"]:
                            #IDs
                            sender_id=messaging_event["sender"]["id"]
                            recipient_id=messaging_event["recipient"]["id"]
                            #checking type of message (simplest)
                            if (messaging_event.get('message')):
                                    #checking for text key in message or not
                                     if ('text' in messaging_event["message"]):
                                             messaging_text=messaging_event["message"]["text"]
                                     else:
                                             messaging_text="no text"

                                     #echo bot
                                     response=messaging_text

                                     bot.send_text_message(sender_id,response)
                                             
                                             
                                    
                            
    
    return "ok",200

def log(message):
    print(message)
    sys.stdout.flush() #complete o/p message stored in the buffer gets printed
    

if(__name__=="__main__"):
    app.run(debug=True, port=80)
