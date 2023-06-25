import json

def load_json_objects(file_path):
    json_objects = []

    with open(file_path, 'r') as file:
        for line in file:
            json_data = json.loads(line)
            json_objects.append(json_data)

    return json_objects

file_path = '/home/adrian/Desktop/desktop/nlp/presto_v1/presto_dataset.jsonl'
json_objects = load_json_objects(file_path)

en_data = []
count = 0
count_all = 0

for entity in json_objects:
    metadata = entity.get("metadata")
    count_all += 1
    if "en-US" in metadata.get("locale"):
        count += 1
        line = ""
        turn_count = 0
        for turn in metadata.get("previous_turns"):
            turn_count += 1
            line += str(turn.get("user_query")).strip().lower() + " # "
            line += str(turn.get("response_text")).strip().lower() + " # "
        line += str(entity.get("inputs")).strip().lower()

        if turn_count > 1:
            en_data.append(line)
        # if count > 10: # do szybkiego testu formatu
        #     break

print(count)
print(count_all)

output_file_path = "en_data_no_one_utterance.txt"

with open(output_file_path, "w") as file:
    # Use print with file parameter to write to the file
    for sentence in en_data:
        print(sentence, file=file)

