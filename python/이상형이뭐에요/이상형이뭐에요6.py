total_list = []

while True:
    question = input("질문을 입력해주세요: ")
    if question == "q":
        break
    else:
        {"질문": question,"답변":""}

for i in total_dictionary:
    print(i)
    answer = input("답변을 입력하세요: ")
    total_dictionary[i] = answer

print(total_dictionary)