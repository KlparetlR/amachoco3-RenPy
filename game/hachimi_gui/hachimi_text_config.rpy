screen hachimi_text_config():
    tag menu
    modal True
    key "mousedown_3" action [Hide("textbox_preview"),Play("sys_sound_3","gui/hachimi_gui/sound/sys_sound_3.ogg"),Return()]
    add "gui/hachimi_gui/config/config_text_bg.png"
    hbox:
        xpos 0.075
        ypos 0.25
        style_prefix "silder"
        bar value VariableValue("preferences.normal_text_cps", range=100, style="slider") at Transform(zoom=1.6)
        xsize 470
    if preferences.normal_text_cps == 0:
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}（瞬间显示）{/color}{/size}{/font}" xpos 0.30 ypos 0.163
    else:
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}（[preferences.normal_text_cps]字/秒）{/color}{/size}{/font}" xpos 0.30 ypos 0.163
    hbox:
        xpos 0.075
        ypos 0.445
        style_prefix "silder"
        bar value VariableValue("preferences.afm_text_cps", range=100, style="slider") at Transform(zoom=1.6)
        xsize 470
    if preferences.afm_text_cps == 0:
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}（瞬间显示）{/color}{/size}{/font}" xpos 0.30 ypos 0.355
    else:
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}（[preferences.afm_text_cps]字/秒）{/color}{/size}{/font}" xpos 0.30 ypos 0.355
    hbox:
        xpos 0.075
        ycenter 0.667
        style_prefix "silder"
        bar value Preference("auto-forward time", range=30) at Transform(zoom=1.6)
        xsize 470
    $ auto_text_speed = int(preferences.afm_time)
    if auto_text_speed == 0:
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}（量子速读）{/color}{/size}{/font}" xpos 0.30 ypos 0.549
    else:
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=40}{color=#6a3615}（等待[auto_text_speed]秒）{/color}{/size}{/font}" xpos 0.30 ypos 0.549

    hbox:
        xcenter 0.655
        ycenter 0.27
        spacing 365
        if preferences.skip_unseen == False:
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_2.png" 
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Preference("skip", "all")]
        else:
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Preference("skip", "seen")]
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_2.png" 

    hbox:
        xcenter 0.605
        ycenter 0.465
        spacing 175
        if persistent.text_color_changeable == True:
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_2.png" 
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),SetField(persistent,"text_color_changeable", False)]
        else:
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),SetField(persistent,"text_color_changeable", True)]
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_2.png" 

    hbox:
        xcenter 0.605
        ycenter 0.656
        spacing 175
        if preferences.text_shadow == True:
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_2.png" 
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),SetVariable("preferences.text_shadow", False)]
        else:
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),SetVariable("preferences.text_shadow", True)]
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_2.png" 

    default display_preview = True

    if display_preview:

        timer 0.2:
            action Show("textbox_preview")

    if persistent.text_normal == True:
        if preferences.normal_text_cps < 20:
            timer 4.0:
                repeat True
                action [Hide('textbox_preview'),SetVariable("countdown_time",textbox_preview_repeat_time+1.0),Show("textbox_preview")]
        else:
            timer 2.0:
                repeat True
                action [Hide('textbox_preview'),SetVariable("countdown_time",textbox_preview_repeat_time+1.0),Show("textbox_preview")]
    else:
        if preferences.afm_text_cps < 20:
            timer 4.0:
                repeat True
                action [Hide('textbox_preview'),SetVariable("countdown_time",textbox_preview_repeat_time+1.0),Show("textbox_preview")]
        else:
            timer 2.0:
                repeat True
                action [Hide('textbox_preview'),SetVariable("countdown_time",textbox_preview_repeat_time+1.0),Show("textbox_preview")]

    hbox:
        xcenter 0.175
        ycenter 0.846
        spacing 350
        if persistent.text_normal == True:
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_2.png" 
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [SetField(persistent,"text_normal", False),SetField(persistent,"text_auto", True),Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg")]
        else:
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [SetField(persistent,"text_normal", True),SetField(persistent,"text_auto", False),Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg")]
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_2.png" 

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

    hbox:
        xpos 0.27
        ypos 0.025
        spacing 120
        imagebutton:
            idle "gui/hachimi_gui/config/config_text_2.png" at Transform(zoom=1.3)
        imagebutton:
            idle "gui/hachimi_gui/config/config_system_1.png" at Transform(zoom=1.3)
            hover "gui/hachimi_gui/config/config_system_2.png"
            selected_idle "gui/hachimi_gui/config/config_system_2.png"
            selected_hover "gui/hachimi_gui/config/config_system_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Hide("textbox_preview"),Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_system_config")]
        imagebutton:
            idle "gui/hachimi_gui/config/config_sound_1.png" at Transform(zoom=1.3)
            hover "gui/hachimi_gui/config/config_sound_2.png"
            selected_idle "gui/hachimi_gui/config/config_sound_2.png"
            selected_hover "gui/hachimi_gui/config/config_sound_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Hide("textbox_preview"),Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_sound_config")]

    imagebutton:
        xalign 0.96
        yalign 0.05
        idle "gui/hachimi_gui/config/config_ask_1.png" at Transform(zoom=1.2)
        hover "gui/hachimi_gui/config/config_ask_2.png"
        hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
        action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("移植交流与反馈群：255105631（Setaria咖啡厅）\n{a=https://qm.qq.com/q/oMdtKloUCs}{u}{color=#6a3615}或者点击本行文本直接申请加入{/color}{/u}{/a}\n欢迎各位来咖啡厅玩~\n在此也募集逆向、跨引擎、RenPy方面的大佬\n一起开展与完善新项目")]