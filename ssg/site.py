import Path from pathlib

class Site:

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(source)

    def create_dir(self, path):
        directory = self.dest/relative_to(self.source)

        mkdir(directory, parents = True, exist_ok = True)

    def build():
        mkdir(self.dest, parents = True, exist_ok = True)

        for path in self.source.rglob("*"):
            if path.isdir(path):
                create_dir(path)
