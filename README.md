# fastCollisionChecking

For a large number of points, it becomes performance intensive to check if any of those points collide with one another. The default method would be to construct a double loop, looping over the set of points twice and checking if the distance between any two given points is less than some value R.

Here, spatial hashing is used to increase performance. Performance increases range from 50x - 1000x with a small collision radius, given an initial set of points of size more than 500.

You may verify the tests yourself by running tests.py. Here, I have posted the results of the tests I ran on my machine.

__________________________________________________
Test 1 of 8

Number of points: 500\n
Collision radius: 0.1


Success! Speed-up: 7.80x
Spatial Hashing : 0.0347s
Double Looping : 0.2707s
__________________________________________________


__________________________________________________
Test 2 of 8

Number of points: 500
Collision radius: 0.01


Success! Speed-up: 35.63x
Spatial Hashing : 0.0077s
Double Looping : 0.2733s
__________________________________________________


__________________________________________________
Test 3 of 8

Number of points: 500
Collision radius: 0.001


Success! Speed-up: 32.14x
Spatial Hashing : 0.0084s
Double Looping : 0.2715s
__________________________________________________


__________________________________________________
Test 4 of 8

Number of points: 1000
Collision radius: 0.0001


Success! Speed-up: 70.12x
Spatial Hashing : 0.0155s
Double Looping : 1.0853s
__________________________________________________


__________________________________________________
Test 5 of 8

Number of points: 2500
Collision radius: 0.25


Success! Speed-up: 1.88x
Spatial Hashing : 3.7105s
Double Looping : 6.9943s
__________________________________________________


__________________________________________________
Test 6 of 8

Number of points: 2500
Collision radius: 0.1


Success! Speed-up: 8.29x
Spatial Hashing : 0.8301s
Double Looping : 6.8796s
__________________________________________________


__________________________________________________
Test 7 of 8

Number of points: 2500
Collision radius: 0.01


Success! Speed-up: 149.66x
Spatial Hashing : 0.0463s
Double Looping : 6.9366s
__________________________________________________
