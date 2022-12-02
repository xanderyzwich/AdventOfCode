package util;

public class StringTools {
    public static boolean isEmpty(String toCheck){
        return toCheck == null || toCheck.length() == 0;
    }

    public static boolean notEmpty(String toCheck){
        return !isEmpty(toCheck);
    }

    public Integer getAscii(String character){
        return character.length() != 1
                ? 0
                : (int) character.toCharArray()[0];
    }
}
