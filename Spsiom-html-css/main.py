if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    new_dict = {}
    for (key, values) in student_marks.items():
        new_dict[key] = (values[0] + values[1] + values[2]) / 3
    query_name = input()
    avg_marks = new_dict[query_name]
    print("{:.2f}".format(avg_marks))




