default persistent.tutorial_shown = False

screen hachimi_chapter():
    tag menu
    add "gui/hachimi_gui/chapter/chapter_bg.png"
    key "mousedown_3" action [Play("sys_sound_3","gui/hachimi_gui/sound/sys_sound_3.ogg"),Return()]
    vbox:
        xpos 0.13
        ypos 0.17
        spacing 16
        imagebutton:
            xalign 1.0
            idle "gui/hachimi_gui/chapter/chapter_mikuri_1.png"
            hover "gui/hachimi_gui/chapter/chapter_mikuri_2.png"
            selected_idle "gui/hachimi_gui/chapter/chapter_mikuri_3.png"
            selected_hover "gui/hachimi_gui/chapter/chapter_mikuri_3.png"
            at main_menu_show_btn(0.1)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [
                Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),
                If(persistent.tutorial_shown,
                    Start("ac3_01mikuri"),
                    Confirm("上滑↑：打开历史文本界面\n下滑↓：打开存档界面\n左滑←：回退上一条对话\n右滑→：快进\n手势教程在您确认后不再显示，请截图或牢记",
                        [SetVariable("persistent.tutorial_shown", True), Start("ac3_01mikuri")]
                    )
                )
            ]
        imagebutton:
            xalign 1.0
            idle "gui/hachimi_gui/chapter/chapter_chieri_1.png"
            hover "gui/hachimi_gui/chapter/chapter_chieri_2.png"
            selected_idle "gui/hachimi_gui/chapter/chapter_chieri_3.png"
            selected_hover "gui/hachimi_gui/chapter/chapter_chieri_3.png"
            at main_menu_show_btn(0.2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [
                Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),
                If(persistent.tutorial_shown,
                    Start("ac3_02chieri"),
                    Confirm("上滑↑：打开历史文本界面\n下滑↓：打开存档界面\n左滑←：回退上一条对话\n右滑→：快进\n手势教程在您确认后不再显示，请截图或牢记",
                        [SetVariable("persistent.tutorial_shown", True), Start("ac3_02chieri")]
                    )
                )
            ]
        imagebutton:
            xalign 1.0
            idle "gui/hachimi_gui/chapter/chapter_ichika_1.png"
            hover "gui/hachimi_gui/chapter/chapter_ichika_2.png"
            selected_idle "gui/hachimi_gui/chapter/chapter_ichika_3.png"
            selected_hover "gui/hachimi_gui/chapter/chapter_ichika_3.png"
            at main_menu_show_btn(0.3)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [
                Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),
                If(persistent.tutorial_shown,
                    Start("ac3_03ichika"),
                    Confirm("上滑↑：打开历史文本界面\n下滑↓：打开存档界面\n左滑←：回退上一条对话\n右滑→：快进\n手势教程在您确认后不再显示，请截图或牢记",
                        [SetVariable("persistent.tutorial_shown", True), Start("ac3_03ichika")]
                    )
                )
            ]
        imagebutton:
            xalign 1.0
            idle "gui/hachimi_gui/chapter/chapter_nana_1.png"
            hover "gui/hachimi_gui/chapter/chapter_nana_2.png"
            selected_idle "gui/hachimi_gui/chapter/chapter_nana_3.png"
            selected_hover "gui/hachimi_gui/chapter/chapter_nana_3.png"
            at main_menu_show_btn(0.4)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [
                Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),
                If(persistent.tutorial_shown,
                    Start("ac3_04nana"),
                    Confirm("上滑↑：打开历史文本界面\n下滑↓：打开存档界面\n左滑←：回退上一条对话\n右滑→：快进\n手势教程在您确认后不再显示，请截图或牢记",
                        [SetVariable("persistent.tutorial_shown", True), Start("ac3_04nana")]
                    )
                )
            ]
    vbox:
        xpos 0.55
        ypos 0.17
        spacing 16
        imagebutton:
            xalign 0.0
            idle "gui/hachimi_gui/chapter/chapter_kaguya_1.png"
            hover "gui/hachimi_gui/chapter/chapter_kaguya_2.png"
            selected_idle "gui/hachimi_gui/chapter/chapter_kaguya_3.png"
            selected_hover "gui/hachimi_gui/chapter/chapter_kaguya_3.png"
            at main_menu_show_btn_2(0.1)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [
                Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),
                If(persistent.tutorial_shown,
                    Start("ac3_05kaguya"),
                    Confirm("上滑↑：打开历史文本界面\n下滑↓：打开存档界面\n左滑←：回退上一条对话\n右滑→：快进\n手势教程在您确认后不再显示，请截图或牢记",
                        [SetVariable("persistent.tutorial_shown", True), Start("ac3_05kaguya")]
                    )
                )
            ]
        imagebutton:
            xalign 0.0
            idle "gui/hachimi_gui/chapter/chapter_mitsuki_1.png"
            hover "gui/hachimi_gui/chapter/chapter_mitsuki_2.png"
            selected_idle "gui/hachimi_gui/chapter/chapter_mitsuki_3.png"
            selected_hover "gui/hachimi_gui/chapter/chapter_mitsuki_3.png"
            at main_menu_show_btn_2(0.2)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [
                Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),
                If(persistent.tutorial_shown,
                    Start("ac3_06mitsuki1"),
                    Confirm("上滑↑：打开历史文本界面\n下滑↓：打开存档界面\n左滑←：回退上一条对话\n右滑→：快进\n手势教程在您确认后不再显示，请截图或牢记",
                        [SetVariable("persistent.tutorial_shown", True), Start("ac3_06mitsuki1")]
                    )
                )
            ]
        imagebutton:
            xalign 0.0
            idle "gui/hachimi_gui/chapter/chapter_kohana_1.png"
            hover "gui/hachimi_gui/chapter/chapter_kohana_2.png"
            selected_idle "gui/hachimi_gui/chapter/chapter_kohana_3.png"
            selected_hover "gui/hachimi_gui/chapter/chapter_kohana_3.png"
            at main_menu_show_btn_2(0.3)
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [
                Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),
                If(persistent.tutorial_shown,
                    Start("ac3_07kohana1"),
                    Confirm("上滑↑：打开历史文本界面\n下滑↓：打开存档界面\n左滑←：回退上一条对话\n右滑→：快进\n手势教程在您确认后不再显示，请截图或牢记",
                        [SetVariable("persistent.tutorial_shown", True), Start("ac3_07kohana1")]
                    )
                )
            ]
        imagebutton:
            xalign 0.0
            if (persistent.mikuri_clear and 
                persistent.chieri_clear and 
                persistent.ichika_clear and 
                persistent.nana_clear and 
                persistent.kaguya_clear and 
                persistent.mitsuki_clear and 
                persistent.kohana_clear):
                idle "gui/hachimi_gui/chapter/chapter_harem_1.png"
                hover "gui/hachimi_gui/chapter/chapter_harem_2.png"
                selected_idle "gui/hachimi_gui/chapter/chapter_harem_3.png"
                selected_hover "gui/hachimi_gui/chapter/chapter_harem_3.png"
                at main_menu_show_btn_2(0.4)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Start("ac3_08harem")]
            else:
                idle "gui/hachimi_gui/chapter/chapter_haremu_0.png"
                hover white_overlay_0("gui/hachimi_gui/chapter/chapter_haremu_0.png", 0.35, 621, 173)
                selected_idle white_overlay_0("gui/hachimi_gui/chapter/chapter_haremu_0.png", 0.35, 621, 173)
                selected_hover white_overlay_0("gui/hachimi_gui/chapter/chapter_haremu_0.png", 0.35, 621, 173)
                at main_menu_show_btn_2(0.4)
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Alert("您必须通关其余章节后\n才能解锁该隐藏章节")]
    imagebutton:
        xpos 0.77
        ypos 0.94
        idle "gui/hachimi_gui/under_button/under_title_1.png"
        hover "gui/hachimi_gui/under_button/under_title_2.png"
        selected_idle "gui/hachimi_gui/under_button/under_title_2.png"
        selected_hover "gui/hachimi_gui/under_button/under_title_2.png"
        at main_menu_show_btn_3(0.4)
        hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
        action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),Return()]