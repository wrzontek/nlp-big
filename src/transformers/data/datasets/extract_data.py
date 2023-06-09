import json

def load_json_objects(file_path):
    json_objects = []

    with open(file_path, 'r') as file:
        for line in file:
            json_data = json.loads(line)
            json_objects.append(json_data)

    return json_objects

file_path = 'presto_dataset.jsonl'
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
        for turn in metadata.get("previous_turns"):
            line += str(turn.get("user_query")).strip().lower() + " # "
            line += str(turn.get("response_text")).strip().lower() + " # "
        line += str(entity.get("inputs")).strip().lower()
        # TODO: filter out lines too long for XLMRoBERTa
        en_data.append(line)

        # if count > 10: # do szybkiego testu formatu
        #     break

print(count)
print(count_all)

output_file_path = "en_data_4.txt"

with open(output_file_path, "w") as file:
    # Use print with file parameter to write to the file
    for sentence in en_data:
        print(sentence, file=file)

