import org.junit.Test;

import java.util.HashSet;
import java.util.Set;

import static org.junit.Assert.*;

public class TestDay9 {

    @Test
    public void part1Example(){
        Day9 day9 = new Day9(Day.Type.EXAMPLE);
        Integer expected = 13;
        Integer actual = day9.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part1Data(){
        Day9 day9 = new Day9(Day.Type.DATA);
        Integer expected = 5930;
        Integer actual = day9.part1();
        // first result
        assertNotEquals(actual, (Integer) 8802);
        assertTrue(actual < 8802);
        // second result
        assertNotEquals(actual, (Integer) 5929);
        assertTrue(actual > 5929);
        // final
        assertEquals(expected, actual);
    }

    @Test
    public void part2Example(){
        Day9 day9 = new Day9(Day.Type.EXAMPLE);
        Integer expected = 0;
        Integer actual = day9.part2();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Data(){
        Day9 day9 = new Day9(Day.Type.DATA);
        Integer expected = 0;
        Integer actual = day9.part2();
        assertEquals(expected, actual);
    }

    @Test
    public void testDumbStuff(){
        System.out.println(Integer.compare(0, 0)); // equal
        System.out.println(Integer.compare(0, 2)); // first smaller
        System.out.println(Integer.compare(2, 0)); // first larger
    }
}
