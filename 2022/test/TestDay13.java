import org.json.JSONArray;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class TestDay13 {

    @Test
    public void dumb(){
        System.out.println(Integer.compare(0, 1));
        System.out.println(Integer.compare(1, 1));
        System.out.println(Integer.compare(1, 0));

    }

    @Test
    public void part1Example(){
        Day13 day13 = new Day13(Day.Type.EXAMPLE);
        Integer expected = 13;
        Integer actual = day13.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part1Data(){
        Day13 day13 = new Day13(Day.Type.DATA);
        Integer expected = 0;
        Integer actual = day13.part1();
        assertTrue(4118<actual);
        assertTrue(4571<actual);
        assertEquals(expected, actual);
    }

    @Test
    public void part2Example(){
        Day13 day13 = new Day13(Day.Type.EXAMPLE);
        Integer expected = 0;
        Integer actual = day13.part2();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Data(){
        Day13 day13 = new Day13(Day.Type.DATA);
        Integer expected = 0;
        Integer actual = day13.part2();
        assertEquals(expected, actual);
    }
}
