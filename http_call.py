# The unique URL used is the following:
# https://webhook.site/2ccbcad3-a4d2-45e3-a047-364c93da579c

import requests

print("Part 1: 3 HTTP Synchronous Calls")

for _ in range(3):
    r = requests.get('https://webhook.site/2ccbcad3-a4d2-45e3-a047-364c93da579c')
    print("X-request-Id:", r.headers['X-request-Id'])
    print("Date:", r.headers['Date'])

print()
