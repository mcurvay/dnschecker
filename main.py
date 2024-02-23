import dns.resolver


def dns_query(url, dns_servers):
    results = {}
    for dns_server in dns_servers:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [dns_server]

        try:
            result = dns.resolver.Resolver.resolve()(url)
            results[dns_server] = [data.to_text() for data in result]
        except dns.exception.DNSException as e:
            results[dns_server] = str(e)
    return results


if __name__ == "__main__":
    url = input("Sorgulamak istediğiniz URL'i girin: ")  # Kullanıcıdan URL alınır
    dns_servers = [
         "8.8.8.8",        # Google Public DNS
        "8.8.4.4",        # Google Public DNS
        "208.67.222.222", # OpenDNS
        "208.67.220.220", # OpenDNS
        "1.1.1.1",        # Cloudflare DNS
        "1.0.0.1",        # Cloudflare DNS
        "9.9.9.9",        # Quad9
        "149.112.112.112",# Quad9
        "64.6.64.6",      # Verisign Public DNS
        "64.6.65.6",      # Verisign Public DNS
        "84.200.69.80",   # DNS.WATCH
        "84.200.70.40",   # DNS.WATCH
        "156.154.70.1",   # Comodo Secure DNS
        "156.154.71.1",   # Comodo Secure DNS
        "8.26.56.26",     # Comodo Secure DNS
        "8.20.247.20",    # Comodo Secure DNS
        "208.67.220.220", # OpenDNS Home
        "208.67.222.222", # OpenDNS Home
        "199.85.126.10",  # Norton ConnectSafe
        "199.85.127.10",  # Norton ConnectSafe
        "77.88.8.8",      # Yandex.DNS
        "77.88.8.1",      # Yandex.DNS
    ]  # Kullanmak istediğiniz DNS sunucularının IP adresleri
    results = dns_query(url, dns_servers)
    for dns_server, result in results.items():
        print(f"DNS Sunucusu: {dns_server}")
        if isinstance(result, list):
            for data in result:
                print(data)
        else:
            print("Hata:", result)
        print("-" * 30)
