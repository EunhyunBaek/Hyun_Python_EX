import re

list =  """
Primary email : skyun.nam@gmail.com
Secondary email : litmuscube@gmail.com
"""
result_list = re.findall(r"(\w+[\w\.]*)@(\w+[\w\.]*)\.([A-Za-z]+)", list)
print (result_list)
for result in result_list:
    print (result)