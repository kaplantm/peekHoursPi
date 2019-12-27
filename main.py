import tkinter as tk
import firebase_service

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)

add_room = tk.Button(frame,
                   text="add_room",
                   command=lambda: firebase_service.add_room("50_milk_women_1"))
add_room.pack(side=tk.LEFT)

delete_room = tk.Button(frame,
                   text="delete_room",
                   command=firebase_service.delete_room)
delete_room.pack(side=tk.LEFT)

update_room = tk.Button(frame,
                   text="update_room",
                   command=firebase_service.update_room)
update_room.pack(side=tk.LEFT)

get_room = tk.Button(frame,
                   text="get_room",
                   command=firebase_service.get_room)
get_room.pack(side=tk.LEFT)

get_all_rooms = tk.Button(frame,
                   text="get_all_rooms",
                   command=firebase_service.get_all_rooms)
get_all_rooms.pack(side=tk.LEFT)

root.mainloop()