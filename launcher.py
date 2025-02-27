from colorama import Fore
import os

ascii = f"""
{Fore.CYAN}
 ______  _______  _______   _____   __   __
  ____/  |______  |______  |     |    \_/  
 /_____  |______  |        |_____|     |   
{Fore.RESET}                                          
"""

def run_views():
    os.system('python modules/views.py')

def run_favorites():
    os.system('python modules/favorites.py')

def run_likes():
    os.system('python modules/hearts.py')

def main():
    print(f"[{Fore.CYAN}?{Fore.RESET}] Choose an option:")
    print()
    print(f"[{Fore.CYAN}1{Fore.RESET}] Views")
    print(f"[{Fore.CYAN}2{Fore.RESET}] Favorites")
    print(f"[{Fore.CYAN}3{Fore.RESET}] Likes")
    print()
    
    choice = input(f"[{Fore.CYAN}>{Fore.RESET}] Enter Option: ")
    
    if choice == '1':
        run_views()
    elif choice == '2':
        run_favorites()
    elif choice == '3':
        run_likes()
    else:
        print(f"[{Fore.RED}!{Fore.RESET}] Invalid choice.")
        main()

if __name__ == "__main__":
    os.system("cls && title Zefoy Tool / github.com/@xRei77")
    print(ascii)
    main()
