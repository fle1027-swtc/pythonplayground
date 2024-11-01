import re
from collections import Counter

def extract_denied_addresses(log_file, action_keyword):
    ipv4_addresses = []
    ipv6_addresses = []

    with open(log_file, mode='r', encoding='utf-8') as file:
        for line in file:
            # Check if the line contains the action keyword
            if action_keyword.lower() in line.lower():
                # Use regex to find the source IP address
                ipv4_match = re.search(r'src outside:(\d+\.\d+\.\d+\.\d+)', line)
                ipv6_match = re.search(r'src outside:([0-9a-fA-F:]+)', line)

                if ipv4_match:
                    ipv4_addresses.append(ipv4_match.group(1))
                if ipv6_match:
                    ipv6_addresses.append(ipv6_match.group(1))

    return ipv4_addresses, ipv6_addresses

def get_most_frequent_address(ipv4_addresses, ipv6_addresses):
    ipv4_counter = Counter(ipv4_addresses)
    ipv6_counter = Counter(ipv6_addresses)

    most_common_ipv4 = ipv4_counter.most_common(1)
    most_common_ipv6 = ipv6_counter.most_common(1)

    return most_common_ipv4, most_common_ipv6

def main():
    log_file = input("Please enter the path to your log file: ")  # Accept user input for the file path
    action_keyword = input("Please enter the action keyword to filter by (e.g., 'Deny'): ")  # Accept user input for action keyword

    ipv4_addresses, ipv6_addresses = extract_denied_addresses(log_file, action_keyword)
    most_common_ipv4, most_common_ipv6 = get_most_frequent_address(ipv4_addresses, ipv6_addresses)

    print("Most frequently denied IPv4 address:", most_common_ipv4[0] if most_common_ipv4 else "None")
    print("Most frequently denied IPv6 address:", most_common_ipv6[0] if most_common_ipv6 else "None")

if __name__ == '__main__':
    main()
