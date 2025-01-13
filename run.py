import os
import yaml
from app import create_app

# Load configuration from config.yaml
def load_config():
    config_path = os.path.join(os.getcwd(), "config.yaml")  # Ensure the path is correct
    if os.path.exists(config_path):
        with open(config_path, "r") as config_file:
            config = yaml.safe_load(config_file)
            return config
    else:
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

# Print the current working directory to confirm the app is running from the right place
print(f"Current working directory: {os.getcwd()}")

# Load configuration
config = load_config()

# Create the Flask app and pass the configuration
app = create_app(config=config)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode
