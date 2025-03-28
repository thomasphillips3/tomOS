class Kernel:
    def __init__(self):
        self.running = True
        self.commands = {
            'help': self.help,
            'exit': self.exit
        }
        print("What up doe!")
        print("Welcome to TomOS Kernel!")
        print("Type 'help' for a list of commands.")

    def help(self):
        print("Available commands:")
        for command in self.commands:
            print(f" - {command}")

    def exit(self):
        print("Shutting down TomOS Kernel.")
        self.running = False

    def run(self):
        while self.running:
            cmd = input("pyos> ").strip().lower()
            if cmd in self.commands:
                self.commands[cmd]()
            else:
                print("Unknown command. Type 'help' for a list of available commands.")

if __name__ == "__main__":
    kernel = Kernel()
    kernel.run()