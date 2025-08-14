print('hello world')

#LESSON 1 
#TASK 1
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
snake_case = "max_value_of_array"
camel_case = snake_to_camel(snake_case)
print(camel_case)  

# TASK 2
def remove_duplicates_preserve_order(lst):
     seen = set()
     return [x for x in lst if not (x in seen or seen.add(x))]
original_list = [1, 2, 3, 2, 4, 3, 5, 6, 1]
unique_list = remove_duplicates_preserve_order(original_list)
print(unique_list)  

# TASK 3
def top_three_sales_months(sales):
    indexed_sales = [(index, value) for index, value in enumerate(sales)]
    sorted_sales = sorted(indexed_sales, key=lambda x: x[1], reverse=True)
    top_three = [month[0] for month in sorted_sales[:3]]
    return tuple(top_three)
yearly_sales = (120, 140, 100, 80, 200, 160, 90, 110, 150, 130, 170, 190)
best_months = top_three_sales_months(yearly_sales)
print(best_months)  