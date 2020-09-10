# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os,sys

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

def main(client_secrets_file, id_list_file, playlist_id):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

    api_service_name = "youtube"
    api_version = "v3"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    with open(id_list_file) as f:
        for id in f:
            request = youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": playlist_id,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": id.strip()
                        }
                    }
                }
            )

            response = request.execute()

            print(response)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])