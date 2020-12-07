

def get_answers_yes(path):
    file = open(path)
    count=0
    questions = set()
    for line in file:
        line = line.replace("\n","")
        if line == "":
            count += len(questions)
            questions = set()
        else:
            for letter in line:
                questions.add(letter)
    count += len(questions)
    return count

def get_answersall_yes(path):
    file = open(path)
    count=0
    questions = set()
    first = True
    for line in file:
        line = line.replace("\n","")
        if line == "":
            first = True
            count += len(questions)
            questions = set()
        else:
            if first:
                for letter in line:
                    questions.add(letter)
                first = False
            else:
                questions2 = set()
                for letter in line:
                    questions2.add(letter)
                questions = questions.intersection(questions2)
    count += len(questions)
    return count


print(get_answers_yes("input.txt"))
print(get_answersall_yes("input.txt"))