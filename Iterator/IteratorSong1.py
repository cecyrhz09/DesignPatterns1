import collections.abc


class Song(collections.abc.Iterable):

    def __init__(self):
        self.name = None

    def __iter__(self):
        return Playlist(self)


class Playlist(collections.abc.Iterator):
    

    def __init__(self, aleatorio):
        self._aleatorio = aleatorio

    def __next__(self):
        if True:  # if no_elements_to_traverse:
            raise StopIteration
        return None  # return element


def main():
    aleatorio = Song()
    for _ in aleatorio:
        pass


if __name__ == "__main__":
    main()
