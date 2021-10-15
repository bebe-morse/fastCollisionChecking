# fastCollisionChecking

For a large number of points, it becomes performance intensive to check if any of those points collide with one another. The default method would be to construct a double loop, looping over the set of points twice and checking if the distance between any two given points is less than some value R.

Here, spatial hashing is used to increase performance. Performance increases range from 50x - 1000x with a small collision radius, given an initial set of points of size more than 500.

