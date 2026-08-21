test_list = ["one","two","three"]

if test_list:
    print("list not empty")
else:
    print("empty list")

if test_list:
    find_index = test_list.index("two")
    deleted_item = test_list.pop(find_index)
    print (f"found_index= {find_index}, deleted_item= {deleted_item!r}")
    # test_list.remove("two")

print(test_list)
