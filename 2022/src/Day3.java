import util.StringTools;

import java.util.List;

public class Day3 extends Day{

    public Day3(Type type){
        super(3, type);
    }

    /**
     * Part 1 result function
     * @return sum of priorities of each elves overlapping item
     */
    public Integer findOverlapPrioritySum(){
        return this.strings.stream()
                .map(Day3::findOverlapBetweenCompartments)
                .map(Day3::getPriority)
                .reduce(0, Integer::sum);
    }

    public static Integer getPriority(String item){
        Integer beforeUpper = 64; // 65 is 'A
        Integer beforeLower = 96; // 97 is 'a'
        Integer upperOffset = 26; // offset A to 27

        Integer object = StringTools.getAscii(item);
        if (object>64 && object<91) { // is uppercase
            return object - beforeUpper + upperOffset;
        } else if (object>96 && object<123) { // is lowercase
            return object - beforeLower;
        }
        return 0;
    }

    public static String findOverlapBetweenCompartments(String rucksack){
        Integer midpoint = rucksack.length() / 2;
        String left = rucksack.substring(0, midpoint);
        String right = rucksack.substring(midpoint);
        for(int i =0; i<left.length(); i++){
            String ch = String.valueOf(left.charAt(i));
            if(right.contains(ch)){
                return ch;
            }
        }
        return "";
    }

    /**
     * Part 2 result function
     * @return sum of priorities of each team's badge item
     */
    public Integer findSumOfTeamBadges(){
        Integer teamCount = this.strings.size() / 3;
        Integer badgeSum = 0;
        for(int i=1; i<=teamCount; i++){
            badgeSum += getPriority(findTeamBadge(this.strings.subList((3*(i-1)), (3*i))));
        }
        return badgeSum;
    }

    public String findTeamBadge(List<String> team){
        String member0 = team.get(0);
        String member1 = team.get(1);
        String member2 = team.get(2);
        for(int i=0; i<member0.length(); i++){
            String ch = String.valueOf(member0.charAt(i));
            if(member1.contains(ch) && member2.contains(ch))
                return ch;
        }
        return "";
    }
}
