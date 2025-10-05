### 存储动画的地方 ###

## Click to Continue 闪烁动画
transform ctc_blink:
    alpha 1.0
    pause 0.01
    linear 0.5 alpha 0.0
    pause 0.3
    linear 0.5 alpha 1.0
    pause(0.3)
    repeat

## Click to Continue 延迟闪烁动画 - 等待文本显示后再开始
transform ctc_blink_delayed:
    alpha 0.0
    pause 1.5  # 等待1.5秒让文本有时间显示
    alpha 1.0
    pause 0.5
    linear 1.0 alpha 0.0
    pause 0.3
    linear 1.0 alpha 1.0
    repeat

## Click to Continue 智能闪烁动画 - 根据文本长度动态延迟
transform ctc_smart_blink(delay_time):
    alpha 0.0
    pause delay_time  # 动态延迟时间
    block:
        linear 0.25 alpha 1.0
        pause 0.25
        linear 0.25 alpha 0.0
        pause 0.25
        linear 0.25 alpha 1.0
        pause 0.25
        repeat

transform multi_shake(count, dx=15, base_duration=0.20, delay_time=0.0):
    pause delay_time
    block:
        easein base_duration*0.25 xoffset dx
        easeout base_duration*0.25 xoffset 0
        easein base_duration*0.25 xoffset -dx
        easeout base_duration*0.25 xoffset 0
        repeat count

transform multi_nod(count, dy=10, base_duration=0.20, delay_time=0.0):
    pause delay_time
    block:
        easein base_duration*0.62 yoffset dy
        easeout base_duration*0.38 yoffset 0
        repeat count

transform multi_jump(dy=10, base_duration=0.5, delay_time=0.0):
    pause delay_time
    # 向上跳跃
    easeout base_duration*0.5 yoffset -dy
    # 落回原位
    easein base_duration*0.6 yoffset 0

#TODO:延时切换立绘最优效果是溶解切换（with dissolve 、renpy.with_statement(Dissolve），但是会导致旧立绘在切换错位，`define config.transitions_use_child_placement = False`也会导致新立绘和旧立绘切换动画不能用自己的数据
transform delayed_switch(old_img, new_img, delay_time=0, trans_time=0.20):
    subpixel True
    old_img
    pause delay_time
    create_atl_dissolve(old_img,new_img,trans_time)
    pause trans_time
    new_img

transform switch(old_img, new_img, trans_time=0.20):
    old_img
    # 切换到新图像
    new_img with Dissolve(trans_time)

transform bust_fadein(trans_time=0.20, delay_time=0.0):
    alpha 0
    pause delay_time
    linear trans_time alpha 1

transform bust_fadeout_and_null(delay_time=0, trans_time=0.2):
    pause delay_time
    alpha 1
    linear trans_time alpha 0
    Null()

transform flash_effect(flash_count, flash_duration):
    # 初始透明
    alpha 0.0
    # 快速闪烁指定次数
    block:
        linear flash_duration alpha 1.0
        linear flash_duration alpha 0.0
        repeat flash_count

transform Fadein_effect(time=0.5):
    alpha 0.0
    linear time alpha 1.0

transform Fadeout_effect(time=0.5):
    alpha 1.0
    linear time alpha 0.0

transform multi_effect(time=0.5,fade_duration=0.3):
    alpha 0.0
    linear fade_duration alpha 1.0
    pause time
    linear fade_duration alpha 0.0

# 从指定的起始坐标移动到结束坐标并淡入的动画
transform spr_fadein_move(start_x, start_y, end_x, end_y, duration):
    # 初始状态: 在起始位置 + 完全透明
    pos (start_x, start_y)
    alpha 0.0
    # 动画: 移动到结束位置 + 淡入
    easein duration pos (end_x, end_y) alpha 1.0

# 向下移动并淡出的动画
transform fadeout_down_move(distance=100, duration=0.5):
    # 初始状态：正常位置 + 完全可见
    yoffset 0
    alpha 1.0
    # 动画：向下移动 + 淡出
    easeout duration yoffset distance alpha 0.0
    Null()

# 从右向左移动并淡入的动画
transform fadein_right_to_left(distance, duration, delay=0.0):
    # 初始状态：在右侧 + 完全透明
    alpha 0.0
    xoffset distance
    pause delay
    # 动画：向左移动到目标位置 + 淡入
    easein duration xoffset 0 alpha 1.0

# 从下向上移动并淡入的动画
transform fadein_down_to_up(distance, duration, delay=0.0):
    # 初始状态：在下侧 + 完全透明
    alpha 0.0
    yoffset -distance
    pause delay
    # 动画：向上移动到目标位置 + 淡入
    easein duration yoffset 0 alpha 1.0

transform event_cg_pan_and_fade(start_x, start_y, end_x, end_y, zoom_val, duration):
    zoom zoom_val
    xcenter start_x
    ycenter start_y
    alpha 1.0
    parallel:
        linear 12.0 xcenter end_x ycenter end_y
    parallel:
        pause 3.5
        linear 2.0 alpha 0.0
        Null()

transform bust_shift_x(dx, duration=0.3):
    # dx > 0 (向右移动), 初始位置在左侧, offset为负
    # dx < 0 (向左移动), 初始位置在右侧, offset为正
    xoffset -dx
    # 将其动画化到最终位置 (xoffset 0)。
    linear duration xoffset 0

transform bustshot_left_fade(move_duration=0.5, distance=10, delay=0.0):
    pause delay
    pause 0.4
    alpha 1.0
    easeout move_duration xoffset -distance alpha 0.0
    Null()

transform bustshot_down_fade(move_duration=0.5, distance=10, delay=0.0):
    pause delay
    pause 0.4
    alpha 1.0
    easeout move_duration yoffset -distance alpha 0.0
    Null()

transform bg_shake(h_range, v_range, loops, duration):
    block:
        linear 0.02 xoffset h_range yoffset v_range
        linear 0.02 xoffset -h_range yoffset -v_range
        linear 0.02 xoffset h_range yoffset -v_range
        linear 0.02 xoffset 0 yoffset 0
        repeat loops - 1

transform bg_myshake(h_range, v_range):
    block:
        linear 0.02 xoffset h_range yoffset v_range
        linear 0.02 xoffset -h_range yoffset -v_range
        linear 0.02 xoffset h_range yoffset -v_range
        linear 0.02 xoffset 0 yoffset 0
    repeat

transform bust_shake(h_range, v_range, loops, duration, delay_time=0.0):
    # 增加延时等待
    pause delay_time
    # 定义相对于立绘当前位置的振动轨迹
    block:
        # 每一帧的持续时间 = 总时长 / 循环次数 / 每次循环的步数
        linear (duration / loops / 4.0) xoffset h_range yoffset v_range
        linear (duration / loops / 4.0) xoffset -h_range yoffset -v_range
        repeat loops
    # 动画结束后，确保偏移量归零，使立绘回到振动前的精确位置
    xoffset 0
    yoffset 0

image linework:  #from Summer Pockets
    truecenter
    "images/misc/linework_01.png"
    pause 0.06
    "images/misc/linework_02.png"
    pause 0.06
    "images/misc/linework_01.png"
    pause 0.06
    repeat

transform f_234_continuous_move(cycle_time, dx, dy):
    subpixel True
    block:
        linear cycle_time/2.0 xoffset dx yoffset dy
        linear cycle_time/2.0 xoffset -dx yoffset -dy
        repeat

transform fade_out_bm(delay_time=0, trans_time=0.5):
    pause delay_time
    alpha 1
    linear trans_time alpha 0
    on hide:
        alpha 0