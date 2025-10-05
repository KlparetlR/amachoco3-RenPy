screen hachimi_extra_video():
    tag menu
    modal True
    key "mousedown_3" action [Play("sys_sound_3","gui/hachimi_gui/sound/sys_sound_3.ogg"),ShowMenu("main_menu_2")]
    add "gui/hachimi_gui/extra/extra_bg.png"
    hbox:
        xalign 0.78
        yalign 0.997
        spacing 18
        imagebutton:
            idle "gui/hachimi_gui/under_button/under_title_1.png"
            hover "gui/hachimi_gui/under_button/under_title_2.png"
            selected_idle "gui/hachimi_gui/under_button/under_title_2.png"
            selected_hover "gui/hachimi_gui/under_button/under_title_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("main_menu_2")]
        imagebutton:
            idle "gui/hachimi_gui/under_button/under_exit_1.png"
            hover "gui/hachimi_gui/under_button/under_exit_2.png"
            selected_idle "gui/hachimi_gui/under_button/under_exit_2.png"
            selected_hover "gui/hachimi_gui/under_button/under_exit_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Quit(confirm=True)]
    vbox:
        xalign 1.0
        yalign 0.04
        spacing 20
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_back_1.png"
            hover "gui/hachimi_gui/extra/extra_back_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("main_menu_2")]

    vbox:
        xpos 0.01
        ypos 0.04
        spacing 30
        imagebutton:
            idle "gui/hachimi_gui/extra/video/extra_video1_1.png" at Transform(zoom=1.07)
            hover "gui/hachimi_gui/extra/video/extra_video1_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Confirm("开始播放视频？",ShowMenu("movie_player_title", filename="ac3_opmv1.webm", video_end=105))]
        imagebutton:
            idle "gui/hachimi_gui/extra/video/extra_video2_1.png" at Transform(zoom=1.07)
            hover "gui/hachimi_gui/extra/video/extra_video2_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Confirm("开始播放视频？",ShowMenu("movie_player_title", filename="ac3_opmv2.webm", video_end=107))]
        imagebutton:
            idle "gui/hachimi_gui/extra/video/extra_video3_1.png" at Transform(zoom=1.07)
            hover "gui/hachimi_gui/extra/video/extra_video3_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Confirm("开始播放视频？",ShowMenu("movie_player_title", filename="ac3_edmv.webm", video_end=229))]

screen movie_player_title(filename, video_end):
    modal True
    add "images/misc/black.png"
    zorder 200
    on "show" action Stop("music")
    on "hide" action Stop("movie")
    add Movie(play=f"mv/{filename}", loop=False, channel='movie') xalign 0.5 yalign 0.5
    
    # 全屏按钮阻止点击事件穿透,防止视频重新播放
    button:
        xfill True
        yfill True
        action NullAction()
    
    textbutton "{font=font/LoliSC.ttc}跳过▸{/font}":
        xalign 0.95
        yalign 0.05
        text_size 60
        text_color "#ffffff"
        text_outlines [(2, "#000000", 0, 0)]
        text_hover_color "#ff6666"
        action [Hide("movie_player_title"), Play("music", "audio/bgm/bgm012.ogg", loop=True)]  
    key "K_ESCAPE" action [Hide("movie_player_title"), Play("music", "audio/bgm/bgm012.ogg", loop=True)]
    key "mousedown_3" action [Hide("movie_player_title"), Play("music", "audio/bgm/bgm012.ogg", loop=True)]
    if video_end is not None and video_end > 0:
        timer video_end action [Hide("movie_player_title"), Play("music", "audio/bgm/bgm012.ogg", loop=True)]