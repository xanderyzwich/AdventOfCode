import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class TestDayX {

    @Test
    public void part1Example(){
        DayX dayX = new DayX(Day.Type.EXAMPLE);
        Integer expected = 0;
        Integer actual = dayX.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part1Data(){
        DayX dayX = new DayX(Day.Type.DATA);
        Integer expected = 0;
        Integer actual = dayX.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Example(){
        DayX dayX = new DayX(Day.Type.EXAMPLE);
        Integer expected = 0;
        Integer actual = dayX.part2();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Data(){
        DayX dayX = new DayX(Day.Type.DATA);
        Integer expected = 0;
        Integer actual = dayX.part2();
        assertEquals(expected, actual);
    }
}
