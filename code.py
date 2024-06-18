import json

# Function to extract information from the JSON data and write to a text file
def extract_info_and_write_to_text(questions, output_file):
    num_options = 4  # Number of options per question

    # Open the output file in write mode
    with open(output_file, 'w') as file:
        # Iterate over each question
        for i in range(len(questions)):
            question = questions[i]
            if question['question_type'] == "MULTIPLE_CHOICE":
                question_text = question['question_content']
                correct_answer = None

                # Extract options for the current question
                options_for_question = []
                options_start_index = i + 1 + 8  # Skip 8 JSON objects after each question
                for j in range(options_start_index, options_start_index + num_options):
                    option = questions[j]
                    options_for_question.append(option['question_content'])
                    if option['answer_count'] == 'TRUE':
                        correct_answer = option['question_content']

                # Convert options to "Option A", "Option B", "Option C", "Option D"
                options_mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
                options_for_question = ["Option " + options_mapping[idx] + ": " + option_text for idx, option_text in enumerate(options_for_question)]

                # Skip explanation for now
                explanation = question['answer_explanation_content']

                # Write extracted information to the file
                file.write("Question: {}\n".format(question_text))
                file.write("Options:\n")
                for option in options_for_question:
                    file.write(option + "\n")
                file.write("Correct Answer: {}\n".format(correct_answer))
                file.write("Explanation: {}\n".format(explanation))
                file.write("\n")

                # Skip to the next question
                i += 8 + num_options

# Read JSON data from file
file_path = 'new.json'  # Replace 'your_file.json' with the path to your JSON file
with open(file_path, 'r') as file:
    json_data = json.load(file)

# Call function to extract information and write to a text file
output_file = 'output.txt'  # Specify the output text file path
extract_info_and_write_to_text(json_data, output_file)
