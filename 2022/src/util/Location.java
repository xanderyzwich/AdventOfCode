package util;

import static java.lang.Math.abs;

public class Location extends Tuple<Integer, Integer>{

    public Location(Integer first, Integer second) {
        super(first, second);
    }

    public Integer getManhattanDistance(Location other){
        Integer firstDiff = abs(this.getFirst() - other.getFirst());
        Integer secondDiff = abs(this.getSecond() - other.getSecond());
        return firstDiff + secondDiff;
    }
}
