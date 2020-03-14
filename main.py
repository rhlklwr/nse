import firebase_admin
from firebase_admin import credentials, firestore
from nse import *
import time

cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

db = firestore.client()

batch = db.batch()

# Set the data
doc_ref_top_gainers = db.collection(u'nse').document(u'top_gainers')
doc_ref_top_losers = db.collection(u'nse').document(u'top_losers')
doc_ref_advances_declines = db.collection(u'nse').document(u'advances_declines')

# write to database
a = 0
while True:
    batch.update(doc_ref_top_gainers, {u'top_gainers': top_gainers()})
    batch.update(doc_ref_top_losers, {u'top_losers': top_losers()})
    batch.update(doc_ref_advances_declines, {u'advances_declines': adv_dec()})

    # commit batch
    batch.commit()
    print(a+1)
    time.sleep(600)