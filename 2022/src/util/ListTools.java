package util;

import java.util.List;

public class ListTools {

    public static boolean notEmpty(List<?> list){
        return !list.isEmpty();
    }
    public static <T> T getFirst(List<T> list){
        return list.get(0);
    }
}
