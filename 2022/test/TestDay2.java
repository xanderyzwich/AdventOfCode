import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotEquals;

public class TestDay2 {
    @Test
    public void part1Example(){
        Day2 day2 = new Day2(Day.Type.EXAMPLE, 1);
        Integer expected = 15;
        Integer actual = day2.takeScore();
        assertEquals(expected, actual);
    }

    @Test
    public void part1Data(){
        Day2 day2 = new Day2(Day.Type.DATA, 1);
        Integer expected = 9241;
        Integer actual = day2.takeScore();
        assertNotEquals(actual, (Integer)16114);
        assertEquals(expected, actual);
    }

    @Test
    public void part2Example(){
        Day2 day2 = new Day2(Day.Type.EXAMPLE, 2);
        Integer expected = 12;
        Integer actual = day2.takeScore();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Data(){
        Day2 day2 = new Day2(Day.Type.DATA, 2);
        Integer expected = 14610;
        Integer actual = day2.takeScore();
        assertEquals(expected, actual);
    }
}
