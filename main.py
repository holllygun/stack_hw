class Stack:
    def __init__(self, items: list):
        self.items = items

    def is_empty(self):
        return len(self.items) == 0

    def push_item(self, item):
        lst = self.items.append(item)
        return lst

    def pop_item(self):
        if len(self.items) != 0:
            popped_item = self.items.pop()
            return popped_item

    def peek_item(self):
        ex = self.items[-1]
        return ex

    def stack_size(self):
        return len(self.items)


def balanced_array(brackets):
    brackets_dict = {')': '(', '}': '{', ']': '['}
    brackets_len = len(brackets)
    b = []
    sequence = Stack(b)
    first_item = brackets.pop(0)
    sequence.push_item(first_item)
    if first_item not in '})]' and brackets_len % 2 == 0:
        while brackets:
            if brackets[0] in '[{(':
                opening = brackets.pop(0)
                sequence.push_item(opening)

            elif brackets[0] in '})]':
                last_item = sequence.peek_item()

                if last_item not in brackets_dict[brackets[0]]:
                    break

                else:
                    sequence.pop_item()
                    brackets.pop(0)

        if sequence.is_empty():
            return 'Сбалансированно'

    return 'Несбалансированно'


brackets_list = list(input('Введите последовательность: '))

print(balanced_array(brackets_list))
