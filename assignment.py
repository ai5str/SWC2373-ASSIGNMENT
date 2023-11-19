#import
from webexteamssdk import WebexTeamsAPI;
from webexteamssdk import ApiError;

#Function to insert the webex token
teams_token = input ("\nEnter your access token: ")
api = WebexTeamsAPI(access_token=teams_token)

#Function to test connection
def test_connection():
    print ("Connecting...")
    webex = api.people.me()
    if webex:
        print("Successful!")

#Function to display users details
def details():
    webex = api.people.me()
    print(f"Name: {webex.displayName}")
    print(f"Nickname: {webex.nickName}")
    print(f"Emails: {',' .join(webex.emails)}")

#Function to display rooms
def displayRoom():
    print("\nList of Rooms:")
    rooms = api.rooms.list(max=5)
    countedRoom = 0  #retrieve a list of up to 5 rooms

    for room in rooms:
        print(f"\nRoom ID: {room.id}")
        print(f"Room Title: {room.title}")
        print(f"Data Created: {room.created}")
        print(f"Last Activity: {room.lastActivity}")

        countedRoom += 1
        if countedRoom >= 5:
            break

    return rooms

#Function to create rooms
def createRoom():
    titleRoom = input("Enter the title of the new room: ")
    try:
        new_room = api.rooms.create(titleRoom)
        print(f"Room '{new_room.title}' (Room ID: {new_room.id}) has been created successfully.")
    except api:
        print(f"Failed to create the room.")

#Function to list rooms
def list_rooms():
    print("\nList of Rooms:")
    rooms = api.rooms.list(max=5)
    room_list = []

    for index, room in enumerate(rooms, start=1):
        room_list.append(room)
        print(f"{index}: {room.title}")

    return room_list

#Function to send a message
def send_message():
    rooms = list_rooms()

    if rooms:
        room_number = input("\nEnter the number of the room to send a message to: ")

        try:
            room_number = int(room_number)

            if 1 <= room_number <= len(rooms):
                room = rooms[room_number - 1]
                message = input("\nEnter your message: ")
                api.messages.create(room.id, text=message)
                print("\nMessage sent successfully.")
            else:
                print("Invalid room number. Please select a valid room number.")
        except ValueError:
            print("Invalid input. Please select a valid number.")

   
#Function to list options
while True:
    print("\nList of Options:")
    print("0: Test Connection")
    print("1: Display Details")
    print("2: Display Rooms")
    print("3: Create a Room")
    print("4: Send a Message")
    print("5: Exit")

    option = input("\nPlease select an option: ")
    if option=="0": #option for test connection
        test_connection() 
    elif option=="1": #option for display details
        details() 
    elif option=="2": #option for display 5 rooms
        displayRoom()
    elif option=="3": #option for create room
        createRoom()
    elif option=="4":
        send_message()
    elif option=="5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Please select a valid option.")
