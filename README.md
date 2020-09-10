This script adds YouTube videos into your playlists.
To allow the app adding videos to your playlist, you will need the authorize it.

# Getting started

## Get a list of video ids
Pass the script a list of video names, seperated by newline.
You will recieve a list of video ids.

```
$ ./getIds.sh names.list
```

## Authorize
- https://console.developers.google.com/
- OAuth-Zustimmungsbildschirm -> create project -> extern -> set a name -> save
- Anmeldedaten -> cretae oauth-client-id -> select Sontiges or desktop client -> create
- download client_secret.json

## Add videos to playlist
```
$ python3 -m venv ./venv

$ ./venv/bin/pip install google_auth_oauthlib google-api-python-client

$ ./venv/bin/python3 add.py client_secret.json id.list $PLAY_LIST_ID
```

# Sources
https://developers.google.com/youtube/v3/getting-started