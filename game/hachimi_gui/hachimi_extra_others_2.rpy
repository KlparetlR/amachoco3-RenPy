# 以下代码全部由天马咲希型千趣编写，属于 UI 代码
# 禁止未通知本人的情况下修改本文件代码的任何部分或数值
# 一旦未经告知本人而进行修改，出现任何问题，不负责任何维护义务，因为那不是我造成的，不要给我徒增工作量，谢谢喵
# 目前的代码已经过充分的测试验证过可行性与稳定性，因为修改文件导致新增的潜在Bug，也请自己测试与负责

screen hachimi_extra_others_2():
    tag menu
    add "gui/hachimi_gui/extra/extra_bg.png"
    key "mousedown_3" action [Play("sys_sound_3","gui/hachimi_gui/sound/sys_sound_3.ogg"),ShowMenu("main_menu_2")]
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

    grid 4 4:
        xalign 0.12
        yalign 0.13
        spacing 20
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg33_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg33_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_15")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg34_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg34_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_16")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg35_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg35_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_17")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg36_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg36_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_18")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg37_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg37_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_19")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg41_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg41_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_20")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg42_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg42_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_21")]

    hbox:
        xalign 0.75
        yalign 0.94
        spacing 50
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_page1_1.png" at Transform(zoom=1.1)
            hover "gui/hachimi_gui/extra/extra_page1_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_others_1")]
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_page2_2.png" at Transform(zoom=1.1)