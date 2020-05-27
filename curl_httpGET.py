import pycurl, sys
from io import BytesIO
b = sys.argv[1]
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, b)
#c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
# Body is a byte string.
# We have to know the encoding in order to print it to a text file
# such as standard output.
print(body.decode('utf-8'))
