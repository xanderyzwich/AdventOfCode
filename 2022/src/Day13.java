import org.json.JSONArray;
import util.Tuple;
import org.json.JSONObject;

import java.util.LinkedList;
import java.util.List;

public class Day13 extends Day{
    static class Pair extends Tuple<JSONArray, JSONArray>{
        public Pair(String first, String second) {
            super(parse(first), parse(second));
        }
    }
    List<Pair> pairList;
    public Day13(Type type){
        super(13, type);
        this.pairList = new LinkedList<>();
        for(int i=0; i<this.strings.size(); i+=3){
            this.pairList.add(new Pair(this.strings.get(i), this.strings.get(i+1)));
        }
    }

    public Integer part1(){
        List<Integer> correctIndexes = new LinkedList<>();
        for(int i=0; i<this.pairList.size(); i++){
            Pair pair = pairList.get(i);
            boolean correctlyOrdered = isCorrectlyOrdered(pair.getFirst(), pair.getSecond());
            System.out.printf("-------iterating part 1: %s, %s = %s%n", pair.getFirst(), pair.getSecond(), correctlyOrdered);
            if (correctlyOrdered){
                correctIndexes.add(i+1); // 1 based indexing for solution
            }
        }
        System.out.println(correctIndexes);
        return correctIndexes.stream().reduce(0, Integer::sum);
    }
    public static JSONArray parse(String s){
        JSONArray result = new JSONArray(s);
        for(int i=0; i< result.length(); i++){
            String piece = result.get(i).toString();
            if(piece.contains("["))
                result.put(i, parse(piece));
        }
        return result;
    }
    public static JSONArray wrap(Integer i){
        return new JSONArray(){{
            put(i);
        }};
    }
    public static boolean isCorrectlyOrdered(JSONArray left, JSONArray right){
        return 0>= compare(left, right);
    }
    public static boolean isCorrectlyOrdered(Integer left, JSONArray right){
        return 0>=compare(wrap(left), right);
    }
    public static boolean isCorrectlyOrdered(JSONArray left, Integer right){
        return 0>=compare(left, wrap(right));
    }
    public static boolean isCorrectlyOrdered(Integer left, Integer right){
        System.out.printf("Is Correctly ordered %s and %s is %s%n", left, right, left<=right);
        return left <= right;
    }

    public static int compare(JSONArray left, JSONArray right){
        System.out.printf("Comparing %s and %s%n", left, right);
        for(int i=0; i<left.length(); i++){
            // if right list runs out of items first then it is  not in right order
            if(i==right.length())
                return 1;

            // get objects
            Object leftCheck = left.get(i);
            Object rightCheck = right.get(i);
            // figure out if they are integers
            boolean leftInt = leftCheck.getClass().equals(Integer.class);
            boolean rightInt = rightCheck.getClass().equals(Integer.class);
            System.out.printf("%s is int: %s, %s is int %s%n", leftCheck, leftInt, rightCheck, rightInt);

            // first rule
            if(leftInt && rightInt) {
                Integer integerLeft = (Integer) leftCheck;
                Integer integerRight = (Integer) rightCheck;
                switch(integerLeft.compareTo(integerRight)){
                    case -1: return -1;  // left integer lower than right then in right order
                    case 1: return 1;  // left higher than right isn't in right order
                    case 0: continue; // same value then continue checking
                }
            }

            // third rule
            // only one is integer, then compare with it as a singleton list
            JSONArray lefty = leftInt ? wrap((Integer) leftCheck) : (JSONArray)leftCheck;
            JSONArray righty = rightInt ? wrap((Integer) rightCheck) : (JSONArray)rightCheck;

            // second rule
            switch(compare(lefty, righty)){
                case -1: return -1;
                case 1: return 1;
            }

            // if left list runs out of items first then it is in the right order
            if(i+1==left.length() && i+1<right.length())
                return -1;
        }
        return 0;
    }

    public Integer part2(){
        return 0;
    }
}
