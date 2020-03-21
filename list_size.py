import argparse
import sys
if sys.version_info[0] == 3:
    from urllib.request import urlopen
    from urllib.error import URLError as error
else:
    from urllib import urlopen
    error = IOError

size, comp, ucomp = 0, 0, 0


class Printer():
    def __init__(self, *args):
        data = ""
        for i in args:
            data += str(i)
            data += ""
        sys.stdout.write("\r\x1b[K"+data.__str__())
        sys.stdout.flush()


def to_gb(x):
    return int(x) / 1024 / 1024 / 1024


def to_mb(x):
    return int(x) / 1024 / 1024


def get_size(link):
    link = link.replace("\n", "")
    try:
        site = urlopen(link)
        meta = site.info()
        if sys.version_info[0] == 3:
            return int(dict(meta.items()).get("Content-Length"))
        else:
            return int(dict(meta.items()).get("content-length"))
    except error:
        return False
    except TypeError:
        return False


location = sys.argv[1]
with open(location) as urls:
    size = 0
    urls = urls.readlines()
    for url in urls:
        Printer(
            "Check ", comp +
            ucomp, " of ", len(
                urls), " ---- size until now: ", int(to_mb(size)), " Mb"
        )
        if url == "\n":
            continue
        size += get_size(url)
        if size:
            comp += 1
        else:
            ucomp += 1
print("\n"*2)
print("count of links:", len(urls))
print("Succesful:", comp)
print("Unsuccessful:", ucomp)
print("Mb:", to_mb(size))
print("Gb:", to_gb(size))
