import re
from collections import Counter

def extract_denied_addresses(log_file, action_keywords):
    ipv4_addresses = []
    ipv6_addresses = []

    # Normalize keywords to lowercase for comparison
    action_keywords = [keyword.lower() for keyword in action_keywords]

    with open(log_file, mode='r', encoding='utf-8') as file:
        for line in file:
            # Check if the line contains any of the action keywords
            if any(keyword in line.lower() for keyword in action_keywords):
                # Use regex to find the source IP address
                ipv4_match = re.search(r'src outside:(\d+\.\d+\.\d+\.\d+)', line)
                # Updated regex for matching valid IPv6 addresses
                ipv6_match = re.search(r'src outside:([0-9a-fA-F:]{7,39})', line)

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
    action_keywords_input = input("Please enter the action keywords to filter by (e.g., 'Deny, denied'): ")  # Accept user input for action keywords
    action_keywords = [keyword.strip() for keyword in action_keywords_input.split(',')]  # Split input into a list

    ipv4_addresses, ipv6_addresses = extract_denied_addresses(log_file, action_keywords)
    most_common_ipv4, most_common_ipv6 = get_most_frequent_address(ipv4_addresses, ipv6_addresses)

    if most_common_ipv4:
        print(f"Most frequently denied IPv4 address: {most_common_ipv4[0][0]} (Denied {most_common_ipv4[0][1]} times)")
    else:
        print("No denied IPv4 addresses found.")

    if most_common_ipv6:
        print(f"Most frequently denied IPv6 address: {most_common_ipv6[0][0]} (Denied {most_common_ipv6[0][1]} times)")
    else:
        print("No denied IPv6 addresses found.")

if __name__ == '__main__':
    main()

