
def count_words(text):
  return len(text.split())

def get_text(path_to_file):
  with open(path_to_file) as f:
    return f.read()

def count_letters(text):
  letter_count = {}

  for letter in text:
    lower_letter = letter.lower()
    if lower_letter in letter_count:
      letter_count[lower_letter] += 1
    else:
      letter_count[lower_letter] = 1

  return letter_count

def sort_on(dict):
  return dict["count"]

def main():
  path_to_file = "books/frankenstein.txt"
  content = get_text(path_to_file)
  word_count = count_words(content)
  letter_count = count_letters(content)

  letters_list = [{"letter": key, "count": val} for (key,val) in letter_count.items()]
  letters_list.sort(reverse=True, key=sort_on)

  print(f"{word_count} words found in the document\n")

  for item in letters_list:
    if(item["letter"].isalpha()):
      print(f"The '{item['letter']}' character was found {item['count']} times")

main()


