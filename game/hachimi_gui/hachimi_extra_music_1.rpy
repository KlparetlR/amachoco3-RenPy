# 以下代码全部由天马咲希型千趣编写，属于 UI 代码
# 禁止未通知本人的情况下修改本文件代码的任何部分或数值
# 一旦未经告知本人而进行修改，出现任何问题，不负责任何维护义务，因为那不是我造成的，不要给我徒增工作量，谢谢喵
# 目前的代码已经过充分的测试验证过可行性与稳定性，因为修改文件导致新增的潜在Bug，也请自己测试与负责

screen hachimi_extra_music_1():
    tag menu
    modal True
    key "mousedown_3" action [Play("sys_sound_3","gui/hachimi_gui/sound/sys_sound_3.ogg"),ShowMenu("main_menu_2"),Play("music", "audio/bgm/bgm012.ogg")]
    add "gui/hachimi_gui/extra/extra_bg.png"
    hbox:
        xalign 0.78
        yalign 0.997
        spacing 18
        imagebutton:
            idle "gui/hachimi_gui/under_button/under_title_1.png"
            hover "gui/hachimi_gui/under_button/under_title_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("main_menu_2"),Play("music", "audio/bgm/bgm012.ogg")]
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
        yalign 0.2
        spacing 35
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm001_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm001_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm001_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm001_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm001.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm003_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm003_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm003_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm003_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm003.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm005_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm005_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm005_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm005_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm005.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm012_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm012_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm012_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm012_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm012.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm014_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm014_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm014_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm014_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm014.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm101_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm101_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm101_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm101_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm101.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm103_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm103_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm103_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm103_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm103.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm105_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm105_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm105_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm105_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm105.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm107_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm107_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm107_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm107_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm107.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm109_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm109_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm109_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm109_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm109.ogg")
    vbox:
        xalign 0.73
        yalign 0.2
        spacing 35
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm002_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm002_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm002_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm002_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm002.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm004_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm004_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm004_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm004_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm004.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm011_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm011_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm011_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm011_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm011.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm013_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm013_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm013_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm013_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm013.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm015_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm015_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm015_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm015_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm015.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm102_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm102_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm102_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm102_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm102.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm104_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm104_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm104_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm104_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm104.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm106_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm106_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm106_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm106_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm106.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm108_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm108_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm108_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm108_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm108.ogg")
        imagebutton:
            idle "gui/hachimi_gui/extra/music/extra_bgm201_1.png"
            hover "gui/hachimi_gui/extra/music/extra_bgm201_2.png"
            selected_idle "gui/hachimi_gui/extra/music/extra_bgm201_2.png"
            selected_hover "gui/hachimi_gui/extra/music/extra_bgm201_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action mr.Play("audio/bgm/bgm201.ogg")

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
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("main_menu_2"),Play("music", "audio/bgm/bgm012.ogg")]

    hbox:
        xalign 0.75
        yalign 0.94
        spacing 50
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_page1_2.png" at Transform(zoom=1.1)
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_page2_1.png" at Transform(zoom=1.1)
            hover "gui/hachimi_gui/extra/extra_page2_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_music_2")]