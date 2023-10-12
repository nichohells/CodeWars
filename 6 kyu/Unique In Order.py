Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.


def unique_in_order(sequence):
    lista = []
    for char in sequence:
        if not lista or char != lista[-1]:
            lista.append(char)
    return lista








Let's delve deeper into the condition if not lista or char != lista[-1] and why it's used to filter out consecutive repeated elements.




# In the context of this code, the goal is to extract unique elements from a sequence (either a string or a list) while preserving their original order. The condition if not lista or char != lista[-1] serves two purposes:




# Checking if 'lista' is empty: The not lista part of the condition checks whether the lista list is empty. If lista is empty, it means that we haven't added any elements to it yet. In this case, the current character (char) is the first element we encounter, so it is, by definition, unique.




# Checking if the current 'char' is different from the last element in 'lista': The char != lista[-1] part of the condition checks whether the current character (char) is different from the last element in the lista list. If it's different, it means the current character is not the same as the previously encountered character, which makes it unique in the context of consecutive elements.




# Here's why we need to check for differences from the last element in lista:




# If consecutive elements in the input sequence are the same, we only want to include one of them in the final list. We don't want duplicates to be added.




# By checking if char is different from the last element in lista, we ensure that we only add unique elements to lista. If char is the same as the last element in lista, it implies that we're encountering a repeated element, and we skip adding it to lista.




# So, this condition allows us to filter out consecutive repeated elements, ensuring that we only include unique elements in the output list while maintaining the original order of elements in the input sequence.