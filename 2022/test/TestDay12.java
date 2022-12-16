import org.junit.Test;
import util.Tuple;

import java.util.List;

import static org.junit.Assert.assertEquals;

public class TestDay12 {

//    @Test
//    public void dumbTest(){
//        Day12 day12 = new Day12(Day.Type.EXAMPLE);
//        List<Tuple<Integer>> neighbors = Day12.getNeighborLocationStream(new Tuple<>(0, 0))
//                .filter(day12::onMap)
//                .peek(System.out::println)
//                .toList();
//    }

    @Test
    public void part1Example(){
        Day12 day12 = new Day12(Day.Type.EXAMPLE);
        Integer expected = 31;
        Integer actual = day12.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part1Data(){
        Day12 day12 = new Day12(Day.Type.DATA);
        Integer expected = 0;
        Integer actual = day12.part1();
        System.out.println(actual);
        assertEquals(expected, actual);
    }

    @Test
    public void part2Example(){
        Day12 day12 = new Day12(Day.Type.EXAMPLE);
        Integer expected = 0;
        Integer actual = day12.part2();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Data(){
        Day12 day12 = new Day12(Day.Type.DATA);
        Integer expected = 0;
        Integer actual = day12.part2();
        assertEquals(expected, actual);
    }
}
