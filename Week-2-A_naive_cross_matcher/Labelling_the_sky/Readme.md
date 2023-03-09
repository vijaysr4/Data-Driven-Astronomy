When investigating astronomical objects, like active galactic nuclei (AGN), astronomers compare data about those objects from different telescopes at different wavelengths.

This requires positional cross-matching to find the closest counterpart within a given radius on the sky.

In this activity you'll cross-match two catalogues: one from a radio survey, [the AT20G Bright Source Sample (BSS) catalogue](http://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775) and one from an optical survey, [the SuperCOSMOS all-sky galaxy catalogue](http://ssa.roe.ac.uk/allSky).

The BSS catalogue lists the brightest sources from the AT20G radio survey while the SuperCOSMOS catalogue lists galaxies observed by visible light surveys. If we can find an optical match for our radio source, we are one step closer to working out what kind of object it is, e.g. a galaxy in the local Universe or a distant quasar.

We've chosen one small catalogue (BSS has only 320 objects) and one large one (SuperCOSMOS has about 240 million) to demonstrate the issues you can encounter when implementing cross-matching algorithms.

The positions of stars, galaxies and other astronomical objects are usually recorded in either equatorial or Galactic coordinates.

Equatorial coordinates are fixed relative to the celestial sphere, so the positions are independent of when or where the observations took place. They are defined relative to the celestial equator (which is in the same plane as the Earth's equator) and the ecliptic (the path the sun traces throughout the year).

A point on the celestial sphere is given by two coordinates:

Right ascension: the angle from the vernal equinox to the point, going east along the celestial equator;
Declination: the angle from the celestial equator to the point, going north (negative values indicate going south).
The vernal equinox is the intersection of the celestial equator and the ecliptic where the ecliptic rises above the celestial equator going further east.

The coordinates of stars in the sky will change slightly over the years due to the slow wobble of Earth's axis. Therefore, it is important to specify the epoch or time period which we are using as a reference for the celestial coordinate system.

Right ascension is often given in hours-minutes-seconds (HMS) notation, because it was convenient to calculate when a star would appear over the horizon. A full circle in HMS notation is 24 hours, which means 1 hour in HMS notation is equal to 15 degrees.

Each hour is split into 60 minutes and each minute into 60 seconds.

You can convert 23 hours, 12 minutes and 6 seconds (written as 23:12:06 or 23h12m06s) to degrees like this:
```
print(15*(23 + 12/60 + 6/(60*60)))
348.025
```
Declination, on the other hand, is traditionally recorded in degrees-minutes-seconds (DMS) notation. A full circle is 360 degrees, each degree has 60 arcminutes and each arcminute has 60 arcseconds.

For example: 73 degrees, 21 arcminutes and 14.4 arcseconds (written 73:21:14.4 or 73° 21' 14.4" or 73d21m14.4s) can be converted to decimal degrees like this:
```
print(73 + 21/60 + 14.4/(60*60))
73.354
```
With negative angles like -5° 31' 12" the negation applies to the whole angle, including arcminutes and arcseconds:
```
print(-1*(5 + 31/60 + 12/(60*60)))
-5.52
```
Problem:
Write two functions, one that converts right ascension from HMS to decimal degrees, called hms2dec, and another that converts declination from DMS to decimal degrees, called dms2dec.

Right ascension is always an angle from 0 to 24 hours and declination is always an angle from -90° to +90°.

Your hms2dec function should work like this:

```
hms2dec(23, 12, 6)
348.025
```
And your dms2dec function should work like this:

```
dms2dec(22, 57, 18)
22.955
```
It should also work with negative angles:

```
dms2dec(-66, 5, 5.1)
-66.08475
```
