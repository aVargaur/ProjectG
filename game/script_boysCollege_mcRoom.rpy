screen boysCollege_mcRoom():
    imagebutton:
        xpos 0.5
        ypos 0.28
        idle "boysCollege_mcRoom/mc_bed.png"
        action Jump("boysCollege_mcRoom_sleep_in_bed")
    imagebutton:
        xpos 0.1
        ypos 0.28
        idle "shared/door_1.png"
        #action Jump("nav_boysCollege_2floor")
        action [Hide("boysCollege_mcRoom"), Jump("nav_boysCollege_2floor")]

label nav_boysCollege_mcRoom:
    $ current_location = "My room"
    scene bg mc room
    show screen boysCollege_mcRoom
    $ renpy.pause(hard=True)

label boysCollege_mcRoom_sleep_in_bed:
    menu:  
        "Do you want to sleep?"
        "Yes":       
            call advance_day() # advances time by 1 unit
        "No":
            "Im not sleepy."
    $ renpy.pause(hard=True)