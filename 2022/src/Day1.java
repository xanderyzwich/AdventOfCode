import util.StringTools;

import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class Day1 extends Day {
    List<Integer> calorieCounts;

    public Day1(Type type){
        super(1, type);
        this.calorieCounts = new LinkedList<>();

        Integer calories =  0;
        for(String line: this.strings){
            if (StringTools.isEmpty(line)){
                calorieCounts.add(calories);
                calories = 0;
            } else {
                calories += Integer.parseInt(line);
            }
        }
        if(calories != 0){
            calorieCounts.add(calories);
        }
        this.calorieCounts.sort(Collections.reverseOrder());
    }

    Integer part1() {
        return this.calorieCounts.get(0);
//        return Collections.max(this.calorieCounts);
    }

    Integer part2() {
        return this.calorieCounts.subList(0, 3)
                .stream().reduce(0, Integer::sum);
    }
}
