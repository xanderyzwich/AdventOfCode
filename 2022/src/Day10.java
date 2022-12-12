import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Day10 extends Day{

    List<Integer> signalStrengths;

    public Day10(Type type){
        super(10, type);

    }

    static class Computer{
        // Members
        int registerX; // main register
        int registerY; // number to be added
        int currentClockCycle;
        int nextOpCycle; // when to fetch next instruction
        int nextInstruction; // next instruction to fetch
        List<Integer> signalStrengths; // list of recorded signal strengths
        List<String> instructions;
        String[][] crt;

        // Constructors
        public Computer(List<String> instructions){
            this.instructions = instructions;
            this.registerX = 1;
            this.currentClockCycle = 1;
            this.nextOpCycle = 1;
            this.nextInstruction = 0;
            this.registerY = 0;
            this.signalStrengths = new LinkedList<>();
            crt = new String[6][40];
        }

        // Accessors
        public static boolean shouldRecordSignalStrength(int cycle){
            return 0 == (cycle-20)%40;
        }

        private String[] fetchNextInstruction() {
            String[] parts = this.instructions.get(this.nextInstruction).split(" ");
            this.nextInstruction++;
            return parts;
        }

        public Integer sumSignalStrengths() {
            return this.signalStrengths.stream().reduce(0, Integer::sum);
        }

        public void showCRT(){
            for(int i = 0; i<6; i++){
                for(int j = 0; j<40; j++){
                    System.out.printf("%s", this.crt[i][j]);
                }
                System.out.printf("%n");
            }
        }

        // Mutators
        public void recordSignalStrength(){
            if (shouldRecordSignalStrength(this.currentClockCycle)) {
                int signalStrength = this.currentClockCycle * this.registerX;
//                System.out.printf("Recording Signal Strength:: Cycle: %4s, Register: %4s, Signal Strength: %10s%n", this.currentClockCycle, this.registerX, signalStrength);
                this.signalStrengths.add(signalStrength);
            }
        }

        public void updateCRT(){
            int pixel = (this.currentClockCycle-1)% 240; // adjust for zero index
            int row = pixel / 40;
            int col = pixel % 40;
            boolean isLit = registerX==col-1 || registerX==col || registerX==col+1;
//            System.out.printf("Updating CRT cycle %5s, pixel%3s, row %2s, col %3s, isLit %s%n", this.currentClockCycle, pixel, row, col, isLit);
            this.crt[row][col] = isLit ? "#" : ".";
        }

        public void execute(){
            for(; this.nextInstruction<this.instructions.size(); this.currentClockCycle++){
                this.recordSignalStrength();
                this.updateCRT();
                this.tick();
            }
        }

        private void tick() {
            if (this.currentClockCycle==this.nextOpCycle){
                // get op and increment index
                this.executeInstruction(this.fetchNextInstruction());

            }  else { // finish addx execution on next cycle
                completeAdd();
            }
        }

        private void completeAdd() {
            this.registerX = this.registerX + this.registerY;
            this.registerY = 0;
        }

        private void executeInstruction(String[] parts) {
            if(parts[0].equals("addx")) {
                this.registerY = Integer.parseInt(parts[1]);
                this.nextOpCycle++; // skip cycle for addx completion
            }
            this.nextOpCycle++; // always increment
        }

    }



    public Integer part1(){
        Computer computer = new Computer(this.strings);
        computer.execute();
        return computer.sumSignalStrengths();
    }


    public void part2(){
        Computer computer = new Computer(this.strings);
        computer.execute();
        computer.showCRT();
    }
}
