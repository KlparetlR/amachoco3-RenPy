# 以下代码全部由天马咲希型千趣编写，属于 UI 代码
# 禁止未通知本人的情况下修改本文件代码的任何部分或数值
# 一旦未经告知本人而进行修改，出现任何问题，不负责任何维护义务，因为那不是我造成的，不要给我徒增工作量，谢谢喵
# 目前的代码已经过充分的测试验证过可行性与稳定性，因为修改文件导致新增的潜在Bug，也请自己测试与负责

screen hachimi_extra_others_1():
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
            idle bordered_image("images/bg/AC_tmb_bg01_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg01_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_01")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg02_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg02_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_02")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg03_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg03_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_03")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg04_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg04_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_04")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg11_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg11_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_05")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg12_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg12_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_06")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg13_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg13_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_07")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg14_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg14_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_08")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg21_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg21_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_09")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg22_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg22_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_10")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg23_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg23_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_11")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg24_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg24_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_12")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg25_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg25_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_13")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg26_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg26_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_14")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg31_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg31_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_15")]
        imagebutton:
            idle bordered_image("images/bg/AC_tmb_bg32_.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/bg/AC_tmb_bg32_.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="others_16")]
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
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_others_2")]