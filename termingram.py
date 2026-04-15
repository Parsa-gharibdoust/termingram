from telethon import TelegramClient
from colorama import Fore, init
import time
import os
import sys


#   =============================== ///
#   www.parsagharibdoust.xyz
#   t.me/odin_developer
#   instagram.com/parsagharibdoust.xyz
#   github.com/parsa-gharibdoust
#   =============================== ///


init(autoreset=True)

if sys.platform.startswith('linux'):
    import locale
    locale.setlocale(locale.LC_ALL, 'fa_IR.UTF-8')
    os.environ['PYTHONIOENCODING'] = 'utf-8'

API_ID = 11111 # YOUR API_ID
API_HASH = "API_HASH" # Your API_HASH
SESSION_NAME = "session_eventg"

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def display_banner():
    clear_screen()
    print(Fore.GREEN + "+--------------------------------------+")
    print(Fore.GREEN + "|        Termingram By ODIN           |")
    print(Fore.GREEN + "+--------------------------------------+")
    time.sleep(1.5)
    clear_screen()
    print(Fore.CYAN + "www.parsagharibdoust.xyz")
    print(Fore.CYAN + "t.me/odin_developer")
    print(Fore.CYAN + "instagram.com/parsagharibdoust.xyz")
    print(Fore.CYAN + "github.com/parsa-gharibdoust")
    print(Fore.MAGENTA + "\n" + "=" * 50)
    print(Fore.YELLOW + "            MESSAGE COMMANDS")
    print(Fore.MAGENTA + "=" * 50)
    print(Fore.WHITE + "   1.  📝 [msg]           -> Send Message")
    print(Fore.WHITE + "   2.  📎 [fmsg]          -> Send File Message")
    print(Fore.WHITE + "   3.  🗑️  [del-msg]       -> Delete Message")
    print(Fore.WHITE + "   4.  ↩️  [fwrd-msg]      -> Forward Message")
    print(Fore.WHITE + "   5.  📌 [pin-msg]        -> Pin Message")
    print(Fore.WHITE + "   6.  📍 [unpin-msg]      -> Unpin Message")
    print(Fore.WHITE + "   7.  ⬇️  [dl-msg]         -> Download Message")
    print(Fore.WHITE + "   8.  💬 [chats]          -> Show All Chats")
    print(Fore.MAGENTA + "=" * 50)
    print(Fore.YELLOW + "            OTHER COMMANDS")
    print(Fore.MAGENTA + "=" * 50)
    print(Fore.WHITE + "   9.  👤 [me]             -> Your Information")
    print(Fore.WHITE + "   10. 🆔 [pid]            -> Get Peer ID")
    print(Fore.WHITE + "   11. 👥 [member-list]    -> List Group Members")
    print(Fore.WHITE + "   12. 🚫 [ban-user]       -> Ban User From Group")
    print(Fore.WHITE + "   13. 👑 [admin-rights]   -> Change Admin Rights")
    print(Fore.WHITE + "   14. 🖼️  [profile-pic]    -> Download Profile Picture")
    print(Fore.WHITE + "   15. 🚪 [leave]          -> Leave Group or Channel")
    print(Fore.WHITE + "   16. 📂 [opench]         -> Open & View Messages")
    print(Fore.WHITE + "   17. ❌ [exit]           -> Exit Program")
    print(Fore.MAGENTA + "=" * 50)

def print_header(title):
    clear_screen()
    print(Fore.CYAN + "+" + "-" * 48 + "+")
    print(Fore.CYAN + "|" + Fore.YELLOW + f"{title:^48}" + Fore.CYAN + "|")
    print(Fore.CYAN + "+" + "-" * 48 + "+\n")

def print_success(message):
    print(Fore.GREEN + "[OK] " + message)

def print_error(message):
    print(Fore.RED + "[ERROR] " + message)

def print_info(message):
    print(Fore.BLUE + "[INFO] " + message)

def print_warning(message):
    print(Fore.YELLOW + "[WARN] " + message)

def wait_for_enter():
    print(Fore.YELLOW + "\n" + "-" * 50)
    try:
        input(Fore.WHITE + "Press Enter to return to main menu...")
    except (UnicodeDecodeError, UnicodeEncodeError):
        input("Press Enter to return to main menu...")

def safe_print(text, color=Fore.WHITE):

    try:
        print(color + text)
    except UnicodeEncodeError:

        text = text.encode('ascii', 'ignore').decode('ascii')
        print(color + text)

async def show_all_chats():
    print_header("YOUR CHATS")
    print_info("Fetching your conversations...\n")
    
    chat_list = []
    async for dialog in client.iter_dialogs():
        chat_name = dialog.name if dialog.name else "Unknown"

        if len(chat_name) > 40:
            chat_name = chat_name[:40] + "..."
        
        chat_type = "User" if dialog.is_user else "Channel" if dialog.is_channel else "Group"
        chat_list.append(f"[{chat_type}] {chat_name:<42} -> ID: {dialog.id}")
    
    for i, chat in enumerate(chat_list, 1):
        if i % 2 == 0:
            safe_print(chat, Fore.LIGHTCYAN_EX)
        else:
            safe_print(chat, Fore.WHITE)
    
    print_success(f"Total chats loaded: {len(chat_list)}")
    wait_for_enter()
    await main()

async def open_chat(target_id, limit=50):
    try:
        print_header(f"MESSAGES FROM: {target_id}")
        print_info(f"Loading last {limit} messages...\n")
        print(Fore.MAGENTA + "-" * 70)
        
        message_count = 0
        async for message in client.iter_messages(target_id, limit=limit):
            timestamp = message.date.strftime("%Y-%m-%d %H:%M") if message.date else "No date"
            
            if message.text:
                message_text = message.text.replace('\n', ' ').strip()
                if len(message_text) > 60:
                    message_text = message_text[:60] + "..."
                safe_print(f"[{timestamp}] {message_text}", Fore.GREEN)
                safe_print(f"   -> Message ID: {message.id}", Fore.YELLOW)
            elif message.media:
                media_type = "MEDIA"
                if message.document:
                    media_type = "DOCUMENT"
                elif message.photo:
                    media_type = "PHOTO"
                elif message.video:
                    media_type = "VIDEO"
                elif message.audio:
                    media_type = "AUDIO"
                elif message.sticker:
                    media_type = "STICKER"
                safe_print(f"[{media_type}] [{timestamp}]", Fore.BLUE)
                safe_print(f"   -> Message ID: {message.id}", Fore.YELLOW)
            else:
                safe_print(f"[EMPTY MESSAGE] [{timestamp}]", Fore.RED)
                safe_print(f"   -> Message ID: {message.id}", Fore.YELLOW)
            
            message_count += 1
            if message_count < limit:
                print(Fore.MAGENTA + "  .")
        
        if message_count == 0:
            print_warning("No messages found in this chat.")
        else:
            print_success(f"Loaded {message_count} messages")
        
        print(Fore.MAGENTA + "-" * 70)
        
        save_choice = input(Fore.YELLOW + "\nSave messages to file? (yes/no): ").lower().strip()
        if save_choice == "yes" or save_choice == "y":
            await save_messages_to_file(target_id)
        
    except Exception as error:
        print_error(f"Failed to fetch messages: {error}")
    
    wait_for_enter()
    await main()

async def save_messages_to_file(target_id, limit=200):
    try:
        if not os.path.exists("chat_exports"):
            os.makedirs("chat_exports")
        
        filename = f"chat_exports/{target_id}_messages_{int(time.time())}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"MESSAGES EXPORT FROM: {target_id}\n")
            file.write(f"Export Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("=" * 70 + "\n\n")
            
            async for message in client.iter_messages(target_id, limit=limit):
                timestamp = message.date.strftime("%Y-%m-%d %H:%M") if message.date else "No date"
                if message.text:
                    file.write(f"[{timestamp}] {message.text} -> Message ID: {message.id}\n")
                elif message.media:
                    file.write(f"[{timestamp}] [MEDIA] -> Message ID: {message.id}\n")
                else:
                    file.write(f"[{timestamp}] [EMPTY] -> Message ID: {message.id}\n")
                file.write("-" * 50 + "\n")
        
        print_success(f"Messages saved to: {filename}")
    except Exception as error:
        print_error(f"Failed to save messages: {error}")

async def send_message(target_id, message_text):
    try:
        print_info(f"Sending message to {target_id}...")
        await client.send_message(target_id, message_text)
        print_success(f"Message sent successfully to {target_id}")
    except Exception as error:
        print_error(f"Failed to send message: {error}")
    time.sleep(1.5)
    await main()

async def send_file_message(target_id, file_path, caption_text=""):
    try:
        if not os.path.exists(file_path):
            print_error(f"File not found: {file_path}")
            time.sleep(1.5)
            await main()
            return
        
        print_info(f"Sending file to {target_id}...")
        if caption_text.strip() == "":
            await client.send_file(target_id, file_path)
        else:
            await client.send_file(target_id, file_path, caption=caption_text)
        print_success("File sent successfully.")
    except Exception as error:
        print_error(f"Failed to send file: {error}")
    time.sleep(1.5)
    await main()

async def delete_message(target_id, message_id):
    try:
        confirm = input(Fore.YELLOW + f"Are you sure you want to delete message {message_id}? (yes/no): ").lower().strip()
        if confirm != "yes" and confirm != "y":
            print_warning("Operation cancelled.")
            await main()
            return
        
        await client.delete_messages(target_id, message_id)
        print_success("Message deleted successfully.")
    except Exception as error:
        print_error(f"Failed to delete message: {error}")
    time.sleep(1.5)
    await main()

async def forward_message(source_id, message_id, destination_id):
    try:
        print_info(f"Forwarding message {message_id} from {source_id} to {destination_id}...")
        await client.forward_messages(destination_id, message_id, source_id)
        print_success("Message forwarded successfully.")
    except Exception as error:
        print_error(f"Failed to forward message: {error}")
    time.sleep(1.5)
    await main()

async def pin_message(target_id, message_id):
    try:
        await client.pin_message(target_id, message_id)
        print_success("Message pinned successfully.")
    except Exception as error:
        print_error(f"Failed to pin message: {error}")
    time.sleep(1.5)
    await main()

async def unpin_message(target_id, message_id):
    try:
        await client.unpin_message(target_id, message_id)
        print_success("Message unpinned successfully.")
    except Exception as error:
        print_error(f"Failed to unpin message: {error}")
    time.sleep(1.5)
    await main()

async def download_message(target_id, message_id, download_path="./downloads"):
    try:
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        message = await client.get_messages(target_id, ids=message_id)
        if message and message.media:
            await client.download_media(message, download_path)
            print_success(f"Media downloaded to {download_path}")
        else:
            print_warning("No media found in this message.")
    except Exception as error:
        print_error(f"Failed to download: {error}")
    time.sleep(1.5)
    await main()

async def get_my_info():
    me = await client.get_me()
    print_header("YOUR INFORMATION")
    print(Fore.CYAN + f"ID: {me.id}")
    print(f"First Name: {me.first_name if me.first_name else 'Not set'}")
    print(f"Last Name: {me.last_name if me.last_name else 'Not set'}")
    print(f"Username: @{me.username if me.username else 'Not set'}")
    print(f"Phone: {me.phone if me.phone else 'Not set'}")
    wait_for_enter()
    await main()

async def get_peer_id(username_or_id):
    try:
        entity = await client.get_entity(username_or_id)
        print_success(f"Peer ID: {entity.id}")
    except Exception as error:
        print_error(f"Error: {error}")
    time.sleep(1.5)
    await main()

async def list_group_members(group_id):
    try:
        print_header("GROUP MEMBERS")
        print_info("Fetching members...\n")
        
        member_count = 0
        async for user in client.iter_participants(group_id):
            first_name = user.first_name if user.first_name else ""
            last_name = user.last_name if user.last_name else ""
            full_name = f"{first_name} {last_name}".strip()
            if not full_name:
                full_name = "Unknown"
            
            safe_print(f"{full_name} -> ID: {user.id}", Fore.WHITE)
            member_count += 1
        
        print_success(f"Total members: {member_count}")
    except Exception as error:
        print_error(f"Failed to fetch members: {error}")
        time.sleep(1.5)
    
    wait_for_enter()
    await main()

async def ban_user(group_id, user_id):
    try:
        confirm = input(Fore.YELLOW + f"Are you sure you want to ban user {user_id}? (yes/no): ").lower().strip()
        if confirm != "yes" and confirm != "y":
            print_warning("Operation cancelled.")
            await main()
            return
        
        await client.kick_participant(group_id, user_id)
        print_success("User banned successfully.")
    except Exception as error:
        print_error(f"Failed to ban user: {error}")
    time.sleep(1.5)
    await main()

async def change_admin_rights(group_id, user_id, is_admin=True):
    try:
        await client.edit_admin(group_id, user_id, is_admin=is_admin)
        status = "granted" if is_admin else "revoked"
        print_success(f"Admin rights {status} successfully.")
    except Exception as error:
        print_error(f"Failed to change admin rights: {error}")
    time.sleep(1.5)
    await main()

async def download_profile_picture(user_id, save_path="./profile_pics"):
    try:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        user = await client.get_entity(user_id)
        photo_path = await client.download_profile_photo(user, file=os.path.join(save_path, f"{user.id}.jpg"))
        if photo_path:
            print_success(f"Profile picture saved to {photo_path}")
        else:
            print_warning("User has no profile picture.")
    except Exception as error:
        print_error(f"Failed to download profile picture: {error}")
    time.sleep(1.5)
    await main()

async def leave_chat(target_id):
    try:
        confirm = input(Fore.YELLOW + f"Are you sure you want to leave {target_id}? (yes/no): ").lower().strip()
        if confirm != "yes" and confirm != "y":
            print_warning("Operation cancelled.")
            await main()
            return
        
        await client.leave_chat(target_id)
        print_success("Left chat successfully.")
    except Exception as error:
        print_error(f"Failed to leave chat: {error}")
    time.sleep(1.5)
    await main()

async def main():
    display_banner()
    
    try:
        choice = input("Select an option: ").strip()
    except (UnicodeDecodeError, UnicodeEncodeError):
        choice = input("Select an option: ").strip()
    
    if choice == "1":
        target = input("Enter ID or Username: ")
        message_text = input("Enter your message: ")
        await send_message(target, message_text)
    
    elif choice == "2":
        target = input("Enter ID or Username: ")
        file_path = input("Enter file path: ")
        caption_text = input("Enter caption (optional): ")
        await send_file_message(target, file_path, caption_text)
    
    elif choice == "3":
        target = input("Enter ID or Username: ")
        try:
            msg_id = int(input("Enter message ID: "))
            await delete_message(target, msg_id)
        except ValueError:
            print_error("Invalid message ID. Must be a number.")
            time.sleep(1.5)
            await main()
    
    elif choice == "4":
        source = input("Enter source ID or Username: ")
        try:
            msg_id = int(input("Enter message ID: "))
            destination = input("Enter destination ID or Username: ")
            await forward_message(source, msg_id, destination)
        except ValueError:
            print_error("Invalid message ID. Must be a number.")
            time.sleep(1.5)
            await main()
    
    elif choice == "5":
        target = input("Enter ID or Username: ")
        try:
            msg_id = int(input("Enter message ID: "))
            await pin_message(target, msg_id)
        except ValueError:
            print_error("Invalid message ID. Must be a number.")
            time.sleep(1.5)
            await main()
    
    elif choice == "6":
        target = input("Enter ID or Username: ")
        try:
            msg_id = int(input("Enter message ID: "))
            await unpin_message(target, msg_id)
        except ValueError:
            print_error("Invalid message ID. Must be a number.")
            time.sleep(1.5)
            await main()
    
    elif choice == "7":
        target = input("Enter ID or Username: ")
        try:
            msg_id = int(input("Enter message ID: "))
            await download_message(target, msg_id)
        except ValueError:
            print_error("Invalid message ID. Must be a number.")
            time.sleep(1.5)
            await main()
    
    elif choice == "8":
        await show_all_chats()
    
    elif choice == "9":
        await get_my_info()
    
    elif choice == "10":
        identifier = input("Enter ID or Username: ")
        await get_peer_id(identifier)
    
    elif choice == "11":
        group = input("Enter group ID or Username: ")
        await list_group_members(group)
    
    elif choice == "12":
        group = input("Enter group ID or Username: ")
        user = input("Enter user ID or Username to ban: ")
        await ban_user(group, user)
    
    elif choice == "13":
        group = input("Enter group ID or Username: ")
        user = input("Enter user ID or Username: ")
        admin_status = input("Grant admin rights? (yes/no): ").lower() == "yes"
        await change_admin_rights(group, user, admin_status)
    
    elif choice == "14":
        user = input("Enter user ID or Username: ")
        await download_profile_picture(user)
    
    elif choice == "15":
        target = input("Enter group or channel ID/Username to leave: ")
        await leave_chat(target)
    
    elif choice == "16":
        target = input("Enter ID or Username to open chat: ")
        msg_limit = input("Number of messages to fetch (default 50): ").strip()
        try:
            limit = int(msg_limit) if msg_limit.isdigit() else 50
        except ValueError:
            limit = 50
        await open_chat(target, limit)
    
    elif choice == "17":
        print(Fore.YELLOW + "Exiting program... Goodbye!")
        await client.disconnect()
        exit()
    
    else:
        clear_screen()
        print_error("Invalid option. Please try again.")
        time.sleep(1.5)
        await main()

with client:
    client.loop.run_until_complete(main())

