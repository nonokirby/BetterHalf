﻿################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 350
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound "audio/Coins (21).wav"
    activate_sound "audio/Coins (2).wav"

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0
            imagebutton auto "gui/qskip_%s.png" hovered Play("sound", "audio/Coins (15).wav") action [Play("sound", "audio/Coins (15).wav"), Skip()] alternate Skip(fast=True, confirm=True)
            imagebutton auto "gui/qsave_%s.png" hovered Play("sound", "audio/Coins (15).wav") action [Play("sound", "audio/Coins (15).wav"), ShowMenu('save')]
            imagebutton auto "gui/qload_%s.png" hovered Play("sound", "audio/Coins (15).wav") action [Play("sound", "audio/Coins (15).wav"), ShowMenu('load')]
            imagebutton auto "gui/qoptions_%s.png" hovered Play("sound", "audio/Coins (15).wav") action [Play("sound", "audio/Coins (15).wav"), ShowMenu('preferences')]
            imagebutton auto "gui/qnext_%s.png" hovered Play("sound", "audio/Coins (15).wav") action [Play("sound", "audio/Coins (15).wav"), Return(value=None)]



## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    imagebutton auto "gui/start_%s.png" xpos 0.42 ypos 0.2 hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Coins (2).wav"), Start()]
    imagebutton auto "gui/load_%s.png" xpos 0.43 ypos 0.3 hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), ShowMenu('load')]
    imagebutton auto "gui/options_%s.png" xpos 0.41 ypos 0.4 hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), ShowMenu('preferences')]
    imagebutton auto "gui/gallery_%s.png" xpos 0.42 ypos 0.5 hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), ShowMenu('endings')]
    imagebutton auto "gui/credits_%s.png" xpos 0.43 ypos 0.6 hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), ShowMenu('about')]
    imagebutton auto "gui/quit_%s.png" xpos 0.41 ypos 0.7 hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), Quit()]
    imagebutton auto "gui/discord_%s.png" xpos .42 ypos 0.8 hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), OpenURL("https://discord.greycraft.us/betterhalf")]


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background


    ## This empty frame darkens the main menu.
    # frame:
    #     pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    add gui.game_menu_background

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

    frame:

        background None
        left_margin 300
        top_margin 150
        bottom_margin 50

        viewport:
            mousewheel True
            #scrollbars "vertical"

            vbox:
                text "Art, story, and coding by {a=https://nemlei.itch.io/}Nemlei{/a}"
                text " "
                text "Re-Released for our wonderful community by {a=https://renpy.greycraft.us/noahkirby}Noah Kirby{/a}"
                text " "
                text "Made with {a=https://www.renpy.org/}Ren'Py{/a}"
                text "{a=https://www.renpy.org/doc/html/license.html}MIT Licence{/a}"
                text " "
                text "Background music by {a=https://freemusicarchive.org/music/Yshwa/}Yshwa{/a}"
                text "Licenced under {a=https://creativecommons.org/licenses/by-sa/4.0/}CC BY-SA 4.0{/a}"
                text " "
                text "Background music via {a=https://www.FesliyanStudios.com/}Fesliyan Studios{/a}"
                text " "
                text "Interface and Item Sounds by {a=https://cafofomusic.com/}Cafofo{/a}"
                text " "
                text "Font: Artifika, Copyright (c) 2011, Cyreal"
                text "{a=https://www.fontsquirrel.com/license/artifika/}SIL Open Font Licence{/a}"
                text " "
                text "Release version 1.0.1"
#CREDITS HERE DUMBASS

    vbox:
        xalign 0.9
        yalign 0.9
        textbutton "Back" action ShowMenu('main_menu')

## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

################################################################################

screen endings():

    tag menu

    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

    vbox:
        xalign 0.9
        yalign 0.9
        textbutton "Back" hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), ShowMenu('main_menu')]

    vbox:
        xalign 0.5
        yalign 0.1
        add "gui/ends_hover.png"

    vbox:
        xalign 0.75
        yalign 0.5
        if persistent.narcissus:
            text "COUPLE":
                xalign 0.5
            imagebutton auto "gui/narcissus_%s.png" hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), ShowMenu('narcissus')]

        else:
            text "????????":
                xalign 0.5
            add "gui/slot2.png"

    vbox:
        xalign 0.25
        yalign 0.5
        if persistent.merge:
            text "MERGE":
                xalign 0.5
            imagebutton auto "gui/merge_%s.png" hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), ShowMenu('merge')]

        else:
            text "????????":
                xalign 0.5
            add "gui/slot2.png"

    vbox:
        xalign 0.5
        yalign 0.5
        if persistent.halved:
            text "HALVED":
                xalign 0.5
            imagebutton auto "gui/halved_%s.png" hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), ShowMenu('halved')]

        else:
            text "????????":
                xalign 0.5
            add "gui/slot2.png"

################################################################################

# This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

#######################################################

screen narcissus():

    tag menu

    key "K_ESCAPE" action ShowMenu('endings')

    add "images/narcissus.jpg"

    vbox:
        xalign 0.9
        yalign 0.9
        textbutton "Back" action ShowMenu('endings')

screen merge():

    tag menu

    key "K_ESCAPE" action ShowMenu('endings')

    add "images/merge.jpg"

    vbox:
        xalign 0.9
        yalign 0.9
        textbutton "Back" action ShowMenu('endings')

screen halved():

    tag menu

    key "K_ESCAPE" action ShowMenu('endings')

    add "images/halved.jpg"

    vbox:
        xalign 0.9
        yalign 0.9
        textbutton "Back" action ShowMenu('endings')

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load


screen save():

    tag menu

    use file_slots(_("Save"))
    add "gui/save_menu.png" xalign 0.5 yalign 0.15
    grid 2 2:
        xalign 0.8
        yalign 0.15
        spacing 5
        textbutton "Back" hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), Return()]
        textbutton "Load" hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), ShowMenu('load')]
        textbutton "Options" hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), ShowMenu('preferences')]
        textbutton "MAIN" hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), MainMenu()]


screen load():

    tag menu

    use file_slots(_("Load"))
    add "gui/load_menu.png" xalign 0.5 yalign 0.15
    grid 2 2:
        xalign 0.8
        yalign 0.15
        spacing 5
        textbutton "Back" hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), Return()]
        textbutton "Save" hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), ShowMenu('save')]
        textbutton "Options" hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), ShowMenu('preferences')]
        textbutton "MAIN" hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), MainMenu()]


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title)

    grid gui.file_slot_cols gui.file_slot_rows:
        xsize 800
        xalign 0.5
        yalign 0.5

        spacing 10

        for i in range(gui.file_slot_cols * gui.file_slot_rows):
            $slot = i + 1

#HERE_STUPID
            button:
                hover_foreground "gui/slotborder.png"
                hover_sound "audio/Coins (21).wav"
                activate_sound "audio/Click (8).wav"
                xsize 200
                ysize 180
                action FileAction(slot)
                add "gui/slot.png"
                vbox:
                    add FileScreenshot(slot) xalign 0.5 size(190,125)
                    text FileTime(slot, format=_("{#file_time}%B %d %Y, %H:%M"), empty=_("empty slot")):
                        xalign 0.5
                key "save_delete" action FileDelete(slot)

    hbox:
        xalign 0.5
        yalign 0.9
        spacing 20

        for i in range(1,8):
            textbutton "[i]" text_size 40 action FilePage(i)



style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

style pref_bar:
    yalign 0.5
    xysize (313,10)
    left_bar "gui/slider.png"
    right_bar "gui/Bar_empty.png"
    thumb None


screen preferences():

        tag menu

        use game_menu(_("Preferences"), scroll="viewport")

        grid 2 2:
            xalign 0.78
            yalign 0.15
            spacing 5
            textbutton "Back" hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), Return()]
            textbutton "Save" hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), ShowMenu('save')]
            textbutton "Load" hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), ShowMenu('load')]
            textbutton "MAIN" hovered Play("sound", "audio/Coins (21).wav") action [Play("sound", "audio/Click (8).wav"), MainMenu()]



        vbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            hbox:
                spacing 20
                #display mode
                add "gui/displaymode.png"
                frame:
                    xysize(155,72)
                    background "gui/wrap.png"
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        textbutton "Windowed" hovered Play("sound", "audio/Click (8).wav") action Preference("display", "window")
                        textbutton "Fullscreen" hovered Play("sound", "audio/Click (8).wav") action Preference("display", "fullscreen")
                #skip options
                add "gui/skipoptions.png"
                frame:
                    xysize(155,72)
                    background "gui/wrap.png"
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        textbutton "Skip All" hovered Play("sound", "audio/Click (8).wav") action Preference("skip", "all")
                        textbutton "Skip Seen" hovered Play("sound", "audio/Click (8).wav") action Preference("skip", "seen")

            hbox:
                spacing 30
                vbox:
                    spacing 20
                    #text "Text Speed"
                    #text "Auto Speed"
                    text "Music Volume"
                    text "Sound Volume"
                vbox:
                    spacing 20
                    #hbox:
                        #spacing 10
                        #text "-" yalign 0.5
                        #bar:
                            #style "pref_bar"
                            #value Preference("text speed")
                        #text "+"
                    #hbox:
                        #spacing 10
                        #text "-" yalign 0.5
                        #bar:
                            #style "pref_bar"
                            #value Preference("auto-forward time")
                        #text "+"
                    hbox:
                        spacing 10
                        text "-" yalign 0.5
                        bar:
                            style "pref_bar"
                            value Preference("music volume")
                        text "+"
                    hbox:
                        spacing 10
                        text "-" yalign 0.5
                        bar:
                            style "pref_bar"
                            value Preference("sound volume")
                        text "+"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450



## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                imagebutton auto "gui/yes_%s.png" hovered Play("sound", "audio/Coins (15).wav") action yes_action
                imagebutton auto "gui/no_%s.png" hovered Play("sound", "audio/Coins (15).wav") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quickd or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        imagebutton auto "gui/qskip_%s.png" hovered Play("sound", "audio/Coins (15).wav") action [Play("sound", "audio/Coins (15).wav"), Skip()] alternate Skip(fast=True, confirm=True)
        imagebutton auto "gui/qsave_%s.png" hovered Play("sound", "audio/Coins (15).wav") action [Play("sound", "audio/Coins (15).wav"), ShowMenu('save')]
        imagebutton auto "gui/qload_%s.png" hovered Play("sound", "audio/Coins (15).wav") action [Play("sound", "audio/Coins (15).wav"), ShowMenu('load')]
        imagebutton auto "gui/qoptions_%s.png" hovered Play("sound", "audio/Coins (15).wav") action [Play("sound", "audio/Coins (15).wav"), ShowMenu('preferences')]
        imagebutton auto "gui/qnext_%s.png" hovered Play("sound", "audio/Coins (15).wav") action [Play("sound", "audio/Coins (15).wav"), Return(value=None)]



style window:
    variant "small"
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
    
style namebox:
    variant "small"
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding
    
style radio_button:
    variant "small"
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600
