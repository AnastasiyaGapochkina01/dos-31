def calc(a, b):
    return a + b, a - b, a * b

host_info = ("dev-compute-25", 128, "2cpu")
print(host_info)
for item in host_info:
    print(item)

i = 1
print(f"{i} - {host_info[i]}")

#host_name = host_info[0]
#mem = host_info[1]
#vcpu = host_info[2]
host_name, mem, vcpu = host_info

print(f"HostName: {host_name}\nMem: {mem}\nCPU: {vcpu}")

summ, diff, mult = calc(5, 9)
print(summ, diff, mult)