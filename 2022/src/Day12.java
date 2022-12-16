import lombok.AllArgsConstructor;
import util.Tuple;

import java.time.Clock;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.*;
import java.util.stream.Stream;

import static java.lang.Math.abs;

public class Day12 extends Day{

    static class Coordinate extends Tuple<Integer, Integer>{
        public Coordinate(Integer first, Integer second) {
            super(first, second);
        }
    }
    @AllArgsConstructor
    static class CoordinateCost{
        int cost;
        Coordinate location;
        @Override
        public boolean equals(Object obj){
            if (this == obj)
                return true;
            if (obj == null)
                return false;
            if (obj.getClass() == Coordinate.class){
                return this.location.equals(obj);
            }
            if (getClass() != obj.getClass())
                return false;
            CoordinateCost other = (CoordinateCost) obj;
            return this.location.equals(other.location);
        }
        @Override
        public int hashCode(){
            final int offset = 10000;
            return this.location.hashCode();
        }
        @Override
        public String toString(){
            return "Cost: %s, Location: %s%n".formatted(this.cost, this.location);
        }
    }
    char[][] altitudes;
//    Queue<CoordinateCost> toCheck;
//    List<CoordinateCost> visited;
    List<Coordinate> lowestPoints;
    Coordinate start;
    Coordinate end;
    public Day12(Type type){
        super(12, type);
        altitudes = new char[this.strings.size()][this.strings.get(0).length()];
//        this.visited = new LinkedList<>();
        this.lowestPoints = new LinkedList<>();

        for(int i=0; i<this.strings.size(); i++){
            String line = this.strings.get(i);
            for(int j=0; j<line.length(); j++){
                char current = line.charAt(j);
                Coordinate currentCoord = new Coordinate(i, j);
                if(current == 'S' || current == 'a')
                    lowestPoints.add(currentCoord);
                if(current == 'S') {
                    start = currentCoord;
                    altitudes[i][j] = 'a';
                } else  if(current == 'E') {
                    end = currentCoord;
                    altitudes[i][j] = 'z';
                } else {
                    altitudes[i][j]=current;
                }
            }
        }
//        this.toCheck = new LinkedList<>(){{
//            add(new CoordinateCost(0, start));
//        }};
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

    private Integer findShortestDistance(Coordinate start){
        Queue<CoordinateCost> toCheck = new LinkedList<>(){{
            add(new CoordinateCost(0, start));
        }};
        List<CoordinateCost> visited = new ArrayList<>();
        while(!toCheck.isEmpty()){
            CoordinateCost current = toCheck.poll();
            visited.add(current);
            if(this.end.equals(current.location)) {
                System.out.printf("End Found: %s%n", current.cost);
                return current.cost;
            }
            this.getNeighborLocations(current.location).stream()
                    .map(neighborLocation -> new CoordinateCost(current.cost +1, neighborLocation))
                    .filter(neighbor -> !visited.contains(neighbor))
                    .filter(neighbor -> !toCheck.contains(neighbor))
                    .filter(neighbor -> this.canClimb(current.location, neighbor.location))
                    .forEach(toCheck::add);
        }
//        System.out.printf("End Location: %s%n", this.end);
        return 0;
    }

    public List<Coordinate> getNeighborLocations(Coordinate currentLocation) {
        return Stream.of(
                new Coordinate(currentLocation.getFirst(), currentLocation.getSecond() - 1),  // Up
                new Coordinate(currentLocation.getFirst(), currentLocation.getSecond() + 1),  // Down
                new Coordinate(currentLocation.getFirst() - 1, currentLocation.getSecond()), // Left
                new Coordinate(currentLocation.getFirst() + 1, currentLocation.getSecond())  // Right
        ).filter(this::onMap).toList();
    }

    public Integer part1(){
        Integer result = this.findShortestDistance(start);
        return result;
    }

    public Integer part2(){
        return this.lowestPoints.stream()
                .map(this::findShortestDistance)
                .filter(i -> i!=0)
                .sorted().findFirst().get();
    }
}
