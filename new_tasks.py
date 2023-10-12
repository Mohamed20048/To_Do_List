
tasks = [{"task":"Quran", "completed":True}, {"task":"Salah", "completed":True}, 
         {"task":"Study", "completed":False}, {"task":"Exercise", "completed":True}, 
         {"task":"Sleep", "completed":False}, {"task":"Visit Hamada", "completed":True}]

def view_tasks():
  if not tasks: print("There are no tasks to view!");return

  for index, task in enumerate(tasks):
    status = "✔️" if task["completed"] else "❌"
    print(f'{index+1}. {task["task"]} {status}')

view_tasks()