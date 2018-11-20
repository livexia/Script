filepath = "/Users/livexia/Workshops/router/dhcp-dns"
etherspath = "/Users/livexia/Workshops/router/ethers"
hosts_dnsmasqpath = "/Users/livexia/Workshops/router/hosts.dnsmasq"
dhcp_staticlistpath = "/Users/livexia/Workshops/router/dhcp_staticlist1.txt"
l=[]
content = ''
with open(filepath, 'r') as f:
    content = f.read().strip()

l = content.split("config host")
print(len(l))
l=l[1:]
print(len(l))

a=[]
for i in l:
    i = i.strip().split("option ")[1:]
    d={}
    for j in i:
        j = j.strip().strip().split(' ')
        j = [x.strip("'") for x in j]
        d[j[0]]=j[1]
    a.append(d)
print(a)

with open(etherspath, 'w') as f:
    for i in a:
        s=i['mac']+' '+i['ip']+'\n'
        f.writelines(s)

with open(hosts_dnsmasqpath, 'w') as f:
    for i in a:
        s=i['ip']+' '+i['name']+'\n'
        f.writelines(s)


with open(dhcp_staticlistpath, 'w') as f:
    for i in a:
        s="<{}>{}>{}".format(i["mac"],i["ip"],i["name"])
        f.writelines(s)