hosts = ["dev-compute-01", "prod-compute-02", "uat-controller-5", "dev-compute-45"]
tests_hosts = []
prod_hosts = list()
#print("===Print list with for===")
#for host in hosts:
#    print(host)

#i = 0
#print("===Print list with while===")
#while i < len(hosts):
#    print(hosts[i])
#    i += 1

#target_host = input("Enter host: ")
#print("===> Find host with 'in' ")
#if target_host in hosts:
#    print(f"{target_host} found")
#else:
#    print(f"{target_host} not found")

#print("===> Find host with 'for' ")
#for host in hosts:
#    if target_host == host:
#        print(f"{target_host} found")
#        break

#new_host = input("Enter host: ")
#hosts.append(new_host)
#prod_hosts.append(new_host)
hosts.sort()
print(f"{hosts[2]}\n")
for host in hosts:
    print(host)
print(f"\n")
print(f"{hosts.pop(2)}\n")
for host in hosts:
    print(host)
#print(hosts.index("dev-compute-01"))


