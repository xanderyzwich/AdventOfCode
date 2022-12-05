import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class TestDay5 {

    @Test
    public void dumbTest(){
        String first = "    [D]";
        System.out.println(first.contains("["));
    }


    @Test
    public void part1Example(){
        Day5 day5 = new Day5(Day.Type.EXAMPLE);
        String expected = "CMZ";
        String actual = day5.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part1Data(){
        Day5 day5 = new Day5(Day.Type.DATA);
        String expected = "FRDSQRRCD";
        String actual = day5.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Example(){
        Day5 day5 = new Day5(Day.Type.EXAMPLE);
        String expected = "MCD";
        String actual = day5.part2();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Data(){
        Day5 day5 = new Day5(Day.Type.DATA);
        String expected = "HRFTQVWNN";
        String actual = day5.part2();
        assertEquals(expected, actual);
    }
}
