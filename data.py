import requests
import json
import api as AK
from twython import Twython
from twitter import twitter

key = AK.key
API_KEY = 'QEINI9FGfTrc3fgbg5ij2eMxS'
APP_SECRET = 'Sxu4Hve1PBrYw2SYxwzqxGNUgsrKHz2SNSKHrO7PGJvSJe0qSz'


def get_senate():
    url = 'https://api.propublica.org/congress/v1/115/senate/members.json'
    r = requests.get(url, headers={"X-API-KEY": key})
    members = json.loads(r.content)
    return members


def get_house():
    url = 'https://api.propublica.org/congress/v1/115/house/members.json'
    r = requests.get(url, headers={"X-API-KEY": key})
    members = json.loads(r.content)
    return members


def get_senator(query):
    state = query
    url = 'https://api.propublica.org/congress/v1/members/senate/' + state + '/current.json'
    r = requests.get(url, headers={"X-API-KEY": key})
    members = json.loads(r.content)
    results = members['results']
    member_api = None
    senators = []
    for i in results:
        member_api = i['api_uri']

        r = requests.get(member_api, headers={"X-API-KEY": key})
        i = json.loads(r.content)
        senators.append(i)
        twitter_username = None
        twitter_username = i['results'][0]['twitter_account']
        twitter_pull = twitter.show_user(screen_name=twitter_username)
        twitter_info = {'twitter_background': twitter_pull['profile_background_image_url'],
                        'twitter_profile_image': twitter_pull['profile_image_url'], 'twitter_followers': twitter_pull['followers_count']}
        senators[-1]['results'][0].update(twitter_info)
    # i['results'][0].update(twitter_info)
    # senators.append(twitter_info)
    return senators
    #


get_senator('NY')
# results = member['results']
#     for i in member:
#         senators.append(member.copy())
# print senators
# print twitter.show_user(screen_name='barackobama')


# get_senator('NY')

# for i in results:
#     individual = {"first_name": i['first_name'], "last_name": i['last_name'], "url": i['url'],
#                   "twitter_account": i['twitter_account'], "facebook_account": i['facebook_account'], "rss_url": i['rss_url'], "domain": i['domain'], }
#     print individual

# for results in members:
#     print members['results'][0]['name']


# def get_reps(query):
#     query = urllib.quote(query)
#     url = "https://api.geocod.io/v1/".format(query)
#     data = urllib2.urlopen(url).read()
#     parsed = json.loads(data)
#     print parsed


# get_reps("11600 Century Oaks Terrace, Austin TX")

# def print_members(data):
#     members = data['results'][0]['members']
#     for i in range(len(members)):
#         print members[i]['first_name'], members[i]['last_name']
#         print ""
#
#
#
# senate = get_senate()
# print_members(senate)

# data = json.loads(r.content)
# members = data['results'][0]['members']
# for i in range(len(members)):
#     print members[i]['first_name']
#     print members[i]['last_name']
#     print members[i]['twitter_account']
#     print members[i]['url']
