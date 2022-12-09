import lombok.AllArgsConstructor;
import lombok.Data;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

import static java.lang.Math.abs;

public class Day9 extends Day{
    // Members
    private final Coordinate head;
    private Coordinate tail;
    private final Set<Coordinate> tailVisited;
    @Data
    @AllArgsConstructor
    static class Coordinate{
        // Members
        private int row;
        private int col;

        // Constructor
        public Coordinate(Coordinate other){
            this.row = other.getRow();
            this.col = other.getCol();
        }

        // Accessors
        public boolean isAdjacent(Coordinate other){
            return abs(this.getCol()-other.getCol())<=1 && abs(this.getRow()-other.getRow())<=1;
        }
        public int distanceTo(Coordinate other){
            int up = abs(this.col - other.getCol());
            int right = abs(this.row - other.getRow());
            int total = up + right;
            return (up!=0 && right!=0) ? total-1 : total;
        }
        @Override
        public boolean equals(Object obj) {
            if (this == obj)
                return true;
            if (obj == null)
                return false;
            if (getClass() != obj.getClass())
                return false;
            Coordinate other = (Coordinate) obj;
            if (col != other.col)
                return false;
            return row == other.row;
        }
        @Override
        public int hashCode(){
            final int offset = 10000;
            return (offset*this.getCol()) + this.getCol();
        }
        public String toString(){
            return String.format("r: %s, c: %s", this.row, this.col);
        }

        // Mutators
        public void up(){
            this.row++;
        }
        public void down(){
            this.row--;
        }
        public void left(){
            this.col--;
        }
        public void right(){
            this.col++;
        }

        /**
         * Move in two d space by given distances
         * @param up distance to move (negative if down)
         * @param right distance to move (negative if left)
         */
        public void move(int up, int right){
            this.row += up;
            this.col += right;
        }

    }

    public Day9(Type type){
        super(9, type);
        this.head = new Coordinate(0, 0);
        this.tail = new Coordinate(0, 0);
        tailVisited = new HashSet<>(){{
            add(tail);
        }};
    }

    private void execute(String movement){
//        System.out.printf("Executing: %s%n", movement);
        String[] parts = movement.split(" ");
        String direction = parts[0];
        int distance = Integer.parseInt(parts[1]);
        for(int i=0; i<distance; i++){
            Coordinate headLast = new Coordinate(this.head);
//            System.out.println("preparing to move");
            switch (direction) {
                case "U" -> this.head.up();
                case "D" -> this.head.down();
                case "L" -> this.head.left();
                case "R" -> this.head.right();
            }
//            System.out.println("moved head");
            if (!this.head.isAdjacent(tail)){
//                System.out.println("moving tail");
                this.tail = new Coordinate(headLast);
                this.tailVisited.add(tail);
            }
//            System.out.printf("HeadBefore{%s}->HeadAfter{%s} - Tail:{%s} %n", headLast, this.head, this.tail);
        }
    }

    public Integer part1(){
        for(String command : this.strings){
            this.execute(command);
        }
        return this.tailVisited.size();
    }

    public Integer part2(){
        return 0;
    }
}
