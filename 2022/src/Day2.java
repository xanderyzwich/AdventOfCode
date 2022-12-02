import util.StringTools;

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

    List<? extends Round> roundList;

    public Day2(Type type, Integer part) {
        super(2, type);
        this.roundList = this.strings.stream()
                .filter(StringTools::notEmpty)
                .map(s -> s.split(" "))
                .map(list -> part == 1
                    ? new RoundPt1(encoding1.get(list[0]), encoding2pt1.get(list[1]))
                    : new RoundPt2(encoding1.get(list[0]), list[1]))
                .toList();
    }

    public Integer takeScore() {
        return this.roundList.stream()
                .map(Round::roundScore)
                .reduce(0, Integer::sum);
    }

    abstract static class Round {
        protected String me;
        protected String them;

        static Map<String, Integer> shapeScore = new HashMap<>(){{
            put("Rock", 1);
            put("Paper", 2);
            put("Scissors", 3);
        }};

        Round(){
            this.me = "";
            this.them = "";
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

    static class RoundPt1 extends Round{
        public RoundPt1(String them, String me){
            this.me = me;
            this.them = them;
        }
    }

    static class RoundPt2 extends Round{
        public RoundPt2(String them, String outcome) {
            this.them = them;
            // lose
            if (outcome.equals("Y")) {
                this.me = them;
            } else {
                boolean win = outcome.equals("Z");
                switch (them) {
                    case "Rock" ->      this.me = win ? "Paper" : "Scissors";
                    case "Paper" ->     this.me = win ? "Scissors" : "Rock";
                    case "Scissors" ->  this.me = win ? "Rock" : "Paper";
                }
            }
        }
    }
}
