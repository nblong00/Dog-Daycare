import pathlib


def get_root():
    root = pathlib.PurePath(
        input("What is the full path to create project at? ")
    )
    if not root.is_absolute():
        return get_root()
    return root


def main():
    project_root = get_root()
    project_name = None
    while not project_name:
        project_name = input("What is full name of project? ").strip()
    print(f"Creating {project_name} in {project_root}")


if __name__ == '__main__':
    main()
