# 以下代码全部由天马咲希型千趣编写，属于 UI 代码
# 禁止未通知本人的情况下修改本文件代码的任何部分或数值
# 一旦未经告知本人而进行修改，出现任何问题，不负责任何维护义务，因为那不是我造成的，不要给我徒增工作量，谢谢喵
# 目前的代码已经过充分的测试验证过可行性与稳定性，因为修改文件导致新增的潜在Bug，也请自己测试与负责

screen hachimi_system_config():
    tag menu
    modal True
    key "mousedown_3" action [Play("sys_sound_3","gui/hachimi_gui/sound/sys_sound_3.ogg"),Return()]
    if renpy.windows:
        add "gui/hachimi_gui/config/config_system_windows_bg.png"
        if persistent.windows_api == 1:
            imagebutton:
                xpos 0.53
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_2.png" 
            imagebutton:
                xpos 0.53
                ypos 0.348
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("angle2"), SetField(persistent,"windows_api", 2)])]
            imagebutton:
                xpos 0.715
                ypos 0.348
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("gl2"), SetField(persistent,"windows_api", 3)])]
        elif persistent.windows_api == 2:
            imagebutton:
                xpos 0.53
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("auto"), SetField(persistent,"windows_api", 1)])]
            imagebutton:
                xpos 0.53
                ypos 0.348
                idle "gui/hachimi_gui/config/config_block_2.png" 
            imagebutton:
                xpos 0.715
                ypos 0.348
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("gl2"), SetField(persistent,"windows_api", 3)])]
        elif persistent.windows_api == 3:
            imagebutton:
                xpos 0.53
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("auto"), SetField(persistent,"windows_api", 1)])]
            imagebutton:
                xpos 0.53
                ypos 0.348
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("angle2"), SetField(persistent,"windows_api", 2)])]
            imagebutton:
                xpos 0.715
                ypos 0.348
                idle "gui/hachimi_gui/config/config_block_2.png" 
    elif renpy.android or renpy.ios or renpy.emscripten:
        add "gui/hachimi_gui/config/config_system_android_ios_web_bg.png"
        if persistent.android_api == 1:
            imagebutton:
                xpos 0.53
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_2.png" 
            imagebutton:
                xpos 0.715
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_1.png"
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("gles2"), SetField(persistent,"android_api", 2)])]
        elif persistent.android_api == 2:
            imagebutton:
                xpos 0.53
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("auto"), SetField(persistent,"android_api", 1)])]
            imagebutton:
                xpos 0.715
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_2.png"
    elif renpy.linux:
        add "gui/hachimi_gui/config/config_system_linux_others_bg.png"
        if persistent.linux_api == 1:
            imagebutton:
                xpos 0.53
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_2.png" 
            imagebutton:
                xpos 0.715
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_1.png"
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("gles2"), SetField(persistent,"linux_api", 2)])]
            imagebutton:
                xpos 0.715
                ypos 0.348
                idle "gui/hachimi_gui/config/config_block_1.png"
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("gl2"), SetField(persistent,"linux_api", 3)])]
        elif persistent.linux_api == 2:
            imagebutton:
                xpos 0.53
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("auto"), SetField(persistent,"linux_api", 1)])]
            imagebutton:
                xpos 0.715
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_2.png"
            imagebutton:
                xpos 0.715
                ypos 0.348
                idle "gui/hachimi_gui/config/config_block_1.png"
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("gl2"), SetField(persistent,"linux_api", 3)])]
        elif persistent.linux_api == 3:
            imagebutton:
                xpos 0.53
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("auto"), SetField(persistent,"linux_api", 1)])]
            imagebutton:
                xpos 0.715
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_1.png"
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("gles2"), SetField(persistent,"linux_api", 2)])]
            imagebutton:
                xpos 0.715
                ypos 0.348
                idle "gui/hachimi_gui/config/config_block_2.png"
    elif renpy.macintosh:
        add "gui/hachimi_gui/config/config_system_mac_bg.png"
        if persistent.mac_api == 1:
            imagebutton:
                xpos 0.53
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_2.png" 
            imagebutton:
                xpos 0.715
                ypos 0.348
                idle "gui/hachimi_gui/config/config_block_1.png"
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("gl2"), SetField(persistent,"mac_api", 2)])]
        elif persistent.mac_api == 2:
            imagebutton:
                xpos 0.53
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("auto"), SetField(persistent,"mac_api", 1)])]
            imagebutton:
                xpos 0.715
                ypos 0.348
                idle "gui/hachimi_gui/config/config_block_2.png"
    else:
        add "gui/hachimi_gui/config/config_system_linux_others_bg.png"
        if persistent.linux_api == 1:
            imagebutton:
                xpos 0.53
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_2.png" 
            imagebutton:
                xpos 0.715
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_1.png"
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("gles2"), SetField(persistent,"linux_api", 2)])]
            imagebutton:
                xpos 0.715
                ypos 0.348
                idle "gui/hachimi_gui/config/config_block_1.png"
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("gl2"), SetField(persistent,"linux_api", 3)])]
        elif persistent.linux_api == 2:
            imagebutton:
                xpos 0.53
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("auto"), SetField(persistent,"linux_api", 1)])]
            imagebutton:
                xpos 0.715
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_2.png"
            imagebutton:
                xpos 0.715
                ypos 0.348
                idle "gui/hachimi_gui/config/config_block_1.png"
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("gl2"), SetField(persistent,"linux_api", 3)])]
        elif persistent.linux_api == 3:
            imagebutton:
                xpos 0.53
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("auto"), SetField(persistent,"linux_api", 1)])]
            imagebutton:
                xpos 0.715
                ypos 0.253
                idle "gui/hachimi_gui/config/config_block_1.png"
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), Confirm("是否确认更改\n重启后生效", [_SetRenderer("gles2"), SetField(persistent,"linux_api", 2)])]
            imagebutton:
                xpos 0.715
                ypos 0.348
                idle "gui/hachimi_gui/config/config_block_2.png"
 


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
            idle "gui/hachimi_gui/config/config_system_2.png" at Transform(zoom=1.3)
        imagebutton:
            idle "gui/hachimi_gui/config/config_sound_1.png" at Transform(zoom=1.3)
            hover "gui/hachimi_gui/config/config_sound_2.png"
            selected_idle "gui/hachimi_gui/config/config_sound_2.png"
            selected_hover "gui/hachimi_gui/config/config_sound_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Hide("textbox_preview"),Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_sound_config")]

    hbox:
        xcenter 0.13
        ycenter 0.318
        spacing 170
        if _preferences.pad_enabled == True:
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_2.png" 
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),SetField(_preferences, "pad_enabled", False)]
        elif _preferences.pad_enabled == False:
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),SetField(_preferences, "pad_enabled", True)]
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_2.png" 

    hbox:
        xcenter 0.13
        ycenter 0.587
        spacing 170
        if preferences.wait_voice == True:
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_2.png" 
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Preference("wait for voice", "disable")]
 
        else:
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_1.png" 
                hover "gui/hachimi_gui/config/config_block_hover.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Preference("wait for voice", "enable")]
            imagebutton:
                idle "gui/hachimi_gui/config/config_block_2.png" 

    if preferences.gl_framerate == None:
        imagebutton:
            xpos 0.53
            ypos 0.53
            idle "gui/hachimi_gui/config/config_block_2.png" 
        imagebutton:
            xpos 0.715
            ypos 0.53
            idle "gui/hachimi_gui/config/config_block_1.png" 
            hover "gui/hachimi_gui/config/config_block_hover.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Confirm("是否确认更改\n重启后生效",Preference("gl framerate", 30))]
        imagebutton:
            xpos 0.53
            ypos 0.613
            idle "gui/hachimi_gui/config/config_block_1.png" 
            hover "gui/hachimi_gui/config/config_block_hover.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Confirm("是否确认更改\n重启后生效",Preference("gl framerate", 60))]
        imagebutton:
            xpos 0.715
            ypos 0.613
            idle "gui/hachimi_gui/config/config_block_1.png" 
            hover "gui/hachimi_gui/config/config_block_hover.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Confirm("是否确认更改\n重启后生效",Preference("gl framerate", 120))]
    elif preferences.gl_framerate == 30:
        imagebutton:
            xpos 0.53
            ypos 0.53
            idle "gui/hachimi_gui/config/config_block_1.png" 
            hover "gui/hachimi_gui/config/config_block_hover.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Confirm("是否确认更改\n重启后生效",Preference("gl framerate", None))]
        imagebutton:
            xpos 0.715
            ypos 0.53
            idle "gui/hachimi_gui/config/config_block_2.png" 
        imagebutton:
            xpos 0.53
            ypos 0.613
            idle "gui/hachimi_gui/config/config_block_1.png" 
            hover "gui/hachimi_gui/config/config_block_hover.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Confirm("是否确认更改\n重启后生效",Preference("gl framerate", 60))]
        imagebutton:
            xpos 0.715
            ypos 0.613
            idle "gui/hachimi_gui/config/config_block_1.png" 
            hover "gui/hachimi_gui/config/config_block_hover.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Confirm("是否确认更改\n重启后生效",Preference("gl framerate", 120))]
    elif preferences.gl_framerate == 60:
        imagebutton:
            xpos 0.53
            ypos 0.53
            idle "gui/hachimi_gui/config/config_block_1.png" 
            hover "gui/hachimi_gui/config/config_block_hover.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Confirm("是否确认更改\n重启后生效",Preference("gl framerate", None))]
        imagebutton:
            xpos 0.715
            ypos 0.53
            idle "gui/hachimi_gui/config/config_block_1.png" 
            hover "gui/hachimi_gui/config/config_block_hover.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Confirm("是否确认更改\n重启后生效",Preference("gl framerate", 30))]
        imagebutton:
            xpos 0.53
            ypos 0.613
            idle "gui/hachimi_gui/config/config_block_2.png" 
        imagebutton:
            xpos 0.715
            ypos 0.613
            idle "gui/hachimi_gui/config/config_block_1.png" 
            hover "gui/hachimi_gui/config/config_block_hover.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Confirm("是否确认更改\n重启后生效",Preference("gl framerate", 120))]
    elif preferences.gl_framerate == 120:
        imagebutton:
            xpos 0.53
            ypos 0.53
            idle "gui/hachimi_gui/config/config_block_1.png" 
            hover "gui/hachimi_gui/config/config_block_hover.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Confirm("是否确认更改\n重启后生效",Preference("gl framerate", None))]
        imagebutton:
            xpos 0.715
            ypos 0.53
            idle "gui/hachimi_gui/config/config_block_1.png" 
            hover "gui/hachimi_gui/config/config_block_hover.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Confirm("是否确认更改\n重启后生效",Preference("gl framerate", 30))]
        imagebutton:
            xpos 0.53
            ypos 0.613
            idle "gui/hachimi_gui/config/config_block_1.png" 
            hover "gui/hachimi_gui/config/config_block_hover.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Confirm("是否确认更改\n重启后生效",Preference("gl framerate", 60))]
        imagebutton:
            xpos 0.715
            ypos 0.613
            idle "gui/hachimi_gui/config/config_block_2.png" 

    if persistent.chosen_font == font_options["思源黑体"]:
        imagebutton:
            xpos 0.52
            ypos 0.79
            idle "gui/hachimi_gui/config/config_block_2.png" 
    else:
        imagebutton:
            xpos 0.52
            ypos 0.79
            idle "gui/hachimi_gui/config/config_block_1.png" 
            hover "gui/hachimi_gui/config/config_block_hover.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Confirm("是否确认更改\n重启后生效", SetVariable("persistent.chosen_font", font_options["思源黑体"]))]

    if persistent.chosen_font == font_options["猫啃什锦体"]:
        imagebutton:
            xpos 0.67
            ypos 0.79
            idle "gui/hachimi_gui/config/config_block_2.png" 
    else:
        imagebutton:
            xpos 0.67
            ypos 0.79
            idle "gui/hachimi_gui/config/config_block_1.png" 
            hover "gui/hachimi_gui/config/config_block_hover.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Confirm("是否确认更改\n重启后生效", SetVariable("persistent.chosen_font", font_options["猫啃什锦体"]))]

    if persistent.chosen_font == font_options["萝莉体"]:
        imagebutton:
            xpos 0.84
            ypos 0.79
            idle "gui/hachimi_gui/config/config_block_2.png" 
    else:
        imagebutton:
            xpos 0.84
            ypos 0.79
            idle "gui/hachimi_gui/config/config_block_1.png" 
            hover "gui/hachimi_gui/config/config_block_hover.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Confirm("是否确认更改\n重启后生效", SetVariable("persistent.chosen_font", font_options["萝莉体"]))]

    hbox:
        xpos 0.072
        ycenter 0.815
        style_prefix "silder"
        bar value FieldValue(persistent, "textbox_transparency", range=1.0, style="slider")  at Transform(zoom=1.6)
        xsize 470
    $ textbox_show = int(persistent.textbox_transparency*100)
    if textbox_show == 100:
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=43}{color=#6a3615}（Sora's Artifact）{/color}{/size}{/font}" xpos 0.3 ypos 0.697
    else:
        text "{font=font/MaokenAssortedSans-Lite.otf}{size=43}{color=#6a3615}（[textbox_show]%）{/color}{/size}{/font}" xpos 0.3 ypos 0.697

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