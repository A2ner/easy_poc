# -*- coding: utf-8 -*-
def read_config():
    f = open('config.txt', 'r')
    config_data = {}
    for line in f.readlines():
        line = line.strip()
        if not len(line):
            continue
        config_data[line.split(':')[0]] = line.split(':')[1]
    f.close()
    return config_data


def produce_sql_poc():
    sql_get_template = '''# coding: utf-8
import requests
import random
import hashlib
class POC:
    def __init__(self):
        self.url = ''
        self.pocInfo = {{
            'author': 'cc',
            'vuInData': '{}',
            'createDate': '2018-01-15',
            'vulnLevel': 'high',
            'reference': ['{}'],
            'pocName': '{}',
            'appName': '{}',
            'appVersion': '{}',
            'appLink': '{}',
            'desc': """
                该应用程序页面存在SQL注入漏洞，类型为get
                """,
            'samples': ['']
        }}
    def verify(self):
        try:
            random_num = random.randint(1111, 9999)
            md5_num = hashlib.md5(str(random_num)).hexdigest()
            payload = self.url + "/{}".format(
                random_num)
            headers = {{
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                "Content-Type": "application/x-www-form-urlencoded"
            }}
            response = requests.get(url=payload, headers=headers, timeout=5).content
            if md5_num in response:
                return True
            else:
                return False
        except Exception as error:
            return False
			
			
#if __name__ == '__main__':
#     test = POC()
#     test.url = 'http://127.0.0.1'
#     print test.verify()
    
    '''
    raw_sql_post = ''''''

    # f = open('config.txt', 'r')
    # config_data = {}
    # for line in f.readlines():
    #     line = line.strip()
    #     if not len(line):
    #         continue
    #     config_data[line.split(':')[0]] = line.split(':')[1]
    # f.close()
    # global pocname
    date = config_data['date']
    pocname = config_data['pocname']
    reference = config_data['reference']
    appname = config_data['appname']
    appversion = config_data['appversion']
    applink = config_data['applink']
    payload = config_data['payload']
    final_content = sql_get_template.format(date, reference, pocname, appname, appversion, applink, payload)
    output = open('{}.py'.format(pocname), 'w')
    output.write(final_content)
    output.close()

def produce_xss_poc():
    xss_reflect_template = '''# coding: utf-8
import random
import hashlib
import requests
class POC:
    def __init__(self):
        self.url = ''
        self.pocInfo = {{
            'author': 'cc',
            'vuInData': '{}',
            'createDate': '2018-1-22',
            'vulnLevel': 'high',
            'reference': ['{}'],
            'pocName': '{}',
            'appName': '{}',
            'appVersion': '{}',
            'appLink': '{}',
            'desc': """
                该应用程序页面存在反射型XSS漏洞
                """,
            'samples': ['']
        }}
    def verify(self):
        random_num = random.randint(1111, 9999)
        md5_num = hashlib.md5(str(random_num)).hexdigest()
        try:
            response = requests.get(self.url+"/{}".format(md5_num), timeout=5)
            data = response.content
            if md5_num in data:
                return True
        except Exception as error:
            return False
			
			
#if __name__ == '__main__':
#     test = POC()
#     test.url = 'http://127.0.0.1'
#     print test.verify()

    '''
    # f = open('config.txt', 'r')
    # config_data = {}
    # for line in f.readlines():
    #     line = line.strip()
    #     if not len(line):
    #         continue
    #     config_data[line.split(':')[0]] = line.split(':')[1]
    # f.close()
    # global pocname
    date = config_data['date']
    pocname = config_data['pocname']
    reference = config_data['reference']
    appname = config_data['appname']
    appversion = config_data['appversion']
    applink = config_data['applink']
    payload = config_data['payload']
    final_content = xss_reflect_template.format(date, reference, pocname, appname, appversion, applink, payload)
    output = open('{}.py'.format(pocname), 'w')
    output.write(final_content)
    output.close()

config_data = read_config()
if config_data['type'] == 'xss':
    produce_xss_poc()
elif config_data['type'] == 'sql':
    produce_sql_poc()

print('success!')

