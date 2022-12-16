import util.Tuple;

import java.util.*;
import java.util.stream.Stream;

import static java.lang.Math.abs;

public class Day12 extends Day{

    static class Coordinate extends Tuple<Integer, Integer>{
        public Coordinate(Integer first, Integer second) {
            super(first, second);
        }
    }
    char[][] altitudes;
    int[][] distances;
    Coordinate start;
    Coordinate end;
    public Day12(Type type){
        super(12, type);
        altitudes = new char[this.strings.size()][this.strings.get(0).length()];
        this.distances = new int[altitudes.length][altitudes[0].length];
        for(int i=0; i<this.strings.size(); i++){
            String line = this.strings.get(i);
            for(int j=0; j<line.length(); j++){
                char current = line.charAt(j);
                if(current == 'S') {
                    start = new Coordinate(i, j);
                    altitudes[i][j] = 'a';
                } else  if(current == 'E') {
                    end = new Coordinate(i, j);
                    altitudes[i][j] = 'z';
                } else {
                    altitudes[i][j]=current;
                }
            }
        }
//        System.out.printf("Start is %s%n", start);
//        System.out.printf("End is %s%n", end);
    }

    public boolean onMap(Coordinate location){
        return location.getFirst() >= 0 && location.getFirst()<this.altitudes.length
                && location.getSecond() >= 0 && location.getSecond()<this.altitudes[0].length;
    }
    public boolean offMap(Coordinate location){ return !this.onMap(location);}
    private char getAltitude(Coordinate location){
        return this.altitudes[location.getFirst()][location.getSecond()];
    }
    public boolean canClimb(Coordinate from, Coordinate to){
        return 1>= this.getAltitude(to)-this.getAltitude(from);
    }
    public boolean cannotClimb(Coordinate from, Coordinate to){ return !this.canClimb(from, to); }
    public int getDistance(Coordinate location){
        return distances[location.getFirst()][location.getSecond()];
    }
    public void setDistance(Coordinate location, int distance){
        distances[location.getFirst()][location.getSecond()] = distance;
    }

    private Integer calculateDistance(List<Coordinate> visited, Coordinate currentLocation){
        // Check if you are at the end
        if(this.end.equals(currentLocation)){
            return 0;
        }

        // check if another path has found this location with a shorter path
        int previousDistance = this.getDistance(currentLocation);
        if(previousDistance>0 && previousDistance <=visited.size())
            return null;
        else
            this.setDistance(currentLocation, visited.size());

//        System.out.printf("shortestPath called for %s, %s%n", currentLocation.getRow(), currentLocation.getCol());

        // add self to visited list for neighbors to consider
        List<Coordinate> newVisited = new LinkedList<>(visited){{
            add(currentLocation);
        }};

        return getNeighborLocationStream(currentLocation).stream()
                .filter(t->!visited.contains(t))
                .filter(t-> canClimb(currentLocation, t))
                .map(t-> this.calculateDistance(newVisited, t))
                .filter(Objects::nonNull)
                .map(i-> i+1)
                .min(Integer::compareTo).orElse(null);
    }

    public List<Coordinate> getNeighborLocationStream(Coordinate currentLocation) {
        return Stream.of(
                new Coordinate(currentLocation.getFirst(), currentLocation.getSecond() - 1),  // Up
                new Coordinate(currentLocation.getFirst(), currentLocation.getSecond() + 1),  // Down
                new Coordinate(currentLocation.getFirst() - 1, currentLocation.getSecond()), // Left
                new Coordinate(currentLocation.getFirst() + 1, currentLocation.getSecond())  // Right
        ).filter(this::onMap).toList();
    }

    public Integer part1(){
        Coordinate checkPoint = new Coordinate(1, 4);
        Integer result = this.calculateDistance(new LinkedList<>(), start);
//        Integer result = this.calculateDistance(new LinkedList<>(), end);
//        Integer result = this.calculateDistance(new LinkedList<>(), checkPoint);
//        System.out.println(Arrays.deepToString(this.distances));
        return result;
    }

    public Integer part2(){
        return 0;
    }
}
