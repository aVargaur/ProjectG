screen boysCollege_2floor():
    imagebutton:
        xpos 0.25
        ypos 0.28
        idle "shared/door_1_unhovered.png"
    imagebutton:
        xpos 0.7
        ypos 0.28
        idle "shared/door_1_unhovered.png"
        action [Hide("boysCollege_2floor"), Jump("nav_boysCollege_mcRoom")]

label nav_boysCollege_2floor:
    $ current_location = "Boys college: 2. floor"
    scene bg boysCollege 2floor
    show screen boysCollege_2floor
    $ renpy.pause(hard=True)
