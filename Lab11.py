import matplotlib.pyplot as plt


def load_students(file_path):
    students = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                name, student_id = line.strip().split(',')
                students[student_id] = name
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return students


def load_assignments(file_path):
    assignments = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                name, points, assignment_id = line.strip().split(',')
                assignments[assignment_id] = (name, int(points))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return assignments


def load_submissions(file_path):
    submissions = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                student_id, assignment_id, percentage = line.strip().split(',')
                submissions.append((student_id, assignment_id, float(percentage)))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return submissions


def calculate_student_grade(student_id, submissions, assignments):
    total_score = 0
    max_score = 0
    for student, assignment, percent in submissions:
        if student == student_id:
            total_score += (percent / 100) * assignments[assignment][1]
            max_score += assignments[assignment][1]
    return round((total_score / max_score) * 100) if max_score else None


def assignment_statistics(assignment_id, submissions):
    scores = [percent for _, aid, percent in submissions if aid == assignment_id]
    if not scores:
        return None
    return min(scores), sum(scores) / len(scores), max(scores)


def plot_histogram(assignment_id, submissions):
    scores = [percent for _, aid, percent in submissions if aid == assignment_id]
    if not scores:
        return False
    plt.hist(scores, bins=[0, 25, 50, 75, 100], edgecolor='black')
    plt.title(f"Histogram for Assignment {assignment_id}")
    plt.xlabel("Score (%)")
    plt.ylabel("Frequency")
    plt.show()
    return True


def main():
    students = load_students("students.txt")
    assignments = load_assignments("assignments.txt")
    submissions = load_submissions("submissions.txt")

    print("1. Student grade\n2. Assignment statistics\n3. Assignment graph")
    choice = input("Enter your selection: ").strip()

    if choice == "1":
        name = input("What is the student's name: ").strip()
        student_id = next((sid for sid, sname in students.items() if sname == name), None)
        if not student_id:
            print("Student not found")
        else:
            grade = calculate_student_grade(student_id, submissions, assignments)
            print(f"{grade}%")

    elif choice == "2":
        assignment_name = input("What is the assignment name: ").strip()
        assignment_id = next((aid for aid, (aname, _) in assignments.items() if aname == assignment_name), None)
        if not assignment_id:
            print("Assignment not found")
        else:
            stats = assignment_statistics(assignment_id, submissions)
            if stats:
                print(f"Min: {stats[0]}%\nAvg: {stats[1]}%\nMax: {stats[2]}%")
            else:
                print("Assignment not found")

    elif choice == "3":
        assignment_name = input("What is the assignment name: ").strip()
        assignment_id = next((aid for aid, (aname, _) in assignments.items() if aname == assignment_name), None)
        if not assignment_id:
            print("Assignment not found")
        else:
            if not plot_histogram(assignment_id, submissions):
                print("Assignment not found")


if __name__ == "__main__":
    main()
