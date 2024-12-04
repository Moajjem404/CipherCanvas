from PIL import Image
import os
import platform
from colorama import Fore, Style, init


init(autoreset=True)

def clear_terminal():
    """Clear the terminal screen based on the operating system."""
    if platform.system().lower() == 'windows':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/Termux

def embed_message(image_path, secret_message, output_path):
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')

        binary_message = ''.join(format(ord(char), '08b') for char in secret_message) + '1111111111111110'
        binary_iter = iter(binary_message)

        # Get pixel data
        pixels = list(img.getdata())
        new_pixels = []

        for pixel in pixels:
            new_pixel = []
            for color in pixel:
                try:
                    bit = next(binary_iter)
                    new_pixel.append((color & ~1) | int(bit))
                except StopIteration:
                    new_pixel.append(color)
            new_pixels.append(tuple(new_pixel))

        new_img = Image.new(img.mode, img.size)
        new_img.putdata(new_pixels)

        new_img.save(output_path, format='PNG')
        print(f"{Fore.GREEN}{Style.BRIGHT}Message embedded successfully! Saved to {output_path}")
    except Exception as e:
        print(f"{Fore.RED}{Style.BRIGHT}Error: {e}")
        
    prompt_continue_exit()

def extract_message(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')
        pixels = list(img.getdata())
        binary_message = ""
        for pixel in pixels:
            for color in pixel:
                binary_message += str(color & 1)
        binary_chunks = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
        message = ""
        for byte in binary_chunks:
            if byte == "11111110":
                break
            try:
                message += chr(int(byte, 2)) 
            except ValueError:
                break
        message = message.rstrip("\x00")
        print(f"\n{Style.BRIGHT}{Fore.CYAN}Extracted Message:\n{Style.BRIGHT}{Fore.YELLOW}{message}")
    except Exception as e:
        print(f"{Fore.RED}{Style.BRIGHT}Error: {e}")
    prompt_continue_exit()
    
def prompt_continue_exit():
    """Prompt the user to continue or exit."""
    while True:
        user_input = input(f"\n{Fore.CYAN}Please press Enter to continue or '0' to exit: ").strip()
        if user_input == "0":
            print(f"{Fore.RED}{Style.BRIGHT}Exiting... Goodbye!")
            exit()
        elif user_input == "":
            clear_terminal()
            print_main_menu()
            break
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid input. Please press Enter to continue or '0' to exit.")

def print_main_menu():
    """Print the main menu."""
    print(f"\n{Style.BRIGHT}{Fore.MAGENTA}==============================")
    print(f"{Fore.CYAN}{Style.BRIGHT}Welcome to the {Fore.MAGENTA}{Style.BRIGHT}CipherCanvas{Fore.CYAN}{Style.BRIGHT} Tool!\n")
    print(f"{Fore.YELLOW}{Style.BRIGHT}Tool Name   : {Fore.MAGENTA}{Style.BRIGHT}CipherCanvas")
    print(f"{Style.BRIGHT}{Fore.YELLOW}Tool Author : {Fore.GREEN}ShadowGlint")
    print(f"{Style.BRIGHT}{Fore.YELLOW}GitHub      : {Fore.GREEN}Moajjem404")
    print(f"{Style.BRIGHT}{Fore.YELLOW}Version     : {Fore.WHITE}1.0.0\n")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}==============================\n")
    print(f"{Style.BRIGHT}{Fore.CYAN}CipherCanvas: {Fore.YELLOW}Embed and extract secret messages within images for secure communication.\n")
    print(f"{Style.BRIGHT}{Fore.GREEN}1. Embed a message into an image")
    print(f"{Style.BRIGHT}{Fore.YELLOW}2. Extract a message from an image")
    print(f"{Style.BRIGHT}{Fore.RED}0. Exit\n")

def main():
    while True:
        clear_terminal()
        print_main_menu()
        
        choice = input(f"{Fore.YELLOW}{Style.BRIGHT}Enter your choice {Fore.WHITE}(1/2/0): ")

        if choice == "1":
            print(f"\n{Fore.YELLOW}---{Fore.CYAN} Embed a message {Fore.YELLOW}---")
            image_path = input(f"{Style.BRIGHT}{Fore.YELLOW}Enter the image file path: {Fore.WHITE}")
            secret_message = input(f"{Style.BRIGHT}{Fore.YELLOW}Enter the secret message to embed: {Fore.WHITE}")
            output_path = input(f"{Style.BRIGHT}{Fore.YELLOW}Enter the output image file path: {Fore.WHITE}")
            
            embed_message(image_path, secret_message, output_path)
        
        elif choice == "2":
            print(f"\n{Fore.YELLOW}--- {Fore.CYAN}Extract a message {Fore.YELLOW}---")
            image_path = input(f"{Style.BRIGHT}{Fore.YELLOW}Enter the image file path: {Fore.WHITE}")
            
            extract_message(image_path)

        elif choice == "0":
            print(f"{Fore.RED}{Style.BRIGHT}Exiting... Goodbye!")
            exit()
        
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid choice. Please select either 1, 2, or 0.")

if __name__ == "__main__":
    main()
