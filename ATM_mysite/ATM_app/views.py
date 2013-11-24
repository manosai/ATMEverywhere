import urllib2
import urllib2
import json

from django.http import * 
from django.http import HtttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

CLIENT_ID = 'DCRBNKLOZCARX3SR3QEA1HTQMW4KUYZZGRHCAABO5SUDLVRI'
CLIENT_SECRET = '2RHBQCXC2VF1UUSWZTDBYIAJ5VOKJ2OLVZP0JDS5NKY4K4GP'

request_token_url = 'https://foursquare.com/oauth2/authenticate'
access_token_url = 'https://foursquare.com/oauth2/access_token'
redirect_url = 'http://127.0.0.1:8080/callback'

def home(request): 
	if request.session.get('access_token'):
		return HttpResponseRedirect('done')
	else:
		return render_to_response('login.html')

def callback( request ):
    # get the code returned from foursquare
    code = request.GET.get('code')

    # build the url to request the access_token
    params = { 'client_id' : CLIENT_ID,
               'client_secret' : CLIENT_SECRET,
               'grant_type' : 'authorization_code',
               'redirect_uri' : redirect_url,
               'code' : code}
    data = urllib.urlencode( params )
    req = urllib2.Request( access_token_url, data )

    # request the access_token
    response = urllib2.urlopen( req )
    access_token = json.loads( response.read( ) )
    access_token = access_token['access_token']

    # store the access_token for later use
    request.session['access_token'] = access_token

    # redirect the user to show we're done
    return HttpResponseRedirect(reverse( 'foursq_done' ) )

