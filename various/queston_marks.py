import re


def find_digits_before_and_after_question_marks(string_text):
    pattern =r'\w*(\d{1})[\?\w*]*\?(\d{1})\w*'
    prog = re.compile(pattern)

    selected_text = prog.sub(r'\1\2', string_text)
    print(f'Selected text: {selected_text}')

    sum_ = sum([int(i) for i in list(selected_text)])

    if sum_ == 10:
        print(f'{sum_} is equal to 10\n')
    else:
        print(f'''{sum_} isn't equal to 10\n''')


if __name__ == '__main__':
    string_list = [
        '2?13acc7?fggh?sss?3rr1',
        '2s63h4?sh7fgjS?sh7rgjc?8ry834n',
        'wret654w7?uydh76sd?u7dg?hd21?3udgdn23'
    ]
    for string_text in string_list:
        find_digits_before_and_after_question_marks(string_text)
