import json
import os
import requests
import urllib
import math
from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
import boto.sdb

def aws_connect():
    conn = boto.sdb.connect_to_region('us-east-1',\
            aws_access_key_id=os.environ['aws_access_key_id'], \
            aws_secret_access_key=os.environ['aws_secret_access_key'])
    return conn

def login(request):
    email = request.GET['email']
    password = request.GET['password']
    # store email to the session
    request.session['email'] = email
    conn = aws_connect()
    user_domain = conn.get_domain('user_table')
    current_attrs = user_domain.get_item(email, consistent_read=True)
    if current_attrs == None:
        attrs = {'password':password}
        user_domain.put_attributes(email, attrs)
        conn.close()
    else:
        if current_attrs['password'] != password:
            response = {'success': False}
    response = {'success': True}
    json_response = json.dumps(response)
    return HttpResponse(json_response)

#submits user's request for desired withdrawl
def submit_request(request):
    request_id = request.session.GET['email'] + "_" + str(datetime.now())
    amount = request.GET['amount']
    time_frame = request.GET['delivery_time']
    latitude, longitude = request.GET['latitude'], request.GET['longitude']
    #gather all current ATM locations, filter by acceptable geographical radius
    response = {'success': True}
    json_response = json.dumps(response)
    return HttpResponse(response)

#send withdrawl request to list of available ATMs
def send_ATM_request(sender_user_id, receiver_ATM_ids, message):
    return None

#adds ATM action (accept / reject) to request object
def store_ATM_request(request):
    request_id = request.GET['request_id']
    result = request.GET['result']
    ATM_id = request.GET['ATM_id']
    return None 

#returns a list of locations of ATMs that have accepted the user's request
#sunny will map these locations
def get_accepted_ATMs(request_id):
    return None

def initiate_transaction(request):
    request_id = request.GET['request_id']
    transaction_id = request_id
    sender_id = request.GET['sender_id']
    ATM_id = request.GET['ATM_id']
    send_payment(conn, sender_id, escrow_venmo_account)
    start_message_thread()

def start_message_thread():
    return None

#increment is_verified column in transaction_table by 1
def verify_transaction(request):
    #check if transaction is verified from both parties
    #verified if is_verified column == 2
    send_payment(escrow_venmo_account, ATM_id)
    return None

#submit 1-5 star transaction rating
def finish_transaction(request):
    # add score to transaction_ratings column in user_table 
    return None

def calculate_ATM_fee():
    return None








