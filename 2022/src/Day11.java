import java.math.BigInteger;
import java.util.*;
import java.util.function.Consumer;
import java.util.function.DoubleFunction;
import java.util.function.IntFunction;

public class Day11 extends Day{
    static class Monkey{
        Queue<Double> worryLevels;
        String[] operation;
        Integer testDivisor;
        Integer ifTrueThrow;
        Integer ifFalseThrow;
        Double inspectionCount;

        public Monkey(LinkedList<Double> worryLevels, String operation,
                      Integer test,  Integer ifTrue, Integer ifFalse){
            this.worryLevels =  worryLevels;
            this.operation = operation.split(" ");
            this.testDivisor = test;
            this.ifTrueThrow = ifTrue;
            this.ifFalseThrow = ifFalse;
            this.inspectionCount = 0d;
        }


        public boolean hasItem(){
            return !this.worryLevels.isEmpty();
        }
        public Double getItem(){
            this.inspectionCount ++;
            return this.worryLevels.poll();
        }
        public Double getInspectionCount(){
            return this.inspectionCount;
        }
        public Double operate(Double oldValue){
            Double left = operation[0].equals("old") ? oldValue : Integer.parseInt(operation[0]);
            Double right = operation[2].equals("old") ? oldValue : Integer.parseInt(operation[2]);
//            System.out.printf("Operating on %30s %s %30s%n", left, operation[1], right);
            return switch (operation[1]){
                case "*"-> left * right;
                case "+"-> left +right;
                default -> null;
            };
        }
        public boolean test(Double worryLevel){
            return worryLevel % this.testDivisor == 0;
        }
        public Integer throwTo(boolean operationTrue){
            return operationTrue ? ifTrueThrow : ifFalseThrow;
        }
        public Integer throwItem(Double worryLevel){
            return this.throwTo(this.test(worryLevel));
        }
        public void catchItem(Double worryLevel) {
            this.worryLevels.add(worryLevel);
        }

        public String toString(){
            return String.format("Monkey: %s, %s, %s, %s, %s%n", worryLevels, Arrays.toString(operation), testDivisor, ifTrueThrow, ifFalseThrow);
        }

    }
    HashMap<Integer, Monkey> monkeys;

    public Day11(Type type){
        super(11, type);
        this.monkeys = new HashMap<>();
        for(int i=0; i<this.strings.size(); i+=7){
            readInMonkey(i);
        }
//        this.monkeys.values().forEach(System.out::println);
    }

    private void readInMonkey(int startingLine){
        Integer id = Integer.parseInt(this.strings.get(startingLine).split("\\W")[1]);
        LinkedList<Double> itemLevels = new LinkedList<>(Arrays.stream(
                        this.strings.get(startingLine + 1)
                                .split(": ")[1]
                                .split(", "))
                .map(Double::parseDouble).toList());
        String operation = this.strings.get(startingLine+2).split(" = ")[1];
        Integer test = Integer.parseInt(this.strings.get(startingLine+3).split(" divisible by ")[1]);
        Integer monkeyIfTrue = Integer.parseInt(this.strings.get(startingLine+4).split("monkey ")[1]);
        Integer monkeyIfFalse = Integer.parseInt(this.strings.get(startingLine+5).split("monkey ")[1]);
        monkeys.put(id, new Monkey(itemLevels, operation, test, monkeyIfTrue, monkeyIfFalse));
    }

    public Double part1(){
        return doRounds(20, (worry)-> worry/3);

    }

    private Double doRounds(int rounds, DoubleFunction<Double> worryReductionFunction) {
        for(int i = 0; i< rounds; i++) {
            round(worryReductionFunction);
//            if(0==i%20){
//                System.out.printf("Current round: %s%n", i);
//            }
        }


        return getProductOfHighestTwoInspections();
    }

    private Double getProductOfHighestTwoInspections() {
        return this.monkeys.values().stream()
                .map(Monkey::getInspectionCount)
                .sorted(Comparator.reverseOrder()).toList().subList(0, 2).stream()
//                .peek(System.out::println)
                .reduce(1d, (a, b)->a*b);
    }

    private void round(DoubleFunction<Double> worryReductionFunction) {
        for(Monkey m: this.monkeys.values()){
            while(m.hasItem()){
                Double worryLevel = m.getItem();
                worryLevel = m.operate(worryLevel); // inspect
                if(worryLevel==null) {
                    System.out.println("Something is wrong");
                    return;
                }
                worryLevel = worryReductionFunction.apply(worryLevel); // relief
//                System.out.println(worryLevel);
                this.monkeys.get(m.throwItem(worryLevel)).catchItem(worryLevel);
            }
        }
    }

    public Double part2(){
        // not working
        int worryReduction = monkeys.values().stream()
                .map(monkey->monkey.testDivisor)
                .reduce(1, (a,b)->a*b);

        return doRounds(10000, (a)-> a%worryReduction);
    }
}
