def remove_www(url):
    if url.startswith('www.'):
        url = url[4:]
    return url
