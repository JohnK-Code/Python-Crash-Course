#### TRY IT YOURSELF - Chapter 8 - Sending Messages
## Copy of code from exercise messages_8-9.py
def show_messages(messages):
    """Print the contents of each short text message"""
    print("Showing all messages.")
    for message in messages:
        print(message)

messages = ['hello', "how's things?", 'be there in 5', "sorry i'm late"]
show_messages(messages)

#### New code 
def send_messages(messages, sent_messages):
    """Print each message and and add it to sent list."""
    print("\nSending all messages.")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)
sent_messages = []
send_messages(messages,sent_messages)
print("\nFinished lists:")
print(f"\t{messages}")
print(f"\t{sent_messages}")