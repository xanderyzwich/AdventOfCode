package util;

public class StringChecker {
    public static boolean isEmpty(String toCheck){
        return toCheck == null || toCheck.length() == 0;
    }

    public static boolean notEmpty(String toCheck){
        return !isEmpty(toCheck);
    }
}
