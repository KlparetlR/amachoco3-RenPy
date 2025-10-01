# 以下代码全部由天马咲希型千趣编写，属于 UI 代码
# 禁止未通知本人的情况下修改本文件代码的任何部分或数值
# 一旦未经告知本人而进行修改，出现任何问题，不负责任何维护义务，因为那不是我造成的，不要给我徒增工作量，谢谢喵
# 目前的代码已经过充分的测试验证过可行性与稳定性，因为修改文件导致新增的潜在Bug，也请自己测试与负责

screen hachimi_extra_cg_kaguya():
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
    grid 4 4:
        xalign 0.12
        yalign 0.25
        spacing 20
        imagebutton:
            idle bordered_image("images/cg/ev/tmb_ev513.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/ev/tmb_ev513.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kaguya_01")]
        imagebutton:
            idle bordered_image("images/cg/hv/tmb_hv508.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/hv/tmb_hv508.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kaguya_02")]
        imagebutton:
            idle bordered_image("images/cg/hv/tmb_hv509.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/hv/tmb_hv509.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kaguya_03")]
        imagebutton:
            idle bordered_image("images/cg/hv/tmb_hv510.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/hv/tmb_hv510.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kaguya_04")]

    vbox:
        xalign 1.0
        yalign 0.14
        spacing 20
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_mikuri_1.png"
            hover "gui/hachimi_gui/extra/extra_mikuri_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            if persistent.mikuri_clear == False:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「美久栗后日谈」章节后\n才能解锁其鉴赏界面")]
            elif persistent.mikuri_clear == True:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_cg_mikuri")]
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_chieri_1.png"
            hover "gui/hachimi_gui/extra/extra_chieri_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            if persistent.chieri_clear == False:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「千绘莉后日谈」章节后\n才能解锁其鉴赏界面")]
            elif persistent.chieri_clear == True:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_cg_chieri")]
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_ichika_1.png"
            hover "gui/hachimi_gui/extra/extra_ichika_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            if persistent.ichika_clear == False:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「莓华后日谈」章节后\n才能解锁其鉴赏界面")]
            elif persistent.ichika_clear == True:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_cg_ichika")]
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_nana_1.png"
            hover "gui/hachimi_gui/extra/extra_nana_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            if persistent.nana_clear == False:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「娜娜后日谈」章节后\n才能解锁其鉴赏界面")]
            elif persistent.nana_clear == True:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_cg_nana")]
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_kaguya_2.png"
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_mitsuki_1.png"
            hover "gui/hachimi_gui/extra/extra_mitsuki_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            if persistent.mitsuki_clear == False:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「月圆月缺曾几度」章节后\n才能解锁其鉴赏界面")]
            elif persistent.mitsuki_clear == True:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_cg_mitsuki_1")]
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_kohana_1.png"
            hover "gui/hachimi_gui/extra/extra_kohana_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            if persistent.kohana_clear == False:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「花开花落会有时」章节后\n才能解锁其鉴赏界面")]
            elif persistent.kohana_clear == True:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_cg_kohana_1")]
        imagebutton:
            if persistent.harem_clear == False:
                idle "gui/hachimi_gui/extra/extra_unknown_1.png"
                hover "gui/hachimi_gui/extra/extra_unknown_2.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须解锁并通关隐藏章节「？？？？？」后\n才能解锁其鉴赏界面")]
            elif persistent.harem_clear == True:
                idle "gui/hachimi_gui/extra/extra_harem_1.png"
                hover "gui/hachimi_gui/extra/extra_harem_2.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_cg_harem")]