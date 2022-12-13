import org.junit.Test;


import java.math.BigInteger;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

import static org.junit.Assert.assertEquals;

public class TestDay11 {

    @Test
    public void dumbTest(){
        List<String> firstMonkey = new LinkedList<>(){{
            add("Monkey 0:");
            add("  Starting items: 79, 98");
            add("  Operation: new = old * 19");
            add("  Test: divisible by 23");
            add("    If true: throw to monkey 2");
            add("    If false: throw to monkey 3");
        }};
        System.out.println(Arrays.toString(firstMonkey.get(0).split("\\W")));

    }

    @Test
    public void part1Example(){
        Day11 day11 = new Day11(Day.Type.EXAMPLE);
        Double expected = 10605d;
        Double actual = day11.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part1Data(){
        Day11 day11 = new Day11(Day.Type.DATA);
        Double expected = 62491d;
        Double actual = day11.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Example(){
        Day11 day11 = new Day11(Day.Type.EXAMPLE);
        Double expected = 2713310158d;
        Double actual = day11.part2();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Data(){
        Day11 day11 = new Day11(Day.Type.DATA);
        Double expected = 17408399184d;
        Double actual = day11.part2();
        assertEquals(expected, actual);
    }
}
