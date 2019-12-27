import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# years - total times triggered that year
# months - total times triggered that month
# days - total times triggered each day

# Use a service account
cred = credentials.Certificate('./credentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def delete_collection(coll_ref, batch_size):
    docs = coll_ref.limit(batch_size).get()
    deleted = 0

    for doc in docs:
        print(u'Deleting doc {} => {}'.format(doc.id, doc.to_dict()))
        doc.reference.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)


def add_room(room_name):
    print("add_room")
    doc_ref = db.collection(u'rooms').document(room_name)
    doc_ref.set({})


def add_or_update_room_aggregate_without_recalculation(room_name, aggregate_type, aggregate_label, value):
    print ("update_room")
    doc_ref = db.collection(u'rooms').document(room_name).collection(aggregate_type).document(aggregate_label)
    doc_ref.set({u'value': value})


def add_or_update_room_year_aggregate(room_name, year, usage):
    print ("update_room_year")
    doc_ref = db.collection(u'rooms').document(room_name).collection('years').document(str(year))
    doc_ref.set({
        u'year': year,
        u'usage': usage
    })


def add_or_update_room_month_aggregate(room_name, year, month, usage):
    print ("update_room_month")
    doc_ref = db.collection(u'rooms').document(room_name).collection('years').document(str(year)).collection('months')\
        .document(str(month))
    doc_ref.set({
        u'month': month,
        u'usage': usage
    })

def add_or_update_room_day_aggregate(room_name, year, month, day, usage):
    # TODO make sure parent collection exists
    print ("update_room_day")
    doc_ref = db.collection(u'rooms').document(room_name).collection('years').document(str(year)).collection('months')\
        .document(str(month)).collection('days').document(str(day))
    doc_ref.set({
        u'day': day,
        u'usage': usage
    })


def delete_room(room_name):
    print ("delete")
    years_ref = db.collection(u'rooms').document(room_name).collection('years')
    months_ref = db.collection(u'rooms').document(room_name).collection('months')
    days_ref = db.collection(u'rooms').document(room_name).collection('days')
    room_ref = db.collection(u'rooms').document(room_name)

    delete_collection(years_ref, 50)
    delete_collection(months_ref, 50)
    delete_collection(days_ref, 50)
    room_ref.delete()


def get_room_aggregate_data(room_name, aggregate_type):
    print ("get_room_aggregate_data", room_name, aggregate_type)
    data_ref = db.collection(u'rooms').document(room_name).collection(aggregate_type)
    docs = data_ref.stream()
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))


def get_all_rooms():
    print ("get_all_rooms")
    rooms_ref = db.collection(u'rooms')
    docs = rooms_ref.stream()

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))