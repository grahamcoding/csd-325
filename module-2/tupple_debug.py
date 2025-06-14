# Daniel Graham
# Date 4/19/25
# Week 5/Module 6.2 Assignment: File Management

print("Welcome to the Module 6.2 Assignment by Daniel Graham!")
print("Let's play with tuples!")

techtuple = (
    "Nvidia", "AMD", "Intel", "MSI", "Sony", "Microsoft", "SanDisk", "Apple", "Samsung", "Huawei",
    "Linksys", "Meta", "Synology", "TSMC", "IBM", "Cisco", "Adobe", "Qualcomm", "Nintendo", "ASUS"
)

def tupletry():
    print("\nWhich part of the assignment would you like to see?")
    print("1 to View the full list of tech companies in the tuple as a single statement")
    print("2 to Iterate through the collection using each value in the tuple")
    print("3 to Repeat the tuple in reverse with a different context")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        print("\nHere is the full list of tech companies:")
        print(techtuple)
    elif choice == "2":
        print("\nTech companies I know and admire:")
        for company in tech_tuple:
            print(f"- {company} is a well-known tech company.")
    elif choice == "3":
        print("\nLooking back through the list of tech companies in reverse:")
        for company in reversed(techtuple):
            print(f"- Have you ever used a product from {company}? They're everywhere!")
    else:
        print("\nInvalid input. Please choose 1, 2, or 3.")
        tupletry()

while True:
    tupletry()
    again = input("\nThank you for using Module 6.2! Wanna do it again? y/n: ").lower()
    if again != "y":
        print("\nThanks for exploring tech companies with me using tuples!")
        break
