class PersonalAssistant:

  def __init__(self, todos):
    self.contacts = {
    }
    self.todos = todos

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

  def get_birthday(self, name):
    if name == "Rob Freese":
      print("Rob's birthday is 3/29/1976")
    elif name == "Maisy Freese":
      print("Maisy's birthday is 1/26/2013")
    elif name == "Milo Freese":
      print("Milo's birthday is 2/17/2017")
    else:
      print("Can't find a birthday for this person")

  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "No contact with that name!"


# Code to test the class
# assistant = PersonalAssistant()
# print(assistant.get_contact("Chelsea"))
# assistant.add_todo("Pick up groceries")
# print(assistant.get_todos())
# print(assistant.get_birthday("Rob Freese"))
