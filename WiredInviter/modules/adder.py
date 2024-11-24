from telethon.tl.functions.channels import InviteToChannelRequest 
from telethon.tl.types import InputPeerUser


async def adder(client, source_group, target_group):
    try:
        source = await client.get_entity(source_group) 
        target = await client.get_entity(target_group)
        participants = await client.get_participants(source_group)
        for user in participants: 
            try: 
                await client(InviteToChannelRequest(target, [InputPeerUser(user.id, user.access_hash)])) 
                print(f"Added: {user.id}") 
            except Exception as e: 
                print(f"Impossible adding {user.id}: {e}")
    except Exception as a:
        print("Error: ", a)