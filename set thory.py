def perform_set_operation():
    # Get input sets from the user
    set1 = set(input("Enter the first set (comma-separated elements): ").split(','))
    set2 = set(input("Enter the second set (comma-separated elements): ").split(','))

    while True:
        print("\nChoose a set operation:")
        print("1. Union")
        print("2. Intersection")
        print("3. Set Difference (Set1 - Set2)")
        print("4. Set Difference (Set2 - Set1)")
        print("5. Symmetric Difference")
        print("6. Check if Set1 is a subset of Set2")
        print("7. Check if Set2 is a subset of Set1")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            result = set1.union(set2)
        elif choice == '2':
            result = set1.intersection(set2)
        elif choice == '3':
            result = set1.difference(set2)
        elif choice == '4':
            result = set2.difference(set1)
        elif choice == '5':
            result = set1.symmetric_difference(set2)
        elif choice == '6':
            result = set1.issubset(set2)
        elif choice == '7':
            result = set2.issubset(set1)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        print("Result: ", result)

if __name__ == "__main__":
    perform_set_operation()