from settings import driver
import time
from selenium.webdriver.support.select import Select
driver.get("F:\selenium\Sandeep_Sir\scripts\HTML FILES\html1.html")
ref=driver.find_element_by_id("standard_car")
time.sleep(3)
opts=Select(ref)
op=opts.options
items=[]
# for item in op:
#     items.append(item.text)
# print(items)
# for i in items:
#     opts.select_by_visible_text(i)
# print(len(op))

# for i in range(len(op)):
#     op.select_by_index(i)
# for i in op:
#     print(i.text)

items=[item.text for item in op]
# for i in reversed(items):
#     opts.select_by_visible_text(i)

# for i in items[::-1]:
#     opts.select_by_visible_text(i)

# for i in range((len(items)-1),-1,-1):
#     opts.select_by_visible_text(items[i])

# for index,item, in enumerate(items):
#     opts.select_by_index(index)
#     time.sleep(1)


# dic={index:item for index,item in enumerate(items)}
# print(dic)

search_car="BMW"

for index,item in enumerate(items):
    if item==search_car:
        opts.select_by_visible_text(item)
        print(f"{item} is at index{index}")