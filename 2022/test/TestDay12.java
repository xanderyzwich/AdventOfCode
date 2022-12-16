import org.junit.Test;
import util.Tuple;

import java.util.Arrays;
import java.util.List;

import static org.junit.Assert.assertEquals;

public class TestDay12 {

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
        Integer expected = 447;
        Integer actual = day12.part1();
        System.out.println(actual);
        assertEquals(expected, actual);
    }

    @Test
    public void part2Example(){
        Day12 day12 = new Day12(Day.Type.EXAMPLE);
        System.out.println(Arrays.deepToString(day12.altitudes));
        System.out.println(day12.lowestPoints);
        Integer expected = 29;
        Integer actual = day12.part2();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Data(){
        Day12 day12 = new Day12(Day.Type.DATA);
        Integer expected = 446;
        Integer actual = day12.part2();
        assertEquals(expected, actual);
    }
}
