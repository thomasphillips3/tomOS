import json
import os

class ConfigManager:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as f:
                    config = json.load(f)
                    return config
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON config file: {e}")
                return self.default_config()
        else:
            print("Configuration file not found. Loading default configuration.")
            config = self.default_config()
            self.save_config(config)
            return config

    def default_config(self):
        return {
            "version": "0.1.0",
            "kernel": {
                "welcome_message": "What up doe!",
                "commands": ["help", "exit", "version"]
            },
            "scheduler": {
                "quantum": 1,
                "max_processes": 10
            },
            "memory": {
                "size": 1024
            }
        }

    def save_config(self, config=None):
        if config is None:
            config = self.config
        try:
            with open(self.config_file, "w") as f:
                json.dump(config, f, indent=4)
            print("Configuration saved successfully.")
        except Exception as e:
            print(f"Error saving configuration: {e}")

    def get(self, key, default=None):
        keys = key.split(".")
        value = self.config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value

    def set(self, key, value):
        keys = key.split(".")
        d = self.config
        for k in keys[:-1]:
            if k not in d or not isinstance(d[k], dict):
                d[k] = {}
            d = d[k]
        d[keys[-1]] = value
        self.save_config()
