tasks = []

def main():
  message = ('''1-add tasks
2-mark task as complited
3-view tasks
4-quit''')

  while True:
    
    print(message)
  
    choice = input('Give a number: ')
    
    if choice == '1':
      add_tasks() 
      
    elif choice == '2':
      mark_them_as_completed()
      
    elif choice == '3':
      view_tasks()
      
    elif choice == '4':
      break
      
    else:
        print('Invalid input, Please enter a  number between 1 to 4!')
      
def add_tasks():
  #get tasks from the user
    task = input('Enter a task: ')
  #define tasks status 
    task_info = {'task':task, 'completed':False}
  #add task to the list
    tasks.append(task_info)
    print('task has been added!')
  
def mark_them_as_completed():

  #get list of incomplete tasks
  incomplete_tasks = []

  for task in tasks: 
    if task['completed'] == False:
       incomplete_tasks.append(task)
      
  if not (incomplete_tasks):
    print("There is no incomplted task to mark!")
    return
  #show them to the user
  for index, task in enumerate(incomplete_tasks):
    print(f'{index+1}-{task["task"]}')
    print('-'*30)
  #get the task from the user
  try:
    task_number = int(input("enter the task number u want to complete: "))
    if task_number < 0 or task_number > len(incomplete_tasks):
      print("Invalid task number!")
      return
    #mark it as completed
    incomplete_tasks[task_number - 1]["completed"] = True
    #print a message
    print('Task marked as completed!')
  except ValueError:
    print("Invalid input, please enter a number!")
    
def view_tasks():
  if not tasks: print("There are no tasks to view!");return

  for index, task in enumerate(tasks):
    status = "✔️" if task["completed"] else "❌"
    print(f'{index+1}. {task["task"]} {status}')

main()