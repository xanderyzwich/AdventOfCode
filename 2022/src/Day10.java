import java.util.LinkedList;
import java.util.List;

public class Day10 extends Day{

    List<Integer> signalStrengths;

    public Day10(Type type){
        super(10, type);
        this.signalStrengths = new LinkedList<>();
    }

    public boolean shouldRecordSignalStrength(int cycle){
        return 0 == (cycle-20)%40;
    }

    public Integer part1(){
        int register = 1; // start value
        int nextOpCycle = 1; // when to get next command
        int op = 0; // next comand to execute
        int toAdd = 0; // value to add on next cycle after addx
        for(int clockCycle = 1; op<this.strings.size(); clockCycle++){
            if (this.shouldRecordSignalStrength(clockCycle)) {
                int signalStrength = clockCycle * register;
                System.out.printf("Recording Signal Strength:: Cycle: %4s, Register: %4s, Signal Strength: %10s%n", clockCycle, register, signalStrength);
                this.signalStrengths.add(signalStrength);
            }

            if (clockCycle==nextOpCycle){
                // get op and increment index
                String[] parts = this.strings.get(op).split(" ");
                op++;

                if(parts[0].equals("addx")) {
                    toAdd = Integer.parseInt(parts[1]);
                    nextOpCycle++; // skip cycle for addx completion
                }
                nextOpCycle++; // always increment

            }  else { // finish addx execution on next cycle
                register += toAdd;
                toAdd = 0;
            }


        }
        return signalStrengths.stream().reduce(0, Integer::sum);
    }


    public Integer part2(){
        return 0;
    }
}
