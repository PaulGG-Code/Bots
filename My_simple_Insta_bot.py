#importation
from instapy import InstaPy

#initialisation
#for a better optimization use headless => it will run the bot without a GUI:
#session = InstaPy(username='test', password='test', headless_browser=True)
session = InstaPy(username="jeepgold", password="kamikaz")
session.login()
'''
#setup all the setting
session.set_relationship_bounds(enable=True,
                                potency_ratio=1.21,
                                delimit_by_numbers=True,
                                max_followers=4000,
                                max_following=5000,
                                min_followers=60,
                                min_following=100)'''

#What my bot like
session.like_by_tags(["kali_linux", "python", "linux", "cybersecurity","cloud", "instatech", "technews", "programming", "cyberattack", "informationsecurity", "cybersecurityawareness", "coder", "networksecurity"], amount=100)

session.set_do_comment(True, percentage=10)
session.set_comments(["I like!", "This is interesting!", "Nice!!"])
session.set_dont_like(["nude"," nswf", "porn"])

#session.set_quota: instagram will notice the bot and will ban some of its actions. 
#using the quota, the bot will keep commenting until it reaches its hourly and daily limits. 
#it will resume commenting after the quota period has passed
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

#end the bot session
session.end()
