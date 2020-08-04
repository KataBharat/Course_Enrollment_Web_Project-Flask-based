import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xfb\xc8\x7f\xcdn\x84GV\xee\x8fs;\x10\xa2\xf4\xe3'           # things like sessions cookies are checked using this key preventing anybody from modifying them
    
    MONGODB_SETTINGS = {'db' : 'UTA_Enrollment'}