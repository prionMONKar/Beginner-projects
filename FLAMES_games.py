def remove_matched_char(list1, list2):                       #Function to remove matched character
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]

                list1.remove(c)
                list2.remove(c)

                list3 = list1+['*']+list2                   #After removing the matched character let's concatenate the both lists and separate them with staric

                return [list3, True]                        #returning the concatenated list with True flag
            
                                                            #if no common characters is found return the concatenated list with False flag        
    list3 = list1 + ['*'] + list2
    return [list3, False]

if __name__ == "__main__":
    p1 = input("1st player's name: ")
    p1 = p1.lower()
    p1.replace(" ","")
    p1_list = list(p1)

    p2 = input("2nd player's name: ")
    p2 = p2.lower()
    p2.replace(" ","")
    p2_list = list(p2)

    proceed = True

    while proceed:
        return_list = remove_matched_char(p1_list, p2_list)
        concatenated_list = return_list[0]                  #taking out the concatenated list from return list
        proceed = return_list[1]                            #taking out the flag value from return list
        star_index = concatenated_list.index("*")           #finding the index of "*"

        p1_list = concatenated_list[:star_index]
        p2_list = concatenated_list[star_index+1:]

    count = len(p1_list) + len(p2_list)

    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]  #list of FLAMES acronym

    while len(result)>1:
        split_index = (count % len(result)-1)

        if split_index >= 0:                                #list slicing
            right = result[split_index+1:]
            left = result[:split_index]

            result = right + left                           #list concatenation
        else:
            result = result[:len(result) - 1]
    print("Relationship status :", result[0])
