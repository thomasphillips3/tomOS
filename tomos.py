import os

class Kernel:
    def __init__(self):
        self.running = True
        self.version_info = self.get_version()
        self.commands = {
            'help': self.help,
            'exit': self.exit,
            'version': self.version,
        }
        print("What up doe!")
        print("tomOS Kernel v", self.version_info)
        print("Type 'help' for a list of commands.")

    def get_version(self):
        # attempt to read the version from a VERSION file
        if os.path.exists("VERSION"):
            with open("VERSION", "r") as f:
                return f.read().strip()
        return "0.0.0"
    
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