import sys
import requests
from colorama import Fore

def __start__():
        try:
                print(Fore.LIGHTRED_EX+" [!] Enter The Domain\n")    
                inp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"KnightSpy"+Fore.BLUE+"~"+Fore.WHITE+"snehraval"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"HTTP-Header"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
                result = requests.get('https://api.hackertarget.com/httpheaders/?q=' + inp).text
                print(Fore.LIGHTBLUE_EX+result)
                try:
                        input(Fore.RED+" [!] "+Fore.GREEN+"Back To Menu (Press Enter...) ")
                except:
                        print("")
                        sys.exit()  

        
        except:
                print("\nExit :)")














