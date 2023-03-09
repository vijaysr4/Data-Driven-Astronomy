**Problem 1: Look around you**

Write a find_closest function that takes a catalogue and the position of a target source (a right ascension and declination) and finds the closest match for the target source in the catalogue.

Your function should return the ID of the closest object and the distance to that object.

The right ascension and declination are in degrees. The catalogue list has been loaded by import_bss from the previous question. The full 320 object BSS catalogue is contained in bss.dat for you to test your code on.

Here's an example of how your function should work:
~~~
>>> cat = import_bss()
>>> find_closest(cat, 175.3, -32.5)
(156, 3.7670580226469053)
~~~
And here's another example:
~~~
>>> cat = import_bss()
>>> find_closest(cat, 32.2, 40.7)
(26, 57.729135775621295)
~~~

**A full cross-matching program**

You now have all the tools necessary to crossmatch the BSS and SuperCOSMOS catalogues. In the next problem you'll put it all together to see how many of the bright radio sources in the BSS catalogue have a counterpart in the SuperCOSMOS catalogue. The process you should follow is:

Select an object from the BSS catalogue;
Go through all the objects in SuperCOSMOS and find the closest one to the BSS object;
If the objects are close enough, record the match;
Repeat 1-3 for all the other objects in the BSS catalogue.
In step 3, if the closest object isn't within a given distance then it's unlikely that the two objects are actually counterparts, and it's more likely that they just happen to be nearby.

The given distance you choose depends on the uncertainty of the measured object positions in each catalogue.

Although we are cross matching based solely on celestial coordinates in the following exercise, there are other properties we could consider while conducting research, such as the brightness and color of an object.

**Problem 2: Matchup**

Write a crossmatch function that crossmatches two catalogues within a maximum distance. It should return a list of matches and non-matches for the first catalogue against the second.

The list of matches contains tuples of the first and second catalogue object IDs and their distance. The list of non-matches contains the unmatched object IDs from the first catalogue only. Both lists should be ordered by the first catalogue's IDs.

The BSS and SuperCOSMOS catalogues will be given as input arguments, each in the format you’ve seen previously. The maximum distance is given in decimal degrees.

Here's how crossmatch should work on our sample catalogues with a maximum distance of 40 arcseconds:
~~~
bss_cat = import_bss()
super_cat = import_super()
max_dist = 40/3600
matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
print(matches[:3])
print(no_matches[:3])
print(len(no_matches))
~~~
~~~
[(1, 2, 0.00010988610938710059), (2, 4, 0.00076498459672424946), (3, 5, 0.00020863352870707666)]
[5, 6, 11]
9
​~~~
Only 9 objects have no match. Let's try a 5 arcsecond maximum:
~~~
bss_cat = import_bss()
super_cat = import_super()
max_dist = 5/3600
matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
print(matches[:3])
print(no_matches[:3])
print(len(no_matches))
~~~
~~~
[(1, 2, 0.00010988610938710059), (2, 4, 0.00076498459672424946), (3, 5, 0.00020863352870707666)]
[5, 6, 11]
40
​~~~
Now 40 objects have no match with the tighter search radius.