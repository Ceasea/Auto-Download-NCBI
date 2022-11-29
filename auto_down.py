#!/usr/bin/env python3
'''
Auto donwload ncbi metagenomal data
'''
import os
import requests

proxies = {
  'http': 'http://127.0.0.1:10809',
  'https': 'http://127.0.0.1:10809',
}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}


def project(name='PRJNA773617'):
    '''获取项目信息'''
    url = 'https://www.ncbi.nlm.nih.gov/sra/?term={}'.format(name)
    req = requests.get(url=url,headers=headers,proxies=proxies)
    print(req.text)

def download(sample,type='fasta'):
    '''下载项目数据'''
    url= 'https://trace.ncbi.nlm.nih.gov/Traces/sra-reads-be/{}?acc={}'.format(type, sample)

    req = requests.get(url=url,headers=headers,proxies=proxies)
    #print(req.headers)
    with open("{}.{}.gz".format(sample, type),'wb') as f:
        f.write(req.content)

if __name__ == '__main__':
    if not os.path.exists("SRR_Acc_List.txt"):
        print("Please get SRR_ACC_List.txt in NCBI According to the tutorial")
        exit()
    with open("SRR_Acc_list.txt", 'r') as f:
        lines = f.readlines()
    for line in lines:
        name = line.strip().split()[0]
        print("Downloading", name)
        download(sample=name)