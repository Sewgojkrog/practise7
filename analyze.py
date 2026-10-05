INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

total_math = 0.0
total_python = 0.0
total_english = 0.0
students_count = 0

best_student_name = ()
best_student_avg = 0

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    next(f)


    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        name = parts[0]
        math = float(parts[1])
        python = float(parts[2])
        english = float(parts[3])

        total_math += math
        total_python += python
        total_english += english
        students_count += 1

        student_avg = (math + python + english) / 3.0
        if student_avg > best_student_avg:
            best_student_avg = student_avg
            best_student_name = name


    if students_count > 0:
        avg_math = total_math / students_count
        avg_python = total_python / students_count
        avg_english = total_english / students_count
    else:
        avg_math = avg_python = avg_english = 0.0

    result_text = (f"Середній бал по класу:\n"
        f"math: {avg_math:.1f}\n"
        f"python: {avg_python:.1f}\n"
        f"english: {avg_english:.1f}\n\n"
        f"Найкращий студент: {best_student_name} ({best_student_avg:.1f})")

    print(result_text)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(result_text)