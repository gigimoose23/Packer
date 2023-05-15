print("[\033[34minfo\033[0m] Would you like to install Packer? ([\033[34my\033[0m]/\033[31mn\033[0m])")
response = input("")
import platform

def install(os):
    print("Downloading module")
    





if response.lower() == "y":
    print("\033[32mInstalling Packer...\033[0m")
    install(platform.system())
elif response.lower() == "n":
    print("\033[31mQuitting...\033[0m")
else:
    print("\033[31mInvalid response.\033[0m Please enter either 'y' or 'n'.")
