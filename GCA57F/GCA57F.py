####################################################################################################
# https://www.geocaching.com/geocache/GCA57F                                                       #
# Go to the SE corner of 45th and Elm St in Vancouver, B.C. There you will see at the intersection #
# of the 45th ave. sidewalk and the Elm St. sidewalk, a small survey mark in the concrete about    #
# 5 mm in diameter. Determine this UTM. From here, go 6,493 meters East, and 12,456 m South.       #
# From your answer, you will have to put in a correction factor to allow for the UTM grid.         #
# The correction factor is, 14.937 meters East, and 9.105 meters North. You should now be          #
# at a manmade object a few feet long. From here go 150 degrees True for 52 meters.                #
####################################################################################################
import pyproj


def shift(lon, lat, deg, dist):
    """Shifts a point by a given distance (meters) into a direction (degrees)."""
    geod = pyproj.Geod(ellps='WGS84')
    return geod.fwd(lon, lat, deg, dist)[:2]


if __name__ == '__main__':
    start = (-123.164261, 49.230950)
    start_east = shift(start[0], start[1], 90, 6493)
    start_east_south = shift(start_east[0], start_east[1], 180, 12456)
    target = shift(start_east_south[0], start_east_south[1], 150, 52)
    print('The geocache is at {Y}, {X}'.format(X=target[0], Y=target[1]))
