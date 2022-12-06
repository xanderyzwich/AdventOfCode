import java.util.*;
import java.util.stream.Stream;

public class Day6 extends Day{

    public Day6(Type type){
        super(6, type);
    }

    public Day6(String input){
        super(6, Type.EXAMPLE);
        this.strings = Collections.singletonList(input);
    }

    public Integer part1(){
        return findDistinctRun(4);
    }

    private int findDistinctRun(Integer size) {
        List<String> stream = Arrays.stream(this.strings.get(0).split("")).toList();
        Set<String> dedup;
        for(int i=size; i< stream.size(); i++){
            dedup = new HashSet<>(stream.subList(i-size, i));
            if(dedup.size()==size)
                return i;
        }
        return -1;
    }

    public Integer part2(){
        return findDistinctRun(14);
    }
}
