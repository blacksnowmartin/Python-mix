def create_story():

  print("Let's create a story together! I need some information from you.")

  # Main Character
  main_character_name = input("What is the name of the main character? ")
  main_character_age = input(f"How old is {main_character_name}? ")
  main_character_personality = input(f"Describe {main_character_name}'s personality (e.g., adventurous, shy, curious): ")

  # Supporting Characters
  friend1_name = input("What is the name of the main character's best friend? ")
  friend1_personality = input(f"Describe {friend1_name}'s personality (e.g., funny, kind, brave): ")
  friend2_name = input("What is the name of another friend? ")
  friend2_personality = input(f"Describe {friend2_name}'s personality (e.g., wise, mischievous, helpful): ")
  antagonist_name = input("Who is the main antagonist in the story? ")
  antagonist_personality = input(f"Describe the antagonist's personality (e.g., cunning, arrogant, greedy): ")
  helper_name = input("Who is a helpful character in the story? ")
  helper_personality = input(f"Describe the helper's personality (e.g., wise, mysterious, kind): ")

  place_name = input("Where does this story take place? (e.g., a magical forest, a bustling city, a deserted island) ")

  print("\nHere's your story:")
  print(f"""
  {main_character_name}, a {main_character_age}-year-old {main_character_personality} child, 
  lived a simple life until an unexpected adventure began. 
  One day, {main_character_name}, along with their best friend, 
  {friend1_name} ({friend1_personality}), and another friend, 
  {friend2_name} ({friend2_personality}), 
  discovered a hidden entrance to the mysterious {place_name}. 

  However, their journey was threatened by {antagonist_name}, 
  a {antagonist_personality} being who guarded the entrance. 
  Fortunately, they met {helper_name}, a {helper_personality} 
  creature who provided them with valuable guidance and assistance. 

  Together, {main_character_name} and their friends, 
  aided by the wisdom of {helper_name}, 
  faced the challenges presented by {antagonist_name} 
  and finally ventured into the unknown wonders of {place_name}. 
  """)

if __name__ == "__main__":
  create_story()
