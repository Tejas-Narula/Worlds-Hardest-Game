import pickle
import os

error_list = []

def create_file():
    pass

def file_check():
    global error_list
    error_list = []
    required_files = ["./level_handler.py","./RoadRage.ttf","./save-states.txt"]
    
    for file in required_files:
      if not os.path.exists(file):
          error_list.append(file)
    if error_list == []:
        return True
    else: 
        return False

def resolve_errors():
    if "./save-states.txt" in error_list:
        save_states = {"tutorial" : False, "inGame_tutorial": False, "level": 0}
        pickle.dump(save_states, open("save-states.txt","wb"))
        print("\nfixed file 'save states'")

def run():
    #print("file check started")
    fileCheck = file_check()
    if fileCheck:
      pass
      #print("file check completed succsefully, starting game!")
    else:
      print("\nFile check completed with errors... \nTrying to resolve few errors")
      resolve_errors()
      if file_check():
        print("resolved all errors")
      else:
        print(f"could not resolve {error_list}, pls reinstall the program!")