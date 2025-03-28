from config_manager import ConfigManager
import os

class Kernel:
    def __init__(self):
        self.running = True
        self.config_manager = ConfigManager()
        self.version_info = self.config_manager.get("version", "0.0.0")
        self.commands = {
            'help': self.help,
            'exit': self.exit,
            'version': self.version,
        }
        welcome_message = self.config_manager.get("kernel.welcome_message", "What up doe!")
        print(welcome_message)
        print(f"tomOS Kernel v {self.version_info}")
        print("Type 'help' for a list of commands.")

    def help(self):
        print("Available commands:")
        for command in self.commands:
            print(f" - {command}")

    def exit(self):
        print("Shutting down tomOS Kernel.")
        self.running = False
    
    def version(self):
        print(f"tomOS Kernel version {self.version_info}")

    def run(self):
        while self.running:
            cmd = input("tomos> ").strip().lower()
            if cmd in self.commands:
                self.commands[cmd]()
            else:
                print("Unknown command. Type 'help' for a list of available commands.")

if __name__ == "__main__":
    kernel = Kernel()
    kernel.run()