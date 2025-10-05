### 函数调用及参数注册和存储 ###
default BUST_LAST_LAYER = {}
default STORE_BUST_POS = {}
default BUST_DELAY_TIMERS = {}
default BUST_DISPLAY_STATE = {}  # 存储每个图层的显示状态
default FLASH_CALLED = False
default FONT_SIZE = None
default EF_KAISOU_ACTIVE = False
default SPR_DISPLAY = {}
default BUST_FADEIN_END_TIMERS = {}
default CURRENT_EVENT_CG = {}
default SCHEDULED_PENDING_LAYERS = []
default SCHEDULED_LAST_LAYERS = []
default temp_voice_path = None
default textbox_mode = 0
default persistent.voice_interrupt_on_page = True
default persistent.character_volumes = {
    "chi": 1.0,
    "ich": 1.0,
    "kag": 1.0,
    "koh": 1.0,
    "mik": 1.0,
    "nan": 1.0,
    "mit": 1.0,
    "tuk": 1.0,
    "mom": 1.0,     # 其他男人
    "mof": 1.0,     # 其他女人
}
default persistent.complete_flags = [False,False,False,False,False,False,False]        # 通关记录
default interruptible_cg_tag = None
default interruptible_bserase_tags = []
default MOVEBS_DELAY = 0
default WHITE_BG_ACTIVE = False
init python:
    import re,math,random
    renpy.music.register_channel("se","sfx")
    renpy.music.register_channel("char_voice", "voice", loop=False)
    def _attach_voice_to_history(entry):
        try:
            # 使用 getattr 避免 lint 在 default 尚未执行时报错
            _lv = getattr(persistent, 'last_voice', None)
            entry.replay_voice = _lv if _lv else None
        except Exception:
            entry.replay_voice = None
    if not hasattr(config, 'history_callbacks'):
        config.history_callbacks = []
    if _attach_voice_to_history not in config.history_callbacks:
        config.history_callbacks.append(_attach_voice_to_history)
    CHARACTER_SIZES = {  #支持中心点自定义覆盖
        "chi01": (936, 1544, 580, 893),
        "chi02": (729, 1530, 375, 875),
        "chi11": (1423, 1836, 707, None),
        "chi12": (1319, 1826, 725, None),
        "ich01": (746, 1598, 357, 948),
        "ich02": (707, 1614, 367, 965),
        "ich11": (1658, 1826, 762, None),
        "ich12": (1581, 1858, 813, None),
        "kag01": (612, 1572, 367, 917),
        "kag02": (736, 1572, 377, 922),
        "kag11": (1199, 1821, 685, None),
        "kag12": (1576, 1809, 788, None),
        "koh01": (887, 1540, 535, 890),
        "koh02": (859, 1554, 484, 905),
        "koh11": (1901, 1827, 1068, 1166),
        "koh12": (1833, 1838, 1100, 1170),
        "mik01": (884, 1680, 425, 1025),
        "mik02": (920, 1638, 500, 988),
        "mik11": (1971, 1917, 943, None),
        "mik12": (2057, 1839, 1050, None),
        "nan01": (958, 1714, 440, 1065),
        "nan02": (844, 1693, 363, 1030),
        "nan11": (2025, 1862, 916, None),
        "nan12": (1865, 1860, 777, None),
        "tuk01": (858, 1596, 383, 935),
        "tuk02": (852, 1606, 485, 957),
        "tuk11": (1764, 1804, 805, None),
        "tuk12": (1833, 1864, 1035, None)
    }

#======辅助函数定义======
    def create_atl_dissolve(old_img, new_img, trans_time):
        old_fading = At(old_img, Fadeout_effect(trans_time))
        new_fading = At(new_img, Fadein_effect(trans_time))
        return Transform(Fixed(old_fading, new_fading),xpos=0,ypos=0,anchor=(0, 0)) #最tm操蛋的研究出来了，至少有十几天的牺牲

    def clear_all(window):
        renpy.hide_screen("solid_bg")
        # 清理非ef_kaisou的SPR_DISPLAY条目
        for layer_id, spr_info in list(store.SPR_DISPLAY.items()):
            if spr_info["filename"] != "ef_kaisou":
                renpy.hide(spr_info["sprite_id"], layer=spr_info["layer"])
                renpy.show(spr_info["sprite_id"]+"_temp", what=At(Image(f"images/misc/{spr_info['filename']}.png"), fadeout_down_move(50,1)), layer=spr_info["layer"])
                store.interruptible_bserase_tags.append(spr_info["sprite_id"]+"_temp")
                del store.SPR_DISPLAY[layer_id]
        if window:
            _window_hide(trans=False, auto=True)
        # 复制图层ID列表（因为清除操作会修改原字典）
        layer_ids = list(store.STORE_BUST_POS.keys())[:]
        for layer_id in layer_ids:
            # 调用已有的擦除函数清除每个立绘
            _bserase([108,0,layer_id,40,400])    # 这里使用默认的原地淡出 0 

    def is_cg_active():
        """
        Checks if any tag shown on the master layer corresponds to a loadable file
        within the 'images/cg/' directory structure.
        """
        master_tags = renpy.get_showing_tags(layer='master')
        for tag in master_tags:
            # Skip any tags that aren't strings or are too short to have a subfolder.
            if not isinstance(tag, basestring) or len(tag) < 2:
                continue
            # Construct the potential path based on the project's file structure.
            # For a tag like 'hv108a', the subfolder is 'hv'.
            folder = tag[:2]
            # Check for common image extensions that exist in your project.
            potential_path_webp = f"images/cg/{folder}/{tag}.webp"
            # renpy.loadable() is the correct way to check if a file exists for Ren'Py.
            if renpy.loadable(potential_path_webp):
                # If a file exists at this constructed CG path, we have a match.
                return True
        # If we check all tags and find no corresponding CG file, return False.
        return False

    def is_all_complete():
        return all(persistent.complete_flags)

    def chapter_complete(params):
        index = params - 1
        persistent.complete_flags[index] = True

#======外部函数定义======
    def _say(params):
        persistent.last_voice = None
        # 然后，检查临时变量是否被设置了
        if store.temp_voice_path:
            # 如果有值，说明当前台词有语音，我们将这个值保存到 persistent 变量中
            persistent.last_voice = store.temp_voice_path
            # 并立即清空临时变量，防止它影响下一句台词
            store.temp_voice_path = None
        u1, u2, u3, speaker, text = params
        if store.FONT_SIZE is not None:
            formatted_text = "{{size={}}} {}{{/size}}".format(store.FONT_SIZE, text)
        else:
            formatted_text = text
        store._last_say_what = text
        _window_show(trans=False, auto=True)
        if speaker == 0:
            renpy.say(None, formatted_text)
        else:
            renpy.say(speaker, formatted_text)
        if not persistent.voice_interrupt_on_page:
            renpy.music.stop(channel="voice")
        if store.FLASH_CALLED == True:
            store.FLASH_CALLED = False
        if store.EF_KAISOU_ACTIVE == True:
            store.EF_KAISOU_ACTIVE = False
        if getattr(store, 'interruptible_cg_tag', None):
            renpy.hide(store.interruptible_cg_tag, layer='bustlayer')
            store.interruptible_cg_tag = None
        if getattr(store, 'interruptible_bserase_tags', []):
            for tag_to_hide in store.interruptible_bserase_tags:
                renpy.hide(tag_to_hide,layer = "bustlayer")
                renpy.hide(tag_to_hide,layer = "master")
                renpy.hide(tag_to_hide,layer = "top")
            store.interruptible_bserase_tags = []
        current_time = renpy.get_game_runtime()
        for layer_id, end_time in list(store.BUST_DELAY_TIMERS.items()):
            if current_time < end_time:
                renpy.log("提前结束动画")
                if layer_id in store.STORE_BUST_POS:
                    pos_info = store.STORE_BUST_POS[layer_id]
                    final_transform = Transform(pos_info["img"], xpos=pos_info["x"], ypos=pos_info["y"], anchor=(0, 0))
                    renpy.show(f"bust_{layer_id}", what=final_transform, layer="bustlayer", zorder=layer_id)
                    pos_info["transform"] = final_transform
                    del store.BUST_DELAY_TIMERS[layer_id]

    def _Wait(params):
        wait_time_ms, skippable = params
        # skippable=1=>True, skippable=0=>False
        renpy.pause(delay=wait_time_ms / 1000.0, hard=not skippable)

    def _PlayBGM(params):
        # 通道ID, 文件名, 未知参数, 循环标志, 音量(DX), 淡入时间(ms)
        channel_id, BGMname, u1, loop_flag, volume, fadein_ms = params
        filepath = "audio/bgm/" + BGMname.lower() + ".ogg"
        if channel_id == 0:
            channel = "music"
        else:
            renpy.error(f"Invalid channel ID: {channel_id}")
        loop = True if loop_flag == 1 else False
        renpy.music.set_volume(volume / 128.0, fadein_ms / 1000.0, channel)
        renpy.music.play(filepath,channel=channel,loop=loop,fadein=fadein_ms / 1000.0,relative_volume=volume / 128.0)

    def _FadeBGM(params):
        # [通道ID, 淡出时间(ms), 未知参数]
        channel_id, fade_duration_ms, u1 = params
        if channel_id == 0:
            channel = "music"
        else:
            renpy.error(f"Invalid channel ID for FadeBGM: {channel_id}")
        renpy.music.stop(channel, fade_duration_ms / 1000.0)

    def _ChangeVolumeOfBGM(params):
        # [通道ID, 目标音量, 淡出时间(ms)]
        channel_id, target_volume,fade_duration_ms  = params
        if channel_id == 0:
            channel = "music"
        else:
            renpy.error(f"Invalid channel ID for FadeBGM: {channel_id}")
        renpy.music.set_volume(target_volume / 233.3, fade_duration_ms / 1000.0, channel)

    def _PresetBG(params):
        # [背景图片名, 过渡时间(ms), 未知参数1, 未知参数2]
        bg_name, duration_ms, u1, u2 = params
        duration = duration_ms / 1000.0
        bg_path = f"images/bg/{bg_name}.webp"
        renpy.music.stop(channel="voice")
        ef_kaisou_layers = []
        for layer_id, spr_info in store.SPR_DISPLAY.items():
            if spr_info["filename"] == "ef_kaisou":
                ef_kaisou_layers.append(layer_id)
        if store.EF_KAISOU_ACTIVE:
            renpy.log(f"1")
            renpy.scene()
            renpy.show(bg_name, what=Image(bg_path), layer="master",zorder=1)
            renpy.with_statement(Dissolve(duration))
            clear_all(True)
            store.EF_KAISOU_ACTIVE = False
        else:
            # 如果有 ef_kaisou 图片
            if ef_kaisou_layers:
                renpy.log(f"2")
                renpy.scene()
                renpy.hide("ef_kaisou_img", layer="bustlayer")
                renpy.show(bg_name, what=Image(bg_path), layer="master",zorder=1)
                renpy.with_statement(Dissolve(duration))
                clear_all(True)
                del store.SPR_DISPLAY[layer_id]
            else:
                renpy.log(f"3")
                clear_all(True)
                renpy.scene()
                if bg_name.startswith('#'):
                    renpy.show_screen("solid_bg", bg_name)
                else:
                    renpy.show(bg_name, what=Image(bg_path), layer="master",zorder=1)
                renpy.with_statement(Dissolve(duration))
                if getattr(store, 'interruptible_bserase_tags', []):
                    for tag_to_hide in store.interruptible_bserase_tags:
                        renpy.hide(tag_to_hide,layer="bustlayer")
                    store.interruptible_bserase_tags = []

    def _PresetEV(params):
        # [cg图片名, 过渡时间(ms), 未知参数1, 未知参数2]
        cg_name, duration_ms, u1, u2 = params
        cg_folder = cg_name[:2]
        if cg_folder == "ex":
            cg_folder = "ev"
        ev_path = f"images/cg/{cg_folder}/{cg_name}.webp"
        clear_all(True)
        renpy.scene()
        renpy.show(cg_name, what=Image(ev_path), layer="master",zorder=1)
        renpy.with_statement(Dissolve(duration_ms / 1000.0))

    def _ExecuteScheduledControl(params):
        """
        作用：
        1. 计算当前所有相关立绘动画（淡入 / 延迟切换 / 擦除 等）的剩余时间并等待结束；
        2. 若当前无新立绘（pending 为空），仅等待动画。
        """
        u1 = params[0] if params else None
        current_time = renpy.get_game_runtime()
        max_wait = 0.0
        # 统计所有记录中的剩余时间
        for d in (store.BUST_FADEIN_END_TIMERS, store.BUST_DELAY_TIMERS):
            for layer_id, end_time in d.items():
                remain = end_time - current_time
                if remain > max_wait:
                    max_wait = remain
        # 等待（跳过模式下尽量压缩）
        if max_wait > 0:
            if renpy.get_skipping():
                renpy.pause(min(0.05, max_wait))
            else:
                renpy.pause(max_wait)
        renpy.log(f"等待立绘动画完成，等待时间 {max_wait} 秒")

    def _PlayVoice(params):
        #  [通道ID, 文件名, 音量, 未知参数（猜测为循环）]
        channel_id, Voicename, volume, u1 = params
        filepath = f"audio/voice/{Voicename}.ogg"
        # ===> 新增代码 <===
        # 将语音路径赋值给一个临时的 store 变量
        store.temp_voice_path = filepath
        # =================
        tag_name = Voicename[4:7]
        if channel_id == 0:
            channel = "voice"
        else:
            renpy.error(f"Invalid channel ID: {channel_id}")
        loop = True if u1 == 1 else False
        character_volume_multiplier = 1.0
        if tag_name and hasattr(persistent, 'character_volumes'):
            character_volume_multiplier = persistent.character_volumes.get(tag_name, 1.0)
        renpy.music.stop(channel=channel)
        renpy.music.play(filepath,channel=channel,loop=loop,relative_volume=volume / 128.0 * character_volume_multiplier)

    def _bustshot(params):
        if is_cg_active(): return
        layer_id, bust_name, pos_x, fadein_time_ms, u2 = params
        base_key = "_".join(bust_name.split("_")[:-1])  # 'mik01C'
        ch_folder = bust_name[:3]
        composited_path = f"images/character_composited/{ch_folder}/{bust_name}.webp"
        bust_img = Image(composited_path)
        size_info = CHARACTER_SIZES.get(base_key[:5], (920, 1638, None, None))
        width, height, center_x, center_y = size_info
        if center_x is None:
            center_x = width // 2
        if center_y is None:
            if base_key[3:5] == "01" or base_key[3:5] == "02":
                center_y = int(height * 0.60)
            else:
                center_y = int(height * 0.645)
        screen_x = 1920 // 2
        screen_y = 1080
        offset_x = 0
        # 处理图层ID（处理继承）
        bust_key = bust_name[:3]  # 'mik'
        if layer_id == -1:
            # 获取角色对应的图层ID
            layer_id = store.BUST_LAST_LAYER.get(bust_key, 5)
            # 继承该图层的位置偏移值
            if layer_id in store.STORE_BUST_POS:
                offset_x = store.STORE_BUST_POS[layer_id].get("offset_x", 0)
        else:
            store.BUST_LAST_LAYER[bust_key] = layer_id
            # 如果图层已存在，继承其偏移值
            if layer_id in store.STORE_BUST_POS:
                offset_x = store.STORE_BUST_POS[layer_id].get("offset_x", 0)
        # 处理位置参数
        if abs(pos_x) >= 1000:
            delay_time = pos_x / 1000.0
            # 延时切换时不改变偏移值，保持当前继承的值
        else:
            # 只有明确指定偏移时才更新
            if pos_x != 0:
                offset_x = pos_x
            delay_time = 0
        # 计算最终显示位置
        target_x = screen_x + offset_x - center_x
        target_y = screen_y - center_y
        # 使用专用层显示立绘
        layer = "bustlayer"
        sprite_id = f"bust_{layer_id}"
        # 检查是否是首次显示（即该图层没有立绘）
        is_new = layer_id not in store.STORE_BUST_POS
        # 获取上次显示状态（如果存在）
        last_was_new = store.BUST_DISPLAY_STATE.get(layer_id, False)  
        same_pose = False
        same_pose_diff_expression = False
        if not is_new and layer_id in store.STORE_BUST_POS:
            current_info = store.STORE_BUST_POS[layer_id]
            current_base = current_info.get("base_key", "")
            current_full_name = current_info.get("full_name", "")
            same_pose = (current_base == base_key)  # 检查base_key是否相同
            # 检查是否为同一姿势但不同表情（完整文件名不同但base_key相同）
            same_pose_diff_expression = same_pose and current_full_name != bust_name
            if same_pose and not same_pose_diff_expression: # 如果是完全相同的姿势和表情，直接使用当前的位置信息
                target_x = current_info["x"]
                target_y = current_info["y"]
        fadein_time =  fadein_time_ms / 1000.0
        if renpy.get_skipping():
            fadein_time = 0.05
        # 处理新立绘的显示
        if is_new:# 首次出场，用淡入变换
            bust_show = At(Transform(bust_img, xpos=target_x, ypos=target_y, anchor=(0, 0)), bust_fadein(fadein_time))
            renpy.show(sprite_id, what=bust_show, layer=layer, zorder=layer_id)
            store.BUST_FADEIN_END_TIMERS[layer_id] = renpy.get_game_runtime() + fadein_time
        else:
            current_info = store.STORE_BUST_POS[layer_id]
            current_img = current_info["img"]
            current_x = current_info["x"]
            current_y = current_info["y"]
            # 检查是否有正在进行的淡入动画（由_bustshotFadein创建）
            is_fadein_active = False
            current_time = renpy.get_game_runtime()
            fadein_end_time = store.BUST_FADEIN_END_TIMERS.get(layer_id, 0)
            if fadein_end_time > current_time:
                is_fadein_active = True
            if delay_time > 0:  # 处理延迟切换的情况
                renpy.log("2")
                if last_was_new or is_fadein_active:
                    # 如果是淡入动画或新立绘，保留当前的动画状态
                    current_transform = current_info.get("transform", None)
                    if current_transform:
                        old_img_at_current_pos = current_transform
                    else:
                        old_img_at_current_pos = At(Transform(current_img, xpos=current_x, ypos=current_y, anchor=(0, 0)), bust_fadein(fadein_time))
                else:
                    old_img_at_current_pos = Transform(current_img, xpos=current_x, ypos=current_y, anchor=(0, 0))
                new_img_at_target_pos = Transform(bust_img, xpos=target_x, ypos=target_y, anchor=(0, 0))
                switch = delayed_switch(old_img_at_current_pos, new_img_at_target_pos, delay_time, fadein_time)
                renpy.show(sprite_id, what=switch, layer=layer, zorder=layer_id)
                store.BUST_DELAY_TIMERS[layer_id] = renpy.get_game_runtime() + delay_time
                store.BUST_FADEIN_END_TIMERS[layer_id] = renpy.get_game_runtime() + fadein_time
                store.STORE_BUST_POS[layer_id] = {"x": target_x, "y": target_y, "img": bust_img, "transform": switch, "offset_x": offset_x, "base_key": base_key, "full_name": bust_name}
                return
            elif not same_pose or same_pose_diff_expression:# 不同姿势切换或同一姿势不同表情切换
                renpy.log("3")
                if is_fadein_active: return
                # 直接使用 renpy.show 和 with 语句进行 dissolve
                old_at_pos = Transform(current_img, xpos=current_x, ypos=current_y, anchor=(0, 0))
                new_at_pos = Transform(bust_img, xpos=target_x, ypos=target_y, anchor=(0, 0))
                # 确保旧图片在正确位置显示
                renpy.show(sprite_id, what=old_at_pos, layer=layer, zorder=layer_id)
                # 使用 with 语句进行 dissolve 到新位置
                renpy.show(sprite_id, what=new_at_pos, layer=layer, zorder=layer_id)
                renpy.with_statement(Dissolve(fadein_time))
                store.BUST_FADEIN_END_TIMERS[layer_id] = renpy.get_game_runtime() + fadein_time
                store.STORE_BUST_POS[layer_id] = {"x": target_x,"y": target_y,"img": bust_img,"offset_x": offset_x,"transform": new_at_pos,"base_key": base_key, "full_name": bust_name}
                return
            else:# 完全相同的姿势和表情，使用直接替换（无渐变）
                renpy.log("4")
                bust_show = Transform(bust_img, xpos=target_x, ypos=target_y, anchor=(0, 0))
                renpy.show(sprite_id, what=bust_show, layer=layer, zorder=layer_id)
        store.STORE_BUST_POS[layer_id] = {"x": target_x,"y": target_y,"img": bust_img,"offset_x": offset_x,"transform": bust_show,"base_key": base_key, "full_name": bust_name}
        store.BUST_DISPLAY_STATE[layer_id] = is_new
        if layer_id not in store.SCHEDULED_PENDING_LAYERS:
            store.SCHEDULED_PENDING_LAYERS.append(layer_id)

    def _BustshotMotion(params):
        if is_cg_active(): return
        u0,layer_id,u1,direction,u2,u3 = params # direction控制移动轴和次数
        if layer_id == -1:
            bust_name = params[6] if len(params) > 6 else None
            if bust_name:
                bust_key = bust_name[:3]
                layer_id = store.BUST_LAST_LAYER.get(bust_key, 5)
        # 获取淡入动画结束时间（如果存在）
        fadein_end_time = store.BUST_FADEIN_END_TIMERS.get(layer_id, 0)
        current_time = renpy.get_game_runtime()
        fadein_delay = max(0, fadein_end_time - current_time)  # 计算需要等待的时间
        # 获取已有的延迟时间（用于处理延迟切换）
        delay_remaining = 0
        if layer_id in store.BUST_DELAY_TIMERS:
            end_time = store.BUST_DELAY_TIMERS[layer_id]
            if current_time < end_time:
                delay_remaining = end_time - current_time
        total_delay = fadein_delay + delay_remaining
        if layer_id not in store.STORE_BUST_POS:
            renpy.error(f"Layer {layer_id} not found in STORE_BUST_POS.")
            return
        # 使用专用层
        layer = "bustlayer"
        sprite_id = f"bust_{layer_id}"
        # 从字典中获取所有必要信息
        pos_info = store.STORE_BUST_POS[layer_id]
        target_x = pos_info["x"]
        target_y = pos_info["y"]
        bust_img = pos_info["img"]
        base_transform = pos_info["transform"]
        # 创建基础 Transform 对象
        bust_transform = Transform(bust_img,xpos=target_x,ypos=target_y,anchor=(0, 0))
        # 确定动画类型和参数
        count = max(1, (direction // 10) % 10) // 2  # 取十位数作为次数
        count = 1 if count == 0 else count  # 处理0次的情况
        if direction >= 100:#TODO:dy和dx参数是振动幅度，目前还没找到规律，先写死了
            # 横向移动（左右晃动）
            atl_transform = multi_shake(count, dx=8, base_duration=0.60, delay_time=total_delay)
        else:
            # 纵向移动（点头）
            atl_transform = multi_nod(count, dy=10, base_duration=0.25, delay_time=total_delay)
        # 将动画和返回原位置显示
        #TODO:如果用户点击较快要取消振动动画
        renpy.show(sprite_id, at_list=[atl_transform], layer=layer, zorder=layer_id)
        renpy.show(sprite_id, what=base_transform, layer=layer, zorder=layer_id)

    def _bserase(params):
        erase_flag = params[1]
        layer_id = params[2]
        distance = params[3]
        duration = params[4] / 1000.0
        layer = "bustlayer"
        sprite_id = f"bust_{layer_id}"
        fadeout_tag = f"bust_{layer_id}_fadeout"
        fadein_end_time = store.BUST_FADEIN_END_TIMERS.get(layer_id, 0)
        current_time = renpy.get_game_runtime()
        delay = max(0, fadein_end_time - current_time)
        # 检查是否有延迟擦除计时器
        if layer_id in store.BUST_DELAY_TIMERS:
            del store.BUST_DELAY_TIMERS[layer_id]
        # 检查是否有淡入结束计时器
        if layer_id in store.BUST_FADEIN_END_TIMERS:
            del store.BUST_FADEIN_END_TIMERS[layer_id]
        # 移除显示状态
        if layer_id in store.BUST_DISPLAY_STATE:
            del store.BUST_DISPLAY_STATE[layer_id]
        # 如果图层存在，执行擦除
        if layer_id in store.STORE_BUST_POS:
            info = store.STORE_BUST_POS[layer_id]
            img = info['img']
            x = info['x']
            y = info['y']
            if erase_flag == 1:
                fadeout_transform = At(Transform(img, xpos=x, ypos=y, anchor=(0, 0)),bustshot_left_fade(duration, -distance, delay=delay))
            elif erase_flag == 2:
                fadeout_transform = At(Transform(img, xpos=x, ypos=y, anchor=(0, 0)),bustshot_left_fade(duration, distance, delay=delay))
            elif erase_flag == 3:
                fadeout_transform = At(Transform(img, xpos=x, ypos=y, anchor=(0, 0)),bustshot_down_fade(duration, -distance, delay=delay))
            else:
                fadeout_transform = At(Transform(img, xpos=x, ypos=y, anchor=(0, 0)), bust_fadeout_and_null(0,duration))
            renpy.show(fadeout_tag, what=fadeout_transform, layer=layer, zorder=layer_id)
            # 注册这个动画的结束时间
            current_time = renpy.get_game_runtime()
            total_duration = duration + delay
            store.BUST_FADEIN_END_TIMERS[layer_id] = current_time + total_duration
            if not isinstance(store.interruptible_bserase_tags, list):
                store.interruptible_bserase_tags = []
            store.interruptible_bserase_tags.append(fadeout_tag)
            renpy.hide(sprite_id, layer=layer)
            del store.STORE_BUST_POS[layer_id]
            for bust_key, last_id in list(store.BUST_LAST_LAYER.items()):
                if last_id == layer_id:
                    del store.BUST_LAST_LAYER[bust_key]
        else:
            renpy.hide(sprite_id, layer=layer)

    def _bseraseEx(params):
        u1, erase_flag, p1, p2, p3, distance, duration = params
        layer_ids = list(store.STORE_BUST_POS.keys())[:]
        if p1 in layer_ids:
            _bserase([u1,erase_flag,p1,distance,duration])
        if p2 in layer_ids:
            _bserase([u1,erase_flag,p2,distance,duration])
        if p3 in layer_ids:
            _bserase([u1,erase_flag,p3,distance,duration])

    def _bseraseAll(params):
        layer_ids = list(store.STORE_BUST_POS.keys())[:]
        for layer_id in layer_ids:
            # 调用已有的擦除函数清除每个立绘
            _bserase([108,0,layer_id,40,400])        # 使用原地淡出的方式清除

    def _FadeScene(params):
        mask_name, u1, duration_ms = params
        ef_kaisou_layers = []
        for layer_id, spr_info in store.SPR_DISPLAY.items():
            if spr_info["filename"] == "ef_kaisou":
                ef_kaisou_layers.append(layer_id)
        clear_all(True)
        renpy.scene()
        renpy.show(f"black", what=Image("images/misc/black.png"), layer="master")
        if ef_kaisou_layers:
            for layer_id in ef_kaisou_layers:
                renpy.hide(spr_info["sprite_id"], layer=spr_info["layer"])
                del store.SPR_DISPLAY[layer_id]
                store.EF_KAISOU_ACTIVE = False
        if mask_name != 0:
            mask_path = f"images/mask/{mask_name}.png"
            renpy.with_statement(ImageDissolve(mask_path, duration_ms / 1000.0, reverse=True))
        else:
            renpy.with_statement(Dissolve(duration_ms / 1000.0))
        if getattr(store, 'interruptible_bserase_tags', []):
            for tag_to_hide in store.interruptible_bserase_tags:
                renpy.hide(tag_to_hide,layer = "bustlayer")
            store.interruptible_bserase_tags = []

    def _PlaySE(params):
        channel_id, se_name, volume, u1,loop_flag, u2 = params
        if channel_id == 0:
            channel = "se"
        else:
            renpy.error(f"Invalid channel ID for PlaySE: {channel_id}")
        filepath = f"audio/se/"+ se_name.lower() +".ogg"
        loop = True if loop_flag == 1 else False
        renpy.music.play(filepath,channel=channel,loop=loop,relative_volume=volume / 128.0)

    def _FadeSE(params):
        channel_id, fade_duration_ms = params
        if channel_id == 0:
            channel = "se"
        else:
            renpy.error(f"Invalid channel ID for FadeSE: {channel_id}")
        renpy.music.stop(channel, fade_duration_ms / 1000.0)

    def _TakeOverBG(params):
        duration_ms, u1, u2 = params
        if renpy.showing("linework"):
            f_311([1,0,0,-256])
        _window_hide(trans=False, auto=True)
        renpy.with_statement(Dissolve(duration_ms / 1000.0))

    def _Flash(params):
        dummy, color, intensity, flash_count, duration_ms = params
        flash_duration = duration_ms / 1000.0 # 每闪一次的持续时间（秒）
        _window_hide(trans=False, auto=True)
        renpy.show("flash_layer", what=Solid("#ffffff"), at_list=[flash_effect(flash_count, flash_duration)], layer="top", zorder=999)
        store.FLASH_CALLED = True
        renpy.pause(flash_duration * flash_count * 2)
        if renpy.get_skipping():
            renpy.hide("flash_layer", layer="top")

    def _DrawBS(params):
        layer_id = params[0]
        cg_name = params[1]
        duration = params[-3]/1000.0
        cg_folder = cg_name[:2]
        bs_path = f"images/cg/{cg_folder}/{cg_name}.webp"
        if cg_folder == "ex":
            zoom_val = 0.78
            x_offset = params[4]
            y_offset = params[5]
            xcenter = (960.0 + x_offset) / 1920.0
            ycenter = (540.0 + y_offset) / 1080.0
            end_xalign = 0.9
            if x_offset < 0:
                end_yalign = 0.1
            else:
                end_yalign = 0.9
            if cg_name == "ex_ev606a":
                end_xalign = 0.1
                end_yalign = 0.1
            if cg_name == "ex_ev113a":
                end_xalign = 0.1
            if cg_name == "ex_ev513a":
                zoom_val = 1.00
            bs_path = f"images/cg/ev/{cg_name}.webp"
            store.CURRENT_EVENT_CG = {"tag": cg_name,"path": bs_path, "zoom": zoom_val,"xcenter": xcenter, "ycenter": ycenter, "end_xalign": end_xalign,"end_yalign": end_yalign}
            renpy.pause(duration)
            clear_all(True)
            renpy.scene()
            initial_transform = Transform(zoom=zoom_val, xalign=xcenter, yalign=ycenter)
            renpy.show(cg_name, what=Image(bs_path), at_list=[initial_transform], layer='bustlayer')
            return
        if cg_name == "black":
            clear_all(True)
            y_offset = params[5]
            bs_path = f"images/misc/black.png"
            if y_offset > 0:
                adjusted_y =  y_offset + 275
            else:
                adjusted_y =  y_offset + 275
            target_x = 1920 // 2 - 960
            target_y = adjusted_y
            new_transform = Transform(Image(bs_path), xpos=target_x, ypos=target_y, anchor=(0, 0))
            renpy.show(f"black_{layer_id}", what=At(new_transform, multi_effect(params[17] / 100.0)), layer="master",zorder=9)
            store.interruptible_bserase_tags.append(f"black_{layer_id}")
            return
        if store.EF_KAISOU_ACTIVE:
            clear_all(True)
            renpy.scene()
            renpy.show(cg_name, what=Image(bs_path), layer="master",zorder=1)
            renpy.with_statement(Dissolve(duration))
            store.EF_KAISOU_ACTIVE = False
            return
        #判定是不是立绘文件
        character_composited_path = f"images/character_composited/{cg_name[:3]}/{cg_name}.webp"
        if renpy.loadable(character_composited_path):
            base_key = "_".join(cg_name.split("_")[:-1])
            ch_folder = cg_name[:3]
            bust_img = Image(character_composited_path)
            size_info = CHARACTER_SIZES.get(base_key[:5], (920, 1638, None, None))
            width, height, center_x, center_y = size_info
            if center_x is None:
                center_x = width // 2
            if center_y is None:
                if base_key[3:5] == "01" or base_key[3:5] == "02":
                    center_y = int(height * 0.60)
                else:
                    center_y = int(height * 0.645)
            screen_x = 1920 // 2
            screen_y = 1080
            # 处理y轴偏移
            y_offset = params[5]
            if y_offset > 0:
                adjusted_y = screen_y - center_y + y_offset
            else:
                adjusted_y = screen_y - center_y - abs(y_offset)
            target_x = screen_x - center_x
            target_y = adjusted_y
            bust_key = cg_name[:3]
            if layer_id == -1:
                layer_id = store.BUST_LAST_LAYER.get(bust_key, 5)
            else:
                store.BUST_LAST_LAYER[bust_key] = layer_id
            layer = "bustlayer"
            sprite_id = f"bust_{layer_id}"
            new_transform = Transform(bust_img, xpos=target_x, ypos=target_y, anchor=(0, 0))
            # 如果图层已存在立绘，执行溶解切换
            if layer_id in store.STORE_BUST_POS:
                renpy.show(sprite_id, what=new_transform, layer=layer, zorder=layer_id)
                renpy.with_statement(Dissolve(duration))
            else:
                renpy.show(sprite_id, what=new_transform, layer=layer, zorder=layer_id)
                renpy.with_statement(Dissolve(duration))
            store.STORE_BUST_POS[layer_id] = {"x": target_x,"y": target_y,"img": bust_img,"offset_x": 0,"transform": new_transform,"base_key": base_key,"full_name": cg_name}
            store.BUST_FADEIN_END_TIMERS[layer_id] = renpy.get_game_runtime() + duration
            return
        if not store.FLASH_CALLED:
            current_bg_tags = renpy.get_showing_tags(layer='master')
            old_tags = [tag for tag in current_bg_tags if tag != cg_name]
            if not old_tags:
                clear_all(True)
                renpy.show(cg_name, what=Image(bs_path), layer="master",zorder=1)
                renpy.with_statement(Dissolve(duration))
            else:
                clear_all(False)
                renpy.show(cg_name, what=Image(bs_path), layer="master",zorder=1)
                renpy.with_statement(Dissolve(duration))
                for tag in old_tags:
                    renpy.hide(tag, layer='master')
        else:
            clear_all(True)
            renpy.pause(duration)
            renpy.scene('master')
            renpy.show(cg_name, what=Image(bs_path), layer='master',zorder=1)

    def _FadeBS(params):
        return

    def _MoveBS(params):
        if is_cg_active(): return
        layer_id = params[0]
        dy = params[5]  # 跳跃幅度（像素）
        duration_ms = params[8] 
        if layer_id == -1:
            bust_name = params[6] if len(params) > 6 else None
            if bust_name:
                bust_key = bust_name[:3]
                layer_id = store.BUST_LAST_LAYER.get(bust_key, 5)
        if layer_id not in store.STORE_BUST_POS:
            renpy.log(f"Layer {layer_id} not found in STORE_BUST_POS for _MoveBS")
            return
        layer = "bustlayer"
        sprite_id = f"bust_{layer_id}"
        pos_info = store.STORE_BUST_POS[layer_id]
        bust_img = pos_info["img"]
        base_transform = pos_info["transform"]
        current_time = renpy.get_game_runtime()
        delay_remaining = 0
        if layer_id in store.BUST_DELAY_TIMERS:
            end_time = store.BUST_DELAY_TIMERS[layer_id]
            if current_time < end_time:
                delay_remaining = end_time - current_time
        jump_transform = multi_jump(dy=dy, base_duration=duration_ms / 1000.0, delay_time=delay_remaining + store.MOVEBS_DELAY)
        renpy.show(sprite_id, at_list=[jump_transform], layer=layer, zorder=layer_id)
        renpy.show(sprite_id, what=base_transform, layer=layer, zorder=layer_id)
        store.MOVEBS_DELAY = 0

    def _Font(params):
        font_size, p2, p3 = params
        if font_size != -1:
            store.FONT_SIZE = font_size
        else:
            store.FONT_SIZE = None 

    def _DrawSPR(params):
        layer_id = params[0]
        filename = params[1]
        fade_duration = params[17] / 1000.0
        spr_path = f"images/misc/{filename}.png"
        if filename == "ef_kaisou":
            clear_all(True)
            store.EF_KAISOU_ACTIVE = True
            renpy.pause(fade_duration)
            renpy.show("ef_kaisou_img", what=Image(spr_path), layer="bustlayer", zorder=layer_id)
            store.SPR_DISPLAY[layer_id] = {"filename": filename,"sprite_id": "ef_kaisou_img","layer": "bustlayer"}
        else:
            clear_all(False)
            layer_name = "bustlayer"
            sprite_id = f"spr_{layer_id}"
            start_x = 1920 // 2 + params[8]
            start_y = 1080 // 2 + params[9]
            end_x = 1920 // 2 + params[4]
            end_y = 1080 // 2 + params[5]
            animated_transform = spr_fadein_move(start_x, start_y, end_x, end_y, fade_duration)
            renpy.show(sprite_id, what=At(Image(spr_path), animated_transform), layer=layer_name, zorder=layer_id)
            store.BUST_FADEIN_END_TIMERS[layer_id] = renpy.get_game_runtime() + fade_duration
            store.SPR_DISPLAY[layer_id] = {"filename": filename,"sprite_id": sprite_id,"layer": layer_name}

    def _FadeSPR(params):
        layer_id = params[0]
        fade_duration = params[-2] / 1000.0
        if layer_id in store.SPR_DISPLAY:
            spr_info = store.SPR_DISPLAY[layer_id]
            if spr_info["filename"] == "ef_kaisou":
                renpy.pause(fade_duration)
                renpy.hide(spr_info["sprite_id"], layer=spr_info["layer"])
                store.EF_KAISOU_ACTIVE = False
            else:
                renpy.hide(spr_info["sprite_id"], layer=spr_info["layer"])
                renpy.show(spr_info["sprite_id"]+"_temp", what=At(Image(f"images/misc/{spr_info['filename']}.png"), fadeout_down_move(50,fade_duration)), layer=spr_info["layer"])
                store.interruptible_bserase_tags.append(spr_info["sprite_id"]+"_temp")
                renpy.pause(fade_duration)
                store.BUST_FADEIN_END_TIMERS[layer_id] = renpy.get_game_runtime() + fade_duration
            del store.SPR_DISPLAY[layer_id]

    def _bustshotFadein(params):
        if is_cg_active(): return
        # 参数: [u1, 淡入方式, 图层id, 立绘名, 移动距离, 偏移值, u2, 动画时间(ms), u3, u4]
        u1, fadein_flag, layer_id, bust_name, distance, pos_x, u3, duration_ms, u4, u5 = params
        base_key = "_".join(bust_name.split("_")[:-1])  # 'mik01C'
        ch_folder = bust_name[:3]
        composited_path = f"images/character_composited/{ch_folder}/{bust_name}.webp"
        size_info = CHARACTER_SIZES.get(base_key[:5], (920, 1638, None, None))
        width, height, center_x, center_y = size_info
        if center_x is None:
            center_x = width // 2
        if center_y is None:
            if base_key[3:5] == "01" or base_key[3:5] == "02":
                center_y = int(height * 0.60)
            else:
                center_y = int(height * 0.645)
        screen_x = 1920 // 2
        screen_y = 1080
        bust_key = bust_name[:3]
        if layer_id == -1:
            layer_id = store.BUST_LAST_LAYER.get(bust_key, 5)
        else:
            store.BUST_LAST_LAYER[bust_key] = layer_id
        offset_x = pos_x
        target_x = screen_x + offset_x - center_x
        target_y = screen_y - center_y
        layer = "bustlayer"
        sprite_id = f"bust_{layer_id}"
        duration = duration_ms / 1000.0
        fadein_end_time = store.BUST_FADEIN_END_TIMERS.get(layer_id, 0)
        current_time = renpy.get_game_runtime()
        delay = max(0, fadein_end_time - current_time)
        renpy.pause(delay)
        bust_img = Image(composited_path)
        base_transform = Transform(bust_img, xpos=target_x, ypos=target_y, anchor=(0, 0))
        if fadein_flag == 1:
            animated_transform = At(base_transform, fadein_right_to_left(distance, duration, delay=0))   # 从右向左
        elif fadein_flag == 2:
            animated_transform = At(base_transform, fadein_right_to_left(-distance, duration, delay=0))  # 从左向右
        elif fadein_flag == 3:
            animated_transform = At(base_transform, fadein_down_to_up(-distance, duration, delay=0))
        current_time = renpy.get_game_runtime()
        store.BUST_FADEIN_END_TIMERS[layer_id] = current_time + duration + 0.4
        store.STORE_BUST_POS[layer_id] = {"x": target_x,"y": target_y,"img": bust_img,"offset_x": offset_x,"transform": animated_transform,"base_key": base_key}
        renpy.show(sprite_id, what=animated_transform, layer=layer, zorder=layer_id)
        if layer_id not in store.SCHEDULED_PENDING_LAYERS:
            store.SCHEDULED_PENDING_LAYERS.append(layer_id)

    def _DrawScene(params):
        filename = params[0]
        duration = params[7] / 1000.0
        file_folder = filename[:2]
        clear_all(True)
        if filename == "white":
            fade_duration = 0.3
            if renpy.is_skipping():
                fade_duration = 0.05
                duration = 0.05
            renpy.show("white_Scene", what=Solid("#ffffff"), at_list=[multi_effect(duration*1.5,fade_duration)], layer="top", zorder=114514)
            renpy.pause(duration)
            store.interruptible_bserase_tags.append("white_Scene")
        else:
            file_path = f"images/cg/{file_folder}/{filename}.webp"
            # 检查是否为事件CG的 "show behind" 操作
            if duration == 0 and store.CURRENT_EVENT_CG and store.CURRENT_EVENT_CG.get("tag"):
                renpy.show(filename, what=Image(file_path), layer='master')
            else:
                renpy.scene()
                renpy.show(filename, what=Image(file_path))
                if duration > 0:
                    renpy.with_statement(Dissolve(duration))
                store.CURRENT_EVENT_CG = {}

    def _EventCGMotion(params):
        if not store.CURRENT_EVENT_CG:
            renpy.error("EventCGMotion called without an active Event CG.")
            return
        duration_ms = params[2]
        duration = duration_ms / 1000.0
        cg_info = store.CURRENT_EVENT_CG
        tag = cg_info["tag"]
        pan_transform = event_cg_pan_and_fade(start_x=cg_info["xcenter"],start_y=cg_info["ycenter"],
        end_x=cg_info["end_xalign"],end_y=cg_info["end_yalign"],zoom_val=cg_info["zoom"],duration=duration)
        renpy.show(tag, at_list=[pan_transform], layer='bustlayer')
        store.interruptible_cg_tag = tag

    def _BustshotShiftX(params):
        if is_cg_active(): return
        # 参数: [图层id, x轴移动数值]
        layer_id, dx = params
        duration = 0.3  # 动画持续时间（秒）
        if layer_id not in store.STORE_BUST_POS:
            renpy.log(f"Layer {layer_id} not found in STORE_BUST_POS for _BustshotShiftX")
            return
        pos_info = store.STORE_BUST_POS[layer_id]
        bust_img = pos_info["img"]
        current_x = pos_info["x"]
        current_y = pos_info["y"]
        sprite_id = f"bust_{layer_id}"
        layer = "bustlayer"
        # 计算新的目标x坐标
        new_x = current_x + dx
        # 创建立绘在 *最终* 位置的静态Transform
        final_transform = Transform(bust_img, xpos=new_x, ypos=current_y, anchor=(0, 0))
        animated_transform = At(final_transform, bust_shift_x(dx, duration))
        # 更新store中的立绘信息为最终状态。这样，任何后续的动画都将从新的正确位置开始
        pos_info["x"] = new_x
        pos_info["offset_x"] = pos_info.get("offset_x", 0) + dx
        pos_info["transform"] = final_transform  # 将基础变换更新为最终状态
        renpy.show(sprite_id, what=animated_transform, layer=layer, zorder=layer_id)

    def _ShakeBS(params):
        if is_cg_active(): return
        # 解析参数: [图层id, 水平范围, 垂直范围, 循环次数, 总时间(ms)]
        layer_id, h_range, v_range, loops, total_time_ms = params
        if loops <= 0:
            return
        if layer_id not in store.STORE_BUST_POS:
            renpy.log(f"Layer {layer_id} not found in STORE_BUST_POS for _ShakeBS")
            return
        # 获取当前游戏时间
        current_time = renpy.get_game_runtime()
        # 计算淡入动画剩余的延迟时间
        fadein_end_time = store.BUST_FADEIN_END_TIMERS.get(layer_id, 0)
        fadein_delay = max(0, fadein_end_time - current_time)
        # 计算切换立绘的剩余延迟时间
        switch_delay_remaining = 0
        if layer_id in store.BUST_DELAY_TIMERS:
            end_time = store.BUST_DELAY_TIMERS[layer_id]
            if current_time < end_time:
                switch_delay_remaining = end_time - current_time
        # 总延迟 = 淡入延迟 + 切换延迟
        total_delay = switch_delay_remaining
        # 处理总时间
        duration = total_time_ms / 1000.0 if total_time_ms > 0 else loops * 0.1
        # 获取立绘信息
        pos_info = store.STORE_BUST_POS[layer_id]
        base_transform = pos_info["transform"]
        sprite_id = f"bust_{layer_id}"
        layer = "bustlayer"
        # 创建并应用变换，传入计算出的 total_delay
        shake_transform = bust_shake(h_range, v_range, loops, duration, delay_time=total_delay)
        renpy.show(sprite_id, at_list=[shake_transform], layer=layer, zorder=layer_id)
        # 恢复原始状态
        renpy.show(sprite_id, what=base_transform, layer=layer, zorder=layer_id)

    def _PlayMovie(params):
        filename,fade_time,u1,video_end = params
        config.skipping = None
        # 淡出所有图片
        clear_all(True)
        renpy.scene()
        renpy.show("black")
        renpy.with_statement(Dissolve(fade_time))
        # 播放视频
        renpy.call_screen("movie_player", filename=filename, video_end=video_end)
        # Q:目前还有一个小问题,在所有图片淡出的时候没办法淡出回想、历史等按钮

    def _PlayStreamSE(params):
        channel_id, se_name, u1, loop_flag, volume, u2 = params
        if channel_id == 0:
            channel = "se"
        else:
            renpy.error(f"Invalid channel ID for _PlayStreamSE: {channel_id}")
        filepath = f"audio/bgm/"+ se_name.lower() +".ogg"
        loop = True if loop_flag == 1 else False
        renpy.music.play(filepath,channel=channel,loop=loop,relative_volume=volume / 128.0)

    def _FadeStreamSE(params):
        channel_id, fade_duration_ms,u1 = params
        if channel_id == 0:
            channel = "se"
        else:
            renpy.error(f"Invalid channel ID for _FadeStreamSE: {channel_id}")
        renpy.music.stop(channel, fade_duration_ms / 1000.0)

    def _ChangeVolumeOfStreamSE(params):
        # [通道ID, 目标音量, 淡出时间(ms)]
        channel_id, target_volume,fade_duration_ms  = params
        if channel_id == 0:
            channel = "se"
        else:
            renpy.error(f"Invalid channel ID for ChangeVolumeOfStreamSE: {channel_id}")
        renpy.music.set_volume(target_volume / 233.3, fade_duration_ms / 1000.0, channel)

    def _ShakeBG(params):
        h_range, v_range, loops, u1 = params
        h_range = h_range * 1.5
        v_range = v_range * 1.5
        if loops <= 0:          # loops < 0 需要 _StopQuakingEx 关闭震动
            shake_transform = bg_myshake(h_range, v_range)
            renpy.show_layer_at([shake_transform], layer='master')
        else:
            duration = loops * 0.08         # 总时间 为 动画次数 * 每次动画的时间
            shake_transform = bg_shake(h_range, v_range, loops, duration)
            renpy.show_layer_at([shake_transform], layer='master')
            renpy.pause(duration)
            renpy.show_layer_at([], layer='master')

    def _StopQuakingEx(params):
        u1,u2 = params
        renpy.show_layer_at([], layer='master')

    def _WaitToFinishBGControlling(params):
        u1 = params

    def _SetDelayCount(params):
        store.MOVEBS_DELAY = params[0] / 1000
#======内部函数定义======
    def f_15d(params):
        mode = params[0] if params else 0
        store.textbox_mode = mode

    def f_232(params):
        u1,u2,h_range,v_range,duration_ms,u3=params
        duration = duration_ms / 10000.0   # 持续时间（毫秒）
        loops = int(duration / 0.08) + 1
        renpy.show_layer_at([bg_shake(h_range*3, v_range*3, loops, duration)],layer='screens')
        renpy.pause(duration)
        renpy.show_layer_at([], layer='screens')

    def f_391(params):
        duration, u1 = params
        _window_hide(trans=False, auto=True)
        renpy.show("white_bg", what=Solid("#ffffff"), at_list=[Fadein_effect(duration/ 1000.0)], layer="bustlayer",zorder=10)
        renpy.pause(duration/ 1000.0)
        clear_all(False)
        store.WHITE_BG_ACTIVE = True

    def f_234(params):
        speed, intensity, decay_rate, direction, duration_val, u1 = params
        total_duration = duration_val / 200.0
        # Time for one full cycle (e.g., right and back to left).
        # Scaled so high speed values result in shorter cycle times (faster movement).
        # A speed of 255 is fastest, a speed of 1 is slowest.
        cycle_time = 0.5 + ((255.0 - speed) / 255.0) * 2.0
        cycle_time = max(0.1, cycle_time) # Prevent division by zero.
        # --- Direction & Vector Calculation ---
        dx, dy = 0.0, 0.0
        if direction == 0:  # 0: Horizontal
            dx = float(intensity)
        elif direction == 1:  # 1: Top-left to bottom-right
            dx = float(intensity) * 0.707
            dy = float(intensity) * 0.707
        elif direction == 2:  # 2: Vertical
            dy = float(intensity)
        elif direction == 3:  # 3: Top-right to bottom-left
            dx = float(intensity) * 0.707
            dy = -float(intensity) * 0.707
        elif direction == 4:  # 4: Random
            angle = random.uniform(0, 2 * math.pi)
            dx = float(intensity) * math.cos(angle) *8
            dy = float(intensity) * math.sin(angle) *8
        move_transform = f_234_continuous_move(cycle_time, dx, dy)
        renpy.show_layer_at([move_transform], layer='master')
        renpy.pause(total_duration)
        renpy.show_layer_at([], layer='master')

    def f_301(params):
        filename = params[1]
        if filename == "ef_syuchu_wh.bm":
            renpy.pause(0.6)
            renpy.show("linework", at_list=[bust_fadein(0.5,0.6)],zorder=2)
            renpy.with_statement(dissolve)

    def f_311(params):
        # 参数: 番号, 延时结束的时间, 延迟下一段对话出现的时间
        layer_id, delay_time, pause_time, u1 = params
        delay_time = delay_time / 1000.0
        renpy.show("linework", at_list=[fade_out_bm(delay_time,0.5)],zorder=2)
        renpy.pause(pause_time)
        renpy.hide("linework")

    def f_388(params):
        duration, u1 = params
        if not store.WHITE_BG_ACTIVE: return
        if not renpy.showing("white_bg", layer="bustlayer"): return
        renpy.pause(duration/ 1000.0)
        renpy.show("white_bg", what=Solid("#ffffff"), at_list=[Fadeout_effect(duration/ 1000.0)], layer="bustlayer",zorder=10)
        renpy.pause(duration/ 1000.0)
        store.interruptible_bserase_tags.append("white_bg")
        store.WHITE_BG_ACTIVE = False

#=====覆盖renpy函数=====
    def _custom_enter_menu():
        config.skipping = None

        renpy.movie_stop(only_fullscreen=True)
        if not renpy.context()._menu:
            _window_hide(trans=Dissolve(0.0), auto=True)
            renpy.take_screenshot((config.thumbnail_width, config.thumbnail_height))
            store._window = True

        for i in config.menu_clear_layers:
            renpy.scene(layer=i)

        renpy.context()._menu = True
        renpy.context()._main_menu = main_menu

        renpy.context_dynamic("main_menu")
        renpy.context_dynamic("_window_subtitle")
        renpy.context_dynamic("_window")
        renpy.context_dynamic("_history")
        renpy.context_dynamic("_menu")

        renpy.context_dynamic("_side_image_old")
        renpy.context_dynamic("_side_image_raw")
        renpy.context_dynamic("_side_image")
        renpy.context_dynamic("_side_image_attributes")
        renpy.context_dynamic("_side_image_attributes_reset")

        store._window_subtitle = config.menu_window_subtitle
        store._window = False
        store._history = False
        store._menu = True
        store._side_image_attributes = None
        store._side_image_attributes_reset = False

        store.mouse_visible = True
        store.suppress_overlay = True

        ui.clear()

        for i in config.clear_layers:
            renpy.scene(layer=i)
    _enter_menu = _custom_enter_menu