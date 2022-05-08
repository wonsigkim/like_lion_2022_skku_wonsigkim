#미리보기/번역기
from fnmatch import translate
from googletrans import Translator

translator = Translator()

sentence = input("언어를 감지할 문지를 입력해주세요 :")

detected = translator.detect(sentence)
result = translator.translate(sentence,'en')

print(detected)
print(result)