import asyncio
import requests

async def download():
    URL = "https://imgs.search.brave.com/VfYZw7XAA-jrfg-ohlkEgdb9iNFsw19FximTDsk1tZk/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJhY2Nlc3Mu/Y29tL2Z1bGwvNDkw/"
    response = requests.get(URL)
    open("Avast.jpg" , "wb").write(response.content)
    print("func1")

async def download2():
    URL = "https://imgs.search.brave.com/VfYZw7XAA-jrfg-ohlkEgdb9iNFsw19FximTDsk1tZk/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJhY2Nlc3Mu/Y29tL2Z1bGwvNDkw/"
    response = requests.get(URL)
    open("Avast2.jpg" , "wb").write(response.content)
    print("func2")
    
async def download3():
    URL = "https://imgs.search.brave.com/VfYZw7XAA-jrfg-ohlkEgdb9iNFsw19FximTDsk1tZk/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJhY2Nlc3Mu/Y29tL2Z1bGwvNDkw/"
    response = requests.get(URL)
    open("Avas3.jpg" , "wb").write(response.content)
    print("func3")

async def main():
    L = await asyncio.gather(
        download(),
        download2(),
        download3()
    )   
    print(L)
asyncio.run(main())