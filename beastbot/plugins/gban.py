from telethon import events
import beastbot.client
import os
import beastbot.resources
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
import asyncio
from telethon.tl.types import ChannelParticipantCreator, ChannelParticipantAdmin
from telethon.tl.functions.channels import GetParticipantRequest
import random


gbanned = []
client = beastbot.client.client
DEVLIST = [5009604489,5004021105,945846353]
FRNDLIST = [2077699752,5029218505,5032100535]
import time

chats = 94
r = {}

@events.register(events.NewMessage(outgoing=True, pattern=r'\.gban'))
async def gban(event):
  global r
  chat = await event.get_chat()
  chats = 94
  userid=chat.id
  m = True
  c = True
  strg = ""
  split = event.text.split(" ")
  try:
    tezt = event.text[6]
    c = False
  except:
    pass
  if userid in r:
    await client.edit_message(event.message,"πππΎ π·π΄ π°π»ππ΄π°π³π πΆ π±π°π½π½π΄π³")
    m = False
  if not event.text[0].isalpha() and c and m:
    reason = event.text[6:1000]
    f = r[userid] = reason
    
  else:
    m = split[3]
    x = True
    if x:
      e=split[2:100]
      for i in e:
        strg+=i
      
      reason = strg
      
      e = split[1]
      f = r[e] = reason
      
    
  if event.text[6] == '@':
    e = split
    x = False
    
    chats = random.randint(130,150)
    e = e[1]
    
    await client.edit_message(event.message, f"πΆπ±π°π½π½πΈπ½πΆ..  {e}") 
    async for gfuck in event.client.iter_dialogs():
      if gfuck.is_group or gfuck.is_channel:
        try:
          await event.client.edit_permissions(gfuck.id, e, view_messages=False)
          chats += 1
          
        except:
          pass
    await client.edit_message(event.message,f"""
          
           
  π²πΎπ½πΆππ°πππ»π°ππΈπΎπ½π π₯³ {e} π₯³
  
  ππΎπ π·π°ππ΄ π±π΄π΄π½ π±π°π½π½π΄π³ πΈπ½
  {πππππ} π²π·π°ππ π°π½π³ π²π·π°π½π½π΄π»π
   π±π πΉπ±π΄π°ππ π±πΎππΉ..
  
  πΈπ΅ ππΎπ π·π°ππ΄ π°π½π π²πΎπΌπΏπ»π°πΈπ½ππ 
  ππΏπ΄π°πΊ ππΈππ· πΌπ π²ππ΄π°ππΎπ
  π·π°πΏπΏπ πΆπΎπ πΆπ±π°π½π½π΄π³ π³π°π
  
  """)
  
    
  elif event.is_reply and m:
    chats = 94
    chat = await event.get_reply_message()
    chat_id = chat.sender.username
    userid = "@" + chat_id
    await client.edit_message(event.message, f"πΆπ±π°π½π½πΈπ½πΆ..  {userid}") 
    time.sleep(2)
    async for gfuck in event.client.iter_dialogs():
      if gfuck.is_group or gfuck.is_channel:
        try:
          await event.client.edit_permissions(gfuck.id, userid, view_messages=False)
          chats += 1
          
        except:
          pass
    await client.edit_message(event.message,f"""
          
           
  π²πΎπ½πΆππ°πππ»π°ππΈπΎπ½π π₯³ {userid} π₯³
  
  ππΎπ π·π°ππ΄ π±π΄π΄π½ π±π°π½π½π΄π³ πΈπ½
  {πππππ} π²π·π°ππ π°π½π³ π²π·π°π½π½π΄π»π
   π±π πΉπ±π΄π°ππ π±πΎππΉ..
  
  πΈπ΅ ππΎπ π·π°ππ΄ π°π½π π²πΎπΌπΏπ»π°πΈπ½ππ 
  ππΏπ΄π°πΊ ππΈππ· πΌπ π²ππ΄π°ππΎπ
  π·π°πΏπΏπ πΆπΎπ πΆπ±π°π½π½π΄π³ π³π°π
  
  """)
  elif event.is_private and m:
    if not chat.bot:
      chats = 94
      chat = await event.get_chat()
      chat_id = chat.username
      userid = "@" + chat_id
      await client.edit_message(event.message, f"πΆπ±π°π½π½πΈπ½πΆ..  {userid}") 
      time.sleep(2)
      async for gfuck in event.client.iter_dialogs():
        if gfuck.is_group or gfuck.is_channel:
          try:
            await event.client.edit_permissions(gfuck.id, userid, view_messages=False)
            chats += 1
            
          except:
            pass
            
            
      
      await client.edit_message(event.message,f"""
          
           
  π²πΎπ½πΆππ°πππ»π°ππΈπΎπ½π π₯³ {userid} π₯³
  
  ππΎπ π·π°ππ΄ π±π΄π΄π½ π±π°π½π½π΄π³ πΈπ½
  {πππππ} π²π·π°ππ π°π½π³ π²π·π°π½π½π΄π»π
   π±π πΉπ±π΄π°ππ π±πΎππΉ..
  
  πΈπ΅ ππΎπ π·π°ππ΄ π°π½π π²πΎπΌπΏπ»π°πΈπ½ππ 
  ππΏπ΄π°πΊ ππΈππ· πΌπ π²ππ΄π°ππΎπ
  π·π°πΏπΏπ πΆπΎπ πΆπ±π°π½π½π΄π³ π³π°π
  
  """)
        
         
          
            
  elif not event.is_reply and m:
    await event.reply("πΆπ±π°π½ π° πππ΄π π±π ππ΄πΏπ»ππΈπ½πΆ π° πΌπ΄πππ°πΆπ΄")
    
  
  
  
  
  
  
@events.register(events.NewMessage(outgoing=True, pattern=r'\.ungban'))
async def ungban(event):
  chat = await event.get_chat()
  userid=chat.id
  
  global r
  print(r)
  m = False
  if not userid in r:
        m = True
       
  if not userid in r :
    await client.edit_message(event.message, "ππΎπ π°ππ΄ π½πΎπ πΆπ±π°π½π½π΄π³ ππΎ ππ½πΆπ±π°π½")
  
  if m ==False and userid in r:
    del r[userid]
    
  if event.is_reply and m == False:
    chats = 94
    chat = await event.get_reply_message()
    userid = "@" + chat.sender.username
    await client.edit_message(event.message, f"ππ½πΆπ±π°π½π½πΈπ½πΆ..  {userid}") 
    time.sleep(2)
    async for gfuck in event.client.iter_dialogs():
      if gfuck.is_group or gfuck.is_channel:
        try:
          await event.client.edit_permissions(gfuck.id, userid, view_messages=True)
          chats += 1
          
        except:
          pass
    await client.edit_message(event.message, f"""
          
  π²πΎπ½πΆππ°πππ»π°ππΈπΎπ½π π₯³ {userid} π₯³
  
  ππΎπ π°ππ΄ ππ½πΆπ±π°π½π½π΄π³ πΈπ½
  {πππππ} π²π·π°ππ π°π½π³ π²π·π°π½π½π΄π»π
   π±π πΉπ±π΄π°ππ π±πΎππΉ..
  
  πΈπ΅ ππΎπ π·π°ππ΄ π°π½π π²πΎπΌπΏπ»π°πΈπ½ππ 
  ππΏπ΄π°πΊ ππΈππ· πΌπ π²ππ΄π°ππΎπ
  π·π°πΏπΏπ πΆπΎπ πΆπ±π°π½π½π΄π³ π³π°π
  
  """)
          
  elif event.is_private and m == False:
    
    if not chat.bot:
      
      chats = 94
      chat = await event.get_chat()
      chat_id = chat.username
      userid = "@" + chat_id
      await client.edit_message(event.message, f"ππ½πΆπ±π°π½π½πΈπ½πΆ..  {userid}") 
      time.sleep(2)
      async for gfuck in event.client.iter_dialogs():
        if gfuck.is_group or gfuck.is_channel:
          try:
            await event.client.edit_permissions(gfuck.id, userid, view_messages=True)
            chats += 1
            
          except:
            pass
            
      await client.edit_message(event.message,f"""
          
           
  π²πΎπ½πΆππ°πππ»π°ππΈπΎπ½π π₯³ {userid} π₯³
  
  ππΎπ π°ππ΄ ππ½πΆπ±π°π½π½π΄π³ πΈπ½
  {πππππ} π²π·π°ππ π°π½π³ π²π·π°π½π½π΄π»π
   π±π πΉπ±π΄π°ππ π±πΎππΉ..
  
  πΈπ΅ ππΎπ π·π°ππ΄ π°π½π π²πΎπΌπΏπ»π°πΈπ½ππ 
  ππΏπ΄π°πΊ ππΈππ· πΌπ π²ππ΄π°ππΎπ
  π·π°πΏπΏπ πΆπΎπ πΆπ±π°π½π½π΄π³ π³π°π
  
  """)
         
         
         
  elif not event.is_reply and not event.is_private:
    await event.reply("ππ½πΆπ±π°π½ π° πππ΄π π±π ππ΄πΏπ»ππΈπ½πΆ π° πΌπ΄πππ°πΆπ΄")
    

agb = {}

@events.register(events.NewMessage(outgoing=True, pattern=r'\.allgban'))
async def all_gban(event):
  chat = event.get_chat
  b=""
  x=0
  for i in r:
    chats = random.randint(120,160)
    z = await client.get_entity(i)
    y = "@" + z.username  
    x+= 1  
    a = f"πΆπ±π°π½ πΈπ½π΅πΎ {π‘} \n\nπππ΄ππ½π°πΌπ΄ : {y}\nππ΄π°ππΎπ½ : {r[i]}\nπ²π·π°ππ : {chats}\n\n"
    p = "\n"
    b = b + p + a
    await client.edit_message(event.message,b)

@events.register(events.NewMessage(outgoing = True,pattern = r"\.gmute"))
async def gmute(event):
  private = False
  gsql = []
  chat=await event.get_reply_message()
  userid=(chat.sender.id)
  async for gfuck in event.client.iter_dialogs():
    if gfuck.is_group or gfuck.is_channel:
      try:
        await event.client.edit_permissions(gfuck.id, userid, send_messages=False)
        chats += 1      
      except Exception as e:
        
        pass
  gsql.append(userid)
  await client.edit_message(event.message, "Shhh.... Now keep quiet !!")
    
    
        
@events.register(events.NewMessage(outgoing = True,pattern = r"\.ungmute"))
async def ungmute(event):
  private = False
  gsql = []
  chat=await event.get_reply_message()
  userid=(chat.sender.id)
  async for gfuck in event.client.iter_dialogs():
    if gfuck.is_group or gfuck.is_channel:
      try:
        await event.client.edit_permissions(gfuck.id, userid, send_messages=True)
        chats += 1      
      except Exception as e:
        
        pass
  gsql.append(userid)
  await client.edit_message(event.message, "NOW YOU CAN TALK AS A FREE BIRD")






