import os
from typing import Final
from dotenv import load_dotenv
from discord import Intents, Client, Message
import dict as d

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)
class coluna:
    def __init__(self, titulo):
        self.id = 0
        self.titulo = titulo
        self.corpo = []
        #o titulo vai com a palavra de referencia da coluna e o corpo com quantas vezes
        #essa palavra titulo aparece com outra que tenha um index igual ao index da palavra
        #titulo + o index desta palavra no corpo da coluna.]
        
    def setCorpo(self, pos, value):
        if len(self.corpo) == 0:
            self.corpo.append(0)
        if len(self.corpo)-1 < pos:
            for n in range(self.corpo[len(self.corpo)-1],pos):
                self.corpo.append(0)
            self.corpo.append(value)
        else:
            self.corpo[pos] = value

    def getCorpo(self, pos):
        if len(self.corpo)-1 < pos:
            self.setCorpo(pos, 0)
        return self.corpo[pos]

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Que porra é sessa caraio')
    try: 
        response: str = d.user_message_to_matrix('sabedoriajaponesa',user_message, d.loadMatrix('sabedoriajaponesa'), d.loadDic('sabedoriajaponesa'), True, 'b', 0.995, False, True)
        if response != None:
            await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} tá correndo!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return 

    username: str = str(message.author)
    user_messsage: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_messsage}"')
    await send_message(message, user_messsage)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()