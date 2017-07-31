text_file = open('dracula.txt', 'r')
text_lines = text_file.readlines()
text_file.close()

num_lines = 0
content_found = False

while not content_found:
    line = text_lines[num_lines].lower()
    if 'contents' in line:
        content_found = True
        print ('The line number of the contents beginning is', num_lines + 1)
    else:
        num_lines += 1

contents_begin = num_lines

for line in text_lines[contents_begin:]:
    if 'dracula' in line.lower():
        print ('The line number of the body beginning is', num_lines + 1)
        break
    else:
        num_lines += 1

contents_end = num_lines - 1
titles = []

for line in text_lines[contents_begin:contents_end]:
    if line.upper() != line:
        if 'Page' not in line:
            line = line.replace(',', '')
            line = line.replace('"', '')
            line = line.replace('-', '')
            words = line.split()
            words.remove(words[-1])
            print (words)
            title = ''
            word_no = 1
            for i in words:
                title = title + i.__str__()
                if word_no != words.__len__():
                    title = title + '_'
                word_no += 1
            print (title)
            titles.append(title)

begin_line_number = num_lines
chapter_number = 1


def counting(chapter_name, chapter_number):
    text = open(chapter_name).readlines()
    lines = 0
    s = 0
    w = 0

    for line in text:
        li = line.split()
        lines += 1
        for word in li:
            l = len(word)
            s += l
            w += 1

    print("The number of letters is:", s, "The number of words is", w, "The number of lines is", lines)
    data = open('Counting', 'a+')
    new_line = 'For Chapter' + chapter_number.__str__() + ', it has ' + lines.__str__() + ' lines,' + w.__str__() + ' words and ' + s.__str__() + ' letters.\n'
    data.write(new_line)

for line in text_lines[begin_line_number:]:
    if 'chapter' in line.lower():
        chapter_begin = num_lines
        chapter_lines = num_lines
        print ('The chapter', chapter_number, 'is found!')
        chapter_name = 'Dracula-Chapter-' + chapter_number.__str__() + '-' + titles[chapter_number - 1]
        print ('chapter_name is ', chapter_name)
        new_chapter = open(chapter_name, 'w')
        for chapter_line in text_lines[num_lines + 1:]:
            if 'chapter' in chapter_line.lower() or 'THE END' in chapter_line:
                chapter_end = chapter_lines - 1
                chapter_text = text_lines[chapter_begin:chapter_end]
                new_chapter.writelines(chapter_text)
                new_chapter.close()
                counting(chapter_name, chapter_number)
                break
            else:
                chapter_lines += 1
        chapter_number += 1
        num_lines += 1
    else:
        num_lines += 1

