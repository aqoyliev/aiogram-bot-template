from environs import Env

# Use the environs library
env = Env()
env.read_env()

# Read the following from the .env file
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # List of admins
IP = env.str("ip")  # Hosting IP address
