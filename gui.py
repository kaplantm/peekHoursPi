import tkinter as tk
import firebase_service

def init(room):
    root = tk.Tk()

    tk.Label(root, text=room).grid(row=0, column=0)

    tk.Button(root, text="QUIT", fg="red", command=quit).grid(row=1, column=0)
    tk.Button(root, text="add_room", command=lambda: firebase_service.add_room(room)).grid(row=2, column=0)
    tk.Button(root, text="delete_room", command=lambda: firebase_service.delete_room(room)).grid(row=3, column=0)

    # tk.Button(root, text="add_or_update_room_aggregate year", command=lambda: firebase_service.add_or_update_room_aggregate(room, 'year', '1995', .5)).grid(row=1, column=0)
    tk.Button(root, text="add_or_update_room_year_aggregate", command=lambda: firebase_service.add_or_update_room_year_aggregate(room, 2019, .5)).grid(row=1, column=1)
    tk.Button(root, text="add_or_update_room_month_aggregate", command=lambda: firebase_service.add_or_update_room_month_aggregate(room, 2019, 10, .25)).grid(row=2, column=1)
    tk.Button(root, text="add_or_update_room_day_aggregate", command=lambda: firebase_service.add_or_update_room_day_aggregate(room, 2019, 10, 1, .5)).grid(row=3, column=1)

    # tk.Button(root, text="get_room_year_data", command=lambda: firebase_service.get_room_aggregate_data(room, 'year')).grid(row=1, column=0).grid(row=2, column=2)
    tk.Button(root, text="get_all_rooms", command=firebase_service.get_all_rooms).grid(row=1, column=2)

    root.mainloop()

