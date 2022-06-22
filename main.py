import requests, os
from colorama import Fore


def drawing():
  """
╦ ╦╔═╗╦ ╦╔╦╗╦ ╦╔╗ ╔═╗  ╔═╗╦═╗╔═╗╔╦╗╦╦ ╦╔╦╗  ╔═╗╔═╗╦═╗╔╦╗
╚╦╝║ ║║ ║ ║ ║ ║╠╩╗║╣   ╠═╝╠╦╝║╣ ║║║║║ ║║║║  ╠╣ ╠═╣╠╦╝║║║
 ╩ ╚═╝╚═╝ ╩ ╚═╝╚═╝╚═╝  ╩  ╩╚═╚═╝╩ ╩╩╚═╝╩ ╩  ╚  ╩ ╩╩╚═╩ ╩
  """
os.system("cls & title Youtube Codes Fetcher [Zardex#1337]")
drawing()
with open('tokens.txt') as e:
  for line in e:
    Token = line.strip('\n')
    headers = {'Authorization': Token}
    try:
      r = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers=headers)
      if 'code' in r.text:
        code = r.json()[0]['code'] 
        print(f'{Fore.RED}[+]{Fore.RESET} Fetched Premium Gift Code | {code} {Fore.GREEN}(Saved)')
        with open('Premium-Codes.txt', 'a') as hmm:
          hmm.write(f'{code}\n')
      else:
        pass
    except Exception:
      pass
  
    


