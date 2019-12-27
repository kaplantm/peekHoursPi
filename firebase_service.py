import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('./credentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def add_room(room_name):
    print("add_room")
    doc_ref = db.collection(u'rooms').document(room_name)
    doc_ref.set({
        u'years': [],
        u'months': [],
        u'days': []
    })

def update_room(room_name):
    print ("update")

def delete_room():
    print ("delete")

def get_room():
    print("delete")

def get_all_rooms():
    users_ref = db.collection(u'users')
    docs = users_ref.stream()

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))