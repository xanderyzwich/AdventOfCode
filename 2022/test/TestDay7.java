import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class TestDay7 {
    @Test
    public void part1Example(){
        Day7 day7 = new Day7(Day.Type.EXAMPLE);
        assertEquals((Integer)95437, day7.part1());
    }

    @Test
    public void part1Data(){
        Day7 day7 = new Day7(Day.Type.DATA);
        Integer expected = 1491614;
        Integer actual = day7.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Example(){
        Day7 day7 = new Day7(Day.Type.EXAMPLE);
        assertEquals((Integer)19, day7.part2());
    }

    @Test
    public void part2Data(){
        Day7 day7 = new Day7(Day.Type.DATA);
        Integer expected = 2383;
        Integer actual = day7.part2();
        assertEquals(expected, actual);
    }
}
