screen hachimi_extra_cg_kohana_1():
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
        yalign 0.13
        spacing 20
        imagebutton:
            idle bordered_image("images/cg/ev/tmb_ev701.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/ev/tmb_ev701.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kohana_01")]
        imagebutton:
            idle bordered_image("images/cg/ev/tmb_ev702.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/ev/tmb_ev702.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kohana_02")]
        imagebutton:
            idle bordered_image("images/cg/ev/tmb_ev703.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/ev/tmb_ev703.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kohana_03")]
        imagebutton:
            idle bordered_image("images/cg/ev/tmb_ev704.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/ev/tmb_ev704.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kohana_04")]
        imagebutton:
            idle bordered_image("images/cg/ev/tmb_ev705.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/ev/tmb_ev705.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kohana_05")]
        imagebutton:
            idle bordered_image("images/cg/ev/tmb_ev706.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/ev/tmb_ev706.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kohana_06")]
        imagebutton:
            idle bordered_image("images/cg/ev/tmb_ev707.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/ev/tmb_ev707.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kohana_07")]
        imagebutton:
            idle bordered_image("images/cg/ev/tmb_ev708.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/ev/tmb_ev708.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kohana_08")]
        imagebutton:
            idle bordered_image("images/cg/ev/tmb_ev709.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/ev/tmb_ev709.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kohana_09")]
        imagebutton:
            idle bordered_image("images/cg/ev/tmb_ev710.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/ev/tmb_ev710.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kohana_10")]
        imagebutton:
            idle bordered_image("images/cg/ev/tmb_ev711.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/ev/tmb_ev711.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kohana_11")]
        imagebutton:
            idle bordered_image("images/cg/ev/tmb_ev712.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/ev/tmb_ev712.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kohana_12")]
        imagebutton:
            idle bordered_image("images/cg/hv/tmb_hv701.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/hv/tmb_hv701.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kohana_13")]
        imagebutton:
            idle bordered_image("images/cg/hv/tmb_hv702.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/hv/tmb_hv702.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kohana_14")]
        imagebutton:
            idle bordered_image("images/cg/hv/tmb_hv703.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/hv/tmb_hv703.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kohana_15")]
        imagebutton:
            idle bordered_image("images/cg/hv/tmb_hv704.webp", white=2, black=2, size=(370,208))
            hover white_overlay("images/cg/hv/tmb_hv704.webp", 0.3, 370, 208, border=True, white=2, black=2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Show("cg_viewer", group="kohana_16")]

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
            idle "gui/hachimi_gui/extra/extra_kaguya_1.png"
            hover "gui/hachimi_gui/extra/extra_kaguya_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            if persistent.kaguya_clear == False:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「辉夜后日谈」章节后\n才能解锁其鉴赏界面")]
            elif persistent.kaguya_clear == True:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_cg_kaguya")]
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_mitsuki_1.png"
            hover "gui/hachimi_gui/extra/extra_mitsuki_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            if persistent.mitsuki_clear == False:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「月圆月缺曾几度」章节后\n才能解锁其鉴赏界面")]
            elif persistent.mitsuki_clear == True:
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_cg_mitsuki_1")]
        imagebutton:
            idle "gui/hachimi_gui/extra/extra_kohana_2.png"
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
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_cg_kohana_2")]