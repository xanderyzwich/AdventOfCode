import util.StringChecker;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Day2 extends Day{

    Map<String, String> encoding1 = new HashMap<>(){{
        put("A", "Rock");
        put("B", "Paper");
        put("C", "Scissors");
    }};
    Map<String, String> encoding2pt1 = new HashMap<>(){{
        put("X", "Rock");
        put("Y", "Paper");
        put("Z", "Scissors");
    }};

    List<RoundPt1> pt1RoundList;
    List<RoundPt2> pt2RoundList;

    public Day2(Type type) {
        super(2, type);
        this.pt1RoundList = this.strings.stream()
                .filter(StringChecker::notEmpty)
                .map(s->s.split(" "))
                .map(list -> new RoundPt1(encoding1.get(list[0]), encoding2pt1.get(list[1])))
                .toList();
        this.pt2RoundList = this.strings.stream()
                .filter(StringChecker::notEmpty)
                .map(s->s.split(" "))
                .map(list -> new RoundPt2(encoding1.get(list[0]), list[1]))
                .toList();
    }

    public Integer part1() {
        return this.pt1RoundList.stream()
                .map(RoundPt1::roundScore)
                .reduce(0, Integer::sum);
    }

    public Integer part2() {
        return this.pt2RoundList.stream()
                .map(RoundPt2::roundScore)
                .reduce(0, Integer::sum);
    }

    static class RoundPt1 {
        protected String me;
        protected String them;

        static Map<String, Integer> shapeScore = new HashMap<>(){{
            put("Rock", 1);
            put("Paper", 2);
            put("Scissors", 3);
        }};

        public  RoundPt1(){
            this.me = "";
            this.them = "";
        }

        public RoundPt1(String them, String me){
            this.me = me;
            this.them = them;
        }

        private Integer outcomeScore(){
            Integer mine = shapeScore.get(this.me);
            Integer theirs = shapeScore.get(this.them);
            int difference = mine - theirs;
            switch (difference) {
                case 0 -> {
                    return 3;
                }
                case 1, -2 -> {
                    return 6;
                }
                case -1, 2 -> {
                    return 0;
                }
            }
            System.out.println("SoMeThInG bOrKeD-----------------------------------------------");
            return -1; // this should never happen

        }

        protected Integer roundScore(){
            Integer shape = shapeScore.get(this.me);
            Integer outcome = this.outcomeScore();
            return shape + outcome;
        }


    }

    static class RoundPt2 extends RoundPt1{

        public RoundPt2(String them, String outcome) {
            String me = "broken";
            this.them = them;
            // lose
            if (outcome.equals("Y")) {
                this.me = them;
            } else {
                boolean win = outcome.equals("Z");
                switch (them) {
                    case "Rock":
                        this.me = win ? "Paper" : "Scissors";
                        break;
                    case "Paper":
                        this.me = win ? "Scissors" : "Rock";
                        break;
                    case "Scissors":
                        this.me = win ? "Rock" : "Paper";
                        break;
                }
            }
            ;
        }
    }
}
