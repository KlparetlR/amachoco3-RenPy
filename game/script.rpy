image hachimi_lanuch = "gui/hachimi_gui/title/title_lanuch_bg.png"
image hachimi_main = "gui/main_menu.png"
default logo_ses = [
    "all_t0002",
    "mit_t0004",
    "chi_t0004",
    "ich_t0004",
    "nan_t0004",
    "kag_t0004",
    "tuk_t0004",
    "koh_t0004"
]

default persistent.from_splashscreen = False

label splashscreen:
    $ persistent.from_splashscreen = True
    scene black
    $_dismiss_pause = False
    scene white with dissolve
    scene brandlogo with dissolve
    $_dismiss_pause = True
    play sound f"audio/voice/ac3_{logo_ses[random.randint(0, 7)]}.ogg"
    pause(1.5)
    $_dismiss_pause = False
    scene white with dissolve
    scene hachimi_lanuch with dissolve
    $_dismiss_pause = True
    pause(5.0)
    $_dismiss_pause = False
    scene white with dissolve
    scene black with dissolve
    $ renpy.movie_cutscene("mv/ac3_opmv1.webm")
    pause(0.1)
    

label before_main_menu:
    $_dismiss_pause = False
    if not persistent.from_splashscreen:
        scene black with dissolve
        pause(0.2)
        scene hachimi_main with dissolve
        play music "audio/bgm/bgm012.ogg" loop
        play sound "audio/voice/ac3_all_t0001.ogg"
    else:
        $ persistent.from_splashscreen = False
        play music "audio/bgm/bgm012.ogg" loop
    $_dismiss_pause = True