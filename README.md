# F-Zero - an Evolved Voron Zero

by Zruncho and `#flying-zero` collaborators on the [DoomCube Discord](https://discord.gg/doomcube):
L.e.o.p.a.r.d, finn, Kayos Maker, hartk, ericsson, sci, and more

### Upgrade your V0 or build a fresh F0.  
### Full auto-calibration at a fraction of the price of a V2.  
### Make every first layer perfect!

### → [Parts List](https://docs.google.com/spreadsheets/d/1EkonubBAvg1huz3OgxQa6iyDdansaWyFQbpp1GPkiBE/edit#gid=0): delta relative to V0.1
### → [See one in action!](https://youtu.be/jLSPeJ7L9R4)  (V0.802 Serial Request)
### → [Get Support](https://discord.gg/doomcube) (#flying-zero on DoomCube Discord)
### → [CAD in browser](https://grabcad.com/library/f-zero-cad-1)

![picture](Renders/iso.png)

Join us on the [DoomCube Discord](https://discord.gg/doomcube) for the latest info and any questions!

### Buildlog and Design Doc

[See the Assembly Manual and Buildlog Gdoc](https://docs.google.com/document/d/1dm8itefYrLIsCcOQht9sdMzrXE8Jk30s56c9IwtRCkM/edit#heading=h.c4f5tznx0p31) for more details.

While the printer is in development, this Gdoc is the source of truth.

Find a changelog, highlights, and more there.

### Parts in this Repo

In this repo are all the STLs you need to make an F-Zero, except for:
- Voron 0.0 or 0.1 parts, including gantry, toolhead, carriage retainers, tophat, and M2 nutbars
- Z endstop (see #micron-v2 on DoomCube Discord)

All parts should be already be in print-ready orientation, and no supports are needed.

Standard Voron settings, or lowered infill and fewer perims, should work fine for most parts:
- 3-4 perimeters
- 16-40% infill, depending on the part
- 0.4-0.5mm width
- 0.2mm layer height

Exceptions include:
- Frame Corners: print at 5 or 6 perimeters, 10% infill, 0.16mm layer height (seriously)
- Electronics Mezzanine Spacers: print at 3 perimeters, 0% infill, 0.2 layer height
- NoDropNuts: print at 3 perimeters, 0% infill, 0.2 layer height

### FAQ

#### Q: F-Zero vs Micron… what’s the difference?

If you're asking this question, you should probably visit the [3D Printers for Ants](https://3dprintersforants.com/) website first, to see a visual landscape of the latest small printers.

To answer your question though... **at a high level, F-Zero and Micron have the same idea:** take the best quality-of-life features from larger printers, and put them on a small printer.

Both have ~120mm-on-a-side build space, use 1515 extrusions, use Klicky and 4 Z motors and belt reduction to enable QGL, have NEMA14-size motors on the gantry, and use the MiniAB from the V0.1 - **but each has a completely opposite execution.**

Hartk took the Voron 2.4 design and scaled it down to create Micron.  It looks like a V2, but smaller.  

Zruncho took the V0 design and wrapped it in a box to create F0.

Micron lives in its own ecosystem, with the V0 toolhead being the only shared item.

F0 lives within the existing V0 ecosystem (the gantry is unchanged!), so you can use existing V0 kits and parts, including LDO color frames, pre-cut panels, toolhead and umbilical boards, and more.  With almost 1500 serial’ed V0s as of March 2022, **this is a huge ecosystem**.  Your wallet gets to benefit from the price competition between suppliers that is only possible with a large ecosystem.  Your printer gets to benefit from the innovative new products that often emerge to support large market: things like easier-to-assemble [visible-joint frames](https://www.aliexpress.com/item/1005003198676826.html), super-solid [metal X-carriages](https://www.aliexpress.com/item/1005003371851612.html), and more.  This attribute is true for any V0-based mod, including [Tri-Zero](https://github.com/zruncho3d/tri-zero), [Double Dragon](https://github.com/zruncho3d/double-dragon), and any others.

**Size?**  From a size perspective, Micron is wider than a V0 or F0 by 20mm, while F0 is deeper by 50mm than both V0 and Micron.  Really, though, they’re both pretty small.  The V0 design is extremely space-efficient in the XY direction, while Micron uses a wider V2-style gantry that removes the need for two extra extrusions.

**Parts?** Nearly all non-printed parts, minus the frame, are shared between the two designs, but nearly all printed parts are different, with the exception of the MiniAB toolhead, which both share with the V0.

**Prints?** Both can print amazingly well and fast, and should scale similarly to larger sizes.

**Documentation?** Micron has its own manual, while F0 has build notes and is able to reuse much of the V0 manual.

**The Takeaway:** If you already have a V0, and want to do an upgrade, F0 is a great option, as it retains more of a V0 kit; you won’t need to waste money on new panels or a new frame, and you'll have fewer parts to print.

It’s more of a personal preference for fresh builds.

### Frame Corners