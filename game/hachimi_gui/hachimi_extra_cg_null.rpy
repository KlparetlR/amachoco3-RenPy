screen hachimi_extra_cg_null():
    tag menu
    modal True
    key "mousedown_3" action [Play("sys_sound_3","gui/hachimi_gui/sound/sys_sound_3.ogg"),ShowMenu("main_menu_2")]
    add "gui/hachimi_gui/extra/extra_bg.png"
    text "{font=font/LoliSC.ttc}{size=70}{color=#6a3615}请在右侧选择对应章节{/color}{/size}{/font}" xpos 0.22 ypos 0.4 kerning 15
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