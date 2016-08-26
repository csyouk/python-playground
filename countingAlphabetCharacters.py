statement = "Such a histogram might be useful for compressing a text file. Because different letters appear with different frequencies, we can compress a file by using shorter codes for common letters and longer codes for letters that appear less frequently."
letterCounts = {}
for letter in statement:
    letterCounts[letter] = letterCounts.get(letter,0) + 1

print letterCounts
print '======================================'
letterItems = letterCounts.items()
letterItems.sort()
print letterItems
