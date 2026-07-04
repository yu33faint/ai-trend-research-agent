from urllib.parse import urlsplit, urlunsplit


def clean_url(url):
    parts = urlsplit(url)

    return urlunsplit((
        parts.scheme,
        parts.netloc,
        parts.path,
        "",
        "",
    ))