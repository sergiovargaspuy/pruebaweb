
from urllib.request import urlopen

class WebClient(object):
    """WebClient class"""
    def __init__(self):
        super(WebClient, self).__init__()
    def download_page(arg):
        #connect to the website
        f = urlopen("http://www.eps.udl.cat/ca/")
        #get the download download_page
        page = f.read()
        #close the connection
        f.close()
        return page

    def run(self):
        # download a web page
        page=self.download_page()
    # seach activities in web page
    # print the activities
        print(page)

if __name__=="__main__":
    c = WebClient()
    c.run()