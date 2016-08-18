#!/usr/bin/python

import argparse, math
import datetime

def getWeeks():
    start = datetime.date(2015, 12, 7)
    # Adjusted for summer break
    now = datetime.date.today() - datetime.timedelta(weeks = 7)
    return (now-start).days / 7

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reps", "-r", type=int, default=getWeeks(),
                        help="reps of the day")
    parser.add_argument("--splits", "--sets", "-s", type=int,
                        help="number of sets")
    parser.add_argument("--inc", "-i", type=float, default=0.3,
                        help="increased number of reps pr set")

    args = parser.parse_args()

    print "One set reps this week is:", args.reps

    if args.splits and args.splits > 0:
        splits = args.splits
        reps = args.reps
        incfactor = args.inc

        total = math.ceil((reps + (splits - 1) * incfactor * reps))
        setreps = total / splits
        ceilreps = math.ceil(setreps)
        diff = ceilreps * splits - total
        sets = [int(ceilreps)] * (splits - 1) + [int(ceilreps - diff)]

        print "Total number of reps for", args.splits, "sets is:", int(total)
        print "Recommended sets:", sets

if __name__ == "__main__":
    main()
