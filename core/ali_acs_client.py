#! /usr/bin/env python3
# coding:utf-8
from aliyunsdkcore.client import AcsClient
import configparser
import os


def acs_client():
    env_list = os.environ
    cf = configparser.ConfigParser()
    # cf.read('config.conf')
    cf.read(env_list['DDNS'] + '/config.conf')
    accesskey_id = cf.get('acs', 'accesskey_id')
    accesskey_secret = cf.get('acs', 'accesskey_secret')
    region_id = cf.get('acs', 'region_id')
    client = AcsClient(accesskey_id, accesskey_secret, region_id)
    return client
