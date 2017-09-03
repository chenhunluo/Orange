'''
Exports all markdown files into html files
'''

import os
import misaka as md

class FilePath(object):
    """
    Path to a file
    """
    def __init__(self, filename, directory):
        "Initialize a file path"
        self.filename = filename
        self.directory = directory

    def __str__(self):
        return os.path.join(self.directory, self.filename)

class StaticSiteGenerator(object):
    """
    The core class for static site generator
    """
    def __init__(self, working_dir):
        "Initialize an StaticSiteGenerator object"
        self.working_dir = working_dir
        self.__posts_dir = os.path.join(self.working_dir, "posts")
        self.__output_dir = os.path.join(self.working_dir, "site")

    def set_posts_directory(self, posts_dir):
        self.__posts_dir = os.path.join(self.working_dir, posts_dir)

    def set_output_directory(self, output_dir):
        self.__output_dir = os.path.join(self.working_dir, output_dir)

    def generate(self):
        """
        Generates a static site from source files
        """

        if not os.path.exists(self.__output_dir):
            os.mkdir(self.__output_dir)
        generate_html(self.__output_dir,
                      list_markdown_files(self.__posts_dir))


def list_markdown_files(directory):
    """
    Return a list of markdown files inside a folder
    """


    for subdir, _, files in os.walk(directory):
        for filename in files:
            if all([
                    filename.endswith("md") or filename.endswith("markdown"),
                    not filename.startswith('.'),
            ]):
                filepath = FilePath(filename, subdir)
                yield filepath

def generate_html(output_dir, files):
    """
    Import list of post source files, output html files
    """
    for filepath in files:
        with open(str(filepath)) as f:
            content = md.html(f.read())

        out_file_name = os.path.splitext(filepath.filename)[0] + '.html'
        out_path = FilePath(out_file_name, output_dir)
        open(str(out_path), 'w').write(content)

def main():
    generator = StaticSiteGenerator("./test")
    generator.generate()


if __name__ == '__main__':
    main()
