# for asynchronous way of 3 HTTP calls, this program will use the
# requests_threads.py script from the GitHub repository requests/requests-threads
# as well as the Twisted engine
from requests_threads import AsyncSession

print("Part 2: 3 HTTP Asynchronous Calls")

session = AsyncSession(n=3)

async def main():
    rArray = []
    for _ in range(3):
        rArray.append(await session.get('https://webhook.site/2ccbcad3-a4d2-45e3-a047-364c93da579c'))
    for r in rArray:
        print("X-request-Id:", r.headers['X-request-Id'])
        print("Date:", r.headers['Date'])

session.run(main)
