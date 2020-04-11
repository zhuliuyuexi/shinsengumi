init python:

    mr = MusicRoom(fadeout=0.5, single_track=True, stop_action=None)

    mr.add("BGM/花びらの刻.mp3", always_unlocked=True)
    mr.add("BGM/花びらの刻.mp3", always_unlocked=True)


screen music_room:
    tag menu
    add "gui/musicroom.png"

    frame:
        top_margin 20
        left_margin 300
        xminimum 900
        yminimum 900
        background "gui/hana_frame.png"
        vbox:
            xpos 280 ypos 200
            text "音乐鉴赏" size 30 xalign 0.5
        vbox:
            xpos 650 ypos 200
            spacing 20
            textbutton _("前一页") action FilePagePrevious()
            textbutton "上一曲" action mr.Previous()
            textbutton "停止" action mr.Stop()
            textbutton "下一曲" action mr.Next()
            textbutton _("后一页") action FilePageNext()
    frame:
        top_margin 280
        left_margin 550
        xminimum 800
        yminimum 550
        style_prefix "music_list"
        background "gui/scrollbar/transparent.png"

        grid 1 3:
            yspacing 10
            textbutton "花びらの刻" action Play("music", "BGM/花びらの刻.mp3")
            textbutton "花びらの刻" action Play("music", "BGM/花びらの刻.mp3")
            textbutton "花びらの刻" action Play("music", "BGM/花びらの刻.mp3")


    frame:
        top_margin 500
        left_margin 950
        xmaximum 1100
        ymaximum 600
        vbox:
            if config.has_music:
                label _("音乐音量")
                hbox:
                    bar value Preference("music volume")
#        bar value Preference("sound volume")
#        bar value Preference("music volume")
#        bar value Preference("vioce volume")

    imagebutton:
        xpos 100 ypos 450
        idle "gui/button/back_idle.png"
        hover "gui/button/back_hover.png"
        action ShowMenu("Nevigation")
