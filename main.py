import schedule
import pyrogram
from random import randint

api_id = 27455735
api_hash = 'e7037156dbe251f6945d672650d312d4'


def prog():
    with pyrogram.Client("TgAvatarChanger3", api_id, api_hash) as app:
        photos = [p for p in app.get_chat_photos("me")]
        app.delete_profile_photos(photos[0].file_id)
        app.set_profile_photo(photo=f'anim/Screenshot_{randint(1, 5)}.png')


def main():
    schedule.every(5).seconds.do(prog)

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
