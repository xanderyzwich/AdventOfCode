import java.util.*;
import java.util.stream.Collectors;

public class Day5 extends Day{

    Map<String, Stack<String>> containerSpace;
    Integer stackRowLocation;

    public Day5(Type type){
        super(5, type);
        containerSpace = new HashMap<>();

        // find the stack id row
        this.stackRowLocation = -1;
        String stackRow = "";
        for(int i=0; i<this.strings.size(); i++){
            String currentRow = this.strings.get(i);
            if(!currentRow.contains("[")) { // id's are on the first line without []'s
                stackRowLocation = i;
                stackRow = currentRow;
                break;
            }
        }

        Integer stackPosition = 0;
        String stackId;
        // create stacks
        while(stackPosition<stackRow.length()){
            Stack<String> containerStack = new Stack<>();

            // shift to the next stack id
            while(String.valueOf(stackRow.charAt(stackPosition)).matches("\\W"))
                stackPosition++;

            // construct that stack
            for(int i=stackRowLocation-1; i>=0; i--){
                String currentLine = this.strings.get(i);
                if (stackPosition>=currentLine.length()) // stack empty in this line
                    break;

                String item = String.valueOf(currentLine.charAt(stackPosition));
                if(item.matches("\\W")) // stack empty in this line
                    break;
                containerStack.push(item);
            }

            containerSpace.put(String.valueOf(stackRow.charAt(stackPosition)), containerStack);
            stackPosition++; // move on from that position
        }
    }

    public String part1(){

        for(int i = this.stackRowLocation+2; i<this.strings.size(); i++){
            String currentLine = this.strings.get(i);
            List<String> instructions = List.of(currentLine.split("[^0-9]+"));

            Integer count = Integer.parseInt(instructions.get(1));
            Stack<String> origin = containerSpace.get(instructions.get(2));
            Stack<String> destination = containerSpace.get(instructions.get(3));

            for(int j=0; j<count; j++)
                destination.push(origin.pop());

        }
        return getStackTops();
    }

    private String getStackTops() {
        return this.containerSpace.keySet()
                .stream().sorted()
                .map(containerSpace::get)
                .map(Stack::peek)
                .collect(Collectors.joining(""));
    }

    public String part2(){
        for(int i = this.stackRowLocation+2; i<this.strings.size(); i++){
            String currentLine = this.strings.get(i);
            List<String> instructions = List.of(currentLine.split("[^0-9]+"));

            Integer count = Integer.parseInt(instructions.get(1));
            Stack<String> origin = containerSpace.get(instructions.get(2));
            Stack<String> destination = containerSpace.get(instructions.get(3));

            Stack<String> temp = new Stack<>();
            for(int j=0; j<count; j++)
                temp.push(origin.pop());

            while(!temp.isEmpty())
                destination.push(temp.pop());
        }

        return getStackTops();
    }
}
