util
====

Cache : Save your data or objects to disk using pickle.

example :
```py
from util import Cache
cache = Cache(timeout=86400, directory="cache/")
data_url = 'https://github.com/irfantoor/util/archive/refs/heads/main.zip'

cache.set('p4', {
    'debug': True,
    'data_url': data_url,
})

# ...

result = cache.get('p4')
# if cache is expired it returns None, else it returns the value saved
```

Downloader : Download and do the extraction of the ziped data files
    .download(url: str, file: str = None, extract: bool = False)
    .extract(file: str)

example :
```py
# store data to this path
# it could be a relative or absolute path
data_source_path = "data/source/"
data_url = 'https://github.com/irfantoor/util/archive/refs/heads/main.zip'

dl = Downloader(data_source_path)

# download the zip file and extract the zip file
dl.download(url=data_url, extract=True)
```
