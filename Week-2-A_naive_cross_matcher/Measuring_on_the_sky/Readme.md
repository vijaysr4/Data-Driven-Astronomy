To crossmatch two catalogues we need to compare the angular distance between objects on the celestial sphere.

People loosely call this a "distance", but technically its an angular distance: the projected angle between objects as seen from Earth.

If we have an object on the celestial sphere with right ascension and declination $\left(\alpha_1, \delta_1\right)$, then the angular distance to another object with coordinates $\left(\alpha_2, \delta_2\right)$ is:
$$
d=2 \arcsin \sqrt{\sin ^2 \frac{\left|\delta_1-\delta_2\right|}{2}+\cos \delta_1 \cos \delta_2 \sin ^2 \frac{\left|\alpha_1-\alpha_2\right|}{2}}
$$

 
Angular distances have the same units as angles (degrees). There are other equations for calculating the angular distance but this one, called the haversine formula, is good at avoiding floating point errors when the two points are close together.

We'll go through an example of how to implement the formula you saw on the previous slide using NumPy's trigonometric functions. Please keep in mind that NumPy trigonometric functions only take radians as input so you need to convert your coordinates when needed.

First, let's break down the formula into smaller parts:
$$ d=2 \arcsin \sqrt{a+b}$$
$$ a= \sin^2 \frac{\left|\delta_1 - \delta_2\right|}{2}$$
$$ b= \cos \delta_1 \cos \delta_2 \sin^2 \frac{\left|\alpha_1 - \alpha_2\right|}{2} $$

We can calculate b with NumPy's sin, cos and abs functions:
~~~
b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
~~~
Here, $r_1$ and $d_1$ are the coordinates of the first point $\left(\alpha_1, \delta_1\right)$ and $r_2$ and $d_2$ similarly correspond to $\alpha_2$ and $\delta_2$.

$a$ can be calculated in a similar way using just sin and abs. Once we have both $a$ and $b$
  we can use numpy.arcsin to calculate $d$:
~~~
d = 2*np.arcsin(np.sqrt(a + b))
~~~
Using NumPy, the code works with individual or arrays of sources.

#### Note:
Trig functions in most languages and libraries (including Python and NumPy) take angle arguments in units of radians, but the databases we're working with use angles of degrees.

Fortunately, NumPy provides convenient conversion functions:
~~~
a_rad = np.radians(a_deg)
a_deg = np.degrees(a_rad)
~~~
The variable a_deg is in units of degrees and a_rad is in radians.

Problem: 
Write a function called angular_dist that calculates the angular distance between any two points on the celestial sphere given their right ascension and declination.

Your function should take arguments in decimal degrees and return the distance in decimal degrees too.

Here's an example of how your function should work:
```
ra1, dec1 = 21.07, 0.1
ra2, dec2 = 21.15, 8.2
angular_dist(ra1, dec1, ra2, dec2)
8.1003923181465041
```
Here’s another example:
```
angular_dist(10.3, -3, 24.3, -29)
29.208498180546595
```
