import asyncio, aiohttp

USERS = ['octocat', 'torvalds', 'mojombo']

async def fetch(session, user):
    url = f'https://api.github.com/users/{user}'
    async with session.get(url) as resp:
        return await resp.json()

async def main():
    async with aiohttp.ClientSession() as s:
        tasks = [fetch(s,u) for u in USERS]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        # sort by public_repos
        users = [r for r in results if isinstance(r, dict)]
        users.sort(key=lambda x: x.get('public_repos',0), reverse=True)
        for u in users:
            print(u.get('login'), 'repos=', u.get('public_repos'))

if __name__ == '__main__':
    asyncio.run(main())
