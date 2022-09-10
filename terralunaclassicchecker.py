# ====================================================================================================================================================
# Name        : terralunaclassicchecker.py
# Author      : Peter Andrei Limpoco Bunao
# Version     : 1.0.0
# Date        : September 07, 2022
# Copyright   : GPL v3.0
# Description : Use this to query unlimited Terra Luna Classic Addresses at once. 
# ====================================================================================================================================================

from terra_sdk.client.lcd import LCDClient
import pandas as pd 

terra = LCDClient(url="https://lcd.terra.dev", chain_id="columbus-5")
data = pd.read_csv('myaddresses.csv') #Reading csv file with Terra Luna Address
Wallet_Address=(data.loc[:,"Address"])
print (Wallet_Address)  
Balance_storage = []
for address in Wallet_Address:
    print(address)
    balance_array = terra.bank.balance(address)
    balance = balance_array[1]['total']
    Balance_storage.append(balance)
new_dataset = pd.DataFrame(data)
new_dataset['Balance'] = Balance_storage
new_dataset.to_csv('myaddresses.csv',index=False) #appends a new column called Balance on the same csv file


