import os

def main(background):
    i = 1
    while True:
        if os.path.exists(f'./saves/galaxy_{i}.png'):
            i += 1
        else:
            background.save(f'./saves/galaxy_{i}.png', optimize=True)
            break
