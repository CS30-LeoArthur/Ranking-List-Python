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
            print("\nINSERT ITEM")
            position_insert_input = int(input("Insert Position: "))
            new_item = input("Enter item: ")
            position_insert = position_insert_input - 1
            ranking_list.insert(position_insert, new_item)


            print("\nRANK LIST")
            for i in range(len(ranking_list)):
                print(f"{str(i + 1)}: {ranking_list[i]}")
        # Remove Item
        elif selection == "5":
            print("\nREMOVE ITEM")
            # Get user input
            position_remove_input = int(input("Insert Position: "))
            # Change user input to index of list
            position_remove = position_remove_input - 1
            # Print what was removed at what position
            print(f"{ranking_list[position_remove]} removed from position {str(position_remove_input)}")
            ranking_list.pop(position_remove)

            print("\nRANK LIST")
            for i in range(len(ranking_list)):
                print(f"{str(i + 1)}: {ranking_list[i]}")
        # Move to Position
        elif selection == "6":
            print("\nMOVE TO POSITION")
            # Get user input
            move_item_from_input = int(input("Move Item from: "))
            move_item_to_input = int(input("Move Item to : "))
            # Change user input to index of list
            move_item_from = move_item_from_input - 1
            move_item_to = move_item_to_input - 1
            # Move the item from one part of the list to another
            moved_item = ranking_list.pop(move_item_from)
            ranking_list.insert(move_item_to, moved_item)

            print("\nRANK LIST")
            for i in range(len(ranking_list)):
                print(f"{str(i + 1)}: {ranking_list[i]}")
        # Edit Item
        elif selection == "7":
            print("\nEDIT ITEM")
            edit_position_input = int(input("Enter Position: "))
            edit_item_input = input("Replace with: ")
            # Change user input to index of list
            edit_item_index = edit_position_input - 1
            # Edit the list
            


            print("\nRANK LIST")
            for i in range(len(ranking_list)):
                print(f"{str(i + 1)}: {ranking_list[i]}")
        elif selection == "8":
            done = True

if __name__ == "__main__":
    main()
