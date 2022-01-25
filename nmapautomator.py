print('''
     :::       NMAP_AUTOMATOR       :::
     :::   USE ONLY IN KALI LINUX   :::

     :::          FEATURES          :::  
    Support URL/DNS - Thanks @KatsuragiCSL
    Add extensions fuzzing for http recon
    Add an nmap progress bar
    List missing tools in recon
    Add option to change output folder
    Save full script output to a file
    Improve performance and efficiency of the script - Thanks @caribpa
    Make nmapAutomater 100% POSIX compatible. - Massive Thanks to @caribpa
    Add network scanning type, so nmapAutomator can discover live hosts on the network.
''')

def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            OUTPUT = str(output.strip())[2:-1]
            print(OUTPUT)
    rc = process.poll()
    return rc

def automator(TARGET_IP,SCAN_TYPE,REMOTE_MODE,DNS_SERVER,OUTPUT_DIRECTORY,STATIC_NMAP_PATH):

    command = f'./nmapAutomator.sh -H {TARGET_IP} -t {SCAN_TYPE}'
    if len(REMOTE_MODE) > 2:
        r = f' -r {REMOTE_MODE}'
        command = str(command) + str(r)
    if len(DNS_SERVER) > 2:
        d = f' -d {DNS_SERVER}'
        command = str(command) + str(d)
    if len(OUTPUT_DIRECTORY) > 2:
        o = f' -o {OUTPUT_DIRECTORY}'
        command = str(command) + str(o)
    if len(STATIC_NMAP_PATH) > 2:
        s = f' -s {STATIC_NMAP_PATH}'
        command = str(command) + str(s)
        
#    os.system(command)
#    print(run_command(command))
    command = command.split(' ')
    print(subprocess.Popen(command, stdout=subprocess.PIPE ).communicate()[0])



if __name__ == '__main__':
    try:
        import os
    except:
        os.system('pip install os')
        import os
    try:
        import subprocess
    except:
        os.system('pip install subprocess')
        import subprocess
    try:
        import shlex
    except:
        os.system('pip install shlex')
        import shlex
    try:
        import re
    except:
        os.system('pip install re')
        import re
    
    TARGET_IPs = input('\t[*] ENTER TARGET_IPs:\n\t(Seperate With "," for Multiple IPs: "IP1,IP2,...")\n\t-> ')
    TARGET_IPs = list(TARGET_IPs.split(','))
    print('''
     :::         Scan Types         :::
    Network : Shows all live hosts in the host's network (~15 seconds)
    Port    : Shows all open ports (~15 seconds)
    Script  : Runs a script scan on found ports (~5 minutes)
    Full    : Runs a full range port scan, then runs a thorough scan on new ports (~5-10 minutes)
    UDP     : Runs a UDP scan "requires sudo" (~5 minutes)
    Vulns   : Runs CVE scan and nmap Vulns scan on all found ports (~5-15 minutes)
    Recon   : Suggests recon commands, then prompts to automatically run them
    All     : Runs all the scans (~20-30 minutes)
    ''')
    SCAN_TYPE = input('\t[*] ENTER SCAN_TYPE:\n\t-> ')
    REMOTE_MODE = input('\t[*] ENTER REMOTE_MODE:\n\t-> ')
    DNS_SERVER = input('\t[*] ENTER DNS_SERVER:\n\t-> ')
    OUTPUT_DIRECTORY = input('\t[*] ENTER OUTPUT_DIRECTORY:\n\t-> ')
    STATIC_NMAP_PATH = input('\t[*] ENTER STATIC_NMAP_PATH:\n\t-> ')
    
    if not os.path.exists("nmapAutomator.sh"):
        if not os.path.isdir("nmapAutomator"):
            print('Updating_APT_RepoList:',end='\r')
            os.system('sudo apt update')
            print('Updating_APT_RepoList: Done')
            print('Installing_ffuf_gobuster',end='\r')
            os.system('sudo apt install ffuf -y')
            print('Installing_ffuf_gobuster: Done')
            os.system('sudo apt install gobuster -y')
            print('Cloning_nmapAutomator_from_GITHUB:',end='\r')
            os.system('git clone https://github.com/21y4d/nmapAutomator.git')
            os.system('sudo ln -s $(pwd)/nmapAutomator/nmapAutomator.sh /usr/local/bin/')
            print('Cloning_nmapAutomator_from_GITHUB: Done')
        print('Change_Directory_to_nmap_Automator:',end='\r')
        os.system('cd nmapAutomator')
        print('Change_Directory_to_nmap_Automator: Done')
    try:
        print("Starting_Operation")
        for TARGET_IP in TARGET_IPs:
            automator(TARGET_IP,SCAN_TYPE,REMOTE_MODE,DNS_SERVER,OUTPUT_DIRECTORY,STATIC_NMAP_PATH)
        print("Operation_Done_Successfully")
    except:
        print('Operation_Error')

