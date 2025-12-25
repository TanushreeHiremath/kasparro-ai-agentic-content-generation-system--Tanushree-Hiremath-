from orchestrator import run_faq, run_description, run_comparison, run_all

def menu():
    while True:
        print("\n=== Kasparro Content Generator ===")
        print("1️.  Generate FAQ")
        print("2️. Generate Product Page")
        print("3️.  Generate Comparison Page")
        print("4️.  Generate ALL")
        print("5️.  Exit")
        choice = input("Choose: ")

        if choice == "1": run_faq()
        elif choice == "2": run_description()
        elif choice == "3": run_comparison()
        elif choice == "4": run_all()
        elif choice == "5": break
        else: print(" Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
