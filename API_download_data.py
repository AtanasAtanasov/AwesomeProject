# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import re

import urllib.request

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_743597663350-79gqqg142sktjk2lsu4t37dao99k504v.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q="Bulgaria"
    )
    response = request.execute()

    videoids = open("videoIds.txt", "w")
    videoids.write(str(response))
    videoids.close()

    print(response)

    videourls = re.findall("https://i\.ytimg\.com/vi/.........../hqdefault\.jpg", str(response))

    print(videourls)

    counter = 1

    for video in videourls:
        urllib.request.urlretrieve(video, 'tb/thumbnail' + str(counter) + '.jpg')
        counter = counter+1

if __name__ == "__main__":
    main()
