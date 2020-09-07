import os.path
file_input = "supp_files/task-5/example"


if os.path.isfile(file_input):
    with open(file_input, 'r') as f:
        list_word = f.read().lower().split()
        list_word = list(map(lambda word: word.strip('.,?!'), list_word))
        sort_list_word = sorted(list_word)
        max_count_word = max(sort_list_word, key=lambda word: sort_list_word.count(word))
        print(max_count_word, list_word.count(max_count_word))
else:
    print("File not found")

