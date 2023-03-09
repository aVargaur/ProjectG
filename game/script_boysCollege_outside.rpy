screen boysCollege_outside():
    imagebutton:
        xpos 0.6355
        ypos 0.55
        idle "shared/door_boyscollege_outside_unhovered.png"
        hover "shared/door_boyscollege_outside_hovered.png"
        action [Hide("boysCollege_outside"), Jump("boysCollege_2floor")]

label nav_boysCollege_outside:
    $ current_location = "Boys college"
    scene bg boyscollege outside day
    show screen boysCollege_outside
    $ renpy.pause(hard=True)
