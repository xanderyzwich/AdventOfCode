import org.junit.Test;
import util.ArrayTools;

import java.util.Arrays;
import java.util.stream.IntStream;

import static org.junit.Assert.*;

public class TestDay8 {

    @Test
    public void part1Example(){
        Day8 day8 = new Day8(Day.Type.EXAMPLE);
        Integer expected = 21;
        Integer actual = day8.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void exampleTestVisible(){
        Day8 day8 = new Day8(Day.Type.EXAMPLE);
        assertTrue(day8.isVisible(1, 1));
        assertTrue(day8.isVisible(1, 2));
        assertFalse(day8.isVisible(1, 3));

        assertTrue(day8.isVisible(2, 1));
        assertFalse(day8.isVisible(2, 2));
        assertTrue(day8.isVisible(2, 3));

        assertFalse(day8.isVisible(3, 1));
        assertTrue(day8.isVisible(3, 2));
        assertFalse(day8.isVisible(3, 3));
    }

    @Test
    public void part1Data(){
        Day8 day8 = new Day8(Day.Type.DATA);
        Integer expected = 1676;
        Integer actual = day8.part1();
        assertEquals(expected, actual);
    }

    @Test
    public void part2Example(){
        Day8 day8 = new Day8(Day.Type.EXAMPLE);
        Integer expected = 8;
        Integer actual = day8.part2();
        assertEquals(expected, actual);
    }

    @Test
    public void exampleTestScenicScore(){
        Day8 day8 = new Day8(Day.Type.EXAMPLE);
        assertEquals(8, day8.getScenicScore(3, 2));
    }

    @Test
    public void part2Data(){
        Day8 day8 = new Day8(Day.Type.DATA);
        Integer expected = 313200;
        Integer actual = day8.part2();
        assertEquals(expected, actual);
    }

    @Test
    public void sliceTest(){
        Day8 day8 = new Day8(Day.Type.EXAMPLE);
        ArrayTools.Direction[] directions = {
                ArrayTools.Direction.UP,
                ArrayTools.Direction.DOWN,
                ArrayTools.Direction.LEFT,
                ArrayTools.Direction.RIGHT
        };
        for (ArrayTools.Direction d : directions){
            System.out.printf("%s: ", d);
            int[] result = ArrayTools.sliceDirection(day8.treeHeights, 0, 1, d);
            for(int i : result){
                System.out.printf("%s, ", i);
            }
            System.out.printf("%n");

        }
    }
}
