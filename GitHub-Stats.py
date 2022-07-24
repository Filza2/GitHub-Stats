from requests import get
import re
print("""
 ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗       ███████╗████████╗
██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗      ██╔════╝╚══██╔══╝
██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝█████╗███████╗   ██║   
██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗╚════╝╚════██║   ██║   
╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝      ███████║   ██║   
 ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝       ╚══════╝   ╚═╝   
                        
                   By @TweakPY - @vv1ck
""")
user=input('[?] Enter The user : ')
try:
    r=get(f'https://github-readme-stats.vercel.app/api?username={user}',headers={'Host': 'github-readme-stats.vercel.app'})
    NF=str(re.findall('        <desc id="descId">(.*?)</desc>',r.text)[0])
    github_stats_Rank=str(re.findall('        <title id="titleId">(.*?)</title>',r.text)[0])
    print(f"""
[+] GitHub Stats : {NF}
[+] GitHub Stats Rank : {github_stats_Rank}    
""")
except IndexError:exit('[!] Error Fetch user data . .')
except:exit(f'[!] Fatel Error !')
