total_jumping_jacks = 100
remaining_jumping_jacks = total_jumping_jacks

while remaining_jumping_jacks > 0:
    print(f"{remaining_jumping_jacks} jumping jacks remaining.")
    if remaining_jumping_jacks >= 10:
        perform = input("Perform 10 jumping jacks? (yes/no): ")
        if perform.lower() == "no" or perform.lower() == "n":
            tired = input("Are you tired? (yes/no): ")
            if tired.lower() == "yes" or tired.lower() == "y":
                skip = input("Do you want to skip the remaining sets? (yes/no): ")
                if skip.lower() == "yes" or skip.lower() == "y":
                    print(f"You completed a total of {total_jumping_jacks - remaining_jumping_jacks} jumping jacks.")
                    break
                else:
                    continue
        else:
            remaining_jumping_jacks -= 10
    else:
        perform = input(f"Perform {remaining_jumping_jacks} jumping jacks? (yes/no): ")
        if perform.lower() == "no" or perform.lower() == "n":
            tired = input("Are you tired? (yes/no): ")
            if tired.lower() == "yes" or tired.lower() == "y":
                skip = input("Do you want to skip the remaining sets? (yes/no): ")
                if skip.lower() == "yes" or skip.lower() == "y":
                    print(f"You completed a total of {total_jumping_jacks - remaining_jumping_jacks} jumping jacks.")
                    break
                else:
                    continue
        else:
            print("Congratulations! You completed the workout.")
            break
