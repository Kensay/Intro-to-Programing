from operator import itemgetter, attrgetter, methodcaller

s = "betty bought a bit of butter but the butter was bitter"
print(s)

list_of_words = s.split()
count_list = [0] * len(list_of_words)
Tuple = [0] * len(list_of_words)
index = 0
while index < len(list_of_words):
  word = list_of_words[index]
  count_list[index] = list_of_words.count(word)
  Tuple[index] = (word, count_list[index])
  index = index + 1

Set_list = set(Tuple)

Sorted_Number = sorted(Set_list, key=itemgetter(0))
Sorted_String = sorted(Sorted_Number, key=itemgetter(1), reverse = True)

print(Sorted_String[:3])