import discord
from discord.ext import (
    commands,
    tasks
)
from time import sleep
import telegram

telbot = telegram.Bot(token='Telegram token Here')
chat_id = telegram chat id here


bot = discord.Client()
bot = commands.Bot(
    
    self_bot=True
    
)

token = "discord bot or user token here"
#지금까지 기타 설정들
@bot.event
async def on_ready():
    print("디스코드와 연결되었습니다. 모든 메시지가 기록됩니다.")
    telbot.sendMessage(chat_id=chat_id, text=f"디스코드와 연결되었습니다. 모든 메시지가 기록됩니다.") # 연결되었다는 알림 보내기

@bot.event
async def on_message(message):
        
    with open("chat_history.log", "a") as f: # 파일 열기
        try:
            async for message in message.channel.history(limit=1):  #다른 사용자가 서버에서 보낸 메시지를 확인하기 위함
                f.write(f"servername = {message.guild.name} ,time = ({message.created_at}) / who = {message.author.name} | content =  {message.content}\n") # 파일로 저장
                
        
                sleep(4) # 메시지 계속 올떄 텔레그램으로 바로 보내면 텔레그램 측에서 일시적으로 차단함
                telbot.sendMessage(chat_id=chat_id, text=f"{message.guild.name} 에서 {message.author.name} 로 부터 ({message.created_at})에 메시지가 도착 또는 발송 하였습니다. 자세한 내용 >>>" + f"servername = {message.guild.name} ,time = ({message.created_at}) / who = {message.author.name} | content =  {message.content}\n") # 텔레그램 으로 전송
        
        except (Exception, AttributeError, ValueError) as e: #기타 에러 또는 {message.guild.name}은 서버에서만 작동함으로 dm이나 채널로 보내면 AttributeError발생함 또한 다른 에러 발생시 텔레그램으로 전송하기 위함
            telbot.sendMessage(chat_id=chat_id, text="에러가 발생했습니다 서버가아닌 채널,DM이신가요? DM모드로 일시 전환후 수신합니다. 그게 아닐경우 에러입니다 해당 앱을 구동하는 서버에 들어가서 확인해보시기 바랍니다.") #에러 발생 표시
            f.write(f"servertype= DM or channel time = ({message.created_at}) / who = {message.author.name} content =  {message.content}\n") #파일로작성
            
        
            sleep(4) # 차단방지
            
            telbot.sendMessage(chat_id=chat_id, text=f"Direct Message(DM) 또는 채널 에서 {message.author.name} 로 부터 ({message.created_at})에 메시지가 도착 또는 발송 하였습니다. >>>" + f"servertype= DM or channel ,time = ({message.created_at}) / who = {message.author.name} | content =  {message.content}\n") #텔레그램으로 전송
 





                
bot.run(token,bot=False, reconnect=True) # 봇 작동엔 필수임


