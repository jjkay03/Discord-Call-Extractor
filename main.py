from modules import *  # Import all custom modules in /modules dir
from datetime import datetime
import colorama

group_link = "https://discord.com/channels/@me/974077775638069338"
db_name = "974077775638069338"
timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

# Initialize colorama
colorama.init()

# Append timestamp to make the DB name unique
db_filename = f"data/database/{db_name}-{timestamp}.db"

driver = setup_discord_browser()
navigate_to_link(driver, group_link)

# Setup database with unique name
conn = setup_database(db_filename)

# Let the user choose when to start
input(colorama.Fore.GREEN + "Press Enter to start tracking Discord calls..." + colorama.Fore.RESET)

# End
input(colorama.Fore.LIGHTRED_EX + "END -- END -- END -- END" + colorama.Fore.RESET)
