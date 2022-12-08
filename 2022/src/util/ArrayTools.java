package util;

import java.util.stream.IntStream;
import java.util.stream.Stream;

public class ArrayTools {

    // Tooling to allow slicing a 1d array in a given direction from a 2d array
    public enum Direction {
        UP, DOWN, LEFT, RIGHT
    };

    public static int[] sliceDirection(int[][] source, int row, int col, Direction direction){
        return switch (direction){
            case UP -> getIndexesReversed(row, 0)
                    .map(i -> source[i][col]).toArray();
            case DOWN -> getIndexes(row+1, source.length)
                    .map(i -> source[i][col]).toArray();
            case LEFT -> getIndexesReversed(col, 0)
                    .map(i -> source[row][i]).toArray();
            case RIGHT -> getIndexes(col+1, source[row].length)
                    .map(i -> source[row][i]).toArray();
        };
    }

    public static int[][] sliceAllDirections(int[][] source, int row, int col){
        return new int[][]{
                sliceDirection(source, row, col, Direction.UP),
                sliceDirection(source, row, col, Direction.DOWN),
                sliceDirection(source, row, col, Direction.LEFT),
                sliceDirection(source, row, col, Direction.RIGHT),
        };
    }

    /**
     * Get stream of numbers from start to end-1
     * if start=0 and end=3 return will be (0, 1, 2)
     * @param start inclusive
     * @param end exclusive
     * @return
     */
    public static IntStream getIndexes(int start, int end){
        return IntStream.range(start, end);
    }

    /**
     * Get descending stream of numbers from end to start
     * if start=3 and end=0 then return will be (2, 1, 0)
     * @param end inclusive
     * @param start exclusive
     * @return
     */
    public static IntStream getIndexesReversed(int end, int start) {
        return getIndexes(start, end)
                .map(i-> start + (end - 1 - i));
    }
}
