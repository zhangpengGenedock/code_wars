import re


def song_decoder(song):
    return re.sub('(WUB)+', ' ', song).strip()


def song_decoder2(song):
    return ' '.join(song.replace('WUB', ' ').split())


if __name__ == '__main__':
    assert song_decoder("AWUBWUBWUBBWUBWUBWUBC") == "A B C"
    assert song_decoder2("AWUBWUBWUBBWUBWUBWUBC") == "A B C"
