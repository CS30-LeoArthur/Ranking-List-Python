# Ranking List Assignment
ranking_list = []

def main():
    # Python Menu Loop 
    done = False
    while not done:
        # Print Main Menu
        print("\n***MAIN MENU***")
        print ("* 1: Print List")
        print ("* 2: Add Item to End")
        print ("* 3: Remove Last Item")
        print("* 4: Insert at Position")
        print("* 5: Remove at Position")
        print("* 6: Move to Position")
        print("* 7: Edit Item")
        print ("* 8: Exit")

        # Get Menu Selection from user
        selection = input("\nEnter Option #: ")

        # Take Action Based on Menu Selection
        # Print list
        if selection == "1":
            print("\nRANK LIST")
            if len(ranking_list) == 0:
                    print("No Items in the Rank List")
            else:
                for i in range(len(ranking_list)):
                    print(f"{str(i + 1)}: {ranking_list[i]}")
        # Add item to end
        elif selection == "2":
            print("\nADD ITEM TO END")
            new_item = input("Enter item: ")
            ranking_list.append(new_item)

            print("\nRANK LIST")
            for i in range(len(ranking_list)):
                print(f"{str(i + 1)}: {ranking_list[i]}")
        # Remove last item
        elif selection == "3":
            print("REMOVE LAST ITEM")
            print(f"{ranking_list[-1]} has been removed from the end of the list.")
            ranking_list.pop()

            print("\nRANK LIST")
            for i in range(len(ranking_list)):
                print(f"{str(i + 1)}: {ranking_list[i]}")
        # Insert item
        elif selection == "4":
            print("INSERT ITEM")
            position = input("Insert Position: ")
            item = input("Item to Insert: ")
            ranking_list.append[int(position - 1)](item)

            print("\nRANK LIST")
            for i in range(len(ranking_list)):
                print(f"{str(i + 1)}: {ranking_list[i]}")
        elif selection == "5":
            print("optrion 5")
        elif selection == "6":
            print("option 6")
        elif selection == "7":
            print("option 7")
        elif selection == "8":
            done = True

if __name__ == "__main__":
    main()
