import tkinter as tk
import firebase_service

def init(room):
    root = tk.Tk()

    tk.Label(root, text=room).grid(row=0, column=0)

    tk.Button(root, text="QUIT", fg="red", command=quit).grid(row=1, column=0)
    tk.Button(root, text="add_room", command=lambda: firebase_service.add_room(room)).grid(row=2, column=0)

    tk.Button(root, text="increment_usage 10/1/2019 3PM",
              command=lambda: firebase_service.increment_usage(firebase_service.db.transaction(),
                                                               room, 2019, 10, 1, 1, 15)).grid(row=1, column=1)
    tk.Button(root, text="increment_usage 10/2/2019 4PM",
              command=lambda: firebase_service.increment_usage(firebase_service.db.transaction(),
                                                               room, 2019, 10, 2, 1, 16)).grid(row=2, column=1)
    tk.Button(root, text="increment_usage 11/2/2019 5PM",
              command=lambda: firebase_service.increment_usage(firebase_service.db.transaction(),
                                                               room, 2019, 11, 2, 1, 17)).grid(row=3, column=1)
    tk.Button(root, text="increment_usage 10/1/2020 6AM",
              command=lambda: firebase_service.increment_usage(firebase_service.db.transaction(),
                                                               room, 2020, 10, 1, 1, 6)).grid(row=4, column=1)

    tk.Button(root, text="get_all_rooms", command=firebase_service.get_all_rooms).grid(row=1, column=2)
    tk.Button(root, text="get_room_years_data", command=lambda: firebase_service.get_room_aggregate_year_data(room))\
        .grid(row=2, column=2)
    tk.Button(root, text="get_room_months_data 2019", command=lambda: firebase_service.
              get_room_aggregate_month_data(room, 2019)).grid(row=3, column=2)
    tk.Button(root, text="get_room_days_data 2019 10", command=lambda: firebase_service.
              get_room_aggregate_day_data(room, 2019, 10)).grid(row=4, column=2)
    tk.Button(root, text="get_room_hours_data 2019 10 1", command=lambda: firebase_service.
              get_room_aggregate_hour_data(room, 2019, 10, 1)).grid(row=5, column=2)


    root.mainloop()

