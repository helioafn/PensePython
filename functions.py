import math

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and i work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# repeat_lyrics()

def print_twice(bruce):
    print(bruce)
    print(bruce)

pc_owner = 'Hélio'
# print_twice('Hélio')
# print_twice(1337)
# print_twice(math.pi)
# print_twice(pc_owner)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = 'Bing tiddle'
line2 = 'tiddle bang.'
cat_twice(line1, line2)

print(cat)
