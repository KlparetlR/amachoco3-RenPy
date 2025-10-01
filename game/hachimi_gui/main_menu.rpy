# 以下代码全部由天马咲希型千趣编写，属于 UI 代码
# 禁止未通知本人的情况下修改本文件代码的任何部分或数值
# 一旦未经告知本人而进行修改，出现任何问题，不负责任何维护义务，因为那不是我造成的，不要给我徒增工作量，谢谢喵
# 目前的代码已经过充分的测试验证过可行性与稳定性，因为修改文件导致新增的潜在Bug，也请自己测试与负责

default persistent.disclaimer_accepted = False
screen main_menu():
    tag menu
    add gui.main_menu_background
    vbox:
        xpos 0.91
        ypos 0.02
        spacing 8
        imagebutton:
            idle "gui/hachimi_gui/title/title_start_1.png"
            hover "gui/hachimi_gui/title/title_start_2.png"
            at main_menu_show_btn(0.1)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [
                Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),
                If(persistent.disclaimer_accepted,
                    ShowMenu("hachimi_chapter"),
                    Confirm("本民间移植版完全免费\n{color=#f14444}禁止倒卖等一切试图盈利的方式！{/color}\n{a=https://store.steampowered.com/app/1238680/}{u}{color=#6a3615}如有条件请点击此处前往Steam支持正版{/color}{/u}{/a}\n您不应该通过任何付费手段获取本移植资源\n如果已被骗，请通过设置或主界面的反馈按钮告知",
                        [SetVariable("persistent.disclaimer_accepted", True), ShowMenu("hachimi_chapter")]
                    )
                )
            ]
        imagebutton:
            idle "gui/hachimi_gui/title/title_continue_1.png"
            hover "gui/hachimi_gui/title/title_continue_2.png"
            insensitive "gui/hachimi_gui/title/title_continue_0.png"
            at main_menu_show_btn(0.2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(fade),Continue()]
        imagebutton:
            idle "gui/hachimi_gui/title/title_load_1.png"
            hover "gui/hachimi_gui/title/title_load_2.png"
            at main_menu_show_btn(0.3)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_load")]
        imagebutton:
            idle "gui/hachimi_gui/title/title_config_1.png"
            hover "gui/hachimi_gui/title/title_config_2.png"
            at main_menu_show_btn(0.4)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_text_config")]
        imagebutton:
            idle "gui/hachimi_gui/title/title_extra_1.png"
            hover "gui/hachimi_gui/title/title_extra_2.png"
            at main_menu_show_btn(0.5)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [
                Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),
                If(
                    persistent.mikuri_clear or persistent.chieri_clear or persistent.ichika_clear or 
                    persistent.nana_clear or persistent.kaguya_clear or persistent.mitsuki_clear or 
                    persistent.kohana_clear or persistent.harem_clear,
                    ShowMenu("main_menu_2"),
                    Alert("您必须通关任意一条路线\n才能解锁鉴赏界面")
                )
            ]
        imagebutton:
            idle "gui/hachimi_gui/title/title_about_1.png"
            hover "gui/hachimi_gui/title/title_about_2.png"
            at main_menu_show_btn(0.6)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("main_menu_3")]
        imagebutton:
            idle "gui/hachimi_gui/title/title_exit_1.png"
            hover "gui/hachimi_gui/title/title_exit_2.png"
            at main_menu_show_btn(0.7)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Quit(confirm=True)]
    # textbutton "{color=#6a3615}版本：v1.1（2025-10-1） 内部测试版{/color}":
    #     xalign 0.01
    #     yalign 1.0
    #     at main_menu_show_btn(0.0)


screen main_menu_2():
    tag menu
    add gui.main_menu_background
    key "mousedown_3" action [Play("sys_sound_3","gui/hachimi_gui/sound/sys_sound_3.ogg"),Return()]
    vbox:
        xpos 0.91
        ypos 0.02
        spacing 8
        imagebutton:
            idle "gui/hachimi_gui/title/title_CG_1.png"
            hover white_overlay_0("gui/hachimi_gui/title/title_CG_1.png", 0.35, 141, 141)
            at main_menu_show_btn(0.1)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_cg_null")]
        imagebutton:
            idle "gui/hachimi_gui/title/title_scene_1.png"
            hover white_overlay_0("gui/hachimi_gui/title/title_scene_1.png", 0.35, 141, 141)
            at main_menu_show_btn(0.2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_scene_1")]
        imagebutton:
            idle "gui/hachimi_gui/title/title_others_1.png"
            hover white_overlay_0("gui/hachimi_gui/title/title_others_1.png", 0.35, 141, 141)
            at main_menu_show_btn(0.3)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_others_1")]
        imagebutton:
            idle "gui/hachimi_gui/title/title_music_1.png"
            hover white_overlay_0("gui/hachimi_gui/title/title_music_1.png", 0.35, 141, 141)
            at main_menu_show_btn(0.4)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_music_1")]
        imagebutton:
            idle "gui/hachimi_gui/title/title_video_1.png"
            hover white_overlay_0("gui/hachimi_gui/title/title_video_1.png", 0.35, 141, 141)
            at main_menu_show_btn(0.5)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_video")]
        imagebutton:
            idle "gui/hachimi_gui/title/title_back_1.png"
            hover white_overlay_0("gui/hachimi_gui/title/title_back_1.png", 0.35, 141, 141)
            at main_menu_show_btn(0.6)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Return()]
    # textbutton "{color=#6a3615}版本：v1.1（2025-10-1） 内部测试版{/color}":
    #     xalign 0.01
    #     yalign 1.0
    #     at main_menu_show_btn(0.0)

screen main_menu_3():
    tag menu
    add gui.main_menu_background
    key "mousedown_3" action [Play("sys_sound_3","gui/hachimi_gui/sound/sys_sound_3.ogg"),Return()]
    vbox:
        xpos 0.91
        ypos 0.02
        spacing 8
        imagebutton:
            idle "gui/hachimi_gui/title/title_say_1.png"
            hover white_overlay_0("gui/hachimi_gui/title/title_say_1.png", 0.35, 141, 141)
            at main_menu_show_btn(0.1)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_about_what_can_i_say")]
        imagebutton:
            idle "gui/hachimi_gui/title/title_update_1.png"
            hover white_overlay_0("gui/hachimi_gui/title/title_update_1.png", 0.35, 141, 141)
            at main_menu_show_btn(0.2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_about_update")]
        imagebutton:
            idle "gui/hachimi_gui/title/title_feedback_1.png"
            hover white_overlay_0("gui/hachimi_gui/title/title_feedback_1.png", 0.35, 141, 141)
            at main_menu_show_btn(0.3)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("移植交流与反馈群：255105631（Setaria咖啡馆）\n或者点击本行文本直接申请加入\n欢迎各位来咖啡馆玩~\n在此也募集逆向、跨引擎、RenPy方面的大佬\n一起开展与完善新项目")]
        imagebutton:
            idle "gui/hachimi_gui/title/title_warning_1.png"
            hover white_overlay_0("gui/hachimi_gui/title/title_warning_1.png", 0.35, 141, 141)
            at main_menu_show_btn(0.4)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_about_warning")]
        imagebutton:
            idle "gui/hachimi_gui/title/title_back_1.png"
            hover white_overlay_0("gui/hachimi_gui/title/title_back_1.png", 0.35, 141, 141)
            at main_menu_show_btn(0.5)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Return()]
    # textbutton "{color=#6a3615}版本：v1.1（2025-10-1） 内部测试版{/color}":
    #     xalign 0.01
    #     yalign 1.0
    #     at main_menu_show_btn(0.0)