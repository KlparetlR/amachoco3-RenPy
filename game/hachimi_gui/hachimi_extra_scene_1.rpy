screen hachimi_extra_scene_1():
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
            if persistent.mikuri_clear == False:
                idle bordered_image("gui/hachimi_gui/extra/extra_blank.png", white=2, black=2, size=(370,208))
                hover white_overlay("gui/hachimi_gui/extra/extra_blank.png", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「美久栗后日谈」章节后\n才能解锁其回想场景")]
            elif persistent.mikuri_clear == True:
                idle bordered_image("images/cg/hv/tmb_hv108.webp", white=2, black=2, size=(370,208))
                hover white_overlay("images/cg/hv/tmb_hv108.webp", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Replay("mikuri_h1_start", locked=False)]
        imagebutton:
            if persistent.mikuri_clear == False:
                idle bordered_image("gui/hachimi_gui/extra/extra_blank.png", white=2, black=2, size=(370,208))
                hover white_overlay("gui/hachimi_gui/extra/extra_blank.png", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「美久栗后日谈」章节后\n才能解锁其回想场景")]
            elif persistent.mikuri_clear == True:
                idle bordered_image("images/cg/hv/tmb_hv109.webp", white=2, black=2, size=(370,208))
                hover white_overlay("images/cg/hv/tmb_hv109.webp", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Replay("ac3_01mikuri1", locked=False)]
        imagebutton:
            if persistent.mikuri_clear == False:
                idle bordered_image("gui/hachimi_gui/extra/extra_blank.png", white=2, black=2, size=(370,208))
                hover white_overlay("gui/hachimi_gui/extra/extra_blank.png", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「美久栗后日谈」章节后\n才能解锁其回想场景")]
            elif persistent.mikuri_clear == True:
                idle bordered_image("images/cg/hv/tmb_hv110.webp", white=2, black=2, size=(370,208))
                hover white_overlay("images/cg/hv/tmb_hv110.webp", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Replay("mikuri_h2_start", locked=False)]
        imagebutton:
            if persistent.chieri_clear == False:
                idle bordered_image("gui/hachimi_gui/extra/extra_blank.png", white=2, black=2, size=(370,208))
                hover white_overlay("gui/hachimi_gui/extra/extra_blank.png", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「千绘莉后日谈」章节后\n才能解锁其回想场景")]
            elif persistent.chieri_clear == True:
                idle bordered_image("images/cg/hv/tmb_hv208.webp", white=2, black=2, size=(370,208))
                hover white_overlay("images/cg/hv/tmb_hv208.webp", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Replay("chieri_h1_start", locked=False)]
        imagebutton:
            if persistent.chieri_clear == False:
                idle bordered_image("gui/hachimi_gui/extra/extra_blank.png", white=2, black=2, size=(370,208))
                hover white_overlay("gui/hachimi_gui/extra/extra_blank.png", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「千绘莉后日谈」章节后\n才能解锁其回想场景")]
            elif persistent.chieri_clear == True:
                idle bordered_image("images/cg/hv/tmb_hv209.webp", white=2, black=2, size=(370,208))
                hover white_overlay("images/cg/hv/tmb_hv209.webp", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Replay("ac3_02chieri1", locked=False)]
        imagebutton:
            if persistent.chieri_clear == False:
                idle bordered_image("gui/hachimi_gui/extra/extra_blank.png", white=2, black=2, size=(370,208))
                hover white_overlay("gui/hachimi_gui/extra/extra_blank.png", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「千绘莉后日谈」章节后\n才能解锁其回想场景")]
            elif persistent.chieri_clear == True:
                idle bordered_image("images/cg/hv/tmb_hv210.webp", white=2, black=2, size=(370,208))
                hover white_overlay("images/cg/hv/tmb_hv210.webp", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Replay("chieri_h2_start", locked=False)]
        imagebutton:
            if persistent.ichika_clear == False:
                idle bordered_image("gui/hachimi_gui/extra/extra_blank.png", white=2, black=2, size=(370,208))
                hover white_overlay("gui/hachimi_gui/extra/extra_blank.png", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「莓华后日谈」章节后\n才能解锁其回想场景")]
            elif persistent.ichika_clear == True:
                idle bordered_image("images/cg/hv/tmb_hv308.webp", white=2, black=2, size=(370,208))
                hover white_overlay("images/cg/hv/tmb_hv308.webp", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Replay("ac3_03ichika1", locked=False)]
        imagebutton:
            if persistent.ichika_clear == False:
                idle bordered_image("gui/hachimi_gui/extra/extra_blank.png", white=2, black=2, size=(370,208))
                hover white_overlay("gui/hachimi_gui/extra/extra_blank.png", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「莓华后日谈」章节后\n才能解锁其回想场景")]
            elif persistent.ichika_clear == True:
                idle bordered_image("images/cg/hv/tmb_hv309.webp", white=2, black=2, size=(370,208))
                hover white_overlay("images/cg/hv/tmb_hv309.webp", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Replay("ichika_h1_start", locked=False)]
        imagebutton:
            if persistent.ichika_clear == False:
                idle bordered_image("gui/hachimi_gui/extra/extra_blank.png", white=2, black=2, size=(370,208))
                hover white_overlay("gui/hachimi_gui/extra/extra_blank.png", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「莓华后日谈」章节后\n才能解锁其回想场景")]
            elif persistent.ichika_clear == True:
                idle bordered_image("images/cg/hv/tmb_hv310.webp", white=2, black=2, size=(370,208))
                hover white_overlay("images/cg/hv/tmb_hv310.webp", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Replay("chieri_h2_start", locked=False)]
        imagebutton:
            if persistent.nana_clear == False:
                idle bordered_image("gui/hachimi_gui/extra/extra_blank.png", white=2, black=2, size=(370,208))
                hover white_overlay("gui/hachimi_gui/extra/extra_blank.png", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「娜娜后日谈」章节后\n才能解锁其回想场景")]
            elif persistent.nana_clear == True:
                idle bordered_image("images/cg/hv/tmb_hv408.webp", white=2, black=2, size=(370,208))
                hover white_overlay("images/cg/hv/tmb_hv408.webp", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Replay("nana_h1_start", locked=False)]
        imagebutton:
            if persistent.nana_clear == False:
                idle bordered_image("gui/hachimi_gui/extra/extra_blank.png", white=2, black=2, size=(370,208))
                hover white_overlay("gui/hachimi_gui/extra/extra_blank.png", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「娜娜后日谈」章节后\n才能解锁其回想场景")]
            elif persistent.nana_clear == True:
                idle bordered_image("images/cg/hv/tmb_hv409.webp", white=2, black=2, size=(370,208))
                hover white_overlay("images/cg/hv/tmb_hv409.webp", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Replay("ac3_04nana1", locked=False)]
        imagebutton:
            if persistent.nana_clear == False:
                idle bordered_image("gui/hachimi_gui/extra/extra_blank.png", white=2, black=2, size=(370,208))
                hover white_overlay("gui/hachimi_gui/extra/extra_blank.png", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「娜娜后日谈」章节后\n才能解锁其回想场景")]
            elif persistent.nana_clear == True:
                idle bordered_image("images/cg/hv/tmb_hv410.webp", white=2, black=2, size=(370,208))
                hover white_overlay("images/cg/hv/tmb_hv410.webp", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Replay("nana_h2_start", locked=False)]
        imagebutton:
            if persistent.kaguya_clear == False:
                idle bordered_image("gui/hachimi_gui/extra/extra_blank.png", white=2, black=2, size=(370,208))
                hover white_overlay("gui/hachimi_gui/extra/extra_blank.png", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「辉夜后日谈」章节后\n才能解锁其回想场景")]
            elif persistent.kaguya_clear == True:
                idle bordered_image("images/cg/hv/tmb_hv508.webp", white=2, black=2, size=(370,208))
                hover white_overlay("images/cg/hv/tmb_hv508.webp", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Replay("ac3_05kaguya1", locked=False)]
        imagebutton:
            if persistent.kaguya_clear == False:
                idle bordered_image("gui/hachimi_gui/extra/extra_blank.png", white=2, black=2, size=(370,208))
                hover white_overlay("gui/hachimi_gui/extra/extra_blank.png", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「辉夜后日谈」章节后\n才能解锁其回想场景")]
            elif persistent.kaguya_clear == True:
                idle bordered_image("images/cg/hv/tmb_hv509.webp", white=2, black=2, size=(370,208))
                hover white_overlay("images/cg/hv/tmb_hv509.webp", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Replay("kaguya_h1_start", locked=False)]
        imagebutton:
            if persistent.kaguya_clear == False:
                idle bordered_image("gui/hachimi_gui/extra/extra_blank.png", white=2, black=2, size=(370,208))
                hover white_overlay("gui/hachimi_gui/extra/extra_blank.png", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「辉夜后日谈」章节后\n才能解锁其回想场景")]
            elif persistent.kaguya_clear == True:
                idle bordered_image("images/cg/hv/tmb_hv510.webp", white=2, black=2, size=(370,208))
                hover white_overlay("images/cg/hv/tmb_hv510.webp", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Replay("kaguya_h2_start", locked=False)]
        imagebutton:
            if persistent.mitsuki_clear == False:
                idle bordered_image("gui/hachimi_gui/extra/extra_blank.png", white=2, black=2, size=(370,208))
                hover white_overlay("gui/hachimi_gui/extra/extra_blank.png", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关「美月后日谈」章节后\n才能解锁其回想场景")]
            elif persistent.mitsuki_clear == True:
                idle bordered_image("images/cg/hv/tmb_hv601.webp", white=2, black=2, size=(370,208))
                hover white_overlay("images/cg/hv/tmb_hv601.webp", 0.3, 370, 208, border=True, white=2, black=2)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),Replay("mitsuki_h1_start", locked=False)]

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
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_extra_scene_2")]