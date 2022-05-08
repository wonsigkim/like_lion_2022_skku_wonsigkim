#미리보기/번역기
from fnmatch import translate
from googletrans import Translator

translator = Translator()

sentence = input("번역할 문장을 입력해주세요 :")
dest = input("어떤 언어로 번역을 원하시나요: ")

detected = translator.detect(sentence)
result = translator.translate(sentence,dest)


print('=======출력결과=======')
print(detected.lang, ":",sentence)
print(result.dest, ":", result.text)
print('====================')