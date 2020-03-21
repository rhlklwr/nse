# This is an production code !!!

# Importing relevant package for Firebase, NSE and Time module
import firebase_admin
from firebase_admin import credentials, firestore
from nsetools import Nse
from time import ctime, time, sleep

# Instantiate NSE class
nse = Nse()

# Calculation of current time and split it to get the list
current_time = ctime(time()).split()

# Authentication with Firebase
cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

# Instantiate Firestore class
db = firestore.client()

# Instantiate batch class to update data in single batch
batch = db.batch()

# Set the data structure
doc_ref_top_gainers = db.collection(u'nse').document(u'top_gainers')
doc_ref_top_losers = db.collection(u'nse').document(u'top_losers')
doc_ref_advances_declines = db.collection(u'nse').document(u'advances_declines')

# write to database
while True:
    if (current_time[0][:3].lower() in ['mon', 'tue', 'wed', 'thu', 'fri']) \
            and \
            (9 < int(current_time[0][:2]) < 17):
        batch.update(doc_ref_top_gainers, {u'top_gainers': nse.get_top_gainers()})
        batch.update(doc_ref_top_losers, {u'top_losers': nse.get_top_losers()})
        batch.update(doc_ref_advances_declines, {u'advances_declines': nse.get_advances_declines()})
        # commit batch
        batch.commit()
        print(nse)
        sleep(600)
        current_time = ctime(time()).split()

