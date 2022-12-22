import org.junit.Test;

import static org.junit.Assert.*;

public class TestDay15 {

    @Test
    public void part1Example(){
        Day15 day15 = new Day15(Day.Type.EXAMPLE);
        Integer expected = 26;
        Integer actual = day15.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part1Data(){
        Day15 day15 = new Day15(Day.Type.DATA);
        Integer expected = 5525990;
        Integer actual = day15.part1();
        assertTrue(actual < 5892814); // first guess
        assertEquals(expected, actual);
    }

    @Test
    public void part2Example(){
        Day15 day15 = new Day15(Day.Type.EXAMPLE);
        Integer expected = 56000011;
        Integer actual = day15.part2();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Data(){
        Day15 day15 = new Day15(Day.Type.DATA);
        Integer expected = 0;
        Integer actual = day15.part2();
        assertTrue(actual > 849139071);
        assertTrue(actual > 853139071); // that + 4M // assuming off by one on col
        assertTrue(actual > 853139072); // that + 1 // assuming also off by one on row
        assertEquals(expected, actual);
    }
}
