# first one

from collections import defaultdict


def ddos_ips(ip_list, window, critical):
    sample, rest = ip_list[:window], ip_list[window:]
    ddos_ips = find_suspisious(sample, critical)

    while rest:
        sample = sample[1:] + [rest.pop(0)]
        ddos_ips = ddos_ips | find_suspisious(sample, critical)

    ddos_ips = sorted(list(ddos_ips))
    return ddos_ips


def find_suspisious(sample, critical):
    ip_frequencies = defaultdict(lambda: 0)

    for ip in sample:
        ip_frequencies[ip] += 1

    return set([ip for ip, frequency in ip_frequencies.items() if frequency >= critical])


# input
ip_list_len = int(input())
window = int(input())
critical = int(input())

ip_list = []
for i in range(ip_list_len):
    ip_list.append(input())

# result calculation
ips = ddos_ips(ip_list, window, critical)
# output
print('\n'.join(ips))
