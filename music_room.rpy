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
            xalign 0.6 ypos 200
            text "音乐鉴赏" size 30 xalign 0.5
            textbutton "花びらの刻" action Play("music", "BGM/花びらの刻.mp3") xalign 0.5
            null height 20
            textbutton "下一曲" action mr.Next()
    frame:
        top_margin 600
        left_margin 1000
        xmaximum 1200
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
