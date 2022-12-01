Day 17:  How To Be Efficient

From https://adventofcode.com/2021/day/17

I should start off by saying that a simple brute-force search works pretty quickly for this challenge.  But the patterns in the data intrigued me, and I felt like I could find a more efficient solution.  This is the quixotic result of that search ;-)

The first insight I had (which is implemented in my original solution (https://github.com/luciansmith/adventOfCode/blob/main/day17.py) is this:  if you can get the Y value into the target range in N steps, and you can also get the X value into the target range in N steps, then (x,y) is one of the solutions to the problem.

The second insight is this:  If you can get X into the target range in N steps when its velocity is zero, the all values [N : inf] are also possible.

The third insight is that if Y is positive, the missle will reach a Y value of exactly zero in 2Y+1 steps, having achieved a height of the Yth triangular number.  From there, the next Y value it will visit is Y+1.  Thus, the largest initial value Y can have is -Ymin-1, where Ymin is the lower bound of the target area.  Any higher Y value will overshoot the target area after reaching a value of 0 again.

[Side note:  Triangular numbers (https://en.wikipedia.org/wiki/Triangular_number) are the values obtained when adding 1 + 2 + ... + N, so (1, 3, 6, 10, ...).]

Taken together, this means that if we want to find the initial trajectory that reaches the greatest height, we should start by assuming a Y value of Ymin-1.  This means checking X values to see if we can find any X value that can reach the target in 2(Ymin-1)+1 steps (aka 2Ymin-1).

Our best bet on this front is to find a value of X that reaches the target are at the same time the missile achieves an X velocity of zero.  We could search for X values starting at zero and going up, but it's going to be more efficient if we work in a frame where X is accelerating, i.e. backwards in time.  Hence, we start with a value of 0, then add 1, then add 2, etc. and see if we can hit the target with this set of numbers (known as 'triangular numbers').

If so, and if Xsteps <= 2Ymin-1, we're done with part 1!  The max height we can achieve is (-Ymin-1)+! (aka the -Ymin-1'th triangular number.  All max height values are triangular numbers!)

If not, or if Xsteps > 2Ymin-1, we need to start our search.  In order to find the answer to part 1 as fast as possible, the primary value we're going to be searching along is *number of steps*, starting from the highest and decreasing from there. We already have Ysteps_max, so our search will start there and go down as we search for valid Ys.  So now we need to do the same with X.

As we noted before, if a triangular number is inside our X target range, Xsteps_max is infinity, since after we reach a velocity of 0, we can stay inside the target range forever.  (In this case, if the Nth triangular number is in our target range, X_init is N.)

Side note: it may be that multiple triangular numbers fulfil this condition--in the example scenario, the X range was [20, 30], which contains both the 6th and 7th triangular numbers (21 and 28).  Because Ymin was -10, the an optimmum Y value was 9, and hence both (6, 9) and (7, 9) could achieve the maximum height of 45.

If we need to search for more X values (either because we didn't get lucky and end up with a range containing a triangular number, or because we did but it took too long to get there), we need to find the X value such that Xsteps <= Ystep_max, then start searching backwards from there.

Our search begins from the triangular number closest to but greater than Xmax.
[Still need to work out how to do this with maximal efficiency.]

Once we find a valid X value with an Xsteps less than Ysteps, we switch to searching for a Y with a Ysteps that matches.  Once that search ends up with a Ysteps less than Xsteps, we switch back to searching X's, etc.

Our search for Y values starts at (-Ymin-1) (aka Y_init) and goes down from there.  Because there's a target range, we know that all values from Y_init to -Ymax-1) will hit the target range, decreasing the number of steps it takes to get there by 2 each time (2Y_init+1 steps at the max, 2(Y_init-1)+1 steps next, etc.)  It's also possible that a particular Y_init will hit the target area twice, which could fill in the skipped step (for the completionist part 2, or for highly-constrained X values).  So the overall algorithm here is to decrease Y_init by one, then check whether moving Y_init+1 *down* from 0 will hit our target, then 2Y_init+2, 3Y_init+3, etc. until we've overshot our target.  We record the number of steps we need to reach the target, and if it's lower than our target X_steps, we switch back to our X search.

If we find no valid X,Y combinations before we get to a Y_init value of 0, we're done with part 1:  the maximum height we can possibly reach is 0.  It will always be possible to reach the target in one step by choosing values of X and Y inside the target range (going straight there in one step), and everything in between will be moving in a negative direction, so 0 is our minimum possible maximum height.

Once we start exploring negative Y_init values, the only reason to do so is for part 2.  Here, the search is identical to our X search, the only difference being that instead of changing to moving backwards in time so our acceleration is positive, we stay in a forwards-in-time frame, because acceleration is already positive.

Once we get to the worse-case scenario of 'we have to move there in a single step', it's easy to count the number of possible one-step solutions:  the total area of the target, one x,y combination for every valid space in the target area.

And that's it!

