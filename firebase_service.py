import firebase_admin
from google.cloud.firestore_v1 import Increment
from firebase_admin import credentials
from firebase_admin import firestore


# years - total times triggered that year
# months - total times triggered that month
# days - total times triggered each day

# Use a service account
cred = credentials.Certificate('./credentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_room(room_name):
    print("add_room")
    doc_ref = db.collection(u'rooms').document(room_name)
    doc_ref.set({})

@firestore.transactional
def increment_usage(transaction, room_name, year, month, day, hour, increment_amount):
    # TODO make sure parent collection exists
    print ("update_room_day")
    room_ref = db.collection(u'rooms').document(room_name)
    year_ref = room_ref.collection(u'years').document(str(year))
    month_ref = year_ref.collection(u'months').document(str(month))
    day_ref = month_ref.collection(u'days').document(str(day))
    hour_ref = day_ref.collection(u'hours').document(str(hour))

    year_snapshot = year_ref.get(transaction=transaction)
    month_snapshot = month_ref.get(transaction=transaction)
    day_snapshot = day_ref.get(transaction=transaction)
    hour_snapshot = hour_ref.get(transaction=transaction)

    old_year_usage = year_snapshot.get(u'usage');
    old_month_usage = month_snapshot.get(u'usage');
    old_day_usage = day_snapshot.get(u'usage');
    old_hour_usage = hour_snapshot.get(u'usage');

    print("old_hour_usage", old_hour_usage)
    transaction.set(year_ref, {
        u'usage': old_year_usage + 1 if old_year_usage else 1,
    }),
    transaction.set(month_ref, {
        u'usage': old_month_usage + 1 if old_month_usage else 1,
    })
    transaction.set(day_ref, {
        u'usage': old_day_usage + 1 if old_day_usage else 1,
    })
    transaction.set(hour_ref, {
        u'usage': old_hour_usage + 1 if old_hour_usage else 1,
    })


def get_room_aggregate_year_data(room_name):
    data_ref = db.collection(u'rooms').document(room_name).collection(u'years')
    docs = data_ref.stream()
    printDocs(docs)


def get_room_aggregate_month_data(room_name, year):
    data_ref = db.collection(u'rooms').document(room_name).collection(u'years').document(str(year)).collection(u'months')
    docs = data_ref.stream()

    printDocs(docs)

def get_room_aggregate_day_data(room_name, year, month):
    data_ref = db.collection(u'rooms').document(room_name).collection(u'years').document(str(year)).collection(u'months')\
        .document(str(month)).collection(u'days')
    docs = data_ref.stream()
    printDocs(docs)

def get_room_aggregate_hour_data(room_name, year, month, day):
    data_ref = db.collection(u'rooms').document(room_name).collection(u'years').document(str(year)).collection(u'months')\
        .document(str(month)).collection(u'days').document(str(day)).collection(u'hours')
    docs = data_ref.stream()
    printDocs(docs)

def printDocs(docs):
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))

def get_all_rooms():
    print ("get_all_rooms")
    rooms_ref = db.collection(u'rooms')
    docs = rooms_ref.stream()

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
