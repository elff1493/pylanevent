import socketEvents

e = socketEvents.Structure("test", text=str)
client = socketEvents.Client(e)

client.start()
print("go")
while True:
    for event in client.events():
        if event.event_name == "test":
            client.send(e, text=event.text+":add")
        print(event)
