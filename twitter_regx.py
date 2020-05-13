# https://github.com/SamiMohsin/text-analysis/blob/master/twitter_regx.py



'''
This script for demonstration not aim
to be in real world all accounts taken are just found in web
for use of regx, with selenium to scraping website and gathering information


Please don't use just learn and study code


Not finish
'''

import re


# original tweet https://twitter.com/_FALCON_01/status/1183960656019644416
scrap = '''
المجموعة الثانية
@BoHamad76881021
@reedmeto
@masm2013hot
@w_o_2m
@Khaled_Ali_100
@uae_adh
@SaSalemali
@fha20150
@om_x22
@MKhmes
@SamirSamir10009
@basta696
@Faisal_UAE_1978
@Unkown730
@almndr16
@TAF115
@obaid_saleh
@turky3778
@abaalwlid
@83_boucharia
@aseem1109
نخلص هذيلا ونواصل
'''


# so i want to split all accounts and put them in simple list
# only accounts

if __name__ == '__main__':
    reg = '\B@[a-z0-9_-]+'
    mgs = re.findall(reg, scrap)
    print(mgs)

# output:
'''
['@reedmeto', '@masm2013hot', '@w_o_2m', '@uae_adh', '@fha20150', '@om_x22', '@basta696', '@almndr16', '@obaid_saleh', '@turky3778', '@abaalwlid', '@83_boucharia', '@aseem1109']
'''