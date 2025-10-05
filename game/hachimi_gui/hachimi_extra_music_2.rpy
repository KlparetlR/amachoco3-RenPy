screen hachimi_extra_music_2():
    tag menu
    modal True
    key "mousedown_3" action [Notify("结束音乐鉴赏，恢复标题界面默认背景音乐"), Play("sys_sound_3","gui/hachimi_gui/sound/sys_sound_3.ogg"),ShowMenu("main_menu_2"),Play("music", "audio/bgm/bgm012.ogg")]
    add "gui/hachimi_gui/extra/extra_bg.png"
    hbox:
        xalign 0.78
        yalign 0.997
        spacing 18
        imagebutton:
            idle "gui/hachimi_gui/under_button/under_title_1.png"
            hover "gui/hachimi_gui/under_button/under_title_2.png"
            action [Notify("结束音乐鉴赏，恢复标题界面默认背景音乐"), Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("main_menu_2"),Play("music", "audio/bgm/bgm012.ogg")]
        imagebutton:
            idle "gui/hachimi_gui/under_button/under_exit_1.png"
            hover "gui/hachimi_gui/under_button/under_exit_2.png"
            selected_idle "gui/hachimi_gui/under_button/under_exit_2.png"
            selected_hover "gui/hachimi_gui/under_button/under_exit_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Quit(confirm=True)]
    timer 0.01:
        action [SetVariable('duration',get_audio_duration()),SetVariable('music_pos',get_audio_position())]
        repeat True
    vbox:
        xalign 0.05
        yalign 0.05
        spacing 35
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm202_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm202_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm202_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm202_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm202.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm602_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm602_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm602_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm602_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm602.ogg")
    vbox:
        xalign 0.73
        yalign 0.05
        spacing 35
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm601_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm601_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm601_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm601_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm601.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm603_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm603_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm603_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm603_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm603.ogg")

    imagebutton:
        xalign 0.06
        yalign 0.93
        idle "gui/hachimi_gui/extra/music/extra_pause_1.png" at Transform(zoom=1.4)
        hover "gui/hachimi_gui/extra/music/extra_pause_2.png"
        selected_idle "gui/hachimi_gui/extra/music/extra_play_1.png"
        selected_hover "gui/hachimi_gui/extra/music/extra_play_2.png"
        if not renpy.music.is_playing() and not renpy.music.get_pause():
            action mr.Play("audio/bgm/bgm012.ogg")
        else:
            action PauseAudio(channel="music", value="toggle")

    imagebutton:
        xalign 0.32
        yalign 0.918
        idle "gui/hachimi_gui/extra/music/extra_music_bar.png" at Transform(zoom=1.4)

    hbox:
        xalign 0.329
        yalign 0.932
        style_prefix "silder"
        bar value Preference("music volume") style "slider" at Transform(zoom=1.4)
        xsize 500
    $ music_volume = int(preferences.get_mixer("music")*100)
    fixed:
        xpos -0.35
        ypos 0.89
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}[music_volume]%{/color}{/size}{/font}" xalign 0.5
    vbox:
        xpos 0.9
        ypos 0.17
        spacing 30
        python:
            music_pos = get_audio_position()
            duration = get_audio_duration()
        text "{color=#ffffff}{size=50}[music_pos]{/size}{/color}"
        text "{color=#ffffff}{size=50}[duration]{/size}{/color}"
    text "{color=#ffffff}{size=50}/{/size}{/color}" xpos 0.93 ypos 0.22

    vbox:
        xalign 1.0
        yalign 0.04
        spacing 20
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_back_1.png"
            hover "gui/hachimi_gui/extra/extra_back_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Notify("结束音乐鉴赏，恢复标题界面默认背景音乐"), Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("main_menu_2"),Play("music", "audio/bgm/bgm012.ogg")]

    hbox:
        xalign 0.75
        yalign 0.94
        spacing 50
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_page1_1.png" at Transform(zoom=1.1)
            hover "gui/hachimi_gui/extra/extra_page1_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_music_1")]
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_page2_2.png" at Transform(zoom=1.1)