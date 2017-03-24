#!/usr/bin/env python
#coding:utf-8

import urllib,json,redis
k8s_pods_url = urllib.urlopen('http://IP/api/v1/pods/')
r = redis.Redis(host='192.168.4.206')
pods_info = json.load(k8s_pods_url)
pods_num = range(len(pods_info['items']))


#访问首页初始化 获取所有K8S pods和rc，写入redis
def getall():
    for i in pods_num:
        if 'ownerReferences' in  pods_info['items'][i]['metadata'].keys() and pods_info['items'][i]['metadata']['namespace'] != 'kube-system':
            r.getset(pods_info['items'][i]['metadata']['ownerReferences'][0]['name'],pods_info['items'][i]['metadata']['name'])

#返回rc值
def get_keys(a):
    return r.keys(a)

#返回所选rc的pod值
def get_values(key):
   try:
        return r.get(key).decode()
   except:
        return 'not find key'

if __name__ == '__main__':
    getall()














