import yaml
import requests
file = open(r"D:\PyCharm\PycharmProjects\papi\api_cases\test\accountserviceid\1addMerchantAccount.yaml",'rb')
api_list = yaml.full_load(file)
print(api_list)
