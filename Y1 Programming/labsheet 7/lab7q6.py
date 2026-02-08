ids = []
marks = []
while (True):
    id_no = int(input('id: '))
    while (id_no < 701 or id_no > 799) and id_no != 0:
        id_no = int(input('Error! Try again: '))

    if id_no == 0: break
    ids.append(id_no)
    mark = float(input('mark: '))
    while (mark < 0 or mark > 100):
        mark = float(input('Error! Try again: '))

    marks.append(mark)
print(ids, marks)
min_mark = 100
max_mark = 0
for mark, id_no in zip(marks, ids):
    if (mark < min_mark):
        min_mark = mark
        min_id = id_no
    if (mark > max_mark):
        max_mark = mark
        max_id = id_no

print('max:', max_id, max_mark)
print('min:', min_id, min_mark)