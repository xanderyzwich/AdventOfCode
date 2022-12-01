import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class TestDay1 {

    @Test
    public void part1Example(){
        Day1 day1 = new Day1(Day.Type.EXAMPLE);
        Integer expected = 24000;
        Integer actual = day1.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part1Data(){
        Day1 day1 = new Day1(Day.Type.DATA);
        Integer expected = 66306;
        Integer actual = day1.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Example(){
        Day1 day1 = new Day1(Day.Type.EXAMPLE);
        Integer expected = 45000;
        Integer actual = day1.part2();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Data(){
        Day1 day1 = new Day1(Day.Type.DATA);
        Integer expected = 195292;
        Integer actual = day1.part2();
        assertEquals(expected, actual);
    }

}
