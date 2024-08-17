from pathlib import Path
for path in Path(__file__).parent.rglob("*"):
    if path.is_dir() and path.name == "f90lib":
        print(path)
        LIB_DIRECTORY = str(path)
