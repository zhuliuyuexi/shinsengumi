
#######CG鉴赏屏幕
screen CG():
    tag menu

    frame:
        add "gui/CG_all.png"
        add sakura_small_fall
        add sakura_midium_fall
        add sakura_big_fall

        #添加9个男主的图片按钮
        imagebutton:
            xpos 40 ypos 250
            idle "gui/button/tiandai_mohu.png"
            hover "gui/button/tiandai.png"
            hover_sound "sounds/CG.mp3"
            action ShowMenu("CG_tiandai")
        imagebutton:
            xpos 160 ypos 150
            idle "gui/button/shannan_mohu.png"
            hover "gui/button/shannan.png"
            hover_sound "sounds/CG.mp3"
            action ShowMenu("CG_shannan")
        imagebutton:
            xpos 280 ypos 210
            idle "gui/button/pingzhu_mohu.png"
            hover "gui/button/pingzhu.png"
            hover_sound "sounds/CG.mp3"
            action ShowMenu("CG_tengtang")
        imagebutton:
            xpos 400 ypos 170
            idle "gui/button/chongtian_mohu.png"
            hover "gui/button/chongtian.png"
            hover_sound "sounds/CG.mp3"
            action ShowMenu("CG_chongtian")
        imagebutton:
            xpos 520 ypos 100
            idle "gui/button/tufang_mohu.png"
            hover "gui/button/tufang.png"
            hover_sound "sounds/CG.mp3"
            action ShowMenu("CG_tufang")
        imagebutton:
            xpos 640 ypos 140
            idle "gui/button/zhaiteng_mohu.png"
            hover "gui/button/zhaiteng.png"
            hover_sound "sounds/CG.mp3"
            action ShowMenu("CG_zhaiteng")
        imagebutton:
            xpos 760 ypos 220
            idle "gui/button/shanqi_mohu.png"
            hover "gui/button/shanqi.png"
            hover_sound "sounds/CG.mp3"
            action ShowMenu("CG_shanqi")
        imagebutton:
            xpos 880 ypos 300
            idle "gui/button/yuantian_mohu.png"
            hover "gui/button/yuantian.png"
            hover_sound "sounds/CG.mp3"
            action ShowMenu("CG_yuantian")
        imagebutton:
            xpos 1000 ypos 250
            idle "gui/button/yongcang_mohu.png"
            hover "gui/button/yongcang.png"
            hover_sound "sounds/CG.mp3"
            action ShowMenu("CG_yongcang")
        imagebutton:
            xpos 1120 ypos 320
            idle "gui/button/shuangyue_mohu.png"
            hover "gui/button/shuangyue.png"
            hover_sound "sounds/CG.mp3"
            action ShowMenu("CG_qita")

        #返回按钮
        imagebutton:
            xpos 30 ypos 660
            idle "gui/button/back_small.png"
            hover "gui/button/back_small2.png"
            action ShowMenu("Nevigation")

#田代的CG画册
screen CG_tiandai():
    tag menu
    add "gui/cg_back.png"
    add "character/td/tiandai_full.png" xpos 30 ypos 150
    frame:
        background None
        left_padding 467
        top_margin 162
        has vbox

        grid 3 3:
            xspacing 76
            yspacing 52
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)

        hbox:
            xpos 200
            ypos 10
            textbutton _("前一页") action FilePagePrevious()

            for i in range(1, 11):
                textbutton str(i) action FilePage(i)

            textbutton _("后一页") action FilePageNext()

    #返回按钮
    imagebutton:
        xpos 30 ypos 660
        idle "gui/button/back_small.png"
        hover "gui/button/back_small2.png"
        action ShowMenu("CG")

#山南的CG画册
screen CG_shannan():
    tag menu
    add "gui/cg_back.png"
    add "character/sn/shannan_full.png" xpos 30 ypos 150
    frame:
        background None
        left_padding 467
        top_margin 162
        has vbox

        grid 3 3:
            xspacing 76
            yspacing 52
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)

        hbox:
            xpos 200
            ypos 10
            textbutton _("前一页") action FilePagePrevious()

            for i in range(1, 11):
                textbutton str(i) action FilePage(i)

            textbutton _("后一页") action FilePageNext()

    #返回按钮
    imagebutton:
        xpos 30 ypos 660
        idle "gui/button/back_small.png"
        hover "gui/button/back_small2.png"
        action ShowMenu("CG")

#藤堂的CG画册
screen CG_tengtang():
    tag menu
    add "gui/cg_back.png"
    add "character/pz/pingzhu_full.png" xpos 30 ypos 150
    frame:
        background None
        left_padding 467
        top_margin 162
        has vbox

        grid 3 3:
            xspacing 76
            yspacing 52
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)

        hbox:
            xpos 200
            ypos 10
            textbutton _("前一页") action FilePagePrevious()

            for i in range(1, 11):
                textbutton str(i) action FilePage(i)

            textbutton _("后一页") action FilePageNext()

    #返回按钮
    imagebutton:
        xpos 30 ypos 660
        idle "gui/button/back_small.png"
        hover "gui/button/back_small2.png"
        action ShowMenu("CG")

#冲田的CG画册
screen CG_chongtian():
    tag menu
    add "gui/cg_back.png"
    add "character/ct/chongtian_full.png" xpos 30 ypos 150
    frame:
        background None
        left_padding 467
        top_margin 162
        has vbox

        grid 3 3:
            xspacing 76
            yspacing 52
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)

        hbox:
            xpos 200
            ypos 10
            textbutton _("前一页") action FilePagePrevious()

            for i in range(1, 11):
                textbutton str(i) action FilePage(i)

            textbutton _("后一页") action FilePageNext()
    #返回按钮
    imagebutton:
        xpos 30 ypos 660
        idle "gui/button/back_small.png"
        hover "gui/button/back_small2.png"
        action ShowMenu("CG")

#土方的CG画册
screen CG_tufang():
    tag menu
    add "gui/cg_back.png"
    add "character/tf/tufang_full.png" xpos 30 ypos 150
    frame:
        background None
        left_padding 467
        top_margin 162
        has vbox

        grid 3 3:
            xspacing 76
            yspacing 52
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)

        hbox:
            xpos 200
            ypos 10
            textbutton _("前一页") action FilePagePrevious()

            for i in range(1, 11):
                textbutton str(i) action FilePage(i)

            textbutton _("后一页") action FilePageNext()

    #返回按钮
    imagebutton:
        xpos 30 ypos 660
        idle "gui/button/back_small.png"
        hover "gui/button/back_small2.png"
        action ShowMenu("CG")

#斋藤的CG画册
screen CG_zhaiteng():
    tag menu
    add "gui/cg_back.png"
    add "character/zt/zhaiteng_full.png" xpos 30 ypos 150
    frame:
        background None
        left_padding 467
        top_margin 162
        has vbox

        grid 3 3:
            xspacing 76
            yspacing 52
            add g.make_button("斋藤赏樱", "斋藤赏樱thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)

        hbox:
            xpos 200
            ypos 10
            textbutton _("前一页") action FilePagePrevious()

            for i in range(1, 11):
                textbutton str(i) action FilePage(i)

            textbutton _("后一页") action FilePageNext()

    #返回按钮
    imagebutton:
        xpos 30 ypos 660
        idle "gui/button/back_small.png"
        hover "gui/button/back_small2.png"
        action ShowMenu("CG")

#原田的CG画册
screen CG_yuantian():
    tag menu
    add "gui/cg_back.png"
    add "character/yt/yuantian_full.png" xpos 30 ypos 150
    frame:
        background None
        left_padding 467
        top_margin 162
        has vbox

        grid 3 3:
            xspacing 76
            yspacing 52
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)

        hbox:
            xpos 200
            ypos 10
            textbutton _("前一页") action FilePagePrevious()

            for i in range(1, 11):
                textbutton str(i) action FilePage(i)

            textbutton _("后一页") action FilePageNext()

    #返回按钮
    imagebutton:
        xpos 30 ypos 660
        idle "gui/button/back_small.png"
        hover "gui/button/back_small2.png"
        action ShowMenu("CG")

#永仓的CG画册
screen CG_yongcang():
    tag menu
    add "gui/cg_back.png"
    add "character/xb/xinba_full.png" xpos 10 ypos 150
    frame:
        background None
        left_padding 467
        top_margin 162
        has vbox

        grid 3 3:
            xspacing 76
            yspacing 52
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("永仓NE", "永仓NEthumb", xalgn = 0.5, yalign = 0.5)

        hbox:
            xpos 200
            ypos 10
            textbutton _("前一页") action FilePagePrevious()

            for i in range(1, 11):
                textbutton str(i) action FilePage(i)

            textbutton _("后一页") action FilePageNext()

    #返回按钮
    imagebutton:
        xpos 30 ypos 660
        idle "gui/button/back_small.png"
        hover "gui/button/back_small2.png"
        action ShowMenu("CG")
#山崎的CG画册
init python:
    g = Gallery()
    g.locked_button = "images/CG/lock.png"#未解锁的图片按钮
    g.button("土方池田屋thumb")#解锁后的图片按钮，以后每有一个就要相应的写2行代码
    g.unlock_image("土方池田屋.png")

screen CG_shanqi():
    tag menu
    add "gui/cg_back.png"
    add "character/sq/shanqi_full.png" xpos 10 ypos 150
    frame:
        background None
        left_padding 467
        top_margin 162
        has vbox

        grid 3 3:
            xspacing 76
            yspacing 52
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)

        hbox:
            xpos 200
            ypos 10
            textbutton _("前一页") action FilePagePrevious()

            for i in range(1, 11):
                textbutton str(i) action FilePage(i)

            textbutton _("后一页") action FilePageNext()

    #返回按钮
    imagebutton:
        xpos 30 ypos 660
        idle "gui/button/back_small.png"
        hover "gui/button/back_small2.png"
        action ShowMenu("CG")

#其他的CG画册
init python:
    g = Gallery()
    g.locked_button = "images/CG/lock.png"#未解锁的图片按钮
    g.button("吃饭")#解锁后的图片按钮，以后每有一个就要相应的写2行代码
    g.unlock_image("吃饭")
    g.button("斋藤赏樱")#解锁后的图片按钮，以后每有一个就要相应的写2行代码
    g.unlock_image("斋藤赏樱")
    g.button("永仓NE")#解锁后的图片按钮，以后每有一个就要相应的写2行代码
    g.unlock_image("永仓NE")
    g.button("土方池田屋")#解锁后的图片按钮，以后每有一个就要相应的写2行代码
    g.unlock_image("土方池田屋")
screen CG_qita():
    tag menu
    add "gui/cg_back.png"
    add "character/sy/shuangyue_full.png" xpos 30 ypos 150
    frame:
        background None
        left_padding 467
        top_margin 162
        has vbox

        grid 3 3:
            xspacing 76
            yspacing 52
            add g.make_button("吃饭", "吃饭thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)
            add g.make_button("土方池田屋", "土方池田屋thumb", xalgn = 0.5, yalign = 0.5)

        hbox:
            xpos 200
            ypos 10
            textbutton _("前一页") action FilePagePrevious()

            for i in range(1, 11):
                textbutton str(i) action FilePage(i)

            textbutton _("后一页") action FilePageNext()

    #返回按钮
    imagebutton:
        xpos 30 ypos 660
        idle "gui/button/back_small.png"
        hover "gui/button/back_small2.png"
        action ShowMenu("CG")
