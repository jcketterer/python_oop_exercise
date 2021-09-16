"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    def __init__(self, file_path):
        txt_file = open(file_path)

        self.words = self.parse(txt_file)

        print(f"{len(self.words)} words read")

    def parse(self, txt_file):
        return [w.strip() for w in txt_file]

    def random(self):
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    def parse(self, txt_file):
        return [w.strip() for w in txt_file if w.strip() and not w.startswith("#")]
