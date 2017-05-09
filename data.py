import urllib2
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
    return r.content


def print_members(data):
    members = data['results'][0]['members']
    for i in range(len(members)):
        print members[i]['first_name'], members[i]['last_name']
        print ""


senate = get_senate()
print_members(senate)

# data = json.loads(r.content)
# members = data['results'][0]['members']
# for i in range(len(members)):
#     print members[i]['first_name']
#     print members[i]['last_name']
#     print members[i]['twitter_account']
#     print members[i]['url']
