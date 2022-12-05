import lombok.Data;

import java.util.List;

public class Day4 extends Day {

    @Data
    static
    class Range {
        int start;
        int end;
        public Range(String start, String end){
            this.start = Integer.parseInt(start);
            this.end = Integer.parseInt(end);
        }

        public String toString(){
            return String.format("start: %s, end: %s", this.start, this.end);
        }

    }
    @Data
    static class ElfPair{
        Range first;
        Range second;
        public ElfPair(Range first, Range second){
            this.first = first;
            this.second = second;
        }
        public boolean oneContainsOther(){
            boolean firstContainsSecond = first.start<=second.start && second.end<=first.end;
            boolean secondContainsFirst = second.start<=first.start && first.end<=second.end;
            System.out.printf("fCs: %s, sCf: %s; - %s%n", firstContainsSecond, secondContainsFirst, this);
            return firstContainsSecond || secondContainsFirst;
        }
        
        public boolean hasOverlap(){
            return
                    (first.start<=second.start && second.start<=first.end)   // second.start within first
                    || (first.start<=second.end && second.end<=first.end)    // second.end within first
                    ||(second.start<=first.start && first.start<=second.end) // first.start within second
                    || (second.start<=first.end && first.end<=second.end);   // first.end within second
        }

        public String toString(){
            return String.format("first: [%s], second: [%s]", first, second);
        }
    }

    List<ElfPair> elves;
    public Day4(Day.Type type){
        super(4, type);
        this.elves = this.strings.stream()
                .map(s-> s.split("[,-]"))
                .map(ranges-> new ElfPair(
                        new Range(ranges[0], ranges[1]),
                        new Range(ranges[2], ranges[3]))
                ).toList();
    }

    private Integer countContainingPairs(){
        return this.elves.stream()
                .filter(ElfPair::oneContainsOther)
                .toList().size();
    }

    public Integer part1(){
        return this.countContainingPairs();
    }

    private Integer countOverlappingPairs(){
        return this.elves.stream()
                .filter(ElfPair::hasOverlap)
                .toList().size();
    }

    public Integer part2(){
        return this.countOverlappingPairs();
    }
}
