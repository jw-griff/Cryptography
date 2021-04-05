#Define Variables & Get Inputs
status = "y"
while status == "y":
        keyinputs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?." 
        partialOne=""
        partialTwo=""
        newAlphabet=""
        message = input("Type in your message: ")
        key = int(input("Enter offset number: "))

#Create the New Alphabet 
        if key == 0:
                newAlphabet = keyinputs
        elif key > 0:
                partialOne = keyinputs[:key]
                partialTwo = keyinputs[key:]
                newAlphabet = partialTwo + partialOne
        else:
                partialOne = keyinputs[:(65 + key)]
                partialTwo = keyinputs [(65 + key):]
                newAlphabet = partialTwo + partialOne

#Shifting Message
        encrypted=""
        for message_index in range(0,len(message)):
                if message[message_index] == " ":
                        encrypted+=" "
                for alphabet_index in range(0,len(newAlphabet)):
                        if message[message_index] == keyinputs[alphabet_index]:
                                encrypted+= newAlphabet[alphabet_index]
        print(encrypted)
        status = input("Another meassage [y/n] ")
        print
status = "n"
while status == "n":
        print("Goodbye")
        exit()
