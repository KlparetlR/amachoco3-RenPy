# 以下代码全部由天马咲希型千趣编写，属于 UI 代码
# 禁止未通知本人的情况下修改本文件代码的任何部分或数值
# 一旦未经告知本人而进行修改，出现任何问题，不负责任何维护义务，因为那不是我造成的，不要给我徒增工作量，谢谢喵
# 目前的代码已经过充分的测试验证过可行性与稳定性，因为修改文件导致新增的潜在Bug，也请自己测试与负责

screen hachimi_sound_config():
    tag menu
    modal True
    key "mousedown_3" action [Play("sys_sound_3","gui/hachimi_gui/sound/sys_sound_3.ogg"),Return()]
    add "gui/hachimi_gui/config/config_voice_bg.png"
    hbox:
        xpos 0.27
        ypos 0.025
        spacing 120
        imagebutton:
            idle "gui/hachimi_gui/config/config_text_1.png" at Transform(zoom=1.3)
            hover "gui/hachimi_gui/config/config_text_2.png"
            selected_idle "gui/hachimi_gui/config/config_text_2.png"
            selected_hover "gui/hachimi_gui/config/config_text_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Hide("textbox_preview"),Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_text_config")]
        imagebutton:
            idle "gui/hachimi_gui/config/config_system_1.png" at Transform(zoom=1.3)
            hover "gui/hachimi_gui/config/config_system_2.png"
            selected_idle "gui/hachimi_gui/config/config_system_2.png"
            selected_hover "gui/hachimi_gui/config/config_system_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Hide("textbox_preview"),Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_system_config")]
        imagebutton:
            idle "gui/hachimi_gui/config/config_sound_2.png" at Transform(zoom=1.3)
    hbox:
        xpos 0.073
        ypos 0.22
        style_prefix "silder"
        bar value Preference("main volume") style "slider" at Transform(zoom=1.5)
        xsize 470
    $ main_volume = int(preferences.get_mixer("main")*100)
    text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}（[main_volume]%）{/color}{/size}{/font}" xpos 0.172 ypos 0.152
    hbox:
        xpos 0.073
        ypos 0.365
        style_prefix "silder"
        bar value Preference("music volume") style "slider" at Transform(zoom=1.5)
        xsize 470
    $ music_volume = int(preferences.get_mixer("music")*100)
    text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}（[music_volume]%）{/color}{/size}{/font}" xpos 0.197 ypos 0.3
    hbox:
        xpos 0.073
        ypos 0.525
        style_prefix "silder"
        bar value Preference("sound volume") style "slider" at Transform(zoom=1.5)
        xsize 470
    $ sound_volume = int(preferences.get_mixer("sfx")*100)
    text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}（[sound_volume]%）{/color}{/size}{/font}" xpos 0.197 ypos 0.46
    hbox:
        xpos 0.073
        ypos 0.686
        bar value FieldValue(persistent, "voicing_bgm_volume", 1.0, step=0.05) style "slider" at Transform(zoom=1.5)
        timer 0.01 action Function(_apply_voicing_bgm_volume_if_needed) repeat True
        xsize 470
    $ text_voicing_bgm_volume = int(persistent.voicing_bgm_volume*100)
    text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}（[text_voicing_bgm_volume]%）{/color}{/size}{/font}" xpos 0.36 ypos 0.625

    #左一
    hbox:
        xpos 0.5455
        ypos 0.263
        style_prefix "silder"
        bar value Preference("voice volume")
        xsize 330
    $ voice_volume = int(preferences.get_mixer("voice")*100)
    hbox:
        xalign 0.514
        yalign 0.29
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}[voice_volume]{/color}{/size}{/font}" outlines [(2, "#ffffff",absolute(0), absolute(0))]

    #左二
    hbox:
        xpos 0.5455
        ypos 0.409
        style_prefix "silder"
        bar value DictValue(persistent.character_volumes, "mik", range=1.0, style="slider")
        xsize 330
    $ mik_vol = int(persistent.character_volumes["mik"] * 100)
    hbox:
        xalign 0.514
        yalign 0.445
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}[mik_vol]{/color}{/size}{/font}" outlines [(2, "#ffffff",absolute(0), absolute(0))]

    #左三
    hbox:
        xpos 0.5455
        ypos 0.55
        style_prefix "silder"
        bar value DictValue(persistent.character_volumes, "chi", range=1.0, style="slider")
        xsize 330
    $ chi_vol = int(persistent.character_volumes["chi"] * 100)
    hbox:
        xalign 0.514
        yalign 0.598
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}[chi_vol]{/color}{/size}{/font}" outlines [(2, "#ffffff",absolute(0), absolute(0))]

    #左四
    hbox:
        xpos 0.5455
        ypos 0.698
        style_prefix "silder"
        bar value DictValue(persistent.character_volumes, "ich", range=1.0, style="slider")
        xsize 330
    $ ich_vol = int(persistent.character_volumes["ich"] * 100)
    hbox:
        xalign 0.514
        yalign 0.75
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}[ich_vol]{/color}{/size}{/font}" outlines [(2, "#ffffff",absolute(0), absolute(0))]

    #左五
    hbox:
        xpos 0.5455
        ypos 0.843
        style_prefix "silder"
        bar value DictValue(persistent.character_volumes, "nan", range=1.0, style="slider")
        xsize 330
    $ nan_vol = int(persistent.character_volumes["nan"] * 100)
    hbox:
        xalign 0.514
        yalign 0.9
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}[nan_vol]{/color}{/size}{/font}" outlines [(2, "#ffffff",absolute(0), absolute(0))]

    #右一
    hbox:
        xpos 0.783
        ypos 0.263
        style_prefix "silder"
        bar value DictValue(persistent.character_volumes, "kag", range=1.0, style="slider")
        xsize 330
    $ kag_vol = int(persistent.character_volumes["kag"] * 100)
    fixed:
        xpos 0.671
        ypos 0.279
        xsize 300
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}[kag_vol]{/color}{/size}{/font}" outlines [(2, "#ffffff",absolute(0), absolute(0))] xalign 0.5

    #右二
    hbox:
        xpos 0.783
        ypos 0.409
        style_prefix "silder"
        bar value DictValue(persistent.character_volumes, "mit", range=1.0, style="slider")
        xsize 330
    $ mit_vol = int(persistent.character_volumes["mit"] * 100)
    fixed:
        xpos 0.671
        ypos 0.425
        xsize 300
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}[mit_vol]{/color}{/size}{/font}" outlines [(2, "#ffffff",absolute(0), absolute(0))] xalign 0.5

    #右三
    hbox:
        xpos 0.783
        ypos 0.55
        style_prefix "silder"
        bar value DictValue(persistent.character_volumes, "koh", range=1.0, style="slider")
        xsize 330
    $ koh_vol = int(persistent.character_volumes["koh"] * 100)
    fixed:
        xpos 0.671
        ypos 0.572
        xsize 300
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}[koh_vol]{/color}{/size}{/font}" outlines [(2, "#ffffff",absolute(0), absolute(0))] xalign 0.5

    #右四
    hbox:
        xpos 0.783
        ypos 0.698
        style_prefix "silder"
        bar value DictValue(persistent.character_volumes, "mom", range=1.0, style="slider")
        xsize 330
    $ mom_vol = int(persistent.character_volumes["mom"] * 100)
    fixed:
        xpos 0.671
        ypos 0.716
        xsize 300
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}[mom_vol]{/color}{/size}{/font}" outlines [(2, "#ffffff",absolute(0), absolute(0))] xalign 0.5

    #右五
    hbox:
        xpos 0.783
        ypos 0.843
        style_prefix "silder"
        bar value DictValue(persistent.character_volumes, "mof", range=1.0, style="slider")
        xsize 330
    $ mof_vol = int(persistent.character_volumes["mof"] * 100)
    fixed:
        xpos 0.671
        ypos 0.862
        xsize 300
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}[mof_vol]{/color}{/size}{/font}" outlines [(2, "#ffffff",absolute(0), absolute(0))] xalign 0.5

    hbox:
        xcenter 0.07
        ycenter 0.815
        spacing 155
        if persistent.voice_interrupt_on_page == True:
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_2.png" 
                hover "gui/hachimi_gui/config/config_block_2.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), SetField(persistent, "voice_interrupt_on_page", False)]
        else:
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), SetField(persistent, "voice_interrupt_on_page", True)]
    
    hbox:
        xpos 0.07
        ypos 0.915
        spacing 50
        imagebutton:
            idle "gui/hachimi_gui/under_button/under_save_1.png"
            hover "gui/hachimi_gui/under_button/under_save_2.png"
            selected_idle "gui/hachimi_gui/under_button/under_save_2.png"
            selected_hover "gui/hachimi_gui/under_button/under_save_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            if main_menu:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("处于标题界面时禁止打开存档界面")]
            else:
                action [Hide("textbox_preview"),Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_save")]
        imagebutton:
            idle "gui/hachimi_gui/under_button/under_load_1.png"
            hover "gui/hachimi_gui/under_button/under_load_2.png"
            selected_idle "gui/hachimi_gui/under_button/under_load_2.png"
            selected_hover "gui/hachimi_gui/under_button/under_load_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Hide("textbox_preview"),Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_load")]
        imagebutton:
            idle "gui/hachimi_gui/under_button/under_config_2.png"
        imagebutton:
            idle "gui/hachimi_gui/under_button/under_return_1.png"
            hover "gui/hachimi_gui/under_button/under_return_2.png"
            selected_idle "gui/hachimi_gui/under_button/under_return_2.png"
            selected_hover "gui/hachimi_gui/under_button/under_return_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Hide("textbox_preview"),Play("sys_sound_3","gui/hachimi_gui/sound/sys_sound_3.ogg"),Return()]
        imagebutton:
            idle "gui/hachimi_gui/under_button/under_title_1.png"
            hover "gui/hachimi_gui/under_button/under_title_2.png"
            selected_idle "gui/hachimi_gui/under_button/under_title_2.png"
            selected_hover "gui/hachimi_gui/under_button/under_title_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            if main_menu:
                action [Hide("textbox_preview"), Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Return()]
            else:
                action [With(Dissolve(0.3)), Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("您确定要返回到标题界面吗？\n此操作将会使未保存的进度丢失", yes=[Stop("voice"), Stop("se"), MainMenu(confirm=False)], no=Play("sys_sound_3","gui/hachimi_gui/sound/sys_sound_3.ogg"))]
        imagebutton:
            idle "gui/hachimi_gui/under_button/under_exit_1.png"
            hover "gui/hachimi_gui/under_button/under_exit_2.png"
            selected_idle "gui/hachimi_gui/under_button/under_exit_2.png"
            selected_hover "gui/hachimi_gui/under_button/under_exit_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Quit(confirm=True)]


    imagebutton:
        xalign 0.96
        yalign 0.05
        idle "gui/hachimi_gui/config/config_ask_1.png" at Transform(zoom=1.2)
        hover "gui/hachimi_gui/config/config_ask_2.png"
        hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
        action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("移植交流与反馈群：255105631（Setaria咖啡馆）\n或者点击本行文本直接申请加入\n欢迎各位来咖啡馆玩~\n在此也募集逆向、跨引擎、RenPy方面的大佬\n一起开展与完善新项目")]