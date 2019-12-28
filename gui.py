import tkinter as tk
import firebase_service

def init(room):
    root = tk.Tk()

    tk.Label(root, text=room).grid(row=0, column=0)

    tk.Button(root, text="QUIT", fg="red", command=quit).grid(row=1, column=0)
    tk.Button(root, text="add_room", command=lambda: firebase_service.add_room(room)).grid(row=2, column=0)

    tk.Button(root, text="increment_usage january monday 3PM",
              command=lambda: firebase_service.increment_usage(firebase_service.db.transaction(),
                                                               room, 'year_2019', 'january', 'monday', 'hour_3', 1)).grid(row=1, column=1)
    tk.Button(root, text="increment_usage january tuesday 4PM",
              command=lambda: firebase_service.increment_usage(firebase_service.db.transaction(),
                                                               room, 'year_2019', 'january', 'tuesday', 'hour_4', 1)).grid(row=2, column=1)
    tk.Button(root, text="increment_usage november monday 5PM",
              command=lambda: firebase_service.increment_usage(firebase_service.db.transaction(),
                                                               room, 'year_2019', 'november', 'monday', 'hour_5', 1)).grid(row=3, column=1)
    tk.Button(root, text="increment_usage november wednesday 2020 5PM",
              command=lambda: firebase_service.increment_usage(firebase_service.db.transaction(),
                                                               room, 'year_2020', 'november', 'wednesday', 'hour_5', 1)).grid(row=4, column=1)

    tk.Button(root, text="get_all_rooms", command=firebase_service.get_all_rooms).grid(row=1, column=2)
    tk.Button(root, text="months_by_year all", command=lambda: firebase_service.get_collection(room, u'months_by_year'))\
        .grid(row=2, column=2)
    tk.Button(root, text="months_by_year 2019", command=lambda: firebase_service.get_collection_document(room, u'months_by_year', 'year_2019'))\
        .grid(row=3, column=2)
    tk.Button(root, text="hours_by_days all", command=lambda: firebase_service.get_collection(room, u'hours_by_days'))\
        .grid(row=4, column=2)
    tk.Button(root, text="hours_by_days monday", command=lambda: firebase_service.get_collection_document(room, u'hours_by_days', 'monday'))\
        .grid(row=5, column=2)


    root.mainloop()

