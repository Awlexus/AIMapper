from BeatmapUtils import get_hitobject_data

hitobjects = get_hitobject_data('testfile.osu')  # Drop - Granat, because it's a short one

print('Length:', len(hitobjects))
print('Head:', hitobjects[:5])
print('Tail:', hitobjects[-5:])

if __name__ == '__main__':
    from PyOsuDBReader.pyosudbreader import OsuDbReader

    with OsuDbReader as db:
        print(db.version)

