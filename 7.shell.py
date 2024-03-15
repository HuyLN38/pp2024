import subprocess

def run_shell_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)

        # Check if the command executed successfully
        if result.returncode == 0:
            # Print the output of the shell command
            print("\033[1;37;40m" + result.stdout)
        else:
            # Print the error message if the command failed
            print("\033[1;31;40m" + result.stderr)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

while True:
    user_input = input("\033[1;32mEnter a command: ")
    if user_input.lower() == "exit":
        break
    run_shell_command(user_input)