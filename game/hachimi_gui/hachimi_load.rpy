screen hachimi_load():
    tag menu
    modal True
    key "mousedown_3" action [Play("sys_sound_3","gui/hachimi_gui/sound/sys_sound_3.ogg"),Return()]
    add "gui/hachimi_gui/save_load/load_bg.png"
    default page_name_value = FilePageNameInputValue(pattern=_(""), auto=_(""), quick=_(""))
    default page_group = 0   # 0..9，每组10页，共100页
    on "show" action SetScreenVariable("page_group", get_page_group_from_current_page())
    on "replace" action SetScreenVariable("page_group", get_page_group_from_current_page())
    grid 5 2:
        xalign 0.5
        yalign 0.57
        xspacing 20
        yspacing 14
        image "gui/hachimi_gui/save_load/save_load_data.png"
        image "gui/hachimi_gui/save_load/save_load_data.png"
        image "gui/hachimi_gui/save_load/save_load_data.png"
        image "gui/hachimi_gui/save_load/save_load_data.png"
        image "gui/hachimi_gui/save_load/save_load_data.png"
        image "gui/hachimi_gui/save_load/save_load_data.png"
        image "gui/hachimi_gui/save_load/save_load_data.png"
        image "gui/hachimi_gui/save_load/save_load_data.png"
        image "gui/hachimi_gui/save_load/save_load_data.png"
        image "gui/hachimi_gui/save_load/save_load_data.png"
    fixed:
        order_reverse True
        button:
            style "page_label"
            key_events True
            xalign 0.5
            action page_name_value.Toggle()
            input:
                style "page_label_text"
                value page_name_value
        grid 5 2:
            style_prefix "slot"
            xpos 0.045
            ypos 0.1992
            xspacing 47
            yspacing 236
            for i in range(5 * 2):
                $ slot = i + 1
                button:
                    action [With(dissolve), Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), FileLoad(slot)]
                    add FileScreenshot(slot) xalign 0.5 yalign 0.5
                    text FileTime(slot, format=_("{color=#ffffff}{size=25}%Y/%m/%d  %H:%M{/size}{/color}"), empty=_("")):
                        outlines [(2, "#4f4f4f",absolute(0), absolute(0))]
                        xalign 0.9
                        yalign -0.67
                        style "slot_time_text"
                    text FileSaveName(slot):
                        style "slot_name_text"
                        ypos 1.42
                    text FileSlotName(slot, 10, auto='A', quick='Q', format='%s%d'):
                        outlines [(2, "#4f4f4f",absolute(0), absolute(0))]
                        xcenter 0.07
                        ycenter -0.35
                    imagebutton:
                        xpos 0.34
                        ypos 1.83
                        at transform:
                            zoom 0.8
                        idle "gui/hachimi_gui/save_load/save_load_delete_1.png"
                        hover "gui/hachimi_gui/save_load/save_load_delete_2.png"
                        selected_idle "gui/hachimi_gui/save_load/save_load_delete_2.png"
                        selected_hover "gui/hachimi_gui/save_load/save_load_delete_2.png"
                        insensitive "gui/hachimi_gui/save_load/save_load_delete_3.png"
                        hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                        action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),With(Dissolve(0.3)),FileDelete(slot)]
                    key "save_delete" action FileDelete(slot)
        hbox:
            style_prefix "page"
            xalign 0.565
            yalign 0.032
            spacing (33 if page_group == 0 else 12)
            $ start = page_group * 10 + 1
            $ end = min(start + 9, 100)
            for page in range(start, end + 1):
                textbutton "{font=font/LoliSC.ttc}{size=47}[page]{/size}{/font}":
                    action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), With(Dissolve(0.3)), FilePage(page)]
        if config.has_quicksave:
            imagebutton:
                xpos 0.83
                ypos 0.04
                at transform:
                    zoom 1.3
                idle "gui/hachimi_gui/save_load/save_load_quick_1.png"
                hover "gui/hachimi_gui/save_load/save_load_quick_2.png"
                selected_idle "gui/hachimi_gui/save_load/save_load_quick_2.png"
                selected_hover "gui/hachimi_gui/save_load/save_load_quick_2.png"
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), With(Dissolve(0.3)), FilePage("quick")]
        # if config.has_autosave:
        #     imagebutton:
        #         xpos 0.88
        #         ypos 0.04
        #         at transform:
        #             zoom 1.3
        #         idle "gui/hachimi_gui/save_load/save_load_auto_1.png"
        #         hover "gui/hachimi_gui/save_load/save_load_auto_2.png"
        #         selected_idle "gui/hachimi_gui/save_load/save_load_auto_2.png"
        #         selected_hover "gui/hachimi_gui/save_load/save_load_auto_2.png"
        #         hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
        #         action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), With(Dissolve(0.3)), FilePage("auto")]
        imagebutton:
            xpos 0.253
            ypos 0.04
            at transform:
                zoom 1.7
            insensitive "gui/hachimi_gui/save_load/save_load_previous_0.png"
            idle "gui/hachimi_gui/save_load/save_load_previous_1.png"
            hover "gui/hachimi_gui/save_load/save_load_previous_2.png"
            selected_idle "gui/hachimi_gui/save_load/save_load_previous_2.png"
            selected_hover "gui/hachimi_gui/save_load/save_load_previous_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), SetScreenVariable("page_group", page_group - 1), With(Dissolve(0.3)), FilePage((page_group - 1) * 10 + 1)]
            sensitive page_group > 0
        imagebutton:
            xpos 0.78
            ypos 0.04
            at transform:
                zoom 1.7
            insensitive "gui/hachimi_gui/save_load/save_load_next_0.png"
            idle "gui/hachimi_gui/save_load/save_load_next_1.png"
            hover "gui/hachimi_gui/save_load/save_load_next_2.png"
            selected_idle "gui/hachimi_gui/save_load/save_load_next_2.png"
            selected_hover "gui/hachimi_gui/save_load/save_load_next_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), SetScreenVariable("page_group", page_group + 1), With(Dissolve(0.3)), FilePage((page_group + 1) * 10 + 1)]
            sensitive page_group < 9
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
            idle "gui/hachimi_gui/under_button/under_load_2.png"
        imagebutton:
            idle "gui/hachimi_gui/under_button/under_config_1.png"
            hover "gui/hachimi_gui/under_button/under_config_2.png"
            selected_idle "gui/hachimi_gui/under_button/under_config_2.png"
            selected_hover "gui/hachimi_gui/under_button/under_config_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"),ShowMenu("hachimi_text_config")]
        imagebutton:
            idle "gui/hachimi_gui/under_button/under_return_1.png"
            hover "gui/hachimi_gui/under_button/under_return_2.png"
            selected_idle "gui/hachimi_gui/under_button/under_return_2.png"
            selected_hover "gui/hachimi_gui/under_button/under_return_2.png"
            hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
            action [Play("sys_sound_3","gui/hachimi_gui/sound/sys_sound_3.ogg"),Return()]
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