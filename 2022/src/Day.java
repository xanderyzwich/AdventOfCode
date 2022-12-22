import util.FileTools;

import java.util.List;

/**
 * Base setup for each day's needs
 */
public abstract class Day {
    List<String> strings;
    Integer day;

    public enum Type {
            EXAMPLE,
            DATA,
    }
    String fileName;
    Type type;

    public Day(Integer day, Type type){
        this.day = day;
        this.type = type;
        this.fileName = type.name().toLowerCase();
        this.strings = FileTools.readLinesFromFile(day, this.fileName);
    }

}
