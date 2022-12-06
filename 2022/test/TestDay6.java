import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class TestDay6 {
    @Test
    public void part1Example(){
        Day6 day6 = new Day6("mjqjpqmgbljsphdztnvjfqwrcgsmlb");
        assertEquals((Integer)7, day6.part1());
        day6 = new Day6("bvwbjplbgvbhsrlpgdmjqwftvncz");
        assertEquals((Integer)5, day6.part1());
        day6 = new Day6("nppdvjthqldpwncqszvftbrmjlhg");
        assertEquals((Integer)6, day6.part1());
        day6 = new Day6("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg");
        assertEquals((Integer)10, day6.part1());
        day6 = new Day6("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw");
        assertEquals((Integer)11, day6.part1());

    }

    @Test
    public void part1Data(){
        Day6 day6 = new Day6(Day.Type.DATA);
        Integer expected = 1766;
        Integer actual = day6.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Example(){
        Day6 day6 = new Day6("mjqjpqmgbljsphdztnvjfqwrcgsmlb");
        assertEquals((Integer)19, day6.part2());
        day6 = new Day6("bvwbjplbgvbhsrlpgdmjqwftvncz");
        assertEquals((Integer)23, day6.part2());
        day6 = new Day6("nppdvjthqldpwncqszvftbrmjlhg");
        assertEquals((Integer)23, day6.part2());
        day6 = new Day6("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg");
        assertEquals((Integer)29, day6.part2());
        day6 = new Day6("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw");
        assertEquals((Integer)26, day6.part2());
    }

    @Test
    public void part2Data(){
        Day6 day6 = new Day6(Day.Type.DATA);
        Integer expected = 2383;
        Integer actual = day6.part2();
        assertEquals(expected, actual);
    }
}
