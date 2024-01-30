def common_list(ls):
    element_count = {}
    
   
    for element in ls:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1


    common_elements = [element for element, count in element_count.items() if count > 1]
    
    return common_elements

result = common_list([1, 2, 2, 3, 3, 3])
print(result)



