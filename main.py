#Get Inputs anf Remove Extra Spaces
first_name = input("Enter first name: ").strip()
last_name= input("Enter last name: ").strip()
section = input("Enter section: ").strip()
subject = input("Enter favorite subject: ").strip()

#Build and Format Full Name
full_name = first_name + "" + last_name
title_name = full_name.title()
upper_name = full_name.upper()

#Format fopr The Other Fields
section_upper = section.upper()
subject_title = subject.title()

#Count Characters
char_count = len(full_name)

#Display Results
print("\nFormatted Output:")
print("Name:", title_name)
print("Name Code:", upper_name)
print("Section:", section_upper)
print("Favorite subject:", subject_title)
print("Character Count:", char_count)
