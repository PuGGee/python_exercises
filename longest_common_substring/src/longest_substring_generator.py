class LongestSubstringGenerator:
  def __init__(self, string1, string2):
    self.string1 = string1
    self.string2 = string2

  def substring(self):
    result = ''
    for i1, char1 in enumerate(self.string1):
      for i2, char2 in enumerate(self.string2):
        if char1 == char2:
          substring = self.__common_chars_at(i1, i2)
          if len(substring) > len(result):
            result = substring
    return result

  def __common_chars_at(self, index1, index2):
    result = self.string1[index1]
    while True:
      try:
        index1 += 1
        index2 += 1
        if self.string1[index1] == self.string2[index2]:
          result += self.string1[index1]
        else:
          break
      except IndexError:
        break
    return result

