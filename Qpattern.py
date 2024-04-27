def get_user_input():
  """
  Prompts user for question paper details and returns a dictionary.
  """
  question_data = {}
  input_method = input("Enter question input method (manual/file): ").lower()

  if input_method == "manual":
    for part in ["A", "B", "C"]:
      num_questions = int(input(f"Enter number of questions for Part {part}: "))
      marks_per_question = int(input(f"Enter marks per question for Part {part}: "))
      question_data[part] = {
        "num_questions": num_questions,
        "marks_per_question": marks_per_question,
        "questions": []  # List to store individual question details
      }

      for i in range(1, num_questions + 1):
        question_type = input(f"Enter question type (MCQ/Short Answer) for Part {part} Q{i}: ").upper()
        question_text = input(f"Enter question text for Part {part} Q{i}: ")
        if question_type == "MCQ":
          answer_choices = []
          for j in range(4):  # Assuming 4 choices (a), (b), (c), (d)
            answer_choices.append(input(f"Enter answer choice {chr(j+97)} for Part {part} Q{i}: "))
        else:
          answer_choices = None  # Set to None for Short Answer questions
        or_choice = input(f"Does Part {part} Q{i} have an OR choice (Y/N): ").upper() == "Y"
        question_data[part]["questions"].append({
          "number": i,
          "type": question_type,
          "text": question_text,
          "choices": answer_choices,
          "or_choice": or_choice
        })
  elif input_method == "file":
    filename = input("Enter filename containing question text: ")
    question_data = read_questions_from_file(filename)
  else:
    print("Invalid input method. Please choose 'manual' or 'file'.")
    return None  # Handle invalid input

  return question_data

def read_questions_from_file(filename):
  """
  Reads question text and details (if available) from a file and returns a dictionary.
  """
  question_data = {}
  try:
    with open(filename, "r", encoding="utf-8") as file:
      # Implement logic to parse question text, type, choices (if MCQ), and OR choice (optional)
      # based on the format of your question file. Here's a basic example assuming lines
      # are separated by semicolons:
      for line in file:
        parts = line.strip().split(";")
        if len(parts) >= 3:
          question_type = parts[0].strip().upper()
          question_text = parts[1].strip()
          if question_type == "MCQ":
            answer_choices = parts[2:]  # Assuming answer choices start from the 3rd element
          else:
            answer_choices = None
          or_choice = False  # Set a default value for OR choice based on your file format
          # ... (Add logic to handle OR choice if present in the file format)
          question_data.setdefault(parts[0].strip()[0], {"questions": []})["questions"].append({
            "type": question_type,
            "text": question_text,
            "choices": answer_choices,
            "or_choice": or_choice
          })
  except FileNotFoundError:
    print("Error: File not found!")
    return None
  except Exception as e:
    print(f"Error reading file: {e}")
    return None

def format_output(question_data):
  """
  Formats the question paper data into a basic text output.
  """
  output = ""
  question_number = 1  # Counter for assigning question numbers

  for part, details in question_data.items():
    output += f"\nPART - {part} ({details['num_questions']} X {details['marks_per_question']} = {details['num_questions'] * details['marks_per_question']} Marks)\n"
    output += "ANSWER ALL QUESTIONS\n\n"
    for question in details["questions"]:
      output += f"{question['number']}. {question['text']}\n"
      if question["type"] == "MCQ":
        for i, choice in enumerate(question["choices"]):
          output += f"  {(chr(i+97))}. {choice}\n"  # Display choices with alphabets (a), (b), etc.
      output += "\n"  # Add a newline after each question
  return output

  # 1. Get user input for question paper details (manual or file)
question_data = get_user_input()

# 2. If user chooses "file", handle potential errors
if question_data is None:  # Check if function returned None due to errors
  exit()

# 3. Format the question paper output based on the collected data
formatted_output = format_output(question_data)

# 4. Print the formatted question paper
print(formatted_output)

