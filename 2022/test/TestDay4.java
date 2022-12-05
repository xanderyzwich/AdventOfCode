import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertEquals;

public class TestDay4 {

    @Test
    public void part1Example(){
        Day4 day4 = new Day4(Day.Type.EXAMPLE);
        Integer expected = 2;
        Integer actual = day4.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part1Data(){
        Day4 day4 = new Day4(Day.Type.DATA);
        Integer expected = 466;
        Integer actual = day4.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Example(){
        Day4 day4 = new Day4(Day.Type.EXAMPLE);
        Integer expected = 4;
        Integer actual = day4.part2();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Data(){
        Day4 day4 = new Day4(Day.Type.DATA);
        Integer expected = 865;
        Integer actual = day4.part2();
        assertEquals(expected, actual);
    }
}