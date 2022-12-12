import org.junit.Test;

import static org.junit.Assert.*;

public class TestDay10 {

    @Test
    public void testShouldRecord(){
        int[] yes = {20, 60, 100, 140, 180};
        int[] no ={1, 3, 5, 40, 50, 144};
        for(int i: yes){
            assertTrue(Day10.Computer.shouldRecordSignalStrength(i));
        }
        for(int i: no){
            assertFalse(Day10.Computer.shouldRecordSignalStrength(i));
        }
    }

    @Test
    public void part1Example(){
        Day10 day10 = new Day10(Day.Type.EXAMPLE);
        Integer expected = 13140;
        Integer actual = day10.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part1Data(){
        Day10 day10 = new Day10(Day.Type.DATA);
        Integer expected = 12880;
        Integer actual = day10.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Example(){
        Day10 day10 = new Day10(Day.Type.EXAMPLE);
        day10.part2();
    }

    @Test
    public void part2Data(){
        Day10 day10 = new Day10(Day.Type.DATA);
        day10.part2();
    }
}
