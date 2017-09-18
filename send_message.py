from select_friend import select_friend
from steganography.steganography import Steganography
from globals import friends,Chat
from datetime import datetime
from termcolor import colored
import re

def send_message():
    #choose a friend from the list.
    friend_choice = select_friend()
    #checking if Frien's List Is not empty
    if friend_choice!=1:
        pattern='^[A-Za-z][0-9A-Za-z\s]*\.jpeg$'
        patternsave='^SOS|SAVE ME|IN DANGER|HELP$'
        a = True
    #prepare the message
    while a:
       original_image = raw_input("Provide the name of the image to hide the message : ")
       if(re.match(pattern,original_image)!=None):
        a=False
       else:
         print colored("Enter Again!!!!",'red')
    a=True
    while a:
        output_image = raw_input("Provide the name of the output image : ")
        if (re.match(pattern,output_image)!=None):
            a=False
    text = raw_input("Enter your message here : ")
    if(len(text)>100):
        #remove friend he/she types more 100 words
        print  colored("Large Message Input!!1",'red')
        print  colored("You are no more a Spy!!!",'red')
        friends.remove(friends[friend_choice])
    else:
        #Handling Exception If Image does not exist
        try:
            #Encrypt the message
            Steganography.encode(original_image, output_image, text )
            chatobject=Chat(output_image,datetime.now())
            friends[friend_choice].chat.append(chatobject)
            # Successful message
            print colored( "Your message encrypted successfully.",'green')
            if(re.match(patternsave,text.upper())!=None):
                print colored("Igot your location!!!!i'll be there soon!",'green')
        except IOError:
            print colored("Image %s does not exist"%(original_image),'red')
    else:
    print colored ("Empty Friend's List!!1",'red')

    #save the messages
    new_chat = {
        'message' : text,
        'time' : datetime.now(),
        'sent_by_me' : True
    }
    friends[friend_choice]['chats'].append(new_chat)
    print"your secret message is ready. "