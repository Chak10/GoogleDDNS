import requests
import ipaddress
import argparse


def check_ip(Ip):
    try:
        ip = ipaddress.ip_address(Ip)
        print(f'{ip} is correct. Version: IPv{ip.version}')
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update IP Google DDNS.')
    parser.add_argument('-u', '--user',
                        help='Username', required=True)
    parser.add_argument('-p', '--passwd',
                        help='Password', required=True)
    parser.add_argument('-d', '--dom',
                        help='Domain', required=True)

    args = parser.parse_args()
    myUname = args.user
    myPasswd = args.passwd
    myDomain = args.dom

    url_ip6 = 'https://domains.google.com/checkip'
    try:
        url_ip6 = requests.get(url_ip6)
        url_ip6 = url_ip6.text
    except:
        pass

    if check_ip(url_ip6):
        url_final = "{url}?hostname={host}&myip={ip}".format(
            url='https://domains.google.com/nic/update', host=myDomain, ip=url_ip6)
        try:
            res = requests.post(url_final,
                                headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'},
                                auth=(myUname, myPasswd)
                                )
            print(res.status_code)
            print(res.text)
        except:
            pass
