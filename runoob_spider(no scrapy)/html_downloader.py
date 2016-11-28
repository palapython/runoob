import requests


class HtmlDownload(object):
    def download(self, url):
        if url is None:
            return

        response = requests.get(url)
        if response.status_code != 200:
            return
        return response.text
