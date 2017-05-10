import urllib2
import urllib
import requests
import json
import api as AK

key = AK.key


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
    return senators

    # results = member['results']
    #     for i in member:
    #         senators.append(member.copy())
    # print senators


print(get_senator('NY'))

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
