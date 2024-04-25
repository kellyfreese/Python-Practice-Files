todo_list = []
done = False

print("Type 'done' at any time to exit")

while not done:
  new_item = input("What would you like to add to your to-do list?")
  if new_item == "done":
    done = True
  else:
    todo_list.append(new_item)

print(todo_list)
