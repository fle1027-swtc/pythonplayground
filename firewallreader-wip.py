import csv
from collections import Counter

def extract_denied_addresses(csv_file):
    ipv4_addresses = []
    ipv6_addresses = []

    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Adjust the 'action' key to the appropriate one from your CSV
            if row.get('action') == 'deny':
                # Adjust the keys for your source IPs in the CSV
                ipv4 = row.get('source_ipv4')
                ipv6 = row.get('source_ipv6')

                if ipv4:
                    ipv4_addresses.append(ipv4)
                if ipv6:
                    ipv6_addresses.append(ipv6)

    return ipv4_addresses, ipv6_addresses

def get_most_frequent_address(ipv4_addresses, ipv6_addresses):
    # Count occurrences of each address
    ipv4_counter = Counter(ipv4_addresses)
    ipv6_counter = Counter(ipv6_addresses)

    # Find the most common IPv4 and IPv6 addresses
    most_common_ipv4 = ipv4_counter.most_common(1)
    most_common_ipv6 = ipv6_counter.most_common(1)

    return most_common_ipv4, most_common_ipv6

def main():
    csv_file = 'path/to/your/logfile.csv'  # Change this to your file path

    ipv4_addresses, ipv6_addresses = extract_denied_addresses(csv_file)
    most_common_ipv4, most_common_ipv6 = get_most_frequent_address(ipv4_addresses, ipv6_addresses)

    print("Most frequently denied IPv4 address:", most_common_ipv4[0] if most_common_ipv4 else "None")
    print("Most frequently denied IPv6 address:", most_common_ipv6[0] if most_common_ipv6 else "None")

if __name__ == '__main__':
    main()
