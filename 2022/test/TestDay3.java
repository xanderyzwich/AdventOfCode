import org.junit.Test;

import java.util.HashMap;
import java.util.Map;

import static org.junit.Assert.assertEquals;

public class TestDay3 {

    @Test
    public void testGetPriority(){
        Map<String, Integer> anchors = new HashMap<>(){{
            put("A", 27);
            put("Z", 52);
            put("a", 1);
            put("z", 26);
        }};
        anchors.forEach((key, value) -> {
            assertEquals(value, Day3.getPriority(key));
        });
    }

    @Test
    public void part1Example(){
        Day3 day3 = new Day3(Day.Type.EXAMPLE);
        Integer expected = 157;
        Integer actual = day3.findOverlapPrioritySum();
        assertEquals(expected, actual);
    }

    @Test
    public void part1Data(){
        Day3 day3 = new Day3(Day.Type.DATA);
        Integer expected = 7727;
        Integer actual = day3.findOverlapPrioritySum();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Example(){
        Day3 day3 = new Day3(Day.Type.EXAMPLE);
        Integer expected = 70;
        Integer actual = day3.findSumOfTeamBadges();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Data(){
        Day3 day3 = new Day3(Day.Type.DATA);
        Integer expected = 2609;
        Integer actual = day3.findSumOfTeamBadges();
        assertEquals(expected, actual);
    }

}
