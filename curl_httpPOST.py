import pycurl,sys
try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode

urlc = sys.argv[1]
crl = pycurl.Curl()
crl.setopt(crl.URL, urlc)
data = {'tset1': 'testobj'}
pf = urlencode(data)

# Sets request method to POST,
# Content-Type header to application/x-www-form-urlencoded
# and data to send in request body.
crl.setopt(crl.POSTFIELDS, pf)
crl.perform()
crl.close()
