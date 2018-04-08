#!/usr/bin/env python3
# get proxies from free-proxy-list.net and check them


from lxml import html
import requests

url = "https://free-proxy-list.net/"
page = requests.get(url)
max_proxies = 100

proxy_table_html = html.fromstring(page.content).xpath("//*[@id=\"proxylisttable\"]/tbody")

proxy_list = []

for row in proxy_table_html:
    proxy_table_rows = row.xpath("./tr")
    proxy_counter = 0
    for table_row in proxy_table_rows:
        table_row_items = table_row.xpath("./td")

        td_counter = 0
        proxy = []
        while td_counter < 2:
            proxy.append(table_row_items[td_counter].text)
            td_counter += 1
        proxy_list.append(tuple(proxy))
        proxy_counter += 1
        if proxy_counter >= max_proxies:
            break

proxies = []

for proxy in proxy_list:
    proxy_ip_port = proxy[0] + ":" + proxy[1]
    print(proxy_ip_port)
    proxies.append(proxy_ip_port)


# ## code from yousefissa/Proxy-Tester (github) (adapted)
# # github.com/yousefissa, twitter @yousefnu
#
# from time import time
# from requests import Session
#
# session = Session()
# session.headers.update({
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36'
#                   '(KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36'})
#
#
# def mil_seconds():
#     return int(round(time() * 1000))
#
#
# # MAIN
# # gets proxies and websites in a text file, rather than hard-coding them
# sites = ["http://footlocker.com/", "http://adidas.com/", "http://reddit.com/", "http://google.com/"]
#
#
# # checks if list is empty
# if not proxies:
#     print('You did not load proxies. Check your proxies.txt file!')
#     exit()
# else:
#     print('\nCurrently loaded: {}\n\n'.format(proxies))
# good_proxies, bad_proxies = [], []
#
# print('Testing on sites {}\n\n'.format(sites))
#
#
# def proxyChecker(proxy):
#     try:
#         proxy_parts = proxy.split(':')
#         ip, port, user, passw = proxy_parts[0], proxy_parts[
#             1], proxy_parts[2], proxy_parts[3]
#         proxies = {
#             'http': 'http://{}:{}@{}:{}'.format(user, passw, ip, port),
#             'https': 'https://{}:{}@{}:{}'.format(user, passw, ip, port)
#         }
#     except IndexError:
#         proxies = {'http': 'http://' + proxy, 'https': 'https://' + proxy}
#
#     for url in sites:
#         start_time = mil_seconds()
#         try:
#             response = session.get(url, proxies=proxies)
#             if response.status_code != 200:
#                 print('{} is not a good proxy.'.format(proxy))
#                 bad_proxies.append(proxy)
#             else:
#                 print(
#                     '{} on site {} ---- {} ms'.format(proxy, url, mil_seconds() - start_time))
#                 good_proxies.append(proxy)
#         except:  # broad exceptions are bad
#             print('Bad Proxy {} on site {}'.format(proxy, url))
#
#
# if __name__ == '__main__':
#     for p in proxies:
#         proxyChecker(p)
#     good_proxies_set, bad_proxies_set = set(good_proxies), set(bad_proxies)
#
#     with open('proxy_results.txt', 'a') as proxy_results:
#         proxy_results.write('\nTested on {}\n'.format(sites))
#         if good_proxies_set:
#             proxy_results.write('\nGood proxies: \n')
#             for proxy in good_proxies_set:
#                 proxy_results.write('{}\n'.format(proxy))
#         if bad_proxies_set:
#             proxy_results.write('Bad proxies: \n')
#             for proxy in bad_proxies_set:
#                 proxy_results.write('{}\n'.format(proxy))
#     if good_proxies_set:
#         print('\n\nGood proxies: {}'.format(good_proxies_set))
#     else:
#         print('\n\nNo good proxies.')