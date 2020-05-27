import pycurl, sys
curlc = sys.argv[1]
c = pycurl.Curl()
c.setopt(c.URL, curlc)

c.setopt(c.HTTPPOST, [('fileupload', (c.FORM_FILE, "file1",)),])

c.perform()
c.close()
