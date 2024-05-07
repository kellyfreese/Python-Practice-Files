class PersonalAssistant:
  def __init__(self, todos, birthdays):
    
    self.todos = todos
    self.birthdays = birthdays

  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "No contact with that name!"

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      # Get the todo_item in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      print("Todo is not in list!")

  def get_todos(self):
    return self.todos

  def get_birthdays(self):
    return self.birthdays

  def get_birthday(self, name):
    if name in self.birthdays:
      return f"{name}'s birthday is on {self.birthdays[name]}."
    else:
      return "No contact with that name!"

  def add_birthday(self, name, date):
    if name in self.birthdays:
      return f"{name}'s birthday is already in the calendar"
    else: 
      self.birthdays[name] = date 
      return f"{name}'s birthday has been added."

  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
      return f"{name}'s birthday has been removed."
    else:
      return f"{name}'s birthday is not in the calendar."
      

  


# Code to test the class
# assistant = PersonalAssistant()
# print(assistant.get_contact("Chelsea"))
# assistant.add_todo("Pick up groceries")
# print(assistant.get_todos())
# print(assistant.get_birthday("Rob Freese"))
