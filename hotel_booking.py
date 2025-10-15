import sys
import importlib

def load_config(env):
    try:
        config = importlib.import_module(f'config.{env}_config')
        return config
    except ModuleNotFoundError:
        print(f"Configuration for {env} not found!")
        sys.exit(1)

def book_room(customer_name, room_type):
    print(f"Booking a {room_type} room for {customer_name}.")

def main():
    # Select environment from argument or default to 'dev'
    env = sys.argv[1] if len(sys.argv) > 1 else 'dev'
    config = load_config(env)
    
    # Show environment-specific details
    print(f"Running in {env.upper()} environment")
    print(f"Using database: {config.DATABASE_URL}")
    print(f"API Key: {config.API_KEY}")
    print(f"Debug mode: {config.DEBUG}")
    
    # Example booking
    customer_name = "John Doe"
    room_type = "Single"
    book_room(customer_name, room_type)

if __name__ == "__main__":
    main()
