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
    print ("update_room_day")
    room_ref = db.collection(u'rooms').document(room_name)
    months_by_year_ref = room_ref.collection(u'months_by_year').document(year)
    hours_by_days_ref = room_ref.collection(u'hours_by_days').document(day)

    months_by_year_dict = months_by_year_ref.get(transaction=transaction).to_dict() or {}
    hours_by_days_dict = hours_by_days_ref.get(transaction=transaction).to_dict() or {}

    old_month_by_year_value = months_by_year_dict[month] if months_by_year_dict and month in months_by_year_dict else 0;
    old_hours_by_days_value = hours_by_days_dict[hour] if hours_by_days_dict and hour in hours_by_days_dict else 0;

    months_by_year_dict[month] =  old_month_by_year_value + increment_amount
    hours_by_days_dict[hour] = old_hours_by_days_value + increment_amount

    transaction.set(months_by_year_ref, months_by_year_dict),
    transaction.set(hours_by_days_ref, hours_by_days_dict)


def get_collection(room_name, collection):
    data_ref = db.collection(u'rooms').document(room_name).collection(collection)
    docs = data_ref.stream()
    printDocs(docs)


def get_collection_document(room_name, collection, document):
    data_ref = db.collection(u'rooms').document(room_name).collection(collection).document(document).get()
    printDoc(data_ref)



def printDoc(doc):
        print(u'{} => {}'.format(doc.id, doc.to_dict()))

def printDocs(docs):
    for doc in docs:
        printDoc(doc)

def get_all_rooms():
    print ("get_all_rooms")
    rooms_ref = db.collection(u'rooms')
    docs = rooms_ref.stream()

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
