#!/usr/bin/env python
from rauth import OAuth1Service # pip install rauth
from rauth import OAuth1Session
import os

if __name__ == '__main__':

    ROOT = 'http://api.cubesensors.com'
    AUTH = '%s/auth' % ROOT
    RES = '%s/v1' % ROOT

    consumer_key = raw_input('Please enter consumer_key:')
    consumer_secret = raw_input('Please enter consumer_secret:')

    cbsr = OAuth1Service(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token_url='%s/access_token' % AUTH,
            authorize_url='%s/authorize' % AUTH,
            request_token_url='%s/request_token' % AUTH,
            base_url='%s/' % RES)

    request_token, request_token_secret = cbsr.get_request_token(params={"oauth_callback":"oob"})

    #print ('request token = %s, request token secret = %s' % (request_token, request_token_secret))

    authorize_url = cbsr.get_authorize_url(request_token)

    print 'Open the following URL in a browser and authorise access.'
    print authorize_url

    print 'Enter the code given below and press enter.'
    oauth_verifier = raw_input('oauth_verifier:')

    access_token, access_token_secret = cbsr.get_access_token(
            request_token,
            request_token_secret,
            method="POST",
            params={"oauth_verifier": oauth_verifier})

    print ('OAuth app token = %s , OAuth app token secret = %s' % (access_token, access_token_secret))
