import os
import matplotlib.pyplot as plt


def main():
        sub_dict = "data/submissions"
        finalgrade = 0
        gradelist = []

        with open("data/assignments.txt") as f:
            assignments = f.read().splitlines()

        print("1. Student grade")
        print("2. Assignment statistics")
        print("3. Assignment graph\n")

        choice = input("Enter your selection: ")
        match choice:
            case "1":
                name = input("What is the student's name: ")
                with open("data/students.txt", "r") as f:
                    for line in f:
                        if line[3:].strip("\n") == name:
                            id = line[0:3]
                            break

                for file in os.listdir(sub_dict):
                    with open(f"{sub_dict}/{file}") as f:
                        line = f.readline().strip("\n")
                    if line.startswith(id):
                        _, assignmentnum, grade = line.split("|")
                        points = int(assignments[assignments.index(assignmentnum) + 1])
                        finalgrade += (points * (int(grade) / 100)) / 10
                print(f"{finalgrade:.0f}%")

            case "2":
                assignment = input("What is the assignment name: ")
                for file in os.listdir(sub_dict):
                    with open(f"{sub_dict}/{file}") as f:
                        line = f.readline().strip("\n")
                    _, assignmentnum, grade = line.split("|")
                    if assignmentnum == assignments[assignments.index(assignment) + 1]:
                        gradelist.append(int(grade))

                print(f"Min: {min(gradelist):.0f}%")
                print(f"Avg: {sum(gradelist) // len(gradelist):.0f}%")
                print(f"Max: {max(gradelist):.0f}%")

            case "3":
                assignment = input("What is the assignment name: ")
                for file in os.listdir(sub_dict):
                    with open(f"{sub_dict}/{file}") as f:
                        line = f.readline().strip("\n")
                    _, assignmentnum, grade = line.split("|")
                    if assignmentnum == assignments[assignments.index(assignment) + 1]:
                        gradelist.append(int(grade))

                plt.hist(gradelist, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
                plt.show()


if __name__ == "__main__":
    main()
