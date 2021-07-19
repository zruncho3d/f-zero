## F-Zero: a Voron-0 mod from Zruncho
Put your Voron-0 in a box and make it fly.  Get your own Voron-2 trainer on the cheap.

![picture](Images/front_green_black_silver.png)

This picture is heavily out of date.  The printer has been printing since June 2021.

A full CAD is in progress.

### Buildlog and Design Doc

[See the Buildlog and Design Gdoc](https://docs.google.com/document/d/1dm8itefYrLIsCcOQht9sdMzrXE8Jk30s56c9IwtRCkM/edit#heading=h.c4f5tznx0p31) for more details:
- status
- BOM
- assembly manual
- design notes
- ...and more

### Parts in this Repo

In this repo are all the STLs you need to make an F-Zero, except for:
- Voron 0.0 or 0.1 parts, including gantry, toolhead, carriage retainers, and M2 nutbars
- Z endstop (see #micron-v2 on DoomCube Discord)

All parts should be already be in print-ready orientation, and no supports are needed.

Standard Voron settings, or lowered infill and fewer perims, should work fine for most parts:
- 3-4 perimeters
- 16-40% infill, depending on the part
- 0.4-0.5mm width
- 0.2mm layer height

Exceptions include:
- Frame Corners: print at 4 perimeters, 0% infill, 0.16mm layer height (seriously)

### Frame Corners

Note that for the frame corners, on 2021-07-18, new _24 versions were added,
with improvements.  The 24 refers to 24mm, for the offset from the top of the
printer to the top of the vertical extrusion.  Previously it was 25mm, which
matched a 250mm height for a BlindJoints F0 made with 250mm vertical extrusions.
However, the normal V0 has a 248mm height, from 200mm vertical extrusions
plus plastic parts on top.  By changing to a 24mm offset, stock V0 enclosure
clips can be used and should fit exactly.
