# 以下代码全部由天马咲希型千趣编写，属于 UI 代码
# 禁止未通知本人的情况下修改本文件代码的任何部分或数值
# 一旦未经告知本人而进行修改，出现任何问题，不负责任何维护义务，因为那不是我造成的，不要给我徒增工作量，谢谢喵
# 目前的代码已经过充分的测试验证过可行性与稳定性，因为修改文件导致新增的潜在Bug，也请自己测试与负责

define config.skip_delay = 1

transform main_menu_show_btn(wait = 0):
    xoffset -100
    alpha 0.0
    pause(wait)
    easein 0.2 xoffset 0 alpha 1

transform main_menu_show_btn_2(wait = 0):
    xoffset 100
    alpha 0.0
    pause(wait)
    easein 0.2 xoffset 0 alpha 1

transform main_menu_show_btn_3(wait = 0):
    yoffset 100
    alpha 0.0
    pause(wait)
    easein 0.2 yoffset 0 alpha 1

init python:
    renpy.music.register_channel('sys_sound_1', mixer="sfx", loop=False)
    renpy.music.register_channel('sys_sound_2', mixer="sfx", loop=False)
    renpy.music.register_channel('sys_sound_3', mixer="sfx", loop=False)

screen movie_player(filename, video_end):
    modal True
    zorder 200
    add "images/misc/black.png"
    on "show" action Stop("music")
    add Movie(play=f"mv/{filename}", loop=False, channel='movie') xalign 0.5 yalign 0.5
    textbutton "跳过▸":
        xalign 0.95
        yalign 0.05
        text_size 60
        text_color "#ffffff"
        text_outlines [(2, "#000000", 0, 0)]
        text_hover_color "#ff6666"
        action [Hide("movie_player"), Return()]  
    key "K_ESCAPE" action [Hide("movie_player"), Return()]
    key "mousedown_3" action [Hide("movie_player"), Return()]
    if video_end is not None and video_end > 0:
        timer video_end action [Hide("movie_player"), Return()]

define config.rollback_length = 99999
define config.hard_rollback_limit = 99999

style say_dialogue:
    line_spacing 15
    kerning 2

default preferences.voice_sustain = True

default preferences.normal_text_cps = 45

default preferences.afm_text_cps = 50

default preferences.skip_unseen = False

default persistent.text_color_changeable = True

default preferences.text_shadow = True

default persistent.textbox_transparency = 0.2

default persistent.last_voice = None

define textbox_preview_repeat_time = 3.0

default countdown_time = 0.0

default persistent.text_normal=True

default persistent.text_auto=False

screen textbox_preview():
    tag preview
    frame:
        pos (1000,873)
        background None
        if persistent.text_normal == True:
            text "{font=font/MaokenAssortedSans-Lite.otf}{size=44}{color=#ffffff}巧克甜恋 3 BGI → Ren'Py跨引擎移植版{/color}{/size}{/font}":
                xoffset 20
                yoffset 10
                color "#606060"
                slow_cps preferences.normal_text_cps
        else:
            text "{font=font/MaokenAssortedSans-Lite.otf}{size=44}{color=#ffffff}巧克甜恋 3 BGI → Ren'Py跨引擎移植版{/color}{/size}{/font}":
                xoffset 20
                yoffset 10
                color "#606060"
                slow_cps preferences.afm_text_cps

#default temp_voice_path = None

default preferences.voice_sustain = True

default preferences.wait_voice = True

default persistent.windows_api = 1

default persistent.android_api = 1

default persistent.linux_api = 1

default persistent.mac_api = 1

default preferences.emphasize_audio = True

define config.emphasize_audio_channels = [ 'voice', 'char_voice' ]

define config.emphasize_audio_time = 0.25

define config.emphasize_audio_volume = 0.45

default persistent.voicing_bgm_volume = 0.45

default preferences.volume.music = 0.75

init python:
    def _apply_voicing_bgm_volume_if_needed():
        try:
            target = float(persistent.voicing_bgm_volume)
            if config.emphasize_audio_volume != target:
                config.emphasize_audio_volume = target
        except Exception:
            pass
    _apply_voicing_bgm_volume_if_needed()

default persistent.mikuri_clear = False
default persistent.chieri_clear = False
default persistent.ichika_clear = False
default persistent.nana_clear = False
default persistent.kaguya_clear = False
default persistent.mitsuki_clear = False
default persistent.kohana_clear = False
default persistent.harem_clear = False

label start:
    scene black with dissolve
    "你刚刚可能经过了一个异常场景或者触发了某个Bug。"
    "当程序出现异常时，会将你带到此脚本处，避免引起游戏崩溃。"
    "你可以返回标题界面，或读取存档以继续游戏。"
    "再次点击将默认返回标题界面。"
    return



screen cg_viewer(group, index=0):
    modal True
    default i = index
    $ imgs = cg_groups.get(group, [])

    key "mousedown_3" action [With(Dissolve(0.3)), Hide("cg_viewer")]
    key "K_ESCAPE" action [With(Dissolve(0.3)), Hide("cg_viewer")]
    key "K_LEFT" action If(i > 0, [SetScreenVariable("i", i-1), Function(lambda : renpy.transition(Dissolve(0.30)))])
    key "K_RIGHT" action If(i < len(imgs)-1, [SetScreenVariable("i", i+1), Function(lambda : renpy.transition(Dissolve(0.30)))], [With(Dissolve(0.3)), Hide("cg_viewer")])

    if imgs:
        add imgs[i]
        text "[i+1]/[len(imgs)]":
            xpos 0.98 ypos 0.02 xanchor 1.0 size 70 color "#ffffff" outlines [(2, "#000000",absolute(0), absolute(0))]
        button:
            xfill True
            yfill True
            action If(
                i < len(imgs)-1,
                [ SetScreenVariable("i", i+1),
                Function(lambda : renpy.transition(Dissolve(0.30))) ],
                [ With(Dissolve(0.3)), Hide("cg_viewer") ]
            )

        vbox:
            align (0.99, 0.98)
            spacing 30
            textbutton "上一张":
                text_size 50
                text_color "#ffffff"
                text_outlines [(2, "#000000", 0, 0)]
                text_hover_color "#ffcc00"
                action If(i > 0, [SetScreenVariable("i", i-1), Function(lambda : renpy.transition(Dissolve(0.30)))])
                sensitive i > 0
                if i <= 0:
                    at transform:
                        alpha 0.4
            
            textbutton "下一张":
                text_size 50
                text_color "#ffffff"
                text_outlines [(2, "#000000", 0, 0)]
                text_hover_color "#ffcc00"
                action If(i < len(imgs)-1, [SetScreenVariable("i", i+1), Function(lambda : renpy.transition(Dissolve(0.30)))])
                sensitive i < len(imgs)-1
                if i >= len(imgs)-1:
                    at transform:
                        alpha 0.4
            
            textbutton "返回":
                text_size 50
                text_color "#ffffff"
                text_outlines [(2, "#000000", 0, 0)]
                text_hover_color "#ff6666"
                action [With(Dissolve(0.3)), Hide("cg_viewer")]
                
    else:
        frame:
            align (0.5,0.5)
            text "错误！未找到图片组 [group]" size 40
        imagebutton:
            xpos 0.43
            ypos 0.6
            idle "gui/hachimi_gui/confirm/confirm_yes_1.png"
            hover "gui/hachimi_gui/confirm/confirm_yes_2.png"
            action [With(Dissolve(0.3)), Hide("cg_viewer")]

init python:
    def _make_bordered(displayable, w, h, white=2, black=2):
        total = white + black
        return LiveComposite(
            (w + 2*total, h + 2*total),
            (0, 0), Solid("#000000", xysize=(w + 2*total, h + 2*total)),
            (black, black), Solid("#FFFFFF", xysize=(w + 2*white, h + 2*white)),
            (black + white, black + white), displayable
        )

    def bordered_image(path, white=2, black=2, size=None):
        if size:
            w, h = size
            base = Transform(path, size=size)
        else:
            w, h = renpy.image_size(path)
            base = path
        return _make_bordered(base, w, h, white, black)

    def white_overlay(path, alpha=0.35, w=None, h=None,
                    border=False, white=2, black=2, keep_size=False):
        if w is not None and h is not None:
            size = (w, h)
        elif w is None and h is None:
            size = None
        else:
            ow, oh = renpy.image_size(path)
            size = (w or ow, h or oh)

        if size:
            sw, sh = size
            base_img = Transform(path, size=size)
        else:
            sw, sh = renpy.image_size(path)
            base_img = path

        overlay = Transform(Solid("#FFFFFF", xysize=(sw, sh)), alpha=alpha)
        comp = LiveComposite(
            (sw, sh),
            (0, 0), base_img,
            (0, 0), overlay
        )

        if border:
            if keep_size and size:
                inner_w = sw - 2*(white+black)
                inner_h = sh - 2*(white+black)
                if inner_w > 0 and inner_h > 0:
                    inner = Transform(comp, size=(inner_w, inner_h))
                    comp = LiveComposite(
                        (sw, sh),
                        (0, 0), Solid("#000000", xysize=(sw, sh)),
                        (black, black), Solid("#FFFFFF", xysize=(sw - 2*black, sh - 2*black)),
                        (black + white, black + white), inner
                    )
                else:
                    comp = _make_bordered(comp, sw, sh, white, black)
            else:
                comp = _make_bordered(comp, sw, sh, white, black)
        return comp

init python:
    def white_overlay_0(path, alpha=0.35, w=370, h=208):
        base = Transform(path, size=(w, h))
        white = Solid("#FFFFFF", xysize=(w, h))
        overlay = AlphaMask(white, base)
        return LiveComposite(
            (w, h),
            (0, 0), base,
            (0, 0), Transform(overlay, alpha=alpha)
        )

init python:
    mr = MusicRoom(fadein = 0.5 , fadeout = 0.5)
    mr.add("audio/bgm/bgm001.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm002.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm003.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm004.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm005.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm011.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm012.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm013.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm014.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm015.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm101.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm102.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm103.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm104.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm105.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm106.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm107.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm108.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm109.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm201.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm202.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm601.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm602.ogg",always_unlocked = True)
    mr.add("audio/bgm/bgm603.ogg",always_unlocked = True)

init python:
    def get_audio_duration(channel="music"):
        duration = renpy.music.get_duration(channel)
        return convert_format(int(duration))
        
 
    def get_audio_position(channel="music"):
        music_pos = renpy.music.get_pos(channel)
        
        if music_pos:
            return convert_format(int(music_pos))
        return "00:00"

    def convert_format(second):
        minute = second // 60
        second = second % 60
        result = ""
        if minute:
            
            if minute < 10:
                result = '0' + str(minute) + ":" + str(second)
                if second < 10:
                    result ='0' + str(minute) + ":" '0' + str(second)
            else:
                result = str(minute) + ":" + str(second)
                if second < 10:
                    result = str(minute) + '0' + str(second)
                       
        else:

            if second < 10:
                result = '00:0' + str(second)
            else:
                result = '00:' + str(second)

        return result

define config.pre_screenshot_actions = [Call("_hide_windows")]

init python:

    def Alert(message, ok=None):
        return renpy.store.Function(renpy.show_screen, "alert", message=message, ok_action=ok)
screen alert(message, ok_action=None):


    modal True

    zorder 200
    fixed at confirm_bg_appear:
        add "gui/hachimi_gui/confirm/confirm_bg.png"

    fixed at confirm_box_appear:
        add "gui/hachimi_gui/confirm/confirm_box.png" xalign 0.47 yalign 0.5

        text _(message):
            layout "subtitle"
            color "#553015" 
            outlines [(2, "#ffffff", 0, 0)]
            size 36
            align (0.492,0.45)
            text_align 0.5
            line_spacing 26
            xoffset -10

        hbox:
            align (0.486,0.675)
            imagebutton:
                idle "gui/hachimi_gui/confirm/confirm_yes_1.png" at Transform(zoom=1.3)
                hover "gui/hachimi_gui/confirm/confirm_yes_2.png"   
                hovered Play("sys_sound_1","gui/hachimi_gui/sound/sys_sound_1.ogg")
                action (Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), ok_action if ok_action else Hide("alert"))
                
    key "mousedown_3" action (Play("sys_sound_2","gui/hachimi_gui/sound/sys_sound_2.ogg"), ok_action if ok_action else Hide("alert"))