#### TRY IT YOURSELF - Chapter 8 - Archived Messages
## Copy of code from exercise messages_8-9.py
def show_messages(messages):
    """Print the contents of each short text message"""
    print("Showing all messages.")
    for message in messages:
        print(message)

messages = ['hello', "how's things?", 'be there in 5', "sorry i'm late"]
show_messages(messages)

## Copy of code from exercise sending_messages_8-10.py
#### 
def send_messages(messages, sent_messages):
    """Print each message and and add it to sent list."""
    print("\nSending all messages.")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)
sent_messages = []
send_messages(messages[:], sent_messages) # 'Call' function with a copy of the 'message' list as an 'argument' unlike in the previous exercise where we just used the original list as the 'argument'
print("\nFinished lists:")
print(f"\t{messages}") # The list will not be empty this time because we used a copy of it in the function call unlike in the previous exercise where we used the original list as the 'argument' and it was edited by the function
print(f"\t{sent_messages}")
