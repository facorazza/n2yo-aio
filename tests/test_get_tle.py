import asyncio

from n2yo.n2yo import N2YO


async def main():
    n2yo = N2YO()
    info, tle = await n2yo.get_tle(25544)
    assert info['satid'] == 25544


if __name__ == '__main__':
    asyncio.run(main())
