import lombok.Getter;
import util.ArrayTools;
import util.ListTools;
import util.Location;

import java.util.*;
import java.util.concurrent.atomic.AtomicReference;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static java.lang.Integer.MAX_VALUE;
import static java.lang.Math.abs;

public class Day15 extends Day{
    @Getter
    private static class Sensor{
        Location sensorLocation;
        Location closestBeacon;
        Integer clearRadius;
        List<Location> edges;
        public Sensor(String input){
            List<Integer> coords = Arrays.stream(input.replaceAll("[=:, ]+", " ").split(" "))
                    .filter(s -> s.matches("-?\\d+"))
                    .map(Integer::parseInt)
                    .toList();
            this.sensorLocation = new Location(coords.get(1), coords.get(0));
            this.closestBeacon = new Location(coords.get(3), coords.get(2));
            this.updateClearRadius();
            Location top = new Location(sensorLocation.getFirst()-(clearRadius+1), sensorLocation.getSecond()); // up
            Location right = new Location(sensorLocation.getFirst(), sensorLocation.getSecond()+(clearRadius+1)); // right
            Location bottom = new Location(sensorLocation.getFirst()+(clearRadius+1), sensorLocation.getSecond()); // down
            Location left = new Location(sensorLocation.getFirst(), sensorLocation.getSecond()-(clearRadius+1)); // left

            edges = new LinkedList<>();
            edges.addAll(getLine(top, right));
            edges.addAll(getLine(right, bottom));
            edges.addAll(getLine(bottom, left));
            edges.addAll(getLine(left, top));
//            System.out.printf("%s%n", this);
        }

        static List<Location> getLine(Location location1, Location location2){
            int diff1 = location2.getFirst() - location1.getFirst();
            int direction1 = diff1 / abs(diff1); // just want the sign
            int diff2 = location2.getSecond() - location1.getSecond();
            int direction2 = diff2 / abs(diff2);

//            System.out.printf("Getting line from %s to %s, with direction %s, %s%n", location1, location2, direction1, direction2);
            // starting to draw line
            List<Location> line = new LinkedList<>();
            // starting point inclusive
            int i = location1.getFirst();
            int j = location1.getSecond();
            Location temp = location1;
            while(!temp.equals(location2)){
//                System.out.printf("Walking %s, %s%n", i, j);
                line.add(temp);
                // take a diagonal step
                i+=direction1;
                j+=direction2;
                temp = new Location(i, j);
//                break;
            }
            return  line;
        }
        public void updateClearRadius(){
            this.clearRadius = this.sensorLocation.getManhattanDistance(this.closestBeacon);
        }
        @Override
        public String toString(){
            return "[sensor: %s, beacon: %s, radius %s]%n".formatted(this.sensorLocation, this.closestBeacon, this.clearRadius);
        }
        public boolean coversLocation(Integer row, Integer col){
            Integer manhattanDistance = this.sensorLocation.getManhattanDistance(new Location(row, col));
            return manhattanDistance <= this.clearRadius;
        }
    }
    List<Sensor> sensorList;
    Location gridMax;
    Location gridMin;

    public Day15(Type type){
        super(15, type);
        System.out.printf("Beginning setup Day: %s, type: %s%n", this.day, this.type);
        this.sensorList = this.strings.stream()
                .map(Sensor::new)
                .toList();

        AtomicReference<Integer> maxRow = new AtomicReference<>(0);
        AtomicReference<Integer> minRow = new AtomicReference<>(MAX_VALUE);
        AtomicReference<Integer> maxCol = new AtomicReference<>(0);
        AtomicReference<Integer> minCol = new AtomicReference<>(MAX_VALUE);
        sensorList.forEach(sensor -> {
            Location location = sensor.getSensorLocation();
            maxRow.set(Math.max(location.getFirst()+sensor.getClearRadius(), maxRow.get()));
            minRow.set(Math.min(location.getFirst()-sensor.getClearRadius(), minRow.get()));
            maxCol.set(Math.max(location.getSecond()+sensor.getClearRadius(), maxCol.get()));
            minCol.set(Math.min(location.getSecond()-sensor.getClearRadius(), minCol.get()));
        });
        this.gridMin = new Location(minRow.get(), minCol.get());
        this.gridMax = new Location(maxRow.get(), maxCol.get());
        System.out.printf("Max: %s%n", this.gridMax);
        System.out.printf("Min: %s%n%n", this.gridMin);
    }

    public Integer countPositionsWhereBeaconCannotBe(Integer row){
        if (row>this.gridMax.getFirst())
            return -1;

        // Find the indexes that are within radius of a beacon
        List<Integer> coveredIndexes = new ArrayList<>(ArrayTools.getIndexes(this.gridMin.getSecond(), this.gridMax.getSecond())
                .filter(index -> {
                    for (Sensor s : sensorList) {
                        if (s.coversLocation(row, index)) {
                            return true;
                        }
                    }
                    return false;
                })
                .boxed().toList());

        // remove indexes that we know hold a beacon
        int beaconCount = sensorList.stream().map(Sensor::getClosestBeacon)
                .filter(beacon -> Objects.equals(beacon.getFirst(), row))
                .filter(beacon -> coveredIndexes.contains(beacon.getSecond()))
                .distinct()
//                .peek(System.out::println)
                .toList().size();

        // return result
        System.out.printf("Covered Indexes - length: %s - beaconCount: %s = %s%n", coveredIndexes.size(), beaconCount, coveredIndexes.size()-beaconCount);
        return coveredIndexes.size()-beaconCount;
    }

    public Integer part1(){
        int rowNumber = this.type.equals(Type.EXAMPLE) ? 10 : 2000000;
        return countPositionsWhereBeaconCannotBe(rowNumber);
    }

    private List<Location> findOverlappingPoints(){
        Map<Location, Integer> overlappingEdges = new HashMap<>();
        for(Sensor a : sensorList){
            for(Sensor b : sensorList){
                if(a.equals(b)){
                    continue;
                }
                a.getEdges().parallelStream()
                        .filter(x-> b.getEdges().contains(x))
                        .forEach(x->{
                            int count = overlappingEdges.getOrDefault(x, 0);
                            overlappingEdges.put(x, count+1);
                        });
            }

        }
        return overlappingEdges.entrySet().stream()
                .filter(e-> e.getValue()==4)
                .map(Map.Entry::getKey)
                .toList();
    }
    public static Integer getTuningFrequency(Location location){
        return location.getFirst() + (4000000 * location.getSecond());
    }

    public Integer part2(){
        System.out.printf("Beginning part 2%n");
        int max = this.type.equals(Type.EXAMPLE) ? 20 : 4000000;

//        Stream<Location> mapCorners = Stream.of(
//            new Location(0, 0),
//            new Location(0, max),
//            new Location(max, 0),
//            new Location(max, max)
//        );

        Stream<Location> candidates = this.sensorList.stream()
                .map(Sensor::getEdges)
                .flatMap(Collection::stream)
                .filter(location -> 0<=location.getFirst() && location.getFirst()<=max)
                .filter(location -> 0<=location.getSecond() && location.getSecond()<=max);

        return candidates.parallel()
                .filter(s->{
                    for(Sensor sensor : sensorList){
                        if(sensor.coversLocation(s.getFirst(), s.getSecond())){
                            return false;
                        }
                    }
                    return true;
                })
                .distinct()
                .peek(System.out::println)
                .map(Day15::getTuningFrequency)
                .findAny().get();
    }
}
