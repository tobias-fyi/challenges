import os


def dirgen():
    cwd = "/Users/Tobias/workshop/Challenges/100DaysofX/02-Story"
    os.chdir(cwd)

    for i in range(33, 51):
        dir_name = str(i).zfill(3)
        os.makedirs(dir_name)
        print(f"Created directory {dir_name}...")

        os.chdir(os.path.join(cwd, dir_name))  # nav into new dir

        # generate draft file
        draft = f"{dir_name}-Draft.md"
        with open(draft, "w") as d:
            d.write(dir_name)
        print(f"Created {dir_name}-Draft.md...")

        # generate story file
        story = f"{dir_name}-Story.md"
        with open(story, "w") as s:
            s.write(dir_name)
        print(f"Created {dir_name}-Story.md...")

        os.chdir(cwd)  # nav back to stories dir
        print()


if __name__ == "__main__":
    dirgen()
