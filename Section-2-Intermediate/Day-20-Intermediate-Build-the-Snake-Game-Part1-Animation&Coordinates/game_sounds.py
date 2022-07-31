import winsound as sounds


def eating_sound():
    sounds.PlaySound("eatingsfxwav-14588.wav", sounds.SND_ASYNC)


def spawn_sound():
    sounds.PlaySound("moody-blip-43107.wav", sounds.SND_ASYNC)


def gameover_sound():
    sounds.PlaySound("game_over.wav", sounds.SND_ASYNC)
