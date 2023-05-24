from csv import writer
from bs4 import BeautifulSoup
import requests


try:
    with open('xmlvalidator.xml', 'r') as f:
        file = f.read()
    
    soup=BeautifulSoup(file,'xml')
    #print(soup)
    contract_ids=soup.find_all('contract_id')
    mbr_ids=soup.find_all('mbr_id')
    mbr_incent_levels=soup.find_all('mbr_incent_level')
    for contract_ids,mbr_ids,mbr_incent_levels in soup:
        contract_id=contract_ids.text
        con=[]
        con.append(contract_id)
        print(contract_id)


except Exception as e:
    print(e)
