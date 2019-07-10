#####################################################################
# List Iteration
#1
office_characters=["Michael", "Dwight", "Jim", "Pam", "Phyllis", "Stanley", "Creed", "Darryl", "Oscar", "Angela", "Kevin", "Kelly", "Meridith", "Andy"]

for character in office_characters:
    print(character + " is a  Dunder Mifflin employee.")
    
    

#####################################################################
#2
print("\n\n*****\n\n") #This is here to organize the console output

# sentence = "The Dunder Mifflin employees are:"
# for character in office_characters:
#     sentence += "\n"
#     sentence += character
    
# print(sentence)

#####################################################################
#3
print("\n\n*****\n\n") #This is here to organize the console output

begins_with_K = []
doesnt_begin_with_K = [] 

for character in office_characters:
    if character[0] == "K":
        begins_with_K.append(character)
    else:
        doesnt_begin_with_K.append(character)

# print("These characters' names begin with K:")
# print(begins_with_K)

# print("\nThese characters' names do not begin with K:")
# print(doesnt_begin_with_K)


####################################################################
## EXPERIMENT ##
# Create your own list and iterate through it.

    

    