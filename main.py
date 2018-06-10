
from fbchat import  Client, log
from fbchat.models import *
import fileinput

class punkjj(Client):

    def onMessage(self, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        toggle = client.fetchThreadMessages(thread_id=client.uid, limit=1) # client.uid means its our own acc
        for message in toggle:
            pText=message.text.lower()
        if("online" in pText):
            self.markAsRead(author_id)
        log.info("Message {} from {} in {}".format(message_object, thread_id, thread_type))  
        msgText = message_object.text.lower()
        if(msgText=="hi" or msgText=="hii" or msgText=="hiii" or msgText=="yo" or msgText=="hi there" or msgText=="hey" or msgText=="heyy"):
            reply = "Hello :D"
        elif(msgText=="hello" or msgText=="hellow" or msgText=="heloo" or msgText=="hlo" or msgText=="hellow"):
            reply = "Hi :)"
        elif(msgText=="hy" or msgText=="hyy"):
            reply = "Hello :D"
        elif(msgText=="whatsup" or msgText=="wassup" or msgText=="what's up" or msgText=="wtsup" or msgText=="watsup" or msgText=="whats up" or "how are you" in msgText or "hw r u" in msgText):
            reply = "Awesome. What about you? :D"
        elif(msgText=="test" or msgText=="debug" or msgText=="aboutme" or msgText=="about" or msgText=="bot"):
            reply = "Hi, I'm a bot written in Python. Created by Pankaj Sheoran"
        elif("birthday" in msgText or "bday" in msgText or "hbd" in msgText):
            reply = "Thank you! :D"
        elif("what you doing" in msgText):
            reply = "Idling, I'm a bot afterall. I work for my creator, Pankaj Sheoran (www.punkjj.cf)"
        elif("bye" in msgText or msgText=="byye" or msgText=="byee"):
            reply = "Ok bye! :D"
        else:
            reply = "Thank you for contacting me. I'm currently not online, I was replying using a Python Script. I will reach out to you shortly."
        def sendMsgg():
            if (author_id!=self.uid):
                self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
            self.markAsDelivered(author_id, thread_id)     
        if ("online" in pText):
            sendMsgg()

client = punkjj("EMAIL", "PASSWORD")
client.listen()
